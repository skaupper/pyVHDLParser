from sys    import stdout
from typing import TextIO

from antlr4 import Lexer, ATNDeserializer, DFA, LexerATNSimulator, PredictionContextCache


def serializedATN():
	return (
			4,0,130,1098,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,
			5,2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,
			2,13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,
			7,19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,
			2,26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,
			7,32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,
			2,39,7,39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,
			7,45,2,46,7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,
			2,52,7,52,2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,
			7,58,2,59,7,59,2,60,7,60,2,61,7,61,2,62,7,62,2,63,7,63,2,64,7,64,
			2,65,7,65,2,66,7,66,2,67,7,67,2,68,7,68,2,69,7,69,2,70,7,70,2,71,
			7,71,2,72,7,72,2,73,7,73,2,74,7,74,2,75,7,75,2,76,7,76,2,77,7,77,
			2,78,7,78,2,79,7,79,2,80,7,80,2,81,7,81,2,82,7,82,2,83,7,83,2,84,
			7,84,2,85,7,85,2,86,7,86,2,87,7,87,2,88,7,88,2,89,7,89,2,90,7,90,
			2,91,7,91,2,92,7,92,2,93,7,93,2,94,7,94,2,95,7,95,2,96,7,96,2,97,
			7,97,2,98,7,98,2,99,7,99,2,100,7,100,2,101,7,101,2,102,7,102,2,103,
			7,103,2,104,7,104,2,105,7,105,2,106,7,106,2,107,7,107,2,108,7,108,
			2,109,7,109,2,110,7,110,2,111,7,111,2,112,7,112,2,113,7,113,2,114,
			7,114,2,115,7,115,2,116,7,116,2,117,7,117,2,118,7,118,2,119,7,119,
			2,120,7,120,2,121,7,121,2,122,7,122,2,123,7,123,2,124,7,124,2,125,
			7,125,2,126,7,126,2,127,7,127,2,128,7,128,2,129,7,129,2,130,7,130,
			2,131,7,131,2,132,7,132,2,133,7,133,2,134,7,134,2,135,7,135,2,136,
			7,136,2,137,7,137,2,138,7,138,2,139,7,139,2,140,7,140,2,141,7,141,
			2,142,7,142,2,143,7,143,1,0,4,0,291,8,0,11,0,12,0,292,1,0,1,0,1,
			1,1,1,1,1,1,1,5,1,301,8,1,10,1,12,1,304,9,1,1,1,1,1,1,2,1,2,1,2,
			1,2,5,2,312,8,2,10,2,12,2,315,9,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,
			3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,
			6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,
			9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,
			10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,
			12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,
			14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,
			16,1,16,1,16,1,17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,19,1,
			19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,20,1,20,1,20,1,20,1,
			20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,21,1,21,1,21,1,
			21,1,21,1,21,1,21,1,21,1,21,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,
			22,1,22,1,22,1,22,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,24,1,24,1,
			24,1,24,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,26,1,26,1,26,1,26,1,
			26,1,27,1,27,1,27,1,27,1,27,1,27,1,28,1,28,1,28,1,28,1,28,1,29,1,
			29,1,29,1,29,1,29,1,30,1,30,1,30,1,30,1,31,1,31,1,31,1,31,1,31,1,
			31,1,31,1,31,1,31,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,
			33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,34,1,34,1,34,1,34,1,34,1,
			34,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,36,1,36,1,36,1,37,1,
			37,1,37,1,37,1,37,1,37,1,37,1,38,1,38,1,38,1,39,1,39,1,39,1,39,1,
			39,1,39,1,39,1,39,1,39,1,40,1,40,1,40,1,40,1,40,1,40,1,41,1,41,1,
			41,1,42,1,42,1,42,1,42,1,42,1,42,1,43,1,43,1,43,1,43,1,43,1,43,1,
			43,1,43,1,44,1,44,1,44,1,44,1,44,1,44,1,44,1,44,1,45,1,45,1,45,1,
			45,1,45,1,46,1,46,1,46,1,46,1,47,1,47,1,47,1,47,1,48,1,48,1,48,1,
			48,1,48,1,49,1,49,1,49,1,49,1,50,1,50,1,50,1,50,1,50,1,51,1,51,1,
			51,1,51,1,52,1,52,1,52,1,52,1,53,1,53,1,53,1,53,1,53,1,54,1,54,1,
			54,1,55,1,55,1,55,1,56,1,56,1,56,1,56,1,56,1,57,1,57,1,57,1,58,1,
			58,1,58,1,58,1,58,1,58,1,58,1,59,1,59,1,59,1,59,1,60,1,60,1,60,1,
			60,1,60,1,60,1,60,1,60,1,61,1,61,1,61,1,61,1,61,1,62,1,62,1,62,1,
			62,1,62,1,62,1,62,1,62,1,62,1,62,1,63,1,63,1,63,1,63,1,63,1,63,1,
			63,1,63,1,64,1,64,1,64,1,64,1,64,1,64,1,64,1,64,1,64,1,64,1,65,1,
			65,1,65,1,65,1,65,1,66,1,66,1,66,1,66,1,66,1,66,1,67,1,67,1,67,1,
			67,1,67,1,67,1,67,1,68,1,68,1,68,1,68,1,69,1,69,1,69,1,69,1,69,1,
			69,1,69,1,70,1,70,1,70,1,70,1,70,1,70,1,70,1,70,1,70,1,71,1,71,1,
			71,1,71,1,71,1,71,1,71,1,72,1,72,1,72,1,72,1,72,1,72,1,72,1,73,1,
			73,1,73,1,73,1,74,1,74,1,74,1,74,1,75,1,75,1,75,1,75,1,75,1,75,1,
			75,1,76,1,76,1,76,1,76,1,76,1,76,1,76,1,76,1,76,1,77,1,77,1,77,1,
			77,1,77,1,77,1,77,1,78,1,78,1,78,1,78,1,78,1,78,1,78,1,79,1,79,1,
			79,1,79,1,80,1,80,1,80,1,80,1,81,1,81,1,81,1,81,1,82,1,82,1,82,1,
			82,1,83,1,83,1,83,1,83,1,83,1,83,1,83,1,83,1,84,1,84,1,84,1,84,1,
			84,1,85,1,85,1,85,1,86,1,86,1,86,1,86,1,86,1,86,1,86,1,86,1,86,1,
			86,1,87,1,87,1,87,1,87,1,87,1,88,1,88,1,88,1,88,1,88,1,88,1,88,1,
			88,1,88,1,88,1,88,1,89,1,89,1,89,1,89,1,89,1,89,1,90,1,90,1,90,1,
			90,1,90,1,90,1,91,1,91,1,91,1,91,1,92,1,92,1,92,1,92,1,92,1,92,1,
			92,1,92,1,92,1,93,1,93,1,93,1,93,1,93,1,94,1,94,1,94,1,94,1,94,1,
			95,1,95,1,95,1,95,1,95,1,96,1,96,1,96,1,96,1,96,1,96,1,97,1,97,1,
			97,1,97,1,97,1,98,1,98,1,98,1,98,1,99,1,99,1,100,1,100,1,100,1,101,
			1,101,1,102,1,102,1,102,1,102,1,103,1,103,1,104,1,104,1,104,1,105,
			1,105,1,106,1,106,1,107,1,107,1,108,1,108,1,109,1,109,1,109,1,110,
			1,110,1,111,1,111,1,111,1,112,1,112,1,112,1,113,1,113,1,113,1,114,
			1,114,1,114,1,115,1,115,1,116,1,116,1,117,1,117,1,118,1,118,1,119,
			1,119,1,120,1,120,1,121,1,121,1,122,1,122,1,123,1,123,1,124,1,124,
			1,125,1,125,1,126,1,126,1,127,1,127,1,128,1,128,5,128,980,8,128,
			10,128,12,128,983,9,128,1,129,1,129,1,129,5,129,988,8,129,10,129,
			12,129,991,9,129,1,130,1,130,3,130,995,8,130,1,130,1,130,1,131,1,
			131,1,131,1,131,3,131,1003,8,131,1,132,1,132,1,132,1,132,1,132,3,
			132,1010,8,132,1,132,1,132,3,132,1014,8,132,1,133,1,133,1,133,3,
			133,1019,8,133,1,134,1,134,1,134,4,134,1024,8,134,11,134,12,134,
			1025,1,134,1,134,1,135,1,135,1,135,4,135,1033,8,135,11,135,12,135,
			1034,1,135,1,135,1,136,1,136,1,136,4,136,1042,8,136,11,136,12,136,
			1043,1,136,1,136,1,137,1,137,1,137,4,137,1051,8,137,11,137,12,137,
			1052,1,137,1,137,1,138,1,138,1,138,1,138,3,138,1061,8,138,1,139,
			1,139,1,139,1,139,1,140,1,140,1,140,1,140,5,140,1071,8,140,10,140,
			12,140,1074,9,140,1,140,1,140,1,141,1,141,1,141,1,141,5,141,1082,
			8,141,10,141,12,141,1085,9,141,1,142,1,142,4,142,1089,8,142,11,142,
			12,142,1090,1,142,1,142,1,143,1,143,3,143,1097,8,143,1,313,0,144,
			1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,25,13,
			27,14,29,15,31,16,33,17,35,18,37,19,39,20,41,21,43,22,45,23,47,24,
			49,25,51,26,53,27,55,28,57,29,59,30,61,31,63,32,65,33,67,34,69,35,
			71,36,73,37,75,38,77,39,79,40,81,41,83,42,85,43,87,44,89,45,91,46,
			93,47,95,48,97,49,99,50,101,51,103,52,105,53,107,54,109,55,111,56,
			113,57,115,58,117,59,119,60,121,61,123,62,125,63,127,64,129,65,131,
			66,133,67,135,68,137,69,139,70,141,71,143,72,145,73,147,74,149,75,
			151,76,153,77,155,78,157,79,159,80,161,81,163,82,165,83,167,84,169,
			85,171,86,173,87,175,88,177,89,179,90,181,91,183,92,185,93,187,94,
			189,95,191,96,193,97,195,98,197,99,199,100,201,101,203,102,205,103,
			207,104,209,105,211,106,213,107,215,108,217,109,219,110,221,111,
			223,112,225,113,227,114,229,115,231,116,233,117,235,118,237,119,
			239,120,241,121,243,122,245,123,247,124,249,125,251,0,253,0,255,
			0,257,0,259,0,261,0,263,0,265,0,267,126,269,0,271,0,273,0,275,0,
			277,127,279,128,281,129,283,0,285,0,287,130,1,0,36,10,0,9,13,32,
			32,133,133,160,160,5760,5760,8192,8202,8232,8233,8239,8239,8287,
			8287,12288,12288,2,0,10,10,13,13,2,0,65,65,97,97,2,0,66,66,98,98,
			2,0,83,83,115,115,2,0,67,67,99,99,2,0,69,69,101,101,2,0,70,70,102,
			102,2,0,84,84,116,116,2,0,82,82,114,114,2,0,76,76,108,108,2,0,73,
			73,105,105,2,0,78,78,110,110,2,0,68,68,100,100,2,0,72,72,104,104,
			2,0,85,85,117,117,2,0,89,89,121,121,2,0,71,71,103,103,2,0,79,79,
			111,111,2,0,75,75,107,107,2,0,77,77,109,109,2,0,80,80,112,112,2,
			0,87,87,119,119,2,0,88,88,120,120,2,0,74,74,106,106,2,0,86,86,118,
			118,2,0,65,90,97,122,1,0,48,57,3,0,48,57,65,90,97,122,2,0,48,57,
			95,95,2,0,43,43,45,45,2,0,48,49,95,95,2,0,48,55,95,95,4,0,48,57,
			65,70,95,95,97,102,3,0,10,10,13,13,34,34,4,0,48,57,65,90,95,95,97,
			122,1108,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,
			0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,
			0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,
			0,0,0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,0,0,0,0,37,1,0,0,0,0,39,1,0,
			0,0,0,41,1,0,0,0,0,43,1,0,0,0,0,45,1,0,0,0,0,47,1,0,0,0,0,49,1,0,
			0,0,0,51,1,0,0,0,0,53,1,0,0,0,0,55,1,0,0,0,0,57,1,0,0,0,0,59,1,0,
			0,0,0,61,1,0,0,0,0,63,1,0,0,0,0,65,1,0,0,0,0,67,1,0,0,0,0,69,1,0,
			0,0,0,71,1,0,0,0,0,73,1,0,0,0,0,75,1,0,0,0,0,77,1,0,0,0,0,79,1,0,
			0,0,0,81,1,0,0,0,0,83,1,0,0,0,0,85,1,0,0,0,0,87,1,0,0,0,0,89,1,0,
			0,0,0,91,1,0,0,0,0,93,1,0,0,0,0,95,1,0,0,0,0,97,1,0,0,0,0,99,1,0,
			0,0,0,101,1,0,0,0,0,103,1,0,0,0,0,105,1,0,0,0,0,107,1,0,0,0,0,109,
			1,0,0,0,0,111,1,0,0,0,0,113,1,0,0,0,0,115,1,0,0,0,0,117,1,0,0,0,
			0,119,1,0,0,0,0,121,1,0,0,0,0,123,1,0,0,0,0,125,1,0,0,0,0,127,1,
			0,0,0,0,129,1,0,0,0,0,131,1,0,0,0,0,133,1,0,0,0,0,135,1,0,0,0,0,
			137,1,0,0,0,0,139,1,0,0,0,0,141,1,0,0,0,0,143,1,0,0,0,0,145,1,0,
			0,0,0,147,1,0,0,0,0,149,1,0,0,0,0,151,1,0,0,0,0,153,1,0,0,0,0,155,
			1,0,0,0,0,157,1,0,0,0,0,159,1,0,0,0,0,161,1,0,0,0,0,163,1,0,0,0,
			0,165,1,0,0,0,0,167,1,0,0,0,0,169,1,0,0,0,0,171,1,0,0,0,0,173,1,
			0,0,0,0,175,1,0,0,0,0,177,1,0,0,0,0,179,1,0,0,0,0,181,1,0,0,0,0,
			183,1,0,0,0,0,185,1,0,0,0,0,187,1,0,0,0,0,189,1,0,0,0,0,191,1,0,
			0,0,0,193,1,0,0,0,0,195,1,0,0,0,0,197,1,0,0,0,0,199,1,0,0,0,0,201,
			1,0,0,0,0,203,1,0,0,0,0,205,1,0,0,0,0,207,1,0,0,0,0,209,1,0,0,0,
			0,211,1,0,0,0,0,213,1,0,0,0,0,215,1,0,0,0,0,217,1,0,0,0,0,219,1,
			0,0,0,0,221,1,0,0,0,0,223,1,0,0,0,0,225,1,0,0,0,0,227,1,0,0,0,0,
			229,1,0,0,0,0,231,1,0,0,0,0,233,1,0,0,0,0,235,1,0,0,0,0,237,1,0,
			0,0,0,239,1,0,0,0,0,241,1,0,0,0,0,243,1,0,0,0,0,245,1,0,0,0,0,247,
			1,0,0,0,0,249,1,0,0,0,0,267,1,0,0,0,0,277,1,0,0,0,0,279,1,0,0,0,
			0,281,1,0,0,0,0,287,1,0,0,0,1,290,1,0,0,0,3,296,1,0,0,0,5,307,1,
			0,0,0,7,321,1,0,0,0,9,325,1,0,0,0,11,332,1,0,0,0,13,338,1,0,0,0,
			15,344,1,0,0,0,17,348,1,0,0,0,19,352,1,0,0,0,21,365,1,0,0,0,23,371,
			1,0,0,0,25,378,1,0,0,0,27,388,1,0,0,0,29,394,1,0,0,0,31,400,1,0,
			0,0,33,405,1,0,0,0,35,412,1,0,0,0,37,416,1,0,0,0,39,421,1,0,0,0,
			41,431,1,0,0,0,43,445,1,0,0,0,45,454,1,0,0,0,47,465,1,0,0,0,49,472,
			1,0,0,0,51,476,1,0,0,0,53,483,1,0,0,0,55,488,1,0,0,0,57,494,1,0,
			0,0,59,499,1,0,0,0,61,504,1,0,0,0,63,508,1,0,0,0,65,517,1,0,0,0,
			67,526,1,0,0,0,69,534,1,0,0,0,71,540,1,0,0,0,73,548,1,0,0,0,75,551,
			1,0,0,0,77,558,1,0,0,0,79,561,1,0,0,0,81,570,1,0,0,0,83,576,1,0,
			0,0,85,579,1,0,0,0,87,585,1,0,0,0,89,593,1,0,0,0,91,601,1,0,0,0,
			93,606,1,0,0,0,95,610,1,0,0,0,97,614,1,0,0,0,99,619,1,0,0,0,101,
			623,1,0,0,0,103,628,1,0,0,0,105,632,1,0,0,0,107,636,1,0,0,0,109,
			641,1,0,0,0,111,644,1,0,0,0,113,647,1,0,0,0,115,652,1,0,0,0,117,
			655,1,0,0,0,119,662,1,0,0,0,121,666,1,0,0,0,123,674,1,0,0,0,125,
			679,1,0,0,0,127,689,1,0,0,0,129,697,1,0,0,0,131,707,1,0,0,0,133,
			712,1,0,0,0,135,718,1,0,0,0,137,725,1,0,0,0,139,729,1,0,0,0,141,
			736,1,0,0,0,143,745,1,0,0,0,145,752,1,0,0,0,147,759,1,0,0,0,149,
			763,1,0,0,0,151,767,1,0,0,0,153,774,1,0,0,0,155,783,1,0,0,0,157,
			790,1,0,0,0,159,797,1,0,0,0,161,801,1,0,0,0,163,805,1,0,0,0,165,
			809,1,0,0,0,167,813,1,0,0,0,169,821,1,0,0,0,171,826,1,0,0,0,173,
			829,1,0,0,0,175,839,1,0,0,0,177,844,1,0,0,0,179,855,1,0,0,0,181,
			861,1,0,0,0,183,867,1,0,0,0,185,871,1,0,0,0,187,880,1,0,0,0,189,
			885,1,0,0,0,191,890,1,0,0,0,193,895,1,0,0,0,195,901,1,0,0,0,197,
			906,1,0,0,0,199,910,1,0,0,0,201,912,1,0,0,0,203,915,1,0,0,0,205,
			917,1,0,0,0,207,921,1,0,0,0,209,923,1,0,0,0,211,926,1,0,0,0,213,
			928,1,0,0,0,215,930,1,0,0,0,217,932,1,0,0,0,219,934,1,0,0,0,221,
			937,1,0,0,0,223,939,1,0,0,0,225,942,1,0,0,0,227,945,1,0,0,0,229,
			948,1,0,0,0,231,951,1,0,0,0,233,953,1,0,0,0,235,955,1,0,0,0,237,
			957,1,0,0,0,239,959,1,0,0,0,241,961,1,0,0,0,243,963,1,0,0,0,245,
			965,1,0,0,0,247,967,1,0,0,0,249,969,1,0,0,0,251,971,1,0,0,0,253,
			973,1,0,0,0,255,975,1,0,0,0,257,977,1,0,0,0,259,984,1,0,0,0,261,
			992,1,0,0,0,263,998,1,0,0,0,265,1004,1,0,0,0,267,1018,1,0,0,0,269,
			1020,1,0,0,0,271,1029,1,0,0,0,273,1038,1,0,0,0,275,1047,1,0,0,0,
			277,1060,1,0,0,0,279,1062,1,0,0,0,281,1066,1,0,0,0,283,1077,1,0,
			0,0,285,1086,1,0,0,0,287,1096,1,0,0,0,289,291,7,0,0,0,290,289,1,
			0,0,0,291,292,1,0,0,0,292,290,1,0,0,0,292,293,1,0,0,0,293,294,1,
			0,0,0,294,295,6,0,0,0,295,2,1,0,0,0,296,297,5,45,0,0,297,298,5,45,
			0,0,298,302,1,0,0,0,299,301,8,1,0,0,300,299,1,0,0,0,301,304,1,0,
			0,0,302,300,1,0,0,0,302,303,1,0,0,0,303,305,1,0,0,0,304,302,1,0,
			0,0,305,306,6,1,1,0,306,4,1,0,0,0,307,308,5,47,0,0,308,309,5,42,
			0,0,309,313,1,0,0,0,310,312,9,0,0,0,311,310,1,0,0,0,312,315,1,0,
			0,0,313,314,1,0,0,0,313,311,1,0,0,0,314,316,1,0,0,0,315,313,1,0,
			0,0,316,317,5,42,0,0,317,318,5,47,0,0,318,319,1,0,0,0,319,320,6,
			2,1,0,320,6,1,0,0,0,321,322,7,2,0,0,322,323,7,3,0,0,323,324,7,4,
			0,0,324,8,1,0,0,0,325,326,7,2,0,0,326,327,7,5,0,0,327,328,7,5,0,
			0,328,329,7,6,0,0,329,330,7,4,0,0,330,331,7,4,0,0,331,10,1,0,0,0,
			332,333,7,2,0,0,333,334,7,7,0,0,334,335,7,8,0,0,335,336,7,6,0,0,
			336,337,7,9,0,0,337,12,1,0,0,0,338,339,7,2,0,0,339,340,7,10,0,0,
			340,341,7,11,0,0,341,342,7,2,0,0,342,343,7,4,0,0,343,14,1,0,0,0,
			344,345,7,2,0,0,345,346,7,10,0,0,346,347,7,10,0,0,347,16,1,0,0,0,
			348,349,7,2,0,0,349,350,7,12,0,0,350,351,7,13,0,0,351,18,1,0,0,0,
			352,353,7,2,0,0,353,354,7,9,0,0,354,355,7,5,0,0,355,356,7,14,0,0,
			356,357,7,11,0,0,357,358,7,8,0,0,358,359,7,6,0,0,359,360,7,5,0,0,
			360,361,7,8,0,0,361,362,7,15,0,0,362,363,7,9,0,0,363,364,7,6,0,0,
			364,20,1,0,0,0,365,366,7,2,0,0,366,367,7,9,0,0,367,368,7,9,0,0,368,
			369,7,2,0,0,369,370,7,16,0,0,370,22,1,0,0,0,371,372,7,2,0,0,372,
			373,7,4,0,0,373,374,7,4,0,0,374,375,7,6,0,0,375,376,7,9,0,0,376,
			377,7,8,0,0,377,24,1,0,0,0,378,379,7,2,0,0,379,380,7,8,0,0,380,381,
			7,8,0,0,381,382,7,9,0,0,382,383,7,11,0,0,383,384,7,3,0,0,384,385,
			7,15,0,0,385,386,7,8,0,0,386,387,7,6,0,0,387,26,1,0,0,0,388,389,
			7,3,0,0,389,390,7,6,0,0,390,391,7,17,0,0,391,392,7,11,0,0,392,393,
			7,12,0,0,393,28,1,0,0,0,394,395,7,3,0,0,395,396,7,10,0,0,396,397,
			7,18,0,0,397,398,7,5,0,0,398,399,7,19,0,0,399,30,1,0,0,0,400,401,
			7,3,0,0,401,402,7,18,0,0,402,403,7,13,0,0,403,404,7,16,0,0,404,32,
			1,0,0,0,405,406,7,3,0,0,406,407,7,15,0,0,407,408,7,7,0,0,408,409,
			7,7,0,0,409,410,7,6,0,0,410,411,7,9,0,0,411,34,1,0,0,0,412,413,7,
			3,0,0,413,414,7,15,0,0,414,415,7,4,0,0,415,36,1,0,0,0,416,417,7,
			5,0,0,417,418,7,2,0,0,418,419,7,4,0,0,419,420,7,6,0,0,420,38,1,0,
			0,0,421,422,7,5,0,0,422,423,7,18,0,0,423,424,7,20,0,0,424,425,7,
			21,0,0,425,426,7,18,0,0,426,427,7,12,0,0,427,428,7,6,0,0,428,429,
			7,12,0,0,429,430,7,8,0,0,430,40,1,0,0,0,431,432,7,5,0,0,432,433,
			7,18,0,0,433,434,7,12,0,0,434,435,7,7,0,0,435,436,7,11,0,0,436,437,
			7,17,0,0,437,438,7,15,0,0,438,439,7,9,0,0,439,440,7,2,0,0,440,441,
			7,8,0,0,441,442,7,11,0,0,442,443,7,18,0,0,443,444,7,12,0,0,444,42,
			1,0,0,0,445,446,7,5,0,0,446,447,7,18,0,0,447,448,7,12,0,0,448,449,
			7,4,0,0,449,450,7,8,0,0,450,451,7,2,0,0,451,452,7,12,0,0,452,453,
			7,8,0,0,453,44,1,0,0,0,454,455,7,13,0,0,455,456,7,11,0,0,456,457,
			7,4,0,0,457,458,7,5,0,0,458,459,7,18,0,0,459,460,7,12,0,0,460,461,
			7,12,0,0,461,462,7,6,0,0,462,463,7,5,0,0,463,464,7,8,0,0,464,46,
			1,0,0,0,465,466,7,13,0,0,466,467,7,18,0,0,467,468,7,22,0,0,468,469,
			7,12,0,0,469,470,7,8,0,0,470,471,7,18,0,0,471,48,1,0,0,0,472,473,
			7,6,0,0,473,474,7,12,0,0,474,475,7,13,0,0,475,50,1,0,0,0,476,477,
			7,6,0,0,477,478,7,12,0,0,478,479,7,8,0,0,479,480,7,11,0,0,480,481,
			7,8,0,0,481,482,7,16,0,0,482,52,1,0,0,0,483,484,7,6,0,0,484,485,
			7,10,0,0,485,486,7,4,0,0,486,487,7,6,0,0,487,54,1,0,0,0,488,489,
			7,6,0,0,489,490,7,10,0,0,490,491,7,4,0,0,491,492,7,11,0,0,492,493,
			7,7,0,0,493,56,1,0,0,0,494,495,7,6,0,0,495,496,7,23,0,0,496,497,
			7,11,0,0,497,498,7,8,0,0,498,58,1,0,0,0,499,500,7,7,0,0,500,501,
			7,11,0,0,501,502,7,10,0,0,502,503,7,6,0,0,503,60,1,0,0,0,504,505,
			7,7,0,0,505,506,7,18,0,0,506,507,7,9,0,0,507,62,1,0,0,0,508,509,
			7,7,0,0,509,510,7,15,0,0,510,511,7,12,0,0,511,512,7,5,0,0,512,513,
			7,8,0,0,513,514,7,11,0,0,514,515,7,18,0,0,515,516,7,12,0,0,516,64,
			1,0,0,0,517,518,7,17,0,0,518,519,7,6,0,0,519,520,7,12,0,0,520,521,
			7,6,0,0,521,522,7,9,0,0,522,523,7,2,0,0,523,524,7,8,0,0,524,525,
			7,6,0,0,525,66,1,0,0,0,526,527,7,17,0,0,527,528,7,6,0,0,528,529,
			7,12,0,0,529,530,7,6,0,0,530,531,7,9,0,0,531,532,7,11,0,0,532,533,
			7,5,0,0,533,68,1,0,0,0,534,535,7,17,0,0,535,536,7,9,0,0,536,537,
			7,18,0,0,537,538,7,15,0,0,538,539,7,21,0,0,539,70,1,0,0,0,540,541,
			7,17,0,0,541,542,7,15,0,0,542,543,7,2,0,0,543,544,7,9,0,0,544,545,
			7,13,0,0,545,546,7,6,0,0,546,547,7,13,0,0,547,72,1,0,0,0,548,549,
			7,11,0,0,549,550,7,7,0,0,550,74,1,0,0,0,551,552,7,11,0,0,552,553,
			7,20,0,0,553,554,7,21,0,0,554,555,7,15,0,0,555,556,7,9,0,0,556,557,
			7,6,0,0,557,76,1,0,0,0,558,559,7,11,0,0,559,560,7,12,0,0,560,78,
			1,0,0,0,561,562,7,11,0,0,562,563,7,12,0,0,563,564,7,6,0,0,564,565,
			7,9,0,0,565,566,7,8,0,0,566,567,7,11,0,0,567,568,7,2,0,0,568,569,
			7,10,0,0,569,80,1,0,0,0,570,571,7,11,0,0,571,572,7,12,0,0,572,573,
			7,18,0,0,573,574,7,15,0,0,574,575,7,8,0,0,575,82,1,0,0,0,576,577,
			7,11,0,0,577,578,7,4,0,0,578,84,1,0,0,0,579,580,7,10,0,0,580,581,
			7,2,0,0,581,582,7,3,0,0,582,583,7,6,0,0,583,584,7,10,0,0,584,86,
			1,0,0,0,585,586,7,10,0,0,586,587,7,11,0,0,587,588,7,3,0,0,588,589,
			7,9,0,0,589,590,7,2,0,0,590,591,7,9,0,0,591,592,7,16,0,0,592,88,
			1,0,0,0,593,594,7,10,0,0,594,595,7,11,0,0,595,596,7,12,0,0,596,597,
			7,19,0,0,597,598,7,2,0,0,598,599,7,17,0,0,599,600,7,6,0,0,600,90,
			1,0,0,0,601,602,7,10,0,0,602,603,7,18,0,0,603,604,7,18,0,0,604,605,
			7,21,0,0,605,92,1,0,0,0,606,607,7,20,0,0,607,608,7,2,0,0,608,609,
			7,21,0,0,609,94,1,0,0,0,610,611,7,20,0,0,611,612,7,18,0,0,612,613,
			7,13,0,0,613,96,1,0,0,0,614,615,7,12,0,0,615,616,7,2,0,0,616,617,
			7,12,0,0,617,618,7,13,0,0,618,98,1,0,0,0,619,620,7,12,0,0,620,621,
			7,6,0,0,621,622,7,22,0,0,622,100,1,0,0,0,623,624,7,12,0,0,624,625,
			7,6,0,0,625,626,7,23,0,0,626,627,7,8,0,0,627,102,1,0,0,0,628,629,
			7,12,0,0,629,630,7,18,0,0,630,631,7,9,0,0,631,104,1,0,0,0,632,633,
			7,12,0,0,633,634,7,18,0,0,634,635,7,8,0,0,635,106,1,0,0,0,636,637,
			7,12,0,0,637,638,7,15,0,0,638,639,7,10,0,0,639,640,7,10,0,0,640,
			108,1,0,0,0,641,642,7,18,0,0,642,643,7,7,0,0,643,110,1,0,0,0,644,
			645,7,18,0,0,645,646,7,12,0,0,646,112,1,0,0,0,647,648,7,18,0,0,648,
			649,7,21,0,0,649,650,7,6,0,0,650,651,7,12,0,0,651,114,1,0,0,0,652,
			653,7,18,0,0,653,654,7,9,0,0,654,116,1,0,0,0,655,656,7,18,0,0,656,
			657,7,8,0,0,657,658,7,14,0,0,658,659,7,6,0,0,659,660,7,9,0,0,660,
			661,7,4,0,0,661,118,1,0,0,0,662,663,7,18,0,0,663,664,7,15,0,0,664,
			665,7,8,0,0,665,120,1,0,0,0,666,667,7,21,0,0,667,668,7,2,0,0,668,
			669,7,5,0,0,669,670,7,19,0,0,670,671,7,2,0,0,671,672,7,17,0,0,672,
			673,7,6,0,0,673,122,1,0,0,0,674,675,7,21,0,0,675,676,7,18,0,0,676,
			677,7,9,0,0,677,678,7,8,0,0,678,124,1,0,0,0,679,680,7,21,0,0,680,
			681,7,18,0,0,681,682,7,4,0,0,682,683,7,8,0,0,683,684,7,21,0,0,684,
			685,7,18,0,0,685,686,7,12,0,0,686,687,7,6,0,0,687,688,7,13,0,0,688,
			126,1,0,0,0,689,690,7,21,0,0,690,691,7,9,0,0,691,692,7,18,0,0,692,
			693,7,5,0,0,693,694,7,6,0,0,694,695,7,4,0,0,695,696,7,4,0,0,696,
			128,1,0,0,0,697,698,7,21,0,0,698,699,7,9,0,0,699,700,7,18,0,0,700,
			701,7,5,0,0,701,702,7,6,0,0,702,703,7,13,0,0,703,704,7,15,0,0,704,
			705,7,9,0,0,705,706,7,6,0,0,706,130,1,0,0,0,707,708,7,21,0,0,708,
			709,7,15,0,0,709,710,7,9,0,0,710,711,7,6,0,0,711,132,1,0,0,0,712,
			713,7,9,0,0,713,714,7,2,0,0,714,715,7,12,0,0,715,716,7,17,0,0,716,
			717,7,6,0,0,717,134,1,0,0,0,718,719,7,9,0,0,719,720,7,6,0,0,720,
			721,7,24,0,0,721,722,7,6,0,0,722,723,7,5,0,0,723,724,7,8,0,0,724,
			136,1,0,0,0,725,726,7,9,0,0,726,727,7,6,0,0,727,728,7,20,0,0,728,
			138,1,0,0,0,729,730,7,9,0,0,730,731,7,6,0,0,731,732,7,5,0,0,732,
			733,7,18,0,0,733,734,7,9,0,0,734,735,7,13,0,0,735,140,1,0,0,0,736,
			737,7,9,0,0,737,738,7,6,0,0,738,739,7,17,0,0,739,740,7,11,0,0,740,
			741,7,4,0,0,741,742,7,8,0,0,742,743,7,6,0,0,743,744,7,9,0,0,744,
			142,1,0,0,0,745,746,7,9,0,0,746,747,7,6,0,0,747,748,7,21,0,0,748,
			749,7,18,0,0,749,750,7,9,0,0,750,751,7,8,0,0,751,144,1,0,0,0,752,
			753,7,9,0,0,753,754,7,6,0,0,754,755,7,8,0,0,755,756,7,15,0,0,756,
			757,7,9,0,0,757,758,7,12,0,0,758,146,1,0,0,0,759,760,7,9,0,0,760,
			761,7,18,0,0,761,762,7,10,0,0,762,148,1,0,0,0,763,764,7,9,0,0,764,
			765,7,18,0,0,765,766,7,9,0,0,766,150,1,0,0,0,767,768,7,4,0,0,768,
			769,7,6,0,0,769,770,7,10,0,0,770,771,7,6,0,0,771,772,7,5,0,0,772,
			773,7,8,0,0,773,152,1,0,0,0,774,775,7,4,0,0,775,776,7,6,0,0,776,
			777,7,25,0,0,777,778,7,6,0,0,778,779,7,9,0,0,779,780,7,11,0,0,780,
			781,7,8,0,0,781,782,7,16,0,0,782,154,1,0,0,0,783,784,7,4,0,0,784,
			785,7,14,0,0,785,786,7,2,0,0,786,787,7,9,0,0,787,788,7,6,0,0,788,
			789,7,13,0,0,789,156,1,0,0,0,790,791,7,4,0,0,791,792,7,11,0,0,792,
			793,7,17,0,0,793,794,7,12,0,0,794,795,7,2,0,0,795,796,7,10,0,0,796,
			158,1,0,0,0,797,798,7,4,0,0,798,799,7,10,0,0,799,800,7,2,0,0,800,
			160,1,0,0,0,801,802,7,4,0,0,802,803,7,10,0,0,803,804,7,10,0,0,804,
			162,1,0,0,0,805,806,7,4,0,0,806,807,7,9,0,0,807,808,7,2,0,0,808,
			164,1,0,0,0,809,810,7,4,0,0,810,811,7,9,0,0,811,812,7,10,0,0,812,
			166,1,0,0,0,813,814,7,4,0,0,814,815,7,15,0,0,815,816,7,3,0,0,816,
			817,7,8,0,0,817,818,7,16,0,0,818,819,7,21,0,0,819,820,7,6,0,0,820,
			168,1,0,0,0,821,822,7,8,0,0,822,823,7,14,0,0,823,824,7,6,0,0,824,
			825,7,12,0,0,825,170,1,0,0,0,826,827,7,8,0,0,827,828,7,18,0,0,828,
			172,1,0,0,0,829,830,7,8,0,0,830,831,7,9,0,0,831,832,7,2,0,0,832,
			833,7,12,0,0,833,834,7,4,0,0,834,835,7,21,0,0,835,836,7,18,0,0,836,
			837,7,9,0,0,837,838,7,8,0,0,838,174,1,0,0,0,839,840,7,8,0,0,840,
			841,7,16,0,0,841,842,7,21,0,0,842,843,7,6,0,0,843,176,1,0,0,0,844,
			845,7,15,0,0,845,846,7,12,0,0,846,847,7,2,0,0,847,848,7,7,0,0,848,
			849,7,7,0,0,849,850,7,6,0,0,850,851,7,5,0,0,851,852,7,8,0,0,852,
			853,7,6,0,0,853,854,7,13,0,0,854,178,1,0,0,0,855,856,7,15,0,0,856,
			857,7,12,0,0,857,858,7,11,0,0,858,859,7,8,0,0,859,860,7,4,0,0,860,
			180,1,0,0,0,861,862,7,15,0,0,862,863,7,12,0,0,863,864,7,8,0,0,864,
			865,7,11,0,0,865,866,7,10,0,0,866,182,1,0,0,0,867,868,7,15,0,0,868,
			869,7,4,0,0,869,870,7,6,0,0,870,184,1,0,0,0,871,872,7,25,0,0,872,
			873,7,2,0,0,873,874,7,9,0,0,874,875,7,11,0,0,875,876,7,2,0,0,876,
			877,7,3,0,0,877,878,7,10,0,0,878,879,7,6,0,0,879,186,1,0,0,0,880,
			881,7,22,0,0,881,882,7,2,0,0,882,883,7,11,0,0,883,884,7,8,0,0,884,
			188,1,0,0,0,885,886,7,22,0,0,886,887,7,11,0,0,887,888,7,8,0,0,888,
			889,7,14,0,0,889,190,1,0,0,0,890,891,7,22,0,0,891,892,7,14,0,0,892,
			893,7,6,0,0,893,894,7,12,0,0,894,192,1,0,0,0,895,896,7,22,0,0,896,
			897,7,14,0,0,897,898,7,11,0,0,898,899,7,10,0,0,899,900,7,6,0,0,900,
			194,1,0,0,0,901,902,7,23,0,0,902,903,7,12,0,0,903,904,7,18,0,0,904,
			905,7,9,0,0,905,196,1,0,0,0,906,907,7,23,0,0,907,908,7,18,0,0,908,
			909,7,9,0,0,909,198,1,0,0,0,910,911,5,61,0,0,911,200,1,0,0,0,912,
			913,5,47,0,0,913,914,5,61,0,0,914,202,1,0,0,0,915,916,5,60,0,0,916,
			204,1,0,0,0,917,918,5,60,0,0,918,919,5,61,0,0,919,920,5,41,0,0,920,
			206,1,0,0,0,921,922,5,62,0,0,922,208,1,0,0,0,923,924,5,62,0,0,924,
			925,5,61,0,0,925,210,1,0,0,0,926,927,5,43,0,0,927,212,1,0,0,0,928,
			929,5,45,0,0,929,214,1,0,0,0,930,931,5,42,0,0,931,216,1,0,0,0,932,
			933,5,47,0,0,933,218,1,0,0,0,934,935,5,42,0,0,935,936,5,42,0,0,936,
			220,1,0,0,0,937,938,5,38,0,0,938,222,1,0,0,0,939,940,5,61,0,0,940,
			941,5,62,0,0,941,224,1,0,0,0,942,943,5,60,0,0,943,944,5,61,0,0,944,
			226,1,0,0,0,945,946,5,58,0,0,946,947,5,61,0,0,947,228,1,0,0,0,948,
			949,5,60,0,0,949,950,5,62,0,0,950,230,1,0,0,0,951,952,5,40,0,0,952,
			232,1,0,0,0,953,954,5,41,0,0,954,234,1,0,0,0,955,956,5,91,0,0,956,
			236,1,0,0,0,957,958,5,93,0,0,958,238,1,0,0,0,959,960,5,58,0,0,960,
			240,1,0,0,0,961,962,5,59,0,0,962,242,1,0,0,0,963,964,5,44,0,0,964,
			244,1,0,0,0,965,966,5,124,0,0,966,246,1,0,0,0,967,968,5,46,0,0,968,
			248,1,0,0,0,969,970,5,39,0,0,970,250,1,0,0,0,971,972,7,26,0,0,972,
			252,1,0,0,0,973,974,7,27,0,0,974,254,1,0,0,0,975,976,7,28,0,0,976,
			256,1,0,0,0,977,981,7,27,0,0,978,980,7,29,0,0,979,978,1,0,0,0,980,
			983,1,0,0,0,981,979,1,0,0,0,981,982,1,0,0,0,982,258,1,0,0,0,983,
			981,1,0,0,0,984,989,3,255,127,0,985,988,5,95,0,0,986,988,3,255,127,
			0,987,985,1,0,0,0,987,986,1,0,0,0,988,991,1,0,0,0,989,987,1,0,0,
			0,989,990,1,0,0,0,990,260,1,0,0,0,991,989,1,0,0,0,992,994,7,6,0,
			0,993,995,7,30,0,0,994,993,1,0,0,0,994,995,1,0,0,0,995,996,1,0,0,
			0,996,997,3,257,128,0,997,262,1,0,0,0,998,999,3,257,128,0,999,1000,
			5,46,0,0,1000,1002,3,257,128,0,1001,1003,3,261,130,0,1002,1001,1,
			0,0,0,1002,1003,1,0,0,0,1003,264,1,0,0,0,1004,1005,3,257,128,0,1005,
			1006,5,35,0,0,1006,1009,3,259,129,0,1007,1008,5,46,0,0,1008,1010,
			3,259,129,0,1009,1007,1,0,0,0,1009,1010,1,0,0,0,1010,1011,1,0,0,
			0,1011,1013,5,35,0,0,1012,1014,3,261,130,0,1013,1012,1,0,0,0,1013,
			1014,1,0,0,0,1014,266,1,0,0,0,1015,1019,3,257,128,0,1016,1019,3,
			263,131,0,1017,1019,3,265,132,0,1018,1015,1,0,0,0,1018,1016,1,0,
			0,0,1018,1017,1,0,0,0,1019,268,1,0,0,0,1020,1021,7,3,0,0,1021,1023,
			5,34,0,0,1022,1024,7,31,0,0,1023,1022,1,0,0,0,1024,1025,1,0,0,0,
			1025,1023,1,0,0,0,1025,1026,1,0,0,0,1026,1027,1,0,0,0,1027,1028,
			5,34,0,0,1028,270,1,0,0,0,1029,1030,7,18,0,0,1030,1032,5,34,0,0,
			1031,1033,7,32,0,0,1032,1031,1,0,0,0,1033,1034,1,0,0,0,1034,1032,
			1,0,0,0,1034,1035,1,0,0,0,1035,1036,1,0,0,0,1036,1037,5,34,0,0,1037,
			272,1,0,0,0,1038,1039,7,13,0,0,1039,1041,5,34,0,0,1040,1042,7,29,
			0,0,1041,1040,1,0,0,0,1042,1043,1,0,0,0,1043,1041,1,0,0,0,1043,1044,
			1,0,0,0,1044,1045,1,0,0,0,1045,1046,5,34,0,0,1046,274,1,0,0,0,1047,
			1048,7,23,0,0,1048,1050,5,34,0,0,1049,1051,7,33,0,0,1050,1049,1,
			0,0,0,1051,1052,1,0,0,0,1052,1050,1,0,0,0,1052,1053,1,0,0,0,1053,
			1054,1,0,0,0,1054,1055,5,34,0,0,1055,276,1,0,0,0,1056,1061,3,269,
			134,0,1057,1061,3,271,135,0,1058,1061,3,273,136,0,1059,1061,3,275,
			137,0,1060,1056,1,0,0,0,1060,1057,1,0,0,0,1060,1058,1,0,0,0,1060,
			1059,1,0,0,0,1061,278,1,0,0,0,1062,1063,5,39,0,0,1063,1064,9,0,0,
			0,1064,1065,5,39,0,0,1065,280,1,0,0,0,1066,1072,5,34,0,0,1067,1071,
			8,34,0,0,1068,1069,5,34,0,0,1069,1071,5,34,0,0,1070,1067,1,0,0,0,
			1070,1068,1,0,0,0,1071,1074,1,0,0,0,1072,1070,1,0,0,0,1072,1073,
			1,0,0,0,1073,1075,1,0,0,0,1074,1072,1,0,0,0,1075,1076,5,34,0,0,1076,
			282,1,0,0,0,1077,1083,7,26,0,0,1078,1079,5,95,0,0,1079,1082,7,28,
			0,0,1080,1082,7,28,0,0,1081,1078,1,0,0,0,1081,1080,1,0,0,0,1082,
			1085,1,0,0,0,1083,1081,1,0,0,0,1083,1084,1,0,0,0,1084,284,1,0,0,
			0,1085,1083,1,0,0,0,1086,1088,5,92,0,0,1087,1089,7,35,0,0,1088,1087,
			1,0,0,0,1089,1090,1,0,0,0,1090,1088,1,0,0,0,1090,1091,1,0,0,0,1091,
			1092,1,0,0,0,1092,1093,5,92,0,0,1093,286,1,0,0,0,1094,1097,3,283,
			141,0,1095,1097,3,285,142,0,1096,1094,1,0,0,0,1096,1095,1,0,0,0,
			1097,288,1,0,0,0,28,0,292,302,313,981,987,989,994,1002,1009,1013,
			1018,1023,1025,1032,1034,1041,1043,1050,1052,1060,1070,1072,1081,
			1083,1088,1090,1096,2,0,2,0,0,3,0
	)


class VHDLLexer(Lexer):
	atn = ATNDeserializer().deserialize(serializedATN())

	decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

	WHITESPACE_CHANNEL = 2
	COMMENT_CHANNEL = 3

	WHITESPACE = 1
	COMMENT_LINE = 2
	COMMENT_BLOCK = 3
	OP_ABS = 4
	KW_ACCESS = 5
	KW_AFTER = 6
	KW_ALIAS = 7
	KW_ALL = 8
	OP_AND = 9
	KW_ARCHITECTURE = 10
	KW_ARRAY = 11
	KW_ASSERT = 12
	KW_ATTRIBUTE = 13
	KW_BEGIN = 14
	KW_BLOCK = 15
	KW_BODY = 16
	KW_BUFFER = 17
	KW_BUS = 18
	KW_CASE = 19
	KW_COMPONENT = 20
	KW_CONFIGURATION = 21
	KW_CONSTANT = 22
	KW_DISCONNECT = 23
	KW_DOWNTO = 24
	KW_END = 25
	KW_ENTITY = 26
	KW_ELSE = 27
	KW_ELSIF = 28
	KW_EXIT = 29
	KW_FILE = 30
	KW_FOR = 31
	KW_FUNCTION = 32
	KW_GENERATE = 33
	KW_GENERIC = 34
	KW_GROUP = 35
	KW_GUARDED = 36
	KW_IF = 37
	KW_IMPURE = 38
	KW_IN = 39
	KW_INERTIAL = 40
	KW_INOUT = 41
	KW_IS = 42
	KW_LABEL = 43
	KW_LIBRARY = 44
	KW_LINKAGE = 45
	KW_LOOP = 46
	KW_MAP = 47
	OP_MOD = 48
	OP_NAND = 49
	KW_NEW = 50
	KW_NEXT = 51
	OP_NOR = 52
	OP_NOT = 53
	KW_NULL = 54
	KW_OF = 55
	KW_ON = 56
	KW_OPEN = 57
	OP_OR = 58
	KW_OTHERS = 59
	KW_OUT = 60
	KW_PACKAGE = 61
	KW_PORT = 62
	KW_POSTPONED = 63
	KW_PROCESS = 64
	KW_PROCEDURE = 65
	KW_PURE = 66
	KW_RANGE = 67
	KW_REJECT = 68
	OP_REM = 69
	KW_RECORD = 70
	KW_REGISTER = 71
	KW_REPORT = 72
	KW_RETURN = 73
	OP_ROL = 74
	OP_ROR = 75
	KW_SELECT = 76
	KW_SEVERITY = 77
	KW_SHARED = 78
	KW_SIGNAL = 79
	OP_SLA = 80
	OP_SLL = 81
	OP_SRA = 82
	OP_SRL = 83
	KW_SUBTYPE = 84
	KW_THEN = 85
	KW_TO = 86
	KW_TRANSPORT = 87
	KW_TYPE = 88
	KW_UNAFFECTED = 89
	KW_UNITS = 90
	KW_UNTIL = 91
	KW_USE = 92
	KW_VARIABLE = 93
	KW_WAIT = 94
	KW_WITH = 95
	KW_WHEN = 96
	KW_WHILE = 97
	OP_XNOR = 98
	OP_XOR = 99
	OP_EQ = 100
	OP_NE = 101
	OP_LT = 102
	OP_LE = 103
	OP_GT = 104
	OP_GE = 105
	OP_PLUS = 106
	OP_MINUS = 107
	OP_MUL = 108
	OP_DIV = 109
	OP_POW = 110
	OP_CONCAT = 111
	TOK_RARROW = 112
	TOK_SIG_ASSIGN = 113
	TOK_VAR_ASSIGN = 114
	TOK_BOX = 115
	TOK_LP = 116
	TOK_RP = 117
	TOK_LB = 118
	TOK_RB = 119
	TOK_COLON = 120
	TOK_SEMICOL = 121
	TOK_COMMA = 122
	TOK_BAR = 123
	TOK_DOT = 124
	TOK_APOSTROPHE = 125
	LIT_ABSTRACT = 126
	LIT_BIT_STRING = 127
	LIT_CHARACTER = 128
	LIT_STRING = 129
	LIT_IDENTIFIER = 130

	channelNames = ("DEFAULT_TOKEN_CHANNEL", "HIDDEN", "WHITESPACE_CHANNEL", "COMMENT_CHANNEL")

	modeNames = ["DEFAULT_MODE"]

	literalNames = ( "<INVALID>",
					"'abs'", "'access'", "'after'", "'alias'", "'all'", "'and'",
					"'architecture'", "'array'", "'assert'", "'attribute'", "'begin'",
					"'block'", "'body'", "'buffer'", "'bus'", "'case'", "'component'",
					"'configuration'", "'constant'", "'disconnect'", "'downto'",
					"'end'", "'entity'", "'else'", "'elsif'", "'exit'", "'file'",
					"'for'", "'function'", "'generate'", "'generic'", "'group'",
					"'guarded'", "'if'", "'impure'", "'in'", "'inertial'", "'inout'",
					"'is'", "'label'", "'library'", "'linkage'", "'loop'", "'map'",
					"'mod'", "'nand'", "'new'", "'next'", "'nor'", "'not'", "'null'",
					"'of'", "'on'", "'open'", "'or'", "'others'", "'out'", "'package'",
					"'port'", "'postponed'", "'process'", "'procedure'", "'pure'",
					"'range'", "'reject'", "'rem'", "'record'", "'register'", "'report'",
					"'return'", "'rol'", "'ror'", "'select'", "'severity'", "'shared'",
					"'signal'", "'sla'", "'sll'", "'sra'", "'srl'", "'subtype'",
					"'then'", "'to'", "'transport'", "'type'", "'unaffected'", "'units'",
					"'until'", "'use'", "'variable'", "'wait'", "'with'", "'when'",
					"'while'", "'xnor'", "'xor'", "'='", "'/='", "'<'", "'<=)'",
					"'>'", "'>='", "'+'", "'-'", "'*'", "'/'", "'**'", "'&'", "'=>'",
					"'<='", "':='", "'<>'", "'('", "')'", "'['", "']'", "':'", "';'",
					"','", "'|'", "'.'", "'''")

	symbolicNames = ( "<INVALID>",
					"WHITESPACE", "COMMENT_LINE", "COMMENT_BLOCK", "OP_ABS", "KW_ACCESS",
					"KW_AFTER", "KW_ALIAS", "KW_ALL", "OP_AND", "KW_ARCHITECTURE",
					"KW_ARRAY", "KW_ASSERT", "KW_ATTRIBUTE", "KW_BEGIN", "KW_BLOCK",
					"KW_BODY", "KW_BUFFER", "KW_BUS", "KW_CASE", "KW_COMPONENT",
					"KW_CONFIGURATION", "KW_CONSTANT", "KW_DISCONNECT", "KW_DOWNTO",
					"KW_END", "KW_ENTITY", "KW_ELSE", "KW_ELSIF", "KW_EXIT", "KW_FILE",
					"KW_FOR", "KW_FUNCTION", "KW_GENERATE", "KW_GENERIC", "KW_GROUP",
					"KW_GUARDED", "KW_IF", "KW_IMPURE", "KW_IN", "KW_INERTIAL",
					"KW_INOUT", "KW_IS", "KW_LABEL", "KW_LIBRARY", "KW_LINKAGE",
					"KW_LOOP", "KW_MAP", "OP_MOD", "OP_NAND", "KW_NEW", "KW_NEXT",
					"OP_NOR", "OP_NOT", "KW_NULL", "KW_OF", "KW_ON", "KW_OPEN",
					"OP_OR", "KW_OTHERS", "KW_OUT", "KW_PACKAGE", "KW_PORT", "KW_POSTPONED",
					"KW_PROCESS", "KW_PROCEDURE", "KW_PURE", "KW_RANGE", "KW_REJECT",
					"OP_REM", "KW_RECORD", "KW_REGISTER", "KW_REPORT", "KW_RETURN",
					"OP_ROL", "OP_ROR", "KW_SELECT", "KW_SEVERITY", "KW_SHARED",
					"KW_SIGNAL", "OP_SLA", "OP_SLL", "OP_SRA", "OP_SRL", "KW_SUBTYPE",
					"KW_THEN", "KW_TO", "KW_TRANSPORT", "KW_TYPE", "KW_UNAFFECTED",
					"KW_UNITS", "KW_UNTIL", "KW_USE", "KW_VARIABLE", "KW_WAIT",
					"KW_WITH", "KW_WHEN", "KW_WHILE", "OP_XNOR", "OP_XOR", "OP_EQ",
					"OP_NE", "OP_LT", "OP_LE", "OP_GT", "OP_GE", "OP_PLUS", "OP_MINUS",
					"OP_MUL", "OP_DIV", "OP_POW", "OP_CONCAT", "TOK_RARROW", "TOK_SIG_ASSIGN",
					"TOK_VAR_ASSIGN", "TOK_BOX", "TOK_LP", "TOK_RP", "TOK_LB", "TOK_RB",
					"TOK_COLON", "TOK_SEMICOL", "TOK_COMMA", "TOK_BAR", "TOK_DOT",
					"TOK_APOSTROPHE", "LIT_ABSTRACT", "LIT_BIT_STRING", "LIT_CHARACTER",
					"LIT_STRING", "LIT_IDENTIFIER" )

	ruleNames = ( "WHITESPACE", "COMMENT_LINE", "COMMENT_BLOCK", "OP_ABS",
								"KW_ACCESS", "KW_AFTER", "KW_ALIAS", "KW_ALL", "OP_AND",
								"KW_ARCHITECTURE", "KW_ARRAY", "KW_ASSERT", "KW_ATTRIBUTE",
								"KW_BEGIN", "KW_BLOCK", "KW_BODY", "KW_BUFFER", "KW_BUS",
								"KW_CASE", "KW_COMPONENT", "KW_CONFIGURATION", "KW_CONSTANT",
								"KW_DISCONNECT", "KW_DOWNTO", "KW_END", "KW_ENTITY", "KW_ELSE",
								"KW_ELSIF", "KW_EXIT", "KW_FILE", "KW_FOR", "KW_FUNCTION",
								"KW_GENERATE", "KW_GENERIC", "KW_GROUP", "KW_GUARDED",
								"KW_IF", "KW_IMPURE", "KW_IN", "KW_INERTIAL", "KW_INOUT",
								"KW_IS", "KW_LABEL", "KW_LIBRARY", "KW_LINKAGE", "KW_LOOP",
								"KW_MAP", "OP_MOD", "OP_NAND", "KW_NEW", "KW_NEXT", "OP_NOR",
								"OP_NOT", "KW_NULL", "KW_OF", "KW_ON", "KW_OPEN", "OP_OR",
								"KW_OTHERS", "KW_OUT", "KW_PACKAGE", "KW_PORT", "KW_POSTPONED",
								"KW_PROCESS", "KW_PROCEDURE", "KW_PURE", "KW_RANGE", "KW_REJECT",
								"OP_REM", "KW_RECORD", "KW_REGISTER", "KW_REPORT", "KW_RETURN",
								"OP_ROL", "OP_ROR", "KW_SELECT", "KW_SEVERITY", "KW_SHARED",
								"KW_SIGNAL", "OP_SLA", "OP_SLL", "OP_SRA", "OP_SRL", "KW_SUBTYPE",
								"KW_THEN", "KW_TO", "KW_TRANSPORT", "KW_TYPE", "KW_UNAFFECTED",
								"KW_UNITS", "KW_UNTIL", "KW_USE", "KW_VARIABLE", "KW_WAIT",
								"KW_WITH", "KW_WHEN", "KW_WHILE", "OP_XNOR", "OP_XOR",
								"OP_EQ", "OP_NE", "OP_LT", "OP_LE", "OP_GT", "OP_GE",
								"OP_PLUS", "OP_MINUS", "OP_MUL", "OP_DIV", "OP_POW", "OP_CONCAT",
								"TOK_RARROW", "TOK_SIG_ASSIGN", "TOK_VAR_ASSIGN", "TOK_BOX",
								"TOK_LP", "TOK_RP", "TOK_LB", "TOK_RB", "TOK_COLON", "TOK_SEMICOL",
								"TOK_COMMA", "TOK_BAR", "TOK_DOT", "TOK_APOSTROPHE", "Letter",
								"Digit", "ExtendedDigit", "Integer", "BasedInteger", "Exponent",
								"Real", "BaseLiteral", "LIT_ABSTRACT", "BinaryBitString",
								"OctalBitString", "DecimalBitString", "HexBitString",
								"LIT_BIT_STRING", "LIT_CHARACTER", "LIT_STRING", "BasicIdentifier",
								"ExtendedIdentifier", "LIT_IDENTIFIER")

	grammarFileName = "VHDLLexer.g4"

	def __init__(self, input=None, output: TextIO = stdout):
		super().__init__(input, output)
		self.checkVersion("4.10.1")
		self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
		self._actions = None
		self._predicates = None
