from AFD import *

TOKENS_POSIBLES = [("TOKEN leer", afd_leer),
                   ("TOKEN si", afd_si),
                   ("TOKEN sino", afd_sino),
                   ("TOKEN finsi", afd_finsi),
                   ("TOKEN repetir", afd_repetir),
                   ("TOKEN hasta", afd_hasta),
                   ("TOKEN mostrar", afd_mostrar),
                   ("TOKEN equal", afd_equal),
                   ("TOKEN func", afd_func),
                   ("TOKEN finfunc", afd_finfunc),
                   ("TOKEN oprel", afd_menor),
                   ("TOKEN oprel", afd_menorigual),
                   ("TOKEN oprel", afd_mayor),
                   ("TOKEN oprel", afd_mayorigual),
                   ("TOKEN oprel", afd_igual),
                   ("TOKEN oprel", afd_distinto),
                   ("TOKEN opsuma", afd_suma),
                   ("TOKEN opsuma", afd_resta),
                   ("TOKEN mult", afd_mult),
                   ("TOKEN div", afd_div),
                   ("TOKEN parentesisIzq", afd_parentesisIzq),
                   ("TOKEN parentesisDer", afd_parentesisDer),
                   ("TOKEN puntoycoma", afd_puntoycoma),
                   ("TOKEN NUM", afd_num),
                   ("TOKEN ID", afd_id)]  # Colocamos el TOKEN ID en último lugar para darle precedencia a palabras reservadas

tokens = []
tokensErroneos = []


def caeEnTrampa(cadena, posibles_tokens_con_un_caracter_mas):
    for (tipoToken, afd) in TOKENS_POSIBLES:
        resultado = afd(cadena)
        if resultado == ESTADO_ACEPTADO or resultado == ESTADO_NO_ACEPTADO:
            posibles_tokens_con_un_caracter_mas.append(tipoToken)
            return False
    return True


def guardarToken(cadena, tokentipo, tokens):

    tokens.append((tokentipo, cadena))
    return tokens


def lexer(codigofuente):

    tokens = []
    tokensErroneos = []
    final = 0

    while final < len(codigofuente):

        while codigofuente[final].isspace():
            final += 1  # cambio el uso de final
        inicio = final
        posibles_tokens = []
        posibles_tokens_con_un_caracter_mas = []

        lexema = ''

        while final <= len(codigofuente) and not caeEnTrampa(lexema, posibles_tokens_con_un_caracter_mas):

            lexema = codigofuente[inicio:final+1]
            posibles_tokens = posibles_tokens_con_un_caracter_mas
            posibles_tokens_con_un_caracter_mas = []
            final += 1

        if len(posibles_tokens) == 0:
            print("ERROR: TOKEN DESCONOCIDO" + lexema)
            tokensErroneos.append(codigofuente[inicio:final])

        else:
            final = final - 1

            tokentipo = posibles_tokens[0]

            tokens = guardarToken(
                codigofuente[inicio:final], tokentipo, tokens)

    return tokens
