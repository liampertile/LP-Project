from LexerV2 import lexer
from ParserV1 import traduccionParser,parser

#parser(traduccionParser(lexer("leer aux")))
#parser(traduccionParser(lexer("aux equal 5")))
parser(traduccionParser(lexer("repetir aux equal 3 hasta 8")))
# #parser(traduccionParser(lexer("aux equal 5")))
# parser(traduccionParser(lexer("aux equal 5")))
#parser(traduccionParser(lexer("mostrar 5")))


