from LexerV1 import lexer

print(lexer("Codigo"))
print(lexer("juan"))
print(lexer("5"))
print(lexer("finsi"))
print(lexer("oprel"))
print(lexer("leer"))

# No logramos solucianar este error, no identifica bien los espacios en blanco

print(lexer("oprel finsi"))
print(lexer("leer 5 finsi"))
print(lexer("5 leer"))
print(lexer("leer 10"))

# En este caso separa el primer termino pero luego toma todo como una id
print(lexer("8 opmult 3"))
print(lexer("2 opsuma 7"))
