from LexerV2 import lexer
from ParserV1 import traduccionParser, parser

# Pruebas:
parser(traduccionParser(lexer("leer var")))
parser(traduccionParser(lexer("aux equal 5")))
parser(traduccionParser(lexer("func aux (aux2) leer aux3 finfunc")))
parser(traduccionParser(lexer("aux equal 9")))
parser(traduccionParser(lexer("mostrar 5")))
parser(traduccionParser(lexer("repetir mostrar 3 hasta aux3")))
