from LexerV2 import *

VN = ['Program', 'ListaSentencias', 'ListaSentenciasP', 'Sentencia', 'SentenciaSi', 'SentenciaRepetir', 'SentenciaAsig',
      'SentenciaLeer', 'SentenciaMostrar', 'SentenciaFun', 'Proc', 'ListaPar', 'ListaParP', 'Expresion', 'Expresion2',
      'Expresion2P', 'Termino', 'TerminoP', 'Factor']

VT = TOKENS_POSIBLES

tabla = {
    'Program': {
        'si': ['ListaSentencias'],
        'repetir': ['ListaSentencias'],
        'id': ['ListaSentencias'],
        'leer': ['ListaSentencias'],
        'mostrar': ['ListaSentencias'],
        'func': ['ListaSentencias']
    },
    'ListaSentencias': {
        'si': ['Sentencia', 'ListaSnteciasP'],
        'repetir': ['Sentencia', 'ListaSnteciasP'],
        'id': ['Sentencia', 'ListaSnteciasP'],
        'leer': ['Sentencia', 'ListaSnteciasP'],
        'mostrar': ['Sentencia', 'ListaSnteciasP'],
        'func': ['Sentencia', 'ListaSnteciasP']
    },
    'ListaSentenciasP': {
        ';': [';'],
        '#': [],
        'sino': [],
        'finsi': [],
        'hasta': [],
        'finfunc': [],
    },
    'Sentencia': {
        'si': ['SentenciaSi'],
        'repetir': ['SentenciaRepetir'],
        'id': ['SentenciaAsig'],
        'leer': ['Sentencialeer'],
        'mostrar': ['SentenciaMostrar'],
        'func': ['SentenciaFun']
    },
    'SentenciaSi': {
        'si': ['si', 'Expresion', 'entonces', 'ListaSentencias', 'sino', 'ListaSentencias', 'finsi'],
        # preguntar
        'si': ['si', 'Expresion', 'entonces', 'ListaSentencias', 'finsi']
    },
    'SentenciaRepetir': {
        'repetir': ['repetir', 'ListaSenteicas', 'hasta', 'Expresion']
    },
    'SentenciaAsig': {
        'id': ['id', 'equal', 'Expresion']
    },
    'SentenciaLeer': {
        'leer': ['leer', 'id']
    },
    'SentenciaMostrar': {
        'mostrar': ['mostrar', 'Expresion']
    },
    'SentenciaFun': {
        'func': ['func', 'Proc', 'finfunc']
    },
    'Proc': {
        'id': ['id', '(', 'ListaPar', ')', 'ListaSentencias']
    },
    'ListaPar': {
        'id': ['id', 'ListaParP']
    },
    'ListaParP': {
        ';': [';', 'id', 'ListaParP'],
        ')': []
    },
    'Expresion': {
        '(': ['Expresion2'],
        'num': ['Expresion2'],
        'id': ['Expresion2']
    },
    'Expresion2': {
        '(': ['Termino', 'Expresion2P'],
        'num': ['Termino', 'Expresion2P'],
        'id': ['Termino', 'Expresion2P']
    },
    'Expresion2P': {
        'opsuma': ['opsuma', 'Termino', 'Expresion2P'],
        'oprel': [],
        '#': [],
        'entonces': [],
        ')': []
    },
    'Termino': {
        '(': ['Factor', 'TerminoP'],
        'num': ['Factor', 'TerminoP'],
        'id': ['Factor', 'TerminoP']
    },
    'TerminoP': {
        'opmult': ['opmult', 'Factor', 'TerminoP'],
        'opsuma': [],
        'oprel': [],
        '#': [],
        'entonces': [],
        ')': []
    },
    'Factor': {
        '(': ['(', 'Expresion', ')'],
        'num': ['num'],
        'id': ['id']
    }
}

P = {'S': [['Token(', 'S', 'Token)', 'S'],
           ['Token(', 'Token)', 'S'],
           ['Token(', 'S', 'Token)'],
           ['Token(', 'Token)']]}


def lex(codigo_fuente):
    lista_tokens = []
    for i in codigo_fuente:
        if i == '(':
            lista_tokens.append(('Token(', '('))
        elif i == ')':
            lista_tokens.append(('Token)', ')'))
        else:
            return []
    lista_tokens.append(('Eof', 'Eof'))
    return lista_tokens


def desc_rec_proc(codigo_fuente):
    datos_locales = {
        'lista_tokens': codigo_fuente,
        'index': 0,
        'error': False,
    }

    def pni(no_terminal):
        for cuerpo_produccion in P[no_terminal]:
            backtracking_index = datos_locales['index']
            procesar(cuerpo_produccion)
            if datos_locales['error']:
                datos_locales['index'] = backtracking_index
            else:
                break

    def procesar(cuerpo_produccion):
        for simbolo in cuerpo_produccion:
            caracter_actual = datos_locales['lista_tokens'][datos_locales['index']][0]
            # lexema_actual = datos_locales['lista_tokens'][datos_locales['index']][1]
            datos_locales['error'] = False
            if simbolo in VT:
                if simbolo == caracter_actual:
                    datos_locales['index'] += 1
                else:
                    datos_locales['error'] = True
                    break
            elif simbolo in VN:
                pni(simbolo)
                if datos_locales['error']:
                    break

    def principal():
        pni('S')
        caracter_actual = datos_locales['lista_tokens'][datos_locales['index']][0]
        if caracter_actual != 'Eof' or datos_locales['error']:
            print('La cadena no pertenece al lenguaje')
            return False
        print('La cadena pertenece al lenguaje')
        return True

    return principal()


print(desc_rec_proc(lex('(())')))
