from LexerV2 import lexer
from ParserV1 import traduccionParser,parser

parser(traduccionParser(lexer("aux equal 5")))