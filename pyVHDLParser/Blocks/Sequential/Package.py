# ==================================================================================================================== #
#            __     ___   _ ____  _     ____                                                                           #
#  _ __  _   \ \   / / | | |  _ \| |   |  _ \ __ _ _ __ ___  ___ _ __                                                  #
# | '_ \| | | \ \ / /| |_| | | | | |   | |_) / _` | '__/ __|/ _ \ '__|                                                 #
# | |_) | |_| |\ V / |  _  | |_| | |___|  __/ (_| | |  \__ \  __/ |                                                    #
# | .__/ \__, | \_/  |_| |_|____/|_____|_|   \__,_|_|  |___/\___|_|                                                    #
# |_|    |___/                                                                                                         #
# ==================================================================================================================== #
# Authors:                                                                                                             #
#   Patrick Lehmann                                                                                                    #
#                                                                                                                      #
# License:                                                                                                             #
# ==================================================================================================================== #
# Copyright 2017-2023 Patrick Lehmann - Boetzingen, Germany                                                            #
# Copyright 2016-2017 Patrick Lehmann - Dresden, Germany                                                               #
#                                                                                                                      #
# Licensed under the Apache License, Version 2.0 (the "License");                                                      #
# you may not use this file except in compliance with the License.                                                     #
# You may obtain a copy of the License at                                                                              #
#                                                                                                                      #
#   http://www.apache.org/licenses/LICENSE-2.0                                                                         #
#                                                                                                                      #
# Unless required by applicable law or agreed to in writing, software                                                  #
# distributed under the License is distributed on an "AS IS" BASIS,                                                    #
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.                                             #
# See the License for the specific language governing permissions and                                                  #
# limitations under the License.                                                                                       #
# ==================================================================================================================== #
#
from pyTooling.Decorators           import export

from pyVHDLParser.Token             import LinebreakToken, WordToken, WhitespaceToken, CommentToken, MultiLineCommentToken, IndentationToken
from pyVHDLParser.Token.Keywords    import PackageKeyword, IsKeyword, EndKeyword, GenericKeyword, BodyKeyword, UseKeyword, VariableKeyword, SignalKeyword
from pyVHDLParser.Token.Keywords    import BoundaryToken, IdentifierToken, TypeKeyword
from pyVHDLParser.Token.Keywords    import ConstantKeyword, SharedKeyword, ProcedureKeyword, FunctionKeyword, PureKeyword, ImpureKeyword
from pyVHDLParser.Blocks            import BlockParserException, Block, CommentBlock, TokenToBlockParser
from pyVHDLParser.Blocks.Whitespace     import LinebreakBlock, IndentationBlock, WhitespaceBlock
from pyVHDLParser.Blocks.Region    import SequentialDeclarativeRegion
from pyVHDLParser.Blocks.Generic   import EndBlock as EndBlockBase, BeginBlock
from pyVHDLParser.Blocks.Sequential import PackageBody
from pyVHDLParser.Blocks.List       import GenericList
from pyVHDLParser.Blocks.Type.Type       import TypeBlock


@export
class EndBlock(EndBlockBase):
	KEYWORD =             PackageKeyword
	KEYWORD_IS_OPTIONAL = True
	EXPECTED_NAME =       KEYWORD.__KEYWORD__

@export
class HeaderBlock(Block):
	@classmethod
	def stateStatementRegion(cls, parserState: TokenToBlockParser):
		token = parserState.Token
		if isinstance(token, WhitespaceToken):
			blockType =                 IndentationBlock if isinstance(token, IndentationToken) else WhitespaceBlock
			parserState.NewBlock =      blockType(parserState.LastBlock, token)
			parserState.TokenMarker =   None
			return
		elif isinstance(token, LinebreakToken):
			parserState.NewBlock =      LinebreakBlock(parserState.LastBlock, token)
			parserState.TokenMarker =   None
			return
		elif isinstance(token, CommentToken):
			parserState.NewBlock =      CommentBlock(parserState.LastBlock, token)
			parserState.TokenMarker =   None
			return
		elif isinstance(token, WordToken):
			tokenValue = token.Value.lower()

			if tokenValue == GenericKeyword.__KEYWORD__:
				newToken =                GenericKeyword(fromExistingToken=token)
				parserState.PushState =   GenericList.OpenBlock.stateGenericKeyword
				parserState.NewToken =    newToken
				parserState.TokenMarker = newToken
				return

			if tokenValue == "end":
				parserState.NewToken =  EndKeyword(fromExistingToken=token)
				parserState.NextState = EndBlock.stateEndKeyword
				return

			parserState.NextState = DeclarativeRegion.stateDeclarativeRegion
			DeclarativeRegion.stateDeclarativeRegion(parserState)



@export
class DeclarativeRegion(SequentialDeclarativeRegion):
	EXPECT_BEGIN_KEYWORD = False
	END_BLOCK =            EndBlock

	@classmethod
	def __cls_init__(cls):
		super().__cls_init__()

		cls.KEYWORDS.update({
			TypeKeyword: TypeBlock.stateTypeKeyword,
		})


@export
class NameBlock(Block):
	@classmethod
	def statePackageKeyword(cls, parserState: TokenToBlockParser):
		token = parserState.Token
		if isinstance(token, WhitespaceToken):
			parserState.NewToken =    BoundaryToken(fromExistingToken=token)
			parserState.NextState =   cls.stateWhitespace1
			return
		elif isinstance(token, (LinebreakToken, CommentToken)):
			block =                   LinebreakBlock if isinstance(token, LinebreakToken) else CommentBlock
			parserState.NewBlock =    cls(parserState.LastBlock, parserState.TokenMarker, endToken=token.PreviousToken, multiPart=True)
			_ =                       block(parserState.NewBlock, token)
			parserState.TokenMarker = None
			parserState.NextState =   cls.stateWhitespace1
			return

		raise BlockParserException("Expected whitespace after keyword PACKAGE.", token)

	@classmethod
	def stateWhitespace1(cls, parserState: TokenToBlockParser):
		token = parserState.Token
		if isinstance(token, WordToken):
			if token <= "body":
				parserState.NewToken =    BodyKeyword(fromExistingToken=token)
				parserState.NextState =   PackageBody.NameBlock.stateBodyKeyword
				return
			else:
				parserState.NewToken =    IdentifierToken(fromExistingToken=token)
				parserState.NextState =   cls.statePackageName
				return
		elif isinstance(token, LinebreakToken):
			if not (isinstance(parserState.LastBlock, CommentBlock) and isinstance(parserState.LastBlock.StartToken, MultiLineCommentToken)):
				parserState.NewBlock =    cls(parserState.LastBlock, parserState.TokenMarker, endToken=token.PreviousToken, multiPart=True)
				_ =                       LinebreakBlock(parserState.NewBlock, token)
			else:
				parserState.NewBlock =    LinebreakBlock(parserState.LastBlock, token)
			parserState.TokenMarker =   None
			return
		elif isinstance(token, CommentToken):
			parserState.NewBlock =      cls(parserState.LastBlock, parserState.TokenMarker, endToken=token.PreviousToken, multiPart=True)
			_ =                         CommentBlock(parserState.NewBlock, token)
			parserState.TokenMarker =   None
			return
		elif isinstance(token, WhitespaceToken) and (isinstance(parserState.LastBlock, CommentBlock) and isinstance(parserState.LastBlock.StartToken, MultiLineCommentToken)):
			parserState.NewToken =      BoundaryToken(fromExistingToken=token)
			parserState.NewBlock =      WhitespaceBlock(parserState.LastBlock, parserState.NewToken)
			parserState.TokenMarker =   None
			return

		raise BlockParserException("Expected package name (identifier).", token)

	@classmethod
	def statePackageName(cls, parserState: TokenToBlockParser):
		token = parserState.Token
		if isinstance(token, WhitespaceToken):
			parserState.NewToken =    BoundaryToken(fromExistingToken=token)
			parserState.NextState =   cls.stateWhitespace2
			return
		elif isinstance(token, (LinebreakToken, CommentToken)):
			block =                   LinebreakBlock if isinstance(token, LinebreakToken) else CommentBlock
			parserState.NewBlock =    cls(parserState.LastBlock, parserState.TokenMarker, endToken=token.PreviousToken, multiPart=True)
			_ =                       block(parserState.NewBlock, token)
			parserState.TokenMarker = None
			parserState.NextState =   cls.stateWhitespace2
			return

		raise BlockParserException("Expected whitespace after package name.", token)

	@classmethod
	def stateWhitespace2(cls, parserState: TokenToBlockParser):
		token = parserState.Token
		if isinstance(token, WordToken) and (token <= "is"):
			parserState.NewToken =      IsKeyword(fromExistingToken=token)
			parserState.NewBlock =      cls(parserState.LastBlock, parserState.TokenMarker, endToken=parserState.NewToken)
			parserState.TokenMarker =   None
			parserState.NextState =     HeaderBlock.stateStatementRegion
			return
		elif isinstance(token, LinebreakToken):
			if not (isinstance(parserState.LastBlock, CommentBlock) and isinstance(parserState.LastBlock.StartToken, MultiLineCommentToken)):
				parserState.NewBlock =    cls(parserState.LastBlock, parserState.TokenMarker, endToken=token.PreviousToken, multiPart=True)
				_ =                       LinebreakBlock(parserState.NewBlock, token)
			else:
				parserState.NewBlock =    LinebreakBlock(parserState.LastBlock, token)
			parserState.TokenMarker =   None
			return
		elif isinstance(token, CommentToken):
			parserState.NewBlock =      cls(parserState.LastBlock, parserState.TokenMarker, endToken=token.PreviousToken, multiPart=True)
			_ =                         CommentBlock(parserState.NewBlock, token)
			parserState.TokenMarker =   None
			return
		elif isinstance(token, WhitespaceToken) and (isinstance(parserState.LastBlock, CommentBlock) and isinstance(parserState.LastBlock.StartToken, MultiLineCommentToken)):
			parserState.NewToken =      BoundaryToken(fromExistingToken=token)
			parserState.NewBlock =      WhitespaceBlock(parserState.LastBlock, parserState.NewToken)
			parserState.TokenMarker =   None
			return

		raise BlockParserException("Expected keyword IS after package name.", token)
