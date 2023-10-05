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
from pyVHDLParser.Token.Parser  import Tokenizer, TokenizerException
from pyVHDLParser.Token         import StartOfDocumentToken, EndOfDocumentToken, Token
from pyVHDLParser.Blocks        import StartOfDocumentBlock, EndOfDocumentBlock, TokenToBlockParser, MetaBlock, Block, BlockParserException

from tests.Interfaces import ITestcase

from typing import Optional


class TokenizerChecks(ITestcase): #, ExpectedDataMixin):
	def check_TokenLinking(self) -> None:
		# test['name']
		tokenStream = Tokenizer.GetVHDLTokenizer(self.code)

		tokenIterator = iter(tokenStream)
		startToken =    next(tokenIterator)

		self.assertIsInstance(startToken, StartOfDocumentToken, msg=f"First token is not StartOfDocumentToken: {startToken}")
		self.assertIsNone(startToken.PreviousToken, msg="First token has no open start.")

		lastToken: Token = startToken
		endToken:  Token = None

		for token in tokenIterator:
			if isinstance(token, EndOfDocumentToken):
				endToken = token
				break

			self.assertEqual(lastToken.NextToken, token, msg=f"Last token is not connected to the current token: {token}")
			self.assertEqual(lastToken, token.PreviousToken, msg=f"Current token is not connected to lastToken: {token}")

			lastToken = token
		else:
			self.fail(msg="No EndOfDocumentToken found.")

		self.assertIsInstance(endToken, EndOfDocumentToken, msg=f"End token is not EndOfDocumentToken: {endToken}")
		self.assertEqual(lastToken.NextToken, endToken, msg=f"Last token is not connected to the end token: {lastToken}")
		self.assertEqual(lastToken, endToken.PreviousToken, msg=f"End token is not connected to lastToken: {lastToken}")
		self.assertIsNone(endToken.NextToken, msg=f"End token has no open end: {endToken.NextToken}")


class BlockParserChecks(ITestcase): #, ExpectedDataMixin):
	def check_BlockLinking(self) -> None:
		# test['name']
		tokenStream = Tokenizer.GetVHDLTokenizer(self.code)
		blockStream = TokenToBlockParser(tokenStream)()

		blockIterator = iter(blockStream)
		startBlock = next(blockIterator)

		self.assertIsInstance(startBlock, StartOfDocumentBlock, msg=f"First token is not StartOfDocumentBlock: {startBlock}")
		self.assertIsNone(startBlock._previousBlock, msg="First block has no open start.")

		lastBlock: Block = startBlock
		endBlock:  Optional[Block] = None

		for block in blockIterator:
			print(block)
			if isinstance(block, EndOfDocumentBlock):
				endBlock = block
				break

			self.assertEqual(lastBlock.NextBlock, block, msg=f"Last block is not connected to the current block: {block}")
			self.assertEqual(lastBlock, block.PreviousBlock, msg=f"Current block is not connected to lastBlock: {block}")

			lastBlock = block
		else:
			self.fail(msg="No EndOfDocumentBlock found.")

		assert endBlock is not None
		self.assertIsInstance(endBlock, EndOfDocumentToken, msg=f"End block is not EndOfDocumentBlock: {endBlock}")
		self.assertEqual(lastBlock.NextToken, endBlock, msg=f"Last block is not connected to the end block: {lastBlock}")
		self.assertEqual(lastBlock, endBlock.PreviousBlock, msg=f"End block is not connected to lastBlock: {lastBlock}")
		self.assertIsNone(endBlock.NextBlock, msg=f"End block has no open end: {endBlock.NextBlock}")
