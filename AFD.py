import string

# --------------CONSTANTES-------------------#
# Pongo las palabras reservadas en una lista
P_RESERVADAS = ['si', 'sino', 'finsi', 'repetir', 'hasta',
                'equal', 'func', 'finfunc', 'oprel', 'opsuma', 'opmult', 'leer']
# Usando el módulo string, hago una lista con las caracters de la a hasta la z (minusculas y mayusculas)
LETRAS_lower = list(string.ascii_lowercase)
LETRAS_upper = list(string.ascii_uppercase)
# Creo una lista con los numeros del 0 al 9
NUMEROS = list(range(10))
NUMEROS = list(map(str, NUMEROS))

# -------------------------------------------#

ESTADO_ACEPTADO = "ESTADO ACEPTADO"
ESTADO_NO_ACEPTADO = "ESTADO NO ACEPTADO"
ESTADO_TRAMPA = "ESTADO TRAMPA"

# -------------------------------------------#

# Automatas para c/token

# AFD ID'S


def afd_id(cadena):
    estado_actual = 0
    primer_caracter = True

    if cadena in P_RESERVADAS:
        return ESTADO_NO_ACEPTADO

    for caracter in cadena:
        if (caracter in NUMEROS) and primer_caracter:
            return ESTADO_TRAMPA
        elif (caracter in LETRAS_lower or caracter in LETRAS_upper or caracter in NUMEROS) and estado_actual == 0:
            primer_caracter = False
            estado_actual = 0
        else:
            estado_actual = -1
            return ESTADO_TRAMPA
        return ESTADO_ACEPTADO

# AFD NUM


def afd_num(cadena):
    estado_actual = 0
    estados_aceptados = [1]

    for caracter in cadena:
        if estado_actual == 0 and caracter in NUMEROS:
            estado_actual = 1
        elif estado_actual == 1 and caracter in NUMEROS:
            estado_actual = 1
        else:
            estado_actual = -1
            return ESTADO_TRAMPA

    if estado_actual in estados_aceptados:
        return ESTADO_ACEPTADO
    else:
        return ESTADO_TRAMPA
# AFD "si"


def afd_si(cadena):
    estado_actual = 0
    estados_aceptados = [2]

    for caracter in cadena:
        if estado_actual == 0 and caracter == 's':
            estado_actual = 1
        elif estado_actual == 1 and caracter == 'i':
            estado_actual = 2
        else:
            estado_actual = -1
            return ESTADO_TRAMPA

    if estado_actual in estados_aceptados:
        return ESTADO_ACEPTADO
    else:
        return ESTADO_NO_ACEPTADO

# AFD "sino"


def afd_sino(cadena):
    estado_actual = 0
    estados_aceptados = [4]

    for caracter in cadena:
        if estado_actual == 0 and caracter == 's':
            estado_actual = 1
        elif estado_actual == 1 and caracter == 'i':
            estado_actual = 2
        elif estado_actual == 2 and caracter == 'n':
            estado_actual = 3
        elif estado_actual == 3 and caracter == 'o':
            estado_actual = 4
        else:
            estado_actual = -1
            return ESTADO_TRAMPA

    if estado_actual in estados_aceptados:
        return ESTADO_ACEPTADO
    else:
        return ESTADO_NO_ACEPTADO

# AFD "finsi"


def afd_finsi(cadena):
    estado_actual = 0
    estados_aceptados = [5]

    for caracter in cadena:
        if estado_actual == 0 and caracter == 'f':
            estado_actual = 1
        elif estado_actual == 1 and caracter == 'i':
            estado_actual = 2
        elif estado_actual == 2 and caracter == 'n':
            estado_actual = 3
        elif estado_actual == 3 and caracter == 's':
            estado_actual = 4
        elif estado_actual == 4 and caracter == 'i':
            estado_actual = 5
        else:
            estado_actual = -1
            return ESTADO_TRAMPA

    if estado_actual in estados_aceptados:
        return ESTADO_ACEPTADO
    else:
        return ESTADO_NO_ACEPTADO

# AFD "repetir"


def afd_repetir(cadena):
    estado_actual = 0
    estados_aceptados = [7]

    for caracter in cadena:
        if estado_actual == 0 and caracter == 'r':
            estado_actual = 1
        elif estado_actual == 1 and caracter == 'e':
            estado_actual = 2
        elif estado_actual == 2 and caracter == 'p':
            estado_actual = 3
        elif estado_actual == 3 and caracter == 'e':
            estado_actual = 4
        elif estado_actual == 4 and caracter == 't':
            estado_actual = 5
        elif estado_actual == 5 and caracter == 'i':
            estado_actual = 6
        elif estado_actual == 6 and caracter == 'r':
            estado_actual = 7
        else:
            estado_actual = -1
            return ESTADO_TRAMPA

    if estado_actual in estados_aceptados:
        return ESTADO_ACEPTADO
    else:
        return ESTADO_NO_ACEPTADO

# AFD "hasta"


def afd_hasta(cadena):
    estado_actual = 0
    estados_aceptados = [5]

    for caracter in cadena:
        if estado_actual == 0 and caracter == 'h':
            estado_actual = 1
        elif estado_actual == 1 and caracter == 'a':
            estado_actual = 2
        elif estado_actual == 2 and caracter == 's':
            estado_actual = 3
        elif estado_actual == 3 and caracter == 't':
            estado_actual = 4
        elif estado_actual == 4 and caracter == 'a':
            estado_actual = 5
        else:
            estado_actual = -1
            return ESTADO_TRAMPA

    if estado_actual in estados_aceptados:
        return ESTADO_ACEPTADO
    else:
        return ESTADO_NO_ACEPTADO

# AFD "equal"


def afd_equal(cadena):
    estado_actual = 0
    estados_aceptados = [5]

    for caracter in cadena:
        if estado_actual == 0 and caracter == 'e':
            estado_actual = 1
        elif estado_actual == 1 and caracter == 'q':
            estado_actual = 2
        elif estado_actual == 2 and caracter == 'u':
            estado_actual = 3
        elif estado_actual == 3 and caracter == 'a':
            estado_actual = 4
        elif estado_actual == 4 and caracter == 'l':
            estado_actual = 5
        else:
            estado_actual = -1
            return ESTADO_TRAMPA

    if estado_actual in estados_aceptados:
        return ESTADO_ACEPTADO
    else:
        return ESTADO_NO_ACEPTADO

# AFD "func"


def afd_func(cadena):
    estado_actual = 0
    estados_aceptados = [4]

    for caracter in cadena:
        if estado_actual == 0 and caracter == 'f':
            estado_actual = 1
        elif estado_actual == 1 and caracter == 'u':
            estado_actual = 2
        elif estado_actual == 2 and caracter == 'n':
            estado_actual = 3
        elif estado_actual == 3 and caracter == 'c':
            estado_actual = 4
        else:
            estado_actual = -1
            return ESTADO_TRAMPA

    if estado_actual in estados_aceptados:
        return ESTADO_ACEPTADO
    else:
        return ESTADO_NO_ACEPTADO

# AFD "finfunc"


def afd_finfunc(cadena):
    estado_actual = 0
    estados_aceptados = [7]

    for caracter in cadena:
        if estado_actual == 0 and caracter == 'f':
            estado_actual = 1
        elif estado_actual == 1 and caracter == 'i':
            estado_actual = 2
        elif estado_actual == 2 and caracter == 'n':
            estado_actual = 3
        elif estado_actual == 3 and caracter == 'f':
            estado_actual = 4
        elif estado_actual == 4 and caracter == 'u':
            estado_actual = 5
        elif estado_actual == 5 and caracter == 'n':
            estado_actual = 6
        elif estado_actual == 6 and caracter == 'c':
            estado_actual = 7
        else:
            estado_actual = -1
            return ESTADO_TRAMPA

    if estado_actual in estados_aceptados:
        return ESTADO_ACEPTADO
    else:
        return ESTADO_NO_ACEPTADO

# AFD "oprel"


def afd_oprel(cadena):
    estado_actual = 0
    estados_aceptados = [5]

    for caracter in cadena:
        if estado_actual == 0 and caracter == 'o':
            estado_actual = 1
        elif estado_actual == 1 and caracter == 'p':
            estado_actual = 2
        elif estado_actual == 2 and caracter == 'r':
            estado_actual = 3
        elif estado_actual == 3 and caracter == 'e':
            estado_actual = 4
        elif estado_actual == 4 and caracter == 'l':
            estado_actual = 5
        else:
            estado_actual = -1
            return ESTADO_TRAMPA

    if estado_actual in estados_aceptados:
        return ESTADO_ACEPTADO
    else:
        return ESTADO_NO_ACEPTADO

# AFD "opsuma"


def afd_opsuma(cadena):
    estado_actual = 0
    estados_aceptados = [6]

    for caracter in cadena:
        if estado_actual == 0 and caracter == 'o':
            estado_actual = 1
        elif estado_actual == 1 and caracter == 'p':
            estado_actual = 2
        elif estado_actual == 2 and caracter == 's':
            estado_actual = 3
        elif estado_actual == 3 and caracter == 'u':
            estado_actual = 4
        elif estado_actual == 4 and caracter == 'm':
            estado_actual = 5
        elif estado_actual == 5 and caracter == 'a':
            estado_actual = 6
        else:
            estado_actual = -1
            return ESTADO_TRAMPA

    if estado_actual in estados_aceptados:
        return ESTADO_ACEPTADO
    else:
        return ESTADO_NO_ACEPTADO

# AFD "opmult"


def afd_opmult(cadena):
    estado_actual = 0
    estados_aceptados = [6]

    for caracter in cadena:
        if estado_actual == 0 and caracter == 'o':
            estado_actual = 1
        elif estado_actual == 1 and caracter == 'p':
            estado_actual = 2
        elif estado_actual == 2 and caracter == 'm':
            estado_actual = 3
        elif estado_actual == 3 and caracter == 'u':
            estado_actual = 4
        elif estado_actual == 4 and caracter == 'l':
            estado_actual = 5
        elif estado_actual == 5 and caracter == 't':
            estado_actual = 6
        else:
            estado_actual = -1
            return ESTADO_TRAMPA

    if estado_actual in estados_aceptados:
        return ESTADO_ACEPTADO
    else:
        return ESTADO_NO_ACEPTADO

# AFD "("


def afd_parentesisIzq(cadena):
    estado_actual = 0
    for caracter in cadena:
        if estado_actual == 0 and caracter == '(':
            estado_actual = 0
        else:
            estado_actual = -1
            return ESTADO_TRAMPA
        return ESTADO_ACEPTADO

# AFD ")"


def afd_parentesisDer(cadena):
    estado_actual = 0
    for caracter in cadena:
        if estado_actual == 0 and caracter == ')':
            estado_actual = 0
        else:
            estado_actual = -1
            return ESTADO_TRAMPA
        return ESTADO_ACEPTADO
# AFD ";"


def afd_puntoycoma(cadena):
    estado_actual = 0
    for caracter in cadena:
        if estado_actual == 0 and caracter == ';':
            estado_actual = 0
        else:
            estado_actual = -1
            return ESTADO_TRAMPA
        return ESTADO_ACEPTADO

# AFD "leer"


def afd_leer(cadena):
    estado_actual = 0
    estados_aceptados = [4]

    for caracter in cadena:
        if estado_actual == 0 and caracter == 'l':
            estado_actual = 1
        elif estado_actual == 1 and caracter == 'e':
            estado_actual = 2
        elif estado_actual == 2 and caracter == 'e':
            estado_actual = 3
        elif estado_actual == 3 and caracter == 'r':
            estado_actual = 4
        else:
            estado_actual = -1
            return ESTADO_TRAMPA

    if estado_actual in estados_aceptados:
        return ESTADO_ACEPTADO
    else:
        return ESTADO_NO_ACEPTADO
