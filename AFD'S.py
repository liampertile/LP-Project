import string

#--------------CONSTANTES-------------------#
#Pongo las palabras reservadas en una lista
P_RESERVADAS = ['si','sino','finsi','repetir','hasta','equal','func','finfunc','oprel','opsuma','opmult']
#Usando el módulo string, hago una lista con las caracters de la a hasta la z (minusculas y mayusculas)
LETRAS_lower = list(string.ascii_lowercase)
LETRAS_upper = list(string.ascii_uppercase)
#Creo una lista con los numeros del 0 al 9
NUMEROS = list(range(10))

#-------------------------------------------#

ESTADO_ACEPTADO = "ESTADO ACEPTADO"
ESTADO_NO_ACEPTADO = "ESTADO NO ACEPTADO"
ESTADO_TRAMPA = "ESTADO TRAMPA"

#-------------------------------------------#

#Automatas para c/token

#AFD ID'S

def afd_id(lexema):
    estado_actual = 0
    primer_caracter = True
    
    if lexema in P_RESERVADAS:
        return ESTADO_NO_ACEPTADO
    
    for caracter in lexema:
        if caracter and primer_caracter in NUMEROS:
            return ESTADO_TRAMPA
        elif (caracter in LETRAS_lower or caracter in LETRAS_upper or caracter in NUMEROS) and estado_actual == 0:
            primer_caracter = False
            estado_actual = 0
        else:
            estado_actual = -1
            return ESTADO_TRAMPA
        return ESTADO_ACEPTADO

#AFD NUM
def afd_num(lexema):
    estado_actual = 0
    for caracter in lexema:
        if caracter in NUMEROS and estado_actual == 0:
            estado_actual = 0
        else:
            estado_actual = -1
            return ESTADO_TRAMPA
    if estado_actual == 0:
        try:
            value = int(lexema)
            return ESTADO_ACEPTADO
        except:
            return ESTADO_TRAMPA
    
#AFD "si"
def afd_si(lexema):
    estado_actual = 0
    estados_aceptados =[2]
    
    for caracter in lexema:
        if estado_actual == 0 and caracter == 's':
            estado_actual = 1
        elif estado_actual == 1 and caracter == 'si':
            estado_actual = 2
        else:
            estado_actual = -1
            return ESTADO_TRAMPA
        
    if estado_actual in estados_aceptados:
        return ESTADO_ACEPTADO
    else:
        return ESTADO_NO_ACEPTADO
    
#AFD "sino"
def afd_sino(lexema):
    estado_actual = 0
    estados_aceptados = [4]
    
    for caracter in lexema:
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
            
#AFD "finsi"   
def afd_finsi(lexema):
    estado_actual = 0
    estados_aceptados = [5]
    
    for caracter in lexema:
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

#AFD "repetir"   
def afd_repetir(lexema):
    estado_actual = 0
    estados_aceptados = [7]
    
    for caracter in lexema:
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

#AFD "hasta"   
def afd_hasta(lexema):
    estado_actual = 0
    estados_aceptados = [5]
    
    for caracter in lexema:
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

#AFD "equal"   
def afd_equal(lexema):
    estado_actual = 0
    estados_aceptados = [5]
    
    for caracter in lexema:
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

#AFD "func"
def afd_func(lexema):
    estado_actual = 0
    estados_aceptados = [4]
    
    for caracter in lexema:
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

#AFD "finfunc"
def afd_finfunc(lexema):
    estado_actual = 0
    estados_aceptados = [7]
    
    for caracter in lexema:
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

#AFD "oprel"   
def afd_oprel(lexema):
    estado_actual = 0
    estados_aceptados = [5]
    
    for caracter in lexema:
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

#AFD "opsuma"   
def afd_opsuma(lexema):
    estado_actual = 0 
    for caracter in lexema:
        if estado_actual == 0 and caracter == '+':
            estado_actual = 0
        else:
            estado_actual = -1
            return ESTADO_TRAMPA
        return ESTADO_ACEPTADO

#AFD "opmult"   
def afd_opmult(lexema):
    estado_actual = 0 
    for caracter in lexema:
        if estado_actual == 0 and caracter == '*':
            estado_actual = 0
        else:
            estado_actual = -1
            return ESTADO_TRAMPA
        return ESTADO_ACEPTADO

#AFD "("
def afd_parentesisIzq(lexema):
    estado_actual = 0 
    for caracter in lexema:
        if estado_actual == 0 and caracter == '(':
            estado_actual = 0
        else:
            estado_actual = -1
            return ESTADO_TRAMPA
        return ESTADO_ACEPTADO

#AFD ")"
def afd_parentesisDer(lexema):
    estado_actual = 0 
    for caracter in lexema:
        if estado_actual == 0 and caracter == ')':
            estado_actual = 0
        else:
            estado_actual = -1
            return ESTADO_TRAMPA
        return ESTADO_ACEPTADO
#AFD ";"
def afd_puntoycoma(lexema):
    estado_actual = 0 
    for caracter in lexema:
        if estado_actual == 0 and caracter == ';':
            estado_actual = 0
        else:
            estado_actual = -1
            return ESTADO_TRAMPA
        return ESTADO_ACEPTADO

#AFD "<"
def afd_menor(lexema):
    estado_actual = 0 
    for caracter in lexema:
        if estado_actual == 0 and caracter == '<':
            estado_actual = 0
        else:
            estado_actual = -1
            return ESTADO_TRAMPA
        return ESTADO_ACEPTADO
#AFD ">"
def afd_mayor(lexema):
    estado_actual = 0 
    for caracter in lexema:
        if estado_actual == 0 and caracter == '>':
            estado_actual = 0
        else:
            estado_actual = -1
            return ESTADO_TRAMPA
        return ESTADO_ACEPTADO
#AFD "<="
def afd_mayorigual(lexema):
    estado_actual = 0
    estados_aceptados = [2] 
    for caracter in lexema:
        if estado_actual == 0 and caracter == '<':
            estado_actual = 1
        elif estado_actual == 1 and caracter == '=':
            estado_actual = 2
        else:
            estado_actual = -1
            return ESTADO_TRAMPA
        return ESTADO_ACEPTADO

#AFD ">="
def afd_mayorigual(lexema):
    estado_actual = 0
    estados_aceptados = [2] 
    for caracter in lexema:
        if estado_actual == 0 and caracter == '>':
            estado_actual = 1
        elif estado_actual == 1 and caracter == '=':
            estado_actual = 2
        else:
            estado_actual = -1
            return ESTADO_TRAMPA
        return ESTADO_ACEPTADO

#-------------------------------------------#
TOKENS_POSIBLES = [("TOKEN ID",afd_id),("TOKEN NUM", afd_num),("TOKEN si", afd_si),("TOKEN sino", afd_sino),("TOKEN finsi", afd_finsi),("TOKEN repetir", afd_repetir)
                   ,("TOKEN hasta", afd_hasta),("TOKEN equal", afd_equal),("TOKEN func", afd_func),("TOKEN finfunc", afd_finfunc),("TOKEN oprel", afd_oprel),("TOKEN opsuma", afd_opsuma),
                   ("TOKEN opmult", afd_opmult),("TOKEN parentesisIzq", afd_parentesisIzq),("TOKEN parentesisDer", afd_parentesisDer),("TOKEN puntoycoma", afd_puntoycoma),]

def lexer(codigofuente):
    tokens = []
    pos_actual = 0
    while pos_actual < len(codigofuente):
        while codigofuente[pos_actual].isspace():
            pos_actual += 1
        comienzo_lexema = pos_actual
        posibles_tokens = []
        posibles_tokens_con_un_caracter_mas = []
        lexema = ""
        todos_en_estado_trampa = False #CENTINELA
        
        while not todos_en_estado_trampa:
            lexema = codigofuente[comienzo_lexema:pos_actual + 1]
            posibles_tokens = posibles_tokens_con_un_caracter_mas
            posibles_tokens_con_un_caracter_mas = []
            
            for (un_tipo_de_token , afd) in TOKENS_POSIBLES:
                simulacion_afd = afd(lexema)
                if simulacion_afd == ESTADO_ACEPTADO:
                    posibles_tokens_con_un_caracter_mas.append(un_tipo_de_token)
                    todos_en_estado_trampa = True
                elif simulacion_afd == ESTADO_NO_ACEPTADO:
                    todos_en_estado_trampa = False
            pos_actual += 1
        
        if len(posibles_tokens) == 0:
            print("ERROR:TOKEN NO VALIDO" + lexema)
            
        un_tipo_de_token = posibles_tokens [0]

        token =(un_tipo_de_token,lexema)
        tokens.append(token)
        
    return tokens


