# Importo el módulo AFD'S

from AFD import *

# Duplas
TOKENS_POSIBLES = [("TOKEN ID", afd_id), ("TOKEN NUM", afd_num), ("TOKEN si", afd_si), ("TOKEN sino", afd_sino), ("TOKEN finsi", afd_finsi), ("TOKEN repetir", afd_repetir), ("TOKEN hasta", afd_hasta), ("TOKEN equal", afd_equal), ("TOKEN func", afd_func), ("TOKEN finfunc", afd_finfunc), ("TOKEN oprel", afd_oprel), ("TOKEN opsuma", afd_opsuma),
                   ("TOKEN opmult", afd_opmult), ("TOKEN parentesisIzq", afd_parentesisIzq), ("TOKEN parentesisDer", afd_parentesisDer), ("TOKEN puntoycoma", afd_puntoycoma),]

tokens = []

# cadenas que terminen en estado trampa


def caeEnTrampa(cadena):
    todosCaen = True

    # Corro la cadena
    for (tipoToken, afd) in TOKENS_POSIBLES:
        resultado = afd(cadena)
        # Si queda en No aceptado o aceptado
        if resultado == (ESTADO_ACEPTADO or ESTADO_NO_ACEPTADO):
            todosCaen = False
            break

    return caeEnTrampa

# guardar el token de cadena en la lista "tokens"


def guardarToken(cadena):
    global tokens

    # Corremos el cadena en todos los automatas

    for (tipoToken, afd) in TOKENS_POSIBLES:
        resultado = afd(cadena)

        if resultado == (ESTADO_ACEPTADO):
            tokens.append((tipoToken, cadena))

        break


def lexer(codigofuente):
    codigofuente += ""
    global tokens
    tokens = []
    tokensErroneos = []
    inicio = 0
    final = 1

    while final <= len(codigofuente):
        while codigofuente[inicio].isspace():
            inicio += 1
            final += 1

            if inicio == len(codigofuente):
                break
        lexema = codigofuente[inicio: final]

        # cuando no se generen estados trampas en los afd le seguimos metiendo caracteres
        while not caeEnTrampa(lexema):
            final += 1
            lexema = codigofuente[inicio:final]

        final -= 1
        guardarToken(codigofuente[inicio:final])

        if inicio == final:
            tokensErroneos.append(codigofuente[inicio])
            inicio += 1
            final += 2
        else:
            inicio = final
            final = inicio + 1

        if final == len(codigofuente):
            break

    return tokens


print(lexer("Codigo"))
