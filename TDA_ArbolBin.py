class NodoArbol():
    def __init__(self, info):
        self.izq = None
        self.der = None
        self.info = info


def insertar_arbol(raiz, dato):
    if raiz is None:
        raiz = NodoArbol(dato)
        raiz.info = dato
    else:
        if dato < raiz.info:
            raiz.izq = insertar_arbol(raiz.izq, dato)
        else:
            raiz.der = insertar_arbol(raiz.der, dato)
    actualizarAltura(raiz)
    raiz = balancear(raiz)
    return(raiz)


def arbol_vacio(raiz):
    return raiz is None


def busqueda(raiz, buscado):
    pos = None
    if raiz is not None:
        if raiz.info == buscado:
            pos = raiz
        else:
            if buscado < raiz.info:
                pos = busqueda(raiz.izq, buscado)
            else:
                pos = busqueda(raiz.der, buscado)
    return pos


def preorden(raiz):
    if raiz is not None:
        print(raiz.info)
        preorden(raiz.izq)
        preorden(raiz.der)


def inorden(raiz):
    if raiz is not None:
        inorden(raiz.izq)
        print(raiz.info)
        inorden(raiz.der)


def postorden(raiz):
    if raiz is not None:
        postorden(raiz.der)
        print(raiz.info)
        postorden(raiz.izq)


def reemplazar(raiz):
    if raiz.der is not None:
        raiz.der == reemplazar(raiz.der)
    else:
        aux = raiz
        raiz = raiz.izq
    return(raiz, aux)


def eliminar(raiz, clave):
    x = None
    if raiz is not None:
        if raiz.info > clave:
            raiz.izq, x = eliminar(raiz.izq, clave)
        elif raiz.info < clave:
            raiz.der, x = eliminar(raiz.der, clave)
        else:
            x = raiz.info
            if raiz.izq is None:
                x == raiz.info
                raiz = raiz.der
            elif raiz.der is None:
                x == raiz.info
                raiz = raiz.izq
            else:
                raiz.izq, aux = reemplazar(raiz.izq)
                raiz.info = aux.info
        return(raiz, x)


def altura(raiz):
    if (raiz is None):
        return 0
    else:
        return raiz.altura


def actualizarAltura(raiz):
    if (altura(raiz.izq) > altura(raiz.der)):
        raiz.altura = altura(raiz.izq) + 1
    else:
        raiz.altura = altura(raiz.der) + 1
    return raiz


def rotacionSimple(raiz, control):  # Si es true rota a la der, sino izq
    '''Realiza rotacion simple'''
    if control:
        aux = raiz.izq
        raiz.izq = aux.der
        aux.der = raiz
    else:
        aux = raiz.der
        raiz.der = aux.izq
        aux.izq = raiz

    actualizarAltura(raiz)
    actualizarAltura(aux)
    raiz = aux

    return raiz


def rotacionDoble(raiz, control):  # La última rotación que se hace le da el
    '''Realiza rotacion doble'''
    if control:                    # nombre si es izquierda o derecha
        raiz.izq = rotacionSimple(raiz.izq, False)
        raiz = rotacionSimple(raiz, True)
    else:
        raiz.der = rotacionSimple(raiz.der, True)
        raiz = rotacionSimple(raiz, False)

    return raiz


def balancear(raiz):
    '''Balancea el arbol'''
    if (raiz is not None):
        if (altura(raiz.izq) - altura(raiz.der) == 2):  # El desbalance es izq
            if (altura(raiz.izq.izq) >= altura(raiz.izq.der)):
                raiz = rotacionSimple(raiz, True)
            else:
                raiz = rotacionDoble(raiz, True)
        elif (altura(raiz.der) - altura(raiz.izq) == 2):  # El desbalancees der
            if (altura(raiz.der.der) >= altura(raiz.der.izq)):
                raiz = rotacionSimple(raiz, False)
            else:
                raiz = rotacionDoble(raiz, False)

    return raiz


def imprimirArbol(raiz, espacios=0):
    ''' Imprime arbol, girado hacia la izquierda'''
    if raiz is not None:
        espacios += 5
        imprimirArbol(raiz.der, espacios)
        print(" " * espacios, str(raiz.info))
        imprimirArbol(raiz.izq, espacios)


def resolver(op, izq, der):
    resultado = 0
    if op == '*':
        resultado = izq * der
    if op == '/':
        resultado = izq / der
    if op == '+':
        resultado = izq + der
    if op == '-':
        resultado = izq - der

    return resultado


def hoja(r):
    if (r.izq is None and r.der is None):
        return True


def calcular(r):
    if hoja(r):
        return r.info
    else:
        return resolver(r.info, calcular(r.izq), calcular(r.der))


def peso(r):
    if r is not None:
        return 1 + peso(r.izq) + peso(r.der)
    else:
        return 0