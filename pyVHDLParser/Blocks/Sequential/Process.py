# EMACS settings: -*-	tab-width: 2; indent-tabs-mode: t; python-indent-offset: 2 -*-
# vim: tabstop=2:shiftwidth=2:noexpandtab
# kate: tab-width 2; replace-tabs off; indent-width 2;
# ==============================================================================
# Authors:            Patrick Lehmann
#
# Python functions:   A streaming VHDL parser
#
# Description:
# ------------------------------------
#		TODO:
#
# License:
# ==============================================================================
# Copyright 2007-2017 Patrick Lehmann - Dresden, Germany
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
#
# load dependencies
from pyVHDLParser.Blocks.Reference import Use
from pyVHDLParser.Token                     import CharacterToken, SpaceToken, LinebreakToken, CommentToken, IndentationToken, MultiLineCommentToken, SingleLineCommentToken
from pyVHDLParser.Token.Keywords            import StringToken, BoundaryToken, IsKeyword, UseKeyword, ConstantKeyword, VariableKeyword, ProcessKeyword, BeginKeyword
from pyVHDLParser.Blocks                    import Block, CommentBlock, TokenParserException
from pyVHDLParser.Blocks.Common             import LinebreakBlock, IndentationBlock, WhitespaceBlock
# from pyVHDLParser.Blocks.ControlStructure   import If, Case, ForLoop, WhileLoop
from pyVHDLParser.Blocks.Generic            import SequentialBeginBlock, EndBlock as EndBlockBase
from pyVHDLParser.Blocks.List               import SensitivityList
from pyVHDLParser.Blocks.ObjectDeclaration  import Constant, Variable
from pyVHDLParser.Blocks.Parser             import TokenToBlockParser
from pyVHDLParser.Blocks.Reporting          import Report


# Type alias for type hinting
ParserState = TokenToBlockParser.TokenParserState


class OpenBlock(Block):
	@classmethod
	def stateProcessKeyword(cls, parserState: ParserState):
		token = parserState.Token
		if (isinstance(token, CharacterToken)and (token == "(")):
			parserState.NewToken =    BoundaryToken(token)
			parserState.NewBlock =    cls(parserState.LastBlock, parserState.TokenMarker, endToken=parserState.NewToken)
			parserState.NextState =   OpenBlock2.stateAfterSensitivityList
			parserState.PushState =   SensitivityList.OpenBlock.stateOpeningParenthesis
			parserState.Counter =     1
			return
		elif isinstance(token, SpaceToken):
			parserState.NextState =   cls.stateWhitespace1
			return
		elif isinstance(token, LinebreakToken):
			parserState.NewBlock =    cls(parserState.LastBlock, parserState.TokenMarker, endToken=token.PreviousToken, multiPart=True)
			_ =                       LinebreakBlock(parserState.NewBlock, token)
			parserState.TokenMarker = None
			parserState.NextState =   cls.stateWhitespace1
			return
		elif isinstance(token, CommentToken):
			parserState.NewBlock =    cls(parserState.LastBlock, parserState.TokenMarker, endToken=token.PreviousToken, multiPart=True)
			_ =                       CommentBlock(parserState.NewBlock, token)
			parserState.TokenMarker = None
			parserState.NextState =   cls.stateWhitespace1
			return

		raise TokenParserException("Expected '(' or whitespace after keyword PROCESS.", token)

	@classmethod
	def stateWhitespace1(cls, parserState: ParserState):
		token = parserState.Token
		if (isinstance(token, CharacterToken)and (token == "(")):
			parserState.NewToken =    BoundaryToken(token)
			parserState.NewBlock =    cls(parserState.LastBlock, parserState.TokenMarker, endToken=parserState.NewToken)
			parserState.NextState =   OpenBlock2.stateAfterSensitivityList
			parserState.PushState =   SensitivityList.OpenBlock.stateOpeningParenthesis
			parserState.Counter =     1
			return
		elif isinstance(token, LinebreakToken):
			if (not (isinstance(parserState.LastBlock, CommentBlock) and isinstance(parserState.LastBlock.StartToken, MultiLineCommentToken))):
				parserState.NewBlock =    cls(parserState.LastBlock, parserState.TokenMarker, endToken=token.PreviousToken, multiPart=True)
				_ =                       LinebreakBlock(parserState.NewBlock, token)
			else:
				parserState.NewBlock =    LinebreakBlock(parserState.LastBlock, token)
			parserState.TokenMarker =   None
			return
		elif isinstance(token, CommentToken):
			parserState.NewBlock =      CommentBlock(parserState.LastBlock, token)
			parserState.TokenMarker =   None
			return
		elif (isinstance(token, IndentationToken) and isinstance(token.PreviousToken, (LinebreakToken, SingleLineCommentToken))):
			return
		elif (isinstance(token, SpaceToken) and (isinstance(parserState.LastBlock, CommentBlock) and isinstance(parserState.LastBlock.StartToken, MultiLineCommentToken))):
			parserState.NewToken =      BoundaryToken(token)
			parserState.NewBlock =      WhitespaceBlock(parserState.LastBlock, parserState.NewToken)
			parserState.TokenMarker =   None
			return

		raise TokenParserException("Expected '(' after keyword PROCESS.", token)


class OpenBlock2(Block):
	@classmethod
	def stateAfterSensitivityList(cls, parserState: ParserState):
		token = parserState.Token
		if isinstance(token, StringToken):
			if (token <= "is"):
				parserState.NewToken = IsKeyword(token)
				parserState.NewBlock = OpenBlock2(parserState.LastBlock, parserState.TokenMarker, parserState.NewToken)
				return
			else:
				parserState.NextState = cls.stateDeclarativeRegion
				parserState.NextState(parserState)
				return
		elif isinstance(token, SpaceToken):
			parserState.NewToken =    BoundaryToken(token)
			parserState.TokenMarker = parserState.NewToken
			parserState.NextState =   cls.stateWhitespace1
			return
		elif isinstance(token, LinebreakToken):
			parserState.NewBlock =    cls(parserState.LastBlock, parserState.TokenMarker, endToken=token.PreviousToken, multiPart=True)
			_ =                       LinebreakBlock(parserState.NewBlock, token)
			parserState.TokenMarker = None
			parserState.NextState =   cls.stateWhitespace1
			return
		elif isinstance(token, CommentToken):
			parserState.NewBlock =    cls(parserState.LastBlock, parserState.TokenMarker, endToken=token.PreviousToken, multiPart=True)
			_ =                       CommentBlock(parserState.NewBlock, token)
			parserState.TokenMarker = None
			parserState.NextState =   cls.stateWhitespace1
			return

		raise TokenParserException("Expected whitespace after keyword ENTITY.", token)

	@classmethod
	def stateWhitespace1(cls, parserState: ParserState):
		token = parserState.Token
		if (isinstance(token, StringToken) and (token <= "is")):
			parserState.NewToken =      IsKeyword(token)
			parserState.NewBlock =      cls(parserState.LastBlock, parserState.TokenMarker, endToken=parserState.NewToken)
			parserState.TokenMarker =   None
			parserState.NextState =     cls.stateDeclarativeRegion
			return
		elif isinstance(token, LinebreakToken):
			if (not (isinstance(parserState.LastBlock, CommentBlock) and isinstance(parserState.LastBlock.StartToken, MultiLineCommentToken))):
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
		elif (isinstance(token, IndentationToken) and isinstance(token.PreviousToken, (LinebreakToken, SingleLineCommentToken))):
			return
		elif (isinstance(token, SpaceToken) and (isinstance(parserState.LastBlock, CommentBlock) and isinstance(parserState.LastBlock.StartToken, MultiLineCommentToken))):
			parserState.NewToken =      BoundaryToken(token)
			parserState.NewBlock =      WhitespaceBlock(parserState.LastBlock, parserState.NewToken)
			parserState.TokenMarker =   None
			return

		raise TokenParserException("Expected declarations or keyword IS after sensitivity list.", token)

	@classmethod
	def stateDeclarativeRegion(cls, parserState: ParserState):
		keywords = {
			# Keyword     Transition
			UseKeyword:       Use.UseBlock.stateUseKeyword,
			ConstantKeyword:  Constant.ConstantBlock.stateConstantKeyword,
			VariableKeyword:  Variable.VariableBlock.stateVariableKeyword,
			# ProcedureKeyword: Procedure.NameBlock.stateProcesdureKeyword,
			# FunctionKeyword:  Function.NameBlock.stateFunctionKeyword,
			# PureKeyword:      Function.NameBlock.statePureKeyword,
			# ImpureKeyword:    Function.NameBlock.stateImpureKeyword
		}

		token = parserState.Token
		if isinstance(token, SpaceToken):
			blockType =                 IndentationBlock if isinstance(token, IndentationToken) else WhitespaceBlock
			parserState.NewBlock =      blockType(parserState.LastBlock, token)
			return
		elif isinstance(token, LinebreakToken):
			parserState.NewBlock =      LinebreakBlock(parserState.LastBlock, token)
			parserState.TokenMarker =   None
			return
		elif isinstance(token, CommentToken):
			parserState.NewBlock =      CommentBlock(parserState.LastBlock, token)
			parserState.TokenMarker =   None
			return
		elif isinstance(token, StringToken):
			tokenValue = token.Value.lower()

			for keyword in keywords:
				if (tokenValue == keyword.__KEYWORD__):
					newToken =                keyword(token)
					parserState.PushState =   keywords[keyword]
					parserState.NewToken =    newToken
					parserState.TokenMarker = newToken
					return

			if (tokenValue == "begin"):
				parserState.NewToken =  BeginKeyword(token)
				parserState.NextState = BeginBlock.stateConcurrentRegion
				return

		raise TokenParserException(
			"Expected one of these keywords: END, {keywords}. Found: '{tokenValue}'.".format(
				keywords=", ".join(
					[kw.__KEYWORD__.upper() for kw in keywords]
				),
				tokenValue=token.Value
			), token)


class EndBlock(EndBlockBase):
	KEYWORD =             ProcessKeyword
	KEYWORD_IS_OPTIONAL = True
	EXPECTED_NAME =       KEYWORD.__KEYWORD__

class BeginBlock(SequentialBeginBlock):
	END_BLOCK = EndBlock
