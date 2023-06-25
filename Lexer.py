#Importo el módulo AFD'S

from AFD import *

#Duplas
TOKENS_POSIBLES = [("TOKEN ID", afd_id),("TOKEN NUM", afd_num),("TOKEN si", afd_si),("TOKEN sino", afd_sino),("TOKEN finsi", afd_finsii),("TOKEN repetir", afd_repetir)
                   ,("TOKEN hasta", afd_hasta),("TOKEN equal", afd_equal),("TOKEN func", afd_func),("TOKEN finfunc", afd_finfunc),("TOKEN oprel", afd_oprel),("TOKEN opsuma", afd_opsuma),
                   ("TOKEN opmult", afd_opmult),("TOKEN parentesisIzq", afd_parentesisIzq),("TOKEN parentesisDer", afd_parentesisDer),("TOKEN puntoycoma", afd_puntoycoma),]

tokens = []

#lexema que terminen en estado trampa

def caeEnTrampa(lexema):
    todosCaen = True
    
    #Corro el lexema
    for (tipoToken,afd) in TOKENS_POSIBLES:
        resultado = afd(lexema)
        #Si queda en No aceptado o aceptado
        if resultado == (ESTADO_ACEPTADO or ESTADO_NO_ACEPTADO):
            todosCaen = False
            break

    return caeEnTrampa

#guardar el token del lexema en la lista "tokens"

def guardarToken(lexema):
    global tokens
    
    #Corremos el lexema en todos los automatas
    
    for(tipoToken,afd) in TOKENS_POSIBLES:
        resultado = afd(lexema)
    
        if resultado == (ESTADO_ACEPTADO):
            tokens.append((tipoToken,lexema))
        
        break


