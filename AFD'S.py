import string

#Pongo las palabras reservadas en una lista
P_RESERVADAS = ['si','sino','finsi','repetir','hasta','equal','func','finfunc','oprel','opsuma','opmult']
#Usando el módulo string, hago una lista con las letras de la a hasta la z (minusculas y mayusculas)
LETRAS_lower = list(string.ascii_lowercase)
LETRAS_upper = list(string.ascii_uppercase)
#Creo una lista con los numeros del 0 al 9
NUMEROS = list(range(10))

#-------------------------------------------

ESTADO_ACEPTADO = "ESTADO ACEPTADO"
ESTADO_NO_ACEPTADO = "ESTADO NO ACEPTADO"
ESTADO_TRAMPA = "ESTADO TRAMPA"

#-------------------------------------------

#Automatas para c/token

#AFD ID'S

def afd_id(string):
    estado_actual = 0
    primera_letra = True
    
    if string in P_RESERVADAS:
        return ESTADO_NO_ACEPTADO
    
    for letra in string:
        if letra and primera_letra in NUMEROS:
            return ESTADO_TRAMPA
        elif (letra in LETRAS_lower or letra in LETRAS_upper or letra in NUMEROS) and estado_actual == 0:
            primera_letra = 1
            estado_actual = 0
        else:
            estado_actual = -1
            return ESTADO_TRAMPA
        return ESTADO_ACEPTADO
    
#AFD "si"
def afd_si(string):
    estado_actual = 0
    estados_aceptados =[2]
    
    for letra in string:
        if estado_actual == 0 and letra == 's':
            estado_actual = 1
        elif estado_actual == 1 and letra == 'si':
            estado_actual = 2
        else:
            estado_actual = -1
            return ESTADO_TRAMPA
        
    if estado_actual in estados_aceptados:
        return ESTADO_ACEPTADO
    else:
        return ESTADO_NO_ACEPTADO
    
#AFD "sino"
 def afd_sino(string):
    estado_actual = 0
    estados_aceptados = [4]
    
    for letra in string:
        if estado_actual == 0 and letra == 's':
            estado_actual = 1
        elif estado_actual == 1 and letra == 'i':
            estado_actual = 2
        elif estado_actual == 2 and letra == 'n':
            estado_actual = 3
        elif estado_actual == 3 and letra == 'o':
            estado_actual = 4
        else:
            estado_actual = -1
            return ESTADO_TRAMPA
        
    if estado_actual in estados_aceptados:
        return ESTADO_ACEPTADO
    else:
        return ESTADO_NO_ACEPTADO
            
#AFD "finsi"   
def afd_finsi(string):
    estado_actual = 0
    estados_aceptados = [5]
    
    for letra in string:
        if estado_actual == 0 and letra == 'f':
            estado_actual = 1
        elif estado_actual == 1 and letra == 'i':
            estado_actual = 2
        elif estado_actual == 2 and letra == 'n':
            estado_actual = 3
        elif estado_actual == 3 and letra == 's':
            estado_actual = 4
        elif estado_actual == 4 and letra == 'i':
            estado_actual = 5
        else:
            estado_actual = -1
            return ESTADO_TRAMPA
        
    if estado_actual in estados_aceptados:
        return ESTADO_ACEPTADO
    else:
        return ESTADO_NO_ACEPTADO

#AFD "repetir"   
def afd_repetir(string):
    estado_actual = 0
    estados_aceptados = [7]
    
    for letra in string:
        if estado_actual == 0 and letra == 'r':
            estado_actual = 1
        elif estado_actual == 1 and letra == 'e':
            estado_actual = 2
        elif estado_actual == 2 and letra == 'p':
            estado_actual = 3
        elif estado_actual == 3 and letra == 'e':
            estado_actual = 4
        elif estado_actual == 4 and letra == 't':
            estado_actual = 5
        elif estado_actual == 5 and letra == 'i':
            estado_actual = 6
        elif estado_actual == 6 and letra == 'r':
            estado_actual = 7
        else:
            estado_actual = -1
            return ESTADO_TRAMPA
        
    if estado_actual in estados_aceptados:
        return ESTADO_ACEPTADO
    else:
        return ESTADO_NO_ACEPTADO

#AFD "hasta"   
def afd_hasta(string):
    estado_actual = 0
    estados_aceptados = [5]
    
    for letra in string:
        if estado_actual == 0 and letra == 'h':
            estado_actual = 1
        elif estado_actual == 1 and letra == 'a':
            estado_actual = 2
        elif estado_actual == 2 and letra == 's':
            estado_actual = 3
        elif estado_actual == 3 and letra == 't':
            estado_actual = 4
        elif estado_actual == 4 and letra == 'a':
            estado_actual = 5
        else:
            estado_actual = -1
            return ESTADO_TRAMPA
        
    if estado_actual in estados_aceptados:
        return ESTADO_ACEPTADO
    else:
        return ESTADO_NO_ACEPTADO

#AFD "equal"   
def afd_equal(string):
    estado_actual = 0
    estados_aceptados = [5]
    
    for letra in string:
        if estado_actual == 0 and letra == 'e':
            estado_actual = 1
        elif estado_actual == 1 and letra == 'q':
            estado_actual = 2
        elif estado_actual == 2 and letra == 'u':
            estado_actual = 3
        elif estado_actual == 3 and letra == 'a':
            estado_actual = 4
        elif estado_actual == 4 and letra == 'l':
            estado_actual = 5
        else:
            estado_actual = -1
            return ESTADO_TRAMPA
        
    if estado_actual in estados_aceptados:
        return ESTADO_ACEPTADO
    else:
        return ESTADO_NO_ACEPTADO

#AFD "func"
def afd_func(string):
    estado_actual = 0
    estados_aceptados = [4]
    
    for letra in string:
        if estado_actual == 0 and letra == 'f':
            estado_actual = 1
        elif estado_actual == 1 and letra == 'u':
            estado_actual = 2
        elif estado_actual == 2 and letra == 'n':
            estado_actual = 3
        elif estado_actual == 3 and letra == 'c':
            estado_actual = 4
        else:
            estado_actual = -1
            return ESTADO_TRAMPA
        
    if estado_actual in estados_aceptados:
        return ESTADO_ACEPTADO
    else:
        return ESTADO_NO_ACEPTADO

#AFD "finfunc"
def afd_finfunc(string):
    estado_actual = 0
    estados_aceptados = [7]
    
    for letra in string:
        if estado_actual == 0 and letra == 'f':
            estado_actual = 1
        elif estado_actual == 1 and letra == 'i':
            estado_actual = 2
        elif estado_actual == 2 and letra == 'n':
            estado_actual = 3
        elif estado_actual == 3 and letra == 'f':
            estado_actual = 4
        elif estado_actual == 4 and letra == 'u':
            estado_actual = 5
        elif estado_actual == 5 and letra == 'n':
            estado_actual = 6
        elif estado_actual == 6 and letra == 'c':
            estado_actual = 7
        else:
            estado_actual = -1
            return ESTADO_TRAMPA
        
    if estado_actual in estados_aceptados:
        return ESTADO_ACEPTADO
    else:
        return ESTADO_NO_ACEPTADO

#AFD "oprel"   
def afd_oprel(string):
    estado_actual = 0
    estados_aceptados = [5]
    
    for letra in string:
        if estado_actual == 0 and letra == 'o':
            estado_actual = 1
        elif estado_actual == 1 and letra == 'p':
            estado_actual = 2
        elif estado_actual == 2 and letra == 'r':
            estado_actual = 3
        elif estado_actual == 3 and letra == 'e':
            estado_actual = 4
        elif estado_actual == 4 and letra == 'l':
            estado_actual = 5
        else:
            estado_actual = -1
            return ESTADO_TRAMPA
        
    if estado_actual in estados_aceptados:
        return ESTADO_ACEPTADO
    else:
        return ESTADO_NO_ACEPTADO

#AFD "opsuma"   
def afd_opsuma(string):
    estado_actual = 0
    estados_aceptados = [6]
    
    for letra in string:
        if estado_actual == 0 and letra == 'o':
            estado_actual = 1
        elif estado_actual == 1 and letra == 'p':
            estado_actual = 2
        elif estado_actual == 2 and letra == 's':
            estado_actual = 3
        elif estado_actual == 3 and letra == 'u':
            estado_actual = 4
        elif estado_actual == 4 and letra == 'm':
            estado_actual = 5
        elif estado_actual == 5 and letra == 'a':
            estado_actual = 6
        else:
            estado_actual = -1
            return ESTADO_TRAMPA
        
    if estado_actual in estados_aceptados:
        return ESTADO_ACEPTADO
    else:
        return ESTADO_NO_ACEPTADO

#AFD "opmult"   
def afd_opsuma(string):
    estado_actual = 0
    estados_aceptados = [6]
    
    for letra in string:
        if estado_actual == 0 and letra == 'o':
            estado_actual = 1
        elif estado_actual == 1 and letra == 'p':
            estado_actual = 2
        elif estado_actual == 2 and letra == 'm':
            estado_actual = 3
        elif estado_actual == 3 and letra == 'u':
            estado_actual = 4
        elif estado_actual == 4 and letra == 'l':
            estado_actual = 5
        elif estado_actual == 5 and letra == 't':
            estado_actual = 6
        else:
            estado_actual = -1
            return ESTADO_TRAMPA
        
    if estado_actual in estados_aceptados:
        return ESTADO_ACEPTADO
    else:
        return ESTADO_NO_ACEPTADO

#AFD "("
def afd_parentesisIzq(string):
    estado_actual = 0 
    for letra in string:
        if estado_actual == 0 and letra == '(':
            estado_actual = 0
        else:
            estado_actual = -1
            return ESTADO_TRAMPA
        return ESTADO_ACEPTADO

#AFD ")"
def afd_parentesisDer(string):
    estado_actual = 0 
    for letra in string:
        if estado_actual == 0 and letra == ')':
            estado_actual = 0
        else:
            estado_actual = -1
            return ESTADO_TRAMPA
        return ESTADO_ACEPTADO
#AFD ";"
def afd_puntoycoma(string):
    estado_actual = 0 
    for letra in string:
        if estado_actual == 0 and letra == ';':
            estado_actual = 0
        else:
            estado_actual = -1
            return ESTADO_TRAMPA
        return ESTADO_ACEPTADO