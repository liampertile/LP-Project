from LexerV1_corregido import lexer

print(lexer("Codigo"))
print(lexer("juan"))
print(lexer("5"))
print(lexer("finsi"))
print(lexer("oprel"))
print(lexer("leer"))
print(lexer("oprel finsi"))
print(lexer("leer 5 finsi"))
print(lexer("5 leer"))
print(lexer("leer 10"))
print(lexer("8 + 3"))
print(lexer("2 * 6"))
print(lexer('+ 5'))
print(lexer("juan = 7 y lucia <= 4"))
print(lexer("var(finsi)"))
print(lexer("func(x) = x**2"))
print(lexer("3<>4"))


print(lexer("233"))
