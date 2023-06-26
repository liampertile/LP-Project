from AFD import *

TOKENS_POSIBLES = [("TOKEN leer", afd_leer), ("TOKEN ID", afd_id), ("TOKEN NUM", afd_num), ("TOKEN si", afd_si), ("TOKEN sino", afd_sino), ("TOKEN finsi", afd_finsi), ("TOKEN repetir", afd_repetir), ("TOKEN hasta", afd_hasta), ("TOKEN equal", afd_equal), ("TOKEN func", afd_func),
                   ("TOKEN finfunc", afd_finfunc), ("TOKEN oprel", afd_oprel), ("TOKEN opsuma", afd_opsuma), ("TOKEN opmult", afd_opmult), ("TOKEN parentesisIzq", afd_parentesisIzq), ("TOKEN parentesisDer", afd_parentesisDer), ("TOKEN puntoycoma", afd_puntoycoma)]

tokens = []
tokensErroneos = []


def caeEnTrampa(cadena):
    for (tipoToken, afd) in TOKENS_POSIBLES:
        resultado = afd(cadena)
        if resultado == ESTADO_ACEPTADO or resultado == ESTADO_NO_ACEPTADO:
            return False
    return True


def guardarToken(cadena):
    global tokens
    for (tipoToken, afd) in TOKENS_POSIBLES:
        resultado = afd(cadena)
        if resultado == ESTADO_ACEPTADO:
            tokens.append((tipoToken, cadena))
            return


def lexer(codigofuente):
    global tokens, tokensErroneos
    tokens = []
    tokensErroneos = []
    inicio = 0

    while inicio < len(codigofuente):
        while codigofuente[inicio].isspace():
            inicio += 1

        final = inicio + 1
        lexema = codigofuente[inicio:final]

        while final <= len(codigofuente) and not caeEnTrampa(lexema):
            final += 1
            lexema = codigofuente[inicio:final]

        if final > inicio + 1:
            guardarToken(codigofuente[inicio:final-1])
            inicio = final - 1
        else:
            tokensErroneos.append(codigofuente[inicio])
            inicio += 1

    return tokens
