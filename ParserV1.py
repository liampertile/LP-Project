from LexerV2 import *

VN = ['Program', 'ListaSentencias', 'ListaSentenciasP', 'Sentencia', 'SentenciaSi', 'SentenciaRepetir', 'SentenciaAsig',
      'SentenciaLeer', 'SentenciaMostrar', 'SentenciaFun', 'Proc', 'ListaPar', 'ListaParP', 'Expresion', 'Expresion2',
      'Expresion2P', 'Termino', 'TerminoP', 'Factor']

VT = ["id", "num", "si", "entonces", "sino", "finsi", "repetir", "hasta", "equal",
    "leer", "mostrar", "func", "finfunc", "(", ")", ";", "oprel", "opsuma", "opmult"]

tabla = {
    'Program': {
        'TOKEN si': ['ListaSentencias'],
        'TOKEN repetir': ['ListaSentencias'],
        'TOKEN ID': ['ListaSentencias'],
        'TOKEN leer': ['ListaSentencias'],
        'TOKEN mostrar': ['ListaSentencias'],
        'TOKEN func': ['ListaSentencias']
    },
    'ListaSentencias': {
        'TOKEN si': ['Sentencia', 'ListaSentenciasP'],
        'TOKEN repetir': ['Sentencia', 'ListaSentenciasP'],
        'TOKEN ID': ['Sentencia', 'ListaSentenciasP'],
        'TOKEN leer': ['Sentencia', 'ListaSentenciasP'],
        'TOKEN mostrar': ['Sentencia', 'ListaSentenciasP'],
        'TOKEN func': ['Sentencia', 'ListaSentenciasP']
    },
    'ListaSentenciasP': {
        'TOKEN puntoycoma': ['TOKEN puntoycoma'],
        '#': [],
        'TOKEN sino': [],
        'TOKEN finsi': [],
        'TOKEN hasta': [],
        'TOKEN finfunc': [],
    },
    'Sentencia': {
        'TOKEN si': ['SentenciaSi'],
        'TOKEN repetir': ['SentenciaRepetir'],
        'TOKEN ID': ['SentenciaAsig'],
        'TOKEN leer': ['Sentencialeer'],
        'TOKEN mostrar': ['SentenciaMostrar'],
        'TOKEN func': ['SentenciaFun']
    },
    'SentenciaSi': {
        'TOKEN si': ['TOKEN si', 'Expresion', 'TOKEN entonces', 'ListaSentencias', 'TOKEN sino', 'ListaSentencias', 'TOKEN finsi'],
        # preguntar
        'TOKEN si': ['TOKEN si', 'Expresion', 'TOKEN entonces', 'ListaSentencias', 'TOKEN finsi']
    },
    'SentenciaRepetir': {
        'TOKEN repetir': ['TOKEN repetir', 'ListaSentencias', 'TOKEN hasta', 'Expresion']
    },
    'SentenciaAsig': {
        'TOKEN ID': ['TOKEN ID', 'TOKEN igual', 'Expresion']
    },
    'SentenciaLeer': {
        'TOKEN leer': ['TOKEN leer', 'TOKEN ID']
    },
    'SentenciaMostrar': {
        'TOKEN mostrar': ['TOKEN mostrar', 'Expresion']
    },
    'SentenciaFun': {
        'TOKEN func': ['TOKEN func', 'Proc', 'TOKEN finfunc']
    },
    'Proc': {
        'TOKEN ID': ['TOKEN ID', 'TOKEN parentesisIzq', 'ListaPar', 'TOKEN parentesisDer', 'ListaSentencias']
    },
    'ListaPar': {
        'TOKEN ID': ['TOKEN ID', 'ListaParP']
    },
    'ListaParP': {
        'TOKEN puntoycoma': ['TOKEN puntoycoma', 'TOKEN ID', 'ListaParP'],
        'TOKEN parentesisDer': []
    },
    'Expresion': {
        'TOKEN parentesisDer': ['Expresion2','ExpresionP'],
        'TOKEN num': ['Expresion2','ExpresionP'],
        'TOKEN ID': ['Expresion2','ExpresionP']
    },
    'ExpresionP': {
        'TOKEN oprel': ['TOKEN oprel','Expresion2','ExpresionP'],
        'TOKEN puntoycoma': [],
        'TOKEN parentesisDer': [],
        'TOKEN entonces': [],
        '#': []
    },
    'Expresion2': {
        'TOKEN parentesisIzq': ['Termino', 'Expresion2P'],
        'TOKEN num': ['Termino', 'Expresion2P'],
        'TOKEN ID': ['Termino', 'Expresion2P']
    },
    'Expresion2P': {
        'TOKEN opsuma': ['TOKEN opsuma', 'Termino', 'Expresion2P'],
        'TOKEN opsuma': [],
        'TOKEN oprel': [],
         'TOKEN #': [],
        # 'TOKEN entonces': [],
        # 'TOKEN parentesisDer': []
    },
    'Termino': {
        '(': ['Factor', 'TerminoP'],
        'TOKEN num': ['Factor', 'TerminoP'],
        'TOKEN ID': ['Factor', 'TerminoP']
    },
    'TerminoP': {
        'TOKEN opmult': ['TOKEN opmult', 'Factor', 'TerminoP'],
        'TOKEN opsuma': [],
        #'TOKEN oprel': [],
         '#': [],
        # 'TOKEN entonces': [],
        # 'TOKEN parentesisDer': []
    },
    'Factor': {
        'TOKEN parentesisIzq': ['TOKEN parentesisIzq', 'Expresion', 'TOKEN parentesisDer'],
        'TOKEN num': ['TOKEN num'],
        'TOKEN ID': ['TOKEN ID']
    }
}

P = {'S': [['Token(', 'S', 'Token)', 'S'],
           ['Token(', 'Token)', 'S'],
           ['Token(', 'S', 'Token)'],
           ['Token(', 'Token)']]}


def traduccionParser(salidaLexer):
    cadena = []
    # Ponemos cada primer elemento de cada tupla (token) en una lista
    for tupla in salidaLexer:
        cadena.append(tupla[0])
    cadena.append('#')
    return cadena

# Función que genera las derivaciones, recibe el elemento a derivar, en que cadena y por que se deriva
def generarDerivacion(topePila, produccionAnterior, derivacion):
    # Obtenemos en que posición se encuentra el elemento a derivar
    indice = produccionAnterior.index(topePila)
    # Eliminamos el elemento a derivar
    produccionAnterior.remove(topePila)
    # Damos vuelta la lista de 'derivacion' para que luego al insertarla quede en el orden original
    produccionReversed = []
    for i in derivacion:
        produccionReversed.insert(0, i)

    # Insertamos la lista dada vuelta en la cadena a derivar
    for i in produccionReversed:
        produccionAnterior.insert(indice, i)
    
    return produccionAnterior



# Función principal
def parser(cadena):
    # Iniciamos la pila con el simbolo EOF (#) y el simbolo distinguido
    pila = ['#', 'Program']
    simboloApuntado = 0
    # Lista donde se trabaja con las derivaciones en cada ciclo
    derivacion = ['Program']
    # Lista donde se guardan todas las derivaciones
    derivaciones = []

    # Flag para salir del ciclo principal
    continuar = True

    # Ciclo principal
    while continuar:
        # Actualizamos el valor del tope
        tope = pila[-1]

        # Condición de éxito
        if (tope == '#') and (cadena[simboloApuntado] == '#'):
            print("La cadena es aceptada por el lenguaje")
            print("Derivaciones:")
            for i in derivaciones:
                print(i)
            break
            
        if tope in VT:
            if tope == cadena[simboloApuntado]:
                # Consumimos el último elemento de la pila
                pila.pop()
                # Avanzamos el puntero en un elemento
                simboloApuntado += 1
            
            # Si no se cumple la condición salimos del ciclo
            else:
                continuar = False
                print("La cadena no pertenece al lenguaje")
        else:
            # Intentamos obtener el elemento de la tabla en la posición indicada
            try:
                produccionTabla = tabla[tope][cadena[simboloApuntado]]
                # Damos vuelta la producción
                produccionReversed = []
                for i in produccionTabla:
                    # Insertamos todos los elementos en la posición 0 de la nueva lista
                    produccionReversed.insert(0, i)
                # Consumimos el último elemento de la pila
                pila.pop()
                # Agregamos la producción dada vuelta a la pila
                pila.extend(produccionReversed)
                # Guardamos la derivación
                derivacion = generarDerivacion(tope, derivacion, produccionTabla)
                # El .copy() es necesario porque sino se copian las referencias y tendriamos una lista con 5 elementos iguales
                derivaciones.append(derivacion.copy())

            # Si hay error salimos del ciclo   
            except:
                continuar = False
                print("La cadena no pertenece al lenguaje")





# def lex(codigo_fuente):
#     lista_tokens = []
#     for i in codigo_fuente:
#         if i == '(':
#             lista_tokens.append(('Token(', '('))
#         elif i == ')':
#             lista_tokens.append(('Token)', ')'))
#         else:
#             return []
#     lista_tokens.append(('Eof', 'Eof'))
#     return lista_tokens


# def desc_rec_proc(codigo_fuente):
#     datos_locales = {
#         'lista_tokens': codigo_fuente,
#         'index': 0,
#         'error': False,
#     }

#     def pni(no_terminal):
#         for cuerpo_produccion in P[no_terminal]:
#             backtracking_index = datos_locales['index']
#             procesar(cuerpo_produccion)
#             if datos_locales['error']:
#                 datos_locales['index'] = backtracking_index
#             else:
#                 break

#     def procesar(cuerpo_produccion):
#         for simbolo in cuerpo_produccion:
#             caracter_actual = datos_locales['lista_tokens'][datos_locales['index']][0]
#             # lexema_actual = datos_locales['lista_tokens'][datos_locales['index']][1]
#             datos_locales['error'] = False
#             if simbolo in VT:
#                 if simbolo == caracter_actual:
#                     datos_locales['index'] += 1
#                 else:
#                     datos_locales['error'] = True
#                     break
#             elif simbolo in VN:
#                 pni(simbolo)
#                 if datos_locales['error']:
#                     break

#     def principal():
#         pni('S')
#         caracter_actual = datos_locales['lista_tokens'][datos_locales['index']][0]
#         if caracter_actual != 'Eof' or datos_locales['error']:
#             print('La cadena no pertenece al lenguaje')
#             return False
#         print('La cadena pertenece al lenguaje')
#         return True

#     return principal()


# print(desc_rec_proc(lex('(())')))
