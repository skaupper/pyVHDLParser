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
from enum                     import IntEnum
from typing                   import Iterator

from pyTooling.Decorators     import export

from pyVHDLParser             import SourceCodePosition
from pyVHDLParser.Base        import ParserException
from pyVHDLParser.Token       import StartOfDocumentToken, EndOfDocumentToken, IndentationToken, FusedCharacterToken
from pyVHDLParser.Token       import CharacterLiteralToken, StringLiteralToken, ExtendedIdentifier, DirectiveToken, IntegerLiteralToken, RealLiteralToken
from pyVHDLParser.Token       import CharacterToken, WhitespaceToken, WordToken, SingleLineCommentToken, MultiLineCommentToken, LinebreakToken


@export
class TokenizerException(ParserException):
	"""A :exc:`~pyVHDLParser.Base.ParserException` generated by the :class:`~pyVHDLParser.Token.Parser.Tokenizer`."""

	def __init__(self, message: str, position: SourceCodePosition):
		super().__init__(message)
		self.Position = position

	def __str__(self) -> str:
		return f"{self.Position!s}: {self._message}"


@export
class Tokenizer:
	class TokenKind(IntEnum):
		"""Enumeration of all Tokenizer states."""

		SpaceChars =                      0   #: Last char was a space
		IntegerChars =                    1   #: Last char was a digit
		RealChars =                       2   #: Last char was a digit
		AlphaChars =                      3   #: Last char was a letter
		DelimiterChars =                  4   #: Last char was a delimiter character
		PossibleSingleLineCommentStart =  5   #: Last char was a dash
		PossibleLinebreak =               6   #: Last char was a ``\r``
		PossibleRealLiteral =             7   #: Last char was a ``.``
		PossibleCharacterLiteral =        8   #: Last char was a ``'``
		PossibleStringLiteralStart =      9   #: Last char was a ``"``
		PossibleExtendedIdentifierStart = 10  #: Last char was a ``\``
		SingleLineComment =               11  #: Found ``--`` before
		MultiLineComment =                12  #: Found ``/*`` before
		Linebreak =                       13  #: Last char was a ``\n``
		Directive =                       14  #: Last char was a `` ` ``
		FuseableCharacter =               15  #: Last char was a character that could be fused
		OtherChars =                      16  #: Anything else

	@classmethod
	def GetVHDLTokenizer(cls, iterable: Iterator[str]):
		previousToken = StartOfDocumentToken()
		tokenKind =     cls.TokenKind.OtherChars
		start =         SourceCodePosition(1, 1, 1)
		buffer =        ""
		absolute =      0
		column =        0
		row =           1

		__NUMBER_CHARACTERS__ =     "0123456789"
		__ALPHA_CHARACTERS__ =      "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
		__WHITESPACE_CHARACTERS__ = " \t"
		__FUSEABLE_CHARS__ =        "=<:/*>?"

		yield previousToken

		for char in iterable:
			absolute +=   1
			column +=     1

			# State: SpaceChars
			if tokenKind is cls.TokenKind.SpaceChars:
				if char in __WHITESPACE_CHARACTERS__:
					buffer += char
				else:
					end = SourceCodePosition(row, column - 1, absolute - 1)
					if isinstance(previousToken, (LinebreakToken, SingleLineCommentToken, StartOfDocumentToken)):
						previousToken = IndentationToken(previousToken, buffer, start, end)
					else:
						previousToken = WhitespaceToken(previousToken, buffer, start, end)
					yield previousToken

					start =   SourceCodePosition(row, column, absolute)
					buffer =  char
					if char in __NUMBER_CHARACTERS__:   tokenKind = cls.TokenKind.IntegerChars
					elif char in __ALPHA_CHARACTERS__:  tokenKind = cls.TokenKind.AlphaChars
					elif char == "'":                   tokenKind = cls.TokenKind.PossibleCharacterLiteral
					elif char == "\"":                  tokenKind = cls.TokenKind.PossibleStringLiteralStart
					elif char == "-":                   tokenKind = cls.TokenKind.PossibleSingleLineCommentStart
					elif char == "\r":                  tokenKind = cls.TokenKind.PossibleLinebreak
					elif char == "\n":
						previousToken = LinebreakToken(previousToken, char, start, start)
						yield previousToken
						tokenKind = cls.TokenKind.OtherChars
					elif char in __FUSEABLE_CHARS__:
						buffer =        char
						tokenKind =     cls.TokenKind.FuseableCharacter
					elif char == ".":                    tokenKind = cls.TokenKind.PossibleRealLiteral
					elif char == "\\":                   tokenKind = cls.TokenKind.PossibleExtendedIdentifierStart
					elif (char == "`") and isinstance(previousToken, (WhitespaceToken, LinebreakToken)):
						tokenKind = cls.TokenKind.Directive
					else:
						previousToken = CharacterToken(previousToken, char, start)
						yield previousToken
						tokenKind =     cls.TokenKind.OtherChars

			# State: IntegerChars
			elif tokenKind is cls.TokenKind.IntegerChars:
				if (char in __NUMBER_CHARACTERS__) or (char == "_"):
					buffer += char
				elif char == ".":
					buffer += char
					tokenKind = cls.TokenKind.RealChars
				else:
					previousToken = IntegerLiteralToken(previousToken, buffer, start, SourceCodePosition(row, column, absolute))
					yield previousToken

					start =   SourceCodePosition(row, column, absolute)
					buffer =  char
					if char in __WHITESPACE_CHARACTERS__: tokenKind = cls.TokenKind.SpaceChars
					elif char in __ALPHA_CHARACTERS__:    tokenKind = cls.TokenKind.AlphaChars
					elif char == "'":                     tokenKind = cls.TokenKind.PossibleCharacterLiteral
					elif char == "\"":                    tokenKind = cls.TokenKind.PossibleStringLiteralStart
					elif char == "-":                     tokenKind = cls.TokenKind.PossibleSingleLineCommentStart
					elif char == "\r":                    tokenKind = cls.TokenKind.PossibleLinebreak
					elif char == "\n":
						previousToken = LinebreakToken(previousToken, char, start, start)
						yield previousToken
						tokenKind = cls.TokenKind.OtherChars
					elif char in __FUSEABLE_CHARS__:
						buffer =        char
						tokenKind =     cls.TokenKind.FuseableCharacter
					elif char == "\\":                    tokenKind = cls.TokenKind.PossibleExtendedIdentifierStart
					elif (char == "`") and isinstance(previousToken, (WhitespaceToken, LinebreakToken)):
						tokenKind = cls.TokenKind.Directive
					else:
						previousToken = CharacterToken(previousToken, char, start)
						yield previousToken
						tokenKind =     cls.TokenKind.OtherChars

			# State: RealChars
			elif tokenKind is cls.TokenKind.RealChars:
				if (char in __NUMBER_CHARACTERS__) or (char == "_"):
					buffer += char
				else:
					previousToken = RealLiteralToken(previousToken, buffer, start, SourceCodePosition(row, column, absolute))
					yield previousToken

					start =   SourceCodePosition(row, column, absolute)
					buffer =  char
					if char in __WHITESPACE_CHARACTERS__: tokenKind = cls.TokenKind.SpaceChars
					elif char in __ALPHA_CHARACTERS__:    tokenKind = cls.TokenKind.AlphaChars
					elif char == "'":                     tokenKind = cls.TokenKind.PossibleCharacterLiteral
					elif char == "\"":                    tokenKind = cls.TokenKind.PossibleStringLiteralStart
					elif char == "-":                     tokenKind = cls.TokenKind.PossibleSingleLineCommentStart
					elif char == "\r":                    tokenKind = cls.TokenKind.PossibleLinebreak
					elif char == "\n":
						previousToken = LinebreakToken(previousToken, char, start, start)
						yield previousToken
						tokenKind = cls.TokenKind.OtherChars
					elif char in __FUSEABLE_CHARS__:
						buffer =        char
						tokenKind =     cls.TokenKind.FuseableCharacter
					elif char == "\\":                    tokenKind = cls.TokenKind.PossibleExtendedIdentifierStart
					elif (char == "`") and isinstance(previousToken, (WhitespaceToken, LinebreakToken)):
						tokenKind = cls.TokenKind.Directive
					else:
						previousToken = CharacterToken(previousToken, char, start)
						yield previousToken
						tokenKind =     cls.TokenKind.OtherChars

			# State: AlphaChars
			elif tokenKind is cls.TokenKind.AlphaChars:
				if (char in __ALPHA_CHARACTERS__) or (char == "_"):
					buffer += char
				else:
					previousToken = WordToken(previousToken, buffer, start, SourceCodePosition(row, column, absolute))
					yield previousToken

					start =   SourceCodePosition(row, column, absolute)
					buffer =  char
					if char in __WHITESPACE_CHARACTERS__: tokenKind = cls.TokenKind.SpaceChars
					elif char == "'":                     tokenKind = cls.TokenKind.PossibleCharacterLiteral
					elif char == "\"":                    tokenKind = cls.TokenKind.PossibleStringLiteralStart
					elif char == "-":                     tokenKind = cls.TokenKind.PossibleSingleLineCommentStart
					elif char == "\r":                    tokenKind = cls.TokenKind.PossibleLinebreak
					elif char == "\n":
						previousToken = LinebreakToken(previousToken, char, start, start)
						yield previousToken
						tokenKind = cls.TokenKind.OtherChars
					elif char in __FUSEABLE_CHARS__:
						buffer =        char
						tokenKind =     cls.TokenKind.FuseableCharacter
					elif char == "\\":                    tokenKind = cls.TokenKind.PossibleExtendedIdentifierStart
					elif (char == "`") and isinstance(previousToken, (WhitespaceToken, LinebreakToken)):
						tokenKind = cls.TokenKind.Directive
					else:
						previousToken = CharacterToken(previousToken, char, start)
						yield previousToken
						tokenKind =     cls.TokenKind.OtherChars

			# State: PossibleSingleLineCommentStart
			elif tokenKind is cls.TokenKind.PossibleSingleLineCommentStart:
				if char == "-":
					buffer =    "--"
					tokenKind = cls.TokenKind.SingleLineComment
				else:
					previousToken = CharacterToken(previousToken, "-", start)
					yield previousToken

					buffer =        char
					if char in __WHITESPACE_CHARACTERS__: tokenKind = cls.TokenKind.SpaceChars
					elif char in __NUMBER_CHARACTERS__:   tokenKind = cls.TokenKind.IntegerChars
					elif char in __ALPHA_CHARACTERS__:    tokenKind = cls.TokenKind.AlphaChars
					elif char == "'":                     tokenKind = cls.TokenKind.PossibleCharacterLiteral
					elif char == "\"":                    tokenKind = cls.TokenKind.PossibleStringLiteralStart
					elif char == "/r":                    tokenKind = cls.TokenKind.PossibleLinebreak
					elif char == "/n":
						previousToken = LinebreakToken(previousToken, char, start, start)
						yield previousToken
						tokenKind =     cls.TokenKind.OtherChars
					elif char in __FUSEABLE_CHARS__:
						buffer =        char
						tokenKind =     cls.TokenKind.FuseableCharacter
					elif char == "\\":                     tokenKind = cls.TokenKind.PossibleExtendedIdentifierStart
					elif (char == "`") and isinstance(previousToken, (WhitespaceToken, LinebreakToken)):
						tokenKind =     cls.TokenKind.Directive
					else:
						previousToken = CharacterToken(previousToken, char, start)
						yield previousToken
						tokenKind = cls.TokenKind.OtherChars

			# State: PossibleLinebreak
			elif tokenKind is cls.TokenKind.PossibleLinebreak:
				end = SourceCodePosition(row, column, absolute)
				if char == "\n":
					tokenKind = cls.TokenKind.OtherChars
					if buffer[:2] == "--":
						buffer += char
						previousToken = SingleLineCommentToken(previousToken, buffer, start, end)
					else:
						previousToken = LinebreakToken(previousToken, "\r\n", start, end)
					buffer = "\r\n"
					yield previousToken
				else:
					previousToken = LinebreakToken(previousToken, "\r", start, end)
					yield previousToken

					start =   end
					buffer =  char
					if char in __WHITESPACE_CHARACTERS__: tokenKind = cls.TokenKind.SpaceChars
					elif char in __NUMBER_CHARACTERS__:   tokenKind = cls.TokenKind.IntegerChars
					elif char in __ALPHA_CHARACTERS__:    tokenKind = cls.TokenKind.AlphaChars
					elif char == "'":                     tokenKind = cls.TokenKind.PossibleCharacterLiteral
					elif char == "\"":                    tokenKind = cls.TokenKind.PossibleStringLiteralStart
					elif char == "-":                     tokenKind = cls.TokenKind.PossibleSingleLineCommentStart
					elif char == "/r":                    tokenKind = cls.TokenKind.PossibleLinebreak
					elif char == "/n":
						previousToken = LinebreakToken(previousToken, char, start, start)
						yield previousToken
						tokenKind =     cls.TokenKind.OtherChars
					elif char in __FUSEABLE_CHARS__:
						buffer =        char
						tokenKind =     cls.TokenKind.FuseableCharacter
					elif char == "\\":                     tokenKind = cls.TokenKind.PossibleExtendedIdentifierStart
					elif (char == "`") and isinstance(previousToken, (WhitespaceToken, LinebreakToken)):
						tokenKind =     cls.TokenKind.Directive
					else:
						previousToken = CharacterToken(previousToken, char, start)
						yield previousToken
						tokenKind =     cls.TokenKind.OtherChars

			# State: PossibleRealLiteral
			elif tokenKind is cls.TokenKind.PossibleRealLiteral:
				if char in __NUMBER_CHARACTERS__:
					buffer +=   char
					tokenKind = cls.TokenKind.RealChars
				else:
					previousToken = CharacterToken(previousToken, ".", start)
					yield previousToken

					start = SourceCodePosition(row, column, absolute)
					buffer = char

					if char in __WHITESPACE_CHARACTERS__: tokenKind = cls.TokenKind.SpaceChars
					elif char in __NUMBER_CHARACTERS__:   tokenKind = cls.TokenKind.IntegerChars
					elif char in __ALPHA_CHARACTERS__:    tokenKind = cls.TokenKind.AlphaChars
					elif char == "'":                     tokenKind = cls.TokenKind.PossibleCharacterLiteral
					elif char == "\"":                    tokenKind = cls.TokenKind.PossibleStringLiteralStart
					elif char == "-":                     tokenKind = cls.TokenKind.PossibleSingleLineCommentStart
					elif char == "/r":                    tokenKind = cls.TokenKind.PossibleLinebreak
					elif char == "/n":
						previousToken = LinebreakToken(previousToken, char, start, start)
						yield previousToken
						tokenKind =     cls.TokenKind.OtherChars
					elif char in __FUSEABLE_CHARS__:
						buffer =        char
						tokenKind =     cls.TokenKind.FuseableCharacter
					elif char == "\\":                     tokenKind = cls.TokenKind.PossibleExtendedIdentifierStart
					elif (char == "`") and isinstance(previousToken, (WhitespaceToken, LinebreakToken)):
						tokenKind =     cls.TokenKind.Directive
					else:
						previousToken = CharacterToken(previousToken, char, start)
						yield previousToken
						tokenKind =     cls.TokenKind.OtherChars

			# State: PossibleCharacterLiteral
			elif tokenKind is cls.TokenKind.PossibleCharacterLiteral:
				buffer += char
				if len(buffer) == 2:
					if buffer[1] == "'":
						previousToken =   CharacterToken(previousToken, "'", start)
						yield previousToken
						previousToken =   CharacterToken(previousToken, "'", SourceCodePosition(row, column, absolute))
						yield previousToken
						tokenKind =       cls.TokenKind.OtherChars
					else:
						continue
				elif (len(buffer) == 3) and (buffer[2] == "'"):
					previousToken =   CharacterLiteralToken(previousToken, buffer, start, SourceCodePosition(row, column, absolute))
					yield previousToken
					tokenKind = cls.TokenKind.OtherChars
				else:
					previousToken =   CharacterToken(previousToken, "'", start)
					yield previousToken

					start.Column +=   1
					start.Absolute += 1
					buffer =          buffer[:2]
					if (buffer[0] in __ALPHA_CHARACTERS__) and (buffer[1] in __ALPHA_CHARACTERS__):
						tokenKind =     cls.TokenKind.AlphaChars
					elif (buffer[0] in __WHITESPACE_CHARACTERS__) and (buffer[1] in __WHITESPACE_CHARACTERS__):
						tokenKind =     cls.TokenKind.SpaceChars
					else:
						raise TokenizerException("Ambiguous syntax detected. buffer: '{buffer}'".format(buffer=buffer), start)

			# State: PossibleStringLiteralStart
			elif tokenKind is cls.TokenKind.PossibleStringLiteralStart:
				buffer += char
				if char == "\"":
					previousToken = StringLiteralToken(previousToken, buffer, start, SourceCodePosition(row, column, absolute))
					yield previousToken
					tokenKind = cls.TokenKind.OtherChars

			# State: PossibleExtendedIdentifierStart
			elif tokenKind is cls.TokenKind.PossibleExtendedIdentifierStart:
				buffer += char
				if char == "\\":
					previousToken = ExtendedIdentifier(previousToken, buffer, start, SourceCodePosition(row, column, absolute))
					yield previousToken
					tokenKind =     cls.TokenKind.OtherChars

			# State: Directive
			elif tokenKind is cls.TokenKind.Directive:
				buffer += char
				if char == "\r":
					tokenKind =     cls.TokenKind.PossibleLinebreak
				elif char == "\n":
					previousToken = DirectiveToken(previousToken, buffer, start, SourceCodePosition(row, column, absolute))
					yield previousToken
					tokenKind =     cls.TokenKind.OtherChars

			# State: SingleLineComment
			elif tokenKind is cls.TokenKind.SingleLineComment:
				buffer += char
				if char == "\r":
					tokenKind =     cls.TokenKind.PossibleLinebreak
				elif char == "\n":
					previousToken = SingleLineCommentToken(previousToken, buffer, start, SourceCodePosition(row, column, absolute))
					yield previousToken
					tokenKind =     cls.TokenKind.OtherChars

			# State: MultiLineComment
			elif tokenKind is cls.TokenKind.MultiLineComment:
				buffer += char
				if buffer[-2:] == "*/":
					previousToken = MultiLineCommentToken(previousToken, buffer, start, SourceCodePosition(row, column, absolute))
					yield previousToken
					tokenKind =     cls.TokenKind.OtherChars

			# State: FuseableCharacter
			elif tokenKind is cls.TokenKind.FuseableCharacter:
				fused = buffer + char
				if fused in ("=>", "**", ":=", "/=", "<=", ">=", "<>", "<<", ">>", "??", "?=", "?<", "?>", "?/=", "?<=", "?>="):
					previousToken = FusedCharacterToken(previousToken, fused, start, SourceCodePosition(row, column, absolute))
					yield previousToken
					tokenKind = cls.TokenKind.OtherChars
				elif fused in ("?/", "?<", "?>"):
					buffer =    fused
				elif fused == "/*":
					buffer =    fused
					tokenKind = cls.TokenKind.MultiLineComment
				else:
					previousToken = CharacterToken(previousToken, buffer[0], start)
					yield previousToken
					if len(buffer) == 2:
						previousToken = CharacterToken(previousToken, buffer[1], start)
						yield previousToken

					buffer = char
					if char in __WHITESPACE_CHARACTERS__:   tokenKind = cls.TokenKind.SpaceChars
					elif char in __NUMBER_CHARACTERS__:     tokenKind = cls.TokenKind.IntegerChars
					elif char in __ALPHA_CHARACTERS__:      tokenKind = cls.TokenKind.AlphaChars
					elif char == "'":                       tokenKind = cls.TokenKind.PossibleCharacterLiteral
					elif char == "\"":                      tokenKind = cls.TokenKind.PossibleStringLiteralStart
					elif char == "-":                       tokenKind = cls.TokenKind.PossibleSingleLineCommentStart
					elif char == "\r":                      tokenKind = cls.TokenKind.PossibleLinebreak
					elif char == "\n":
						previousToken = LinebreakToken(previousToken, char, start, start)
						yield previousToken
						tokenKind = cls.TokenKind.OtherChars
					elif char in __FUSEABLE_CHARS__:
						pass
					elif char == "\\":                       tokenKind = cls.TokenKind.PossibleExtendedIdentifierStart
					elif (char == "`") and isinstance(previousToken, (WhitespaceToken, LinebreakToken)):
						tokenKind = cls.TokenKind.Directive
					else:
						previousToken = CharacterToken(previousToken, char, start)
						yield previousToken

			# State: OtherChars
			elif tokenKind is cls.TokenKind.OtherChars:
				start =     SourceCodePosition(row, column, absolute)
				buffer =    char
				if char in __WHITESPACE_CHARACTERS__:   tokenKind = cls.TokenKind.SpaceChars
				elif char in __NUMBER_CHARACTERS__:     tokenKind = cls.TokenKind.IntegerChars
				elif char in __ALPHA_CHARACTERS__:      tokenKind = cls.TokenKind.AlphaChars
				elif char == "'":                       tokenKind = cls.TokenKind.PossibleCharacterLiteral
				elif char == "\"":                      tokenKind = cls.TokenKind.PossibleStringLiteralStart
				elif char == "-":                       tokenKind = cls.TokenKind.PossibleSingleLineCommentStart
				elif char == "\r":                      tokenKind = cls.TokenKind.PossibleLinebreak
				elif char == "\n":
					previousToken = LinebreakToken(previousToken, char, start, start)
					yield previousToken
					tokenKind = cls.TokenKind.OtherChars
				elif char in __FUSEABLE_CHARS__:
					buffer =        char
					tokenKind =     cls.TokenKind.FuseableCharacter
				elif char == "\\":                       tokenKind = cls.TokenKind.PossibleExtendedIdentifierStart
				elif (char == "`") and isinstance(previousToken, (WhitespaceToken, LinebreakToken)):
					tokenKind =     cls.TokenKind.Directive
				else:
					tokenKind =     cls.TokenKind.OtherChars
					previousToken = CharacterToken(previousToken, char, start)
					yield previousToken

			# State: unknown
			else:
				raise TokenizerException("Unknown state.", SourceCodePosition(row, column, absolute))

			if char == "\n":
				column =  0
				row +=    1
		# end for

		if tokenKind is cls.TokenKind.MultiLineComment:
			raise TokenizerException("End of document before end of multi line comment.", SourceCodePosition(row, column, absolute))

		# close open token when input stream is empty
		if tokenKind is cls.TokenKind.AlphaChars:
			previousToken = WordToken(previousToken, buffer, start, SourceCodePosition(row, column, absolute))
			yield previousToken
		elif tokenKind is cls.TokenKind.IntegerChars:
			previousToken = IntegerLiteralToken(previousToken, buffer, start, SourceCodePosition(row, column, absolute))
			yield previousToken
		elif tokenKind is cls.TokenKind.RealChars:
			previousToken = RealLiteralToken(previousToken, buffer, start, SourceCodePosition(row, column, absolute))
			yield previousToken
		elif tokenKind is cls.TokenKind.SpaceChars:
			end = SourceCodePosition(row, column - 1, absolute - 1)
			if isinstance(previousToken, (LinebreakToken, SingleLineCommentToken, StartOfDocumentToken)):
				previousToken = IndentationToken(previousToken, buffer, start, end)
			else:
				previousToken = WhitespaceToken(previousToken, buffer, start, end)
			yield previousToken
		elif tokenKind is cls.TokenKind.SingleLineComment:
			previousToken = SingleLineCommentToken(previousToken, buffer, start, SourceCodePosition(row, column, absolute))
			yield previousToken
		elif tokenKind in (cls.TokenKind.OtherChars, cls.TokenKind.DelimiterChars):
			pass
		else:
			raise TokenizerException("End of document before ...", SourceCodePosition(row, column, absolute))

		# End of document
		yield EndOfDocumentToken(previousToken, SourceCodePosition(row, column, absolute))
