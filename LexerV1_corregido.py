from AFD import *

TOKENS_POSIBLES = [("TOKEN leer", afd_leer),
                   ("TOKEN NUM", afd_num),
                   ("TOKEN si", afd_si),
                   ("TOKEN sino", afd_sino),
                   ("TOKEN finsi", afd_finsi),
                   ("TOKEN repetir", afd_repetir),
                   ("TOKEN hasta", afd_hasta),
                   ("TOKEN equal", afd_equal),
                   ("TOKEN func", afd_func),
                   ("TOKEN finfunc", afd_finfunc),
                   ("TOKEN menor", afd_menor),
                   ("TOKEN menorigual", afd_menorigual),
                   ("TOKEN mayor", afd_mayor),
                   ("TOKEN mayorigual", afd_mayorigual),
                   ("TOKEN igual", afd_igual),
                   ("TOKEN distinto", afd_distinto),
                   ("TOKEN suma", afd_suma),
                   ("TOKEN resta", afd_resta),
                   ("TOKEN mult", afd_mult),
                   ("TOKEN div", afd_div),
                   ("TOKEN parentesisIzq", afd_parentesisIzq),
                   ("TOKEN parentesisDer", afd_parentesisDer),
                   ("TOKEN puntoycoma", afd_puntoycoma),
                   ("TOKEN ID", afd_id)] # Colocamos el TOKEN ID en último lugar para darle precedencia a palabras reservadas

tokens = []
tokensErroneos = []


def caeEnTrampa(cadena, posibles_tokens_con_un_caracter_mas): # agregamos el parametro tokens con un carácter más,
                                                              # y además evitamos usar globales
    for (tipoToken, afd) in TOKENS_POSIBLES:
        resultado = afd(cadena)
        # if resultado == ESTADO_ACEPTADO or resultado == ESTADO_NO_ACEPTADO:
        #     return False
        # Cambiando por esto, en cada recorrido detecta los tipos de tokens aceptados con un carácter más
        if resultado == ESTADO_ACEPTADO:
            posibles_tokens_con_un_caracter_mas.append(tipoToken))
            return False
        else resultado == ESTADO_NO_ACEPTADO:
            return False
    return True


def guardarToken(cadena,tokentipo, tokens): 
    # Esta reescribirla porque asume que un solo afd estará en aceptado para un cierto token
    # y no es cierto por ejemplo para las palabras reservadas
    # con este cambio, ya sabemos que el tokentipo es el que corresponde
    
    # for (tipoToken, afd) in TOKENS_POSIBLES:
    #     resultado = afd(cadena)
    #     if resultado == ESTADO_ACEPTADO:
            tokens.append((tokentipo, cadena))
            return tokens


def lexer(codigofuente):
    global tokens, tokensErroneos #no usar globales, porque tiene efectos de lado imprevisibles
                                  # Además lexer puede acceder a las variables tokens y tokensErroneos porque si no son locales de lexer las busca en el cuerpo principal o el script que llame a lexer
    tokens = []
    tokensErroneos = []
    final = 0 # usar final para marcar la posición en la cadena total y inicio para el lexema actual

    while final < len(codigofuente):
        # Aquí habría que resetear los tokens posibles y tokens con un carácter más para cada lexema,
        # por eso sino luego de reconocer el primero, toma todo lo siguiente como el mismo
        # también el inicio de cada token, usar inicio para eso y final por ejemplo para la posición en la 
        # cadena total (códigofuente), luego de saltear espacios en blanco
        while codigofuente[inicio].isspace():
            final += 1 # cambio el uso de final
        inicio = final 
        posibles_tokens=[]
        posibles_tokens_con_un_caracter_mas=[]

        # final = inicio + 1
        # lexema = codigofuente[inicio:final]
        # en cada iteración comienzo en un lexema vacio y agrego de a un carácter
        lexema = ''

        while final <= len(codigofuente) and not caeEnTrampa(lexema, posibles_tokens_con_un_caracter_mas): # agregamos un parametro a la función para evitar globales
            # Agrego el uso de posibles_tokens y con un carácter más
            lexema = codigofuente[inicio:final+1]
            posibles_tokens=posibles_tokens_con_un_caracter_mas
            posibles_tokens_con_un_caracter_mas=[]
            final += 1

        #if final > inicio + 1:
        if len(posibles_tokens) == 0:
            print("ERROR: TOKEN DESCONOCIDO" + lexema)
            tokensErroneos.append(codigofuente[inicio:final])
            
        else:
            final = final - 1
            # ESTA LINEA SE AGREGA PORQUE CUANDO SE BUSCA EL TOKEN CON UN CARACTER MAS, 
            # INDICE SE QUEDA EN CON UN CARACTER EXTRA, Y SI LOS TOKENS EN EL CODIGO 	
            # FUENTE NO ESTAN SEPARADOS POR UN ESPACIO, EL LEXER RECONOCE BIEN EL TOKEN 		
            # PERO GUARDA MAL EL LEXEMA PORQUE EL AGREGA UN CARACTER EXTRA QUE EN
                        # REALIDAD CORRESPONDERÍA AL SIGUIENTE, QUE A SU VEZ COMIENZA CON UN 
                        # CARACTER MENOS. ES DECIR ESTO ES NECESARIO POR SI TENGO ALGO COMO 344aux
                        # QUE SON DOS TOKENS SEPARADOS SIN UN ESPACIO LO RECONOZCA COMO EL TOKEN 
                        # "CTE" Y LEXEMA 344 SEGUIDO DEL TOKEN "ID" Y LEXEMA aux. SIN ESTO 
                        # ERA NECESARIO EL ESPACIO "344 aux"
            tokentipo = posibles_tokens[0]
            tokens = guardarToken(codigofuente[inicio:final],tokentipo, tokens) # agregamos parametros a la función para 
            # evitar el uso de variables globales
            
           # inicio += 1

    return tokens
