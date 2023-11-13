from LexerV2 import lexer
from ParserV1 import traduccionParser, parser

# Pruebas:
#parser(traduccionParser(lexer("leer var")))
#parser(traduccionParser(lexer("aux equal 5")))
#parser(traduccionParser(lexer("func aux (aux2) leer aux3 finfunc")))
#parser(traduccionParser(lexer("aux equal 9")))
#parser(traduccionParser(lexer("mostrar 5")))
#parser(traduccionParser(lexer("repetir mostrar 3 hasta aux3")))
#parser(traduccionParser(lexer("si 5>5 entonces mostrar x+6 finsi")))
#parser(traduccionParser(lexer("mostrar x+3")))
#parser(traduccionParser(lexer("func rest(n1; n2) x equal n1 - n2; mostrar x finfunc")))
#parser(traduccionParser(lexer("mostrar x + 5")))
#parser(traduccionParser(lexer("func hello(x) hello equal 1234; mostrar hello finfunc")))
#parser(traduccionParser(lexer("mostrar x equal 5"))) # NO PERTENECE AL LENGUAJE
#parser(traduccionParser(lexer("repetir leer vuxi hasta vauxi > variable")))
#parser(traduccionParser(lexer("leer variable")))
#parser(traduccionParser(lexer("si 5>5 entonces mostrar x + 5 finsi")))
#parser(traduccionParser(lexer("si 5>5 entonces mostrar id1  mostrar id2 finsi"))) #NO PERTENECE AL LENGUAJE
#parser(traduccionParser(lexer("leer x; leer y; si x>y entonces x equal x+y sino y equal x+y finsi")))
#parser(traduccionParser(lexer("func rest(n1; n2) x equal n1 - n2; mostrar x finfunc")))
#parser(traduccionParser(lexer("vmax equal 0; repetir i equal i+1; si edad>vmax entonces pepe equal pepe2 finsi hasta i=50")))