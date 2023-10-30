from LexerV2 import *

VN = ['Program', 'ListaSentencias', 'ListaSentenciasP', 'Sentencia', 'SentenciaSi', 'SentenciaRepetir', 'SentenciaAsig',
      'SentenciaLeer', 'SentenciaMostrar', 'SentenciaFun', 'Proc', 'ListaPar', 'ListaParP', 'Expresion', 'Expresion2',
      'Expresion2P', 'Termino', 'TerminoP', 'Factor']

VT = ["TOKEN ID", "TOKEN NUM", "TOKEN si", "TOKEN entonces", "TOKEN sino", "TOKEN finsi", "TOKEN repetir","TOKEN hasta", "TOKEN equal", "TOKEN leer", "TOKEN mostrar", "TOKEN func", "TOKEN finfunc", "TOKEN parentesisIzq", "TOKEN parentesisDer", "TOKEN puntoycoma", "TOKEN oprel", "TOKEN opsuma", "TOKEN opmult"]

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
        'TOKEN leer': ['SentenciaLeer'],
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
        'TOKEN ID': ['TOKEN ID', 'TOKEN equal', 'Expresion']
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
        'TOKEN parentesisDer': ['Expresion2'],
        'TOKEN NUM': ['Expresion2'],
        'TOKEN ID': ['Expresion2']
    },
    'Expresion2': {
        'TOKEN parentesisIzq': ['Termino', 'Expresion2P'],
        'TOKEN NUM': ['Termino', 'Expresion2P'],
        'TOKEN ID': ['Termino', 'Expresion2P']
    },
    'Expresion2P': {
        'TOKEN opsuma': ['TOKEN opsuma', 'Termino', 'Expresion2P'],
        'TOKEN oprel': [],
        '#': [],
        'TOKEN entonces': [],
        'TOKEN parentesisDer': []
    },
    'Termino': {
        '(': ['Factor', 'TerminoP'],
        'TOKEN NUM': ['Factor', 'TerminoP'],
        'TOKEN ID': ['Factor', 'TerminoP']
    },
    'TerminoP': {
        'TOKEN opmult': ['TOKEN opmult', 'Factor', 'TerminoP'],
        'TOKEN opsuma': [],
        'TOKEN oprel': [],
        '#': [],
        'TOKEN entonces': [],
        'TOKEN parentesisDer': []
    },
    'Factor': {
        'TOKEN parentesisIzq': ['TOKEN parentesisIzq', 'Expresion', 'TOKEN parentesisDer'],
        'TOKEN NUM': ['TOKEN NUM'],
        'TOKEN ID': ['TOKEN ID']
    }
}

def traduccionParser(salidaLexer):
    cadena = []
    # Ponemos cada primer elemento de cada tupla (token) en una lista
    for tupla in salidaLexer:
        cadena.append(tupla[0])
    cadena.append('#')
    return cadena

# Función que genera las derivaciones, recibe el elemento a derivar, en que cadena y por que se deriva
def genDerivacion(topePila, produccionAnterior, derivacion):
    # Obtenemos en que posición se encuentra el elemento a derivar
    indice = produccionAnterior.index(topePila)
    # Eliminamos el elemento a derivar
    produccionAnterior.remove(topePila)
    # Damos vuelta la lista de 'derivacion' para que luego al insertarla quede en el orden original
    produccionInvertida = []
    for i in derivacion:
        produccionInvertida.insert(0, i)

    # Insertamos la lista dada vuelta en la cadena a derivar
    for i in produccionInvertida:
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
                produccionInvertida = []
                for i in produccionTabla:
                    # Insertamos todos los elementos en la posición 0 de la nueva lista
                    produccionInvertida.insert(0, i)
                # Consumimos el último elemento de la pila
                pila.pop()
                # Agregamos la producción dada vuelta a la pila
                pila.extend(produccionInvertida)
                # Guardamos la derivación
                derivacion = genDerivacion(tope, derivacion, produccionTabla)
                # El .copy() es necesario porque sino se copian las referencias y tendriamos una lista con 5 elementos iguales
                derivaciones.append(derivacion.copy())

            # Si hay error salimos del ciclo   
            except:
                continuar = False
                print("La cadena no pertenece al lenguaje")

