import random
max = 10


class Pila():

    def __init__(self):
        self.tope = -1
        self.datos = []
        for i in range(0, max):
            self.datos.append(None)


def cargaAutoInt(pila):
    """Carga toda la pila con enteros"""
    while not pila_llena(pila):
        dato = random.randint(0, 10)
        apilar(pila, dato)


def cargaAutoStr(pila):
    """Carga tola la pila con strings"""
    while not pila_llena(pila):
        largo = random.randint(1, 15)
        apilar(pila, randString(largo))


def apilar(pila, dato):
    """Apila un elemento en la pila"""
    pila.tope += 1
    pila.datos[pila.tope] = dato


def desapilar(pila):
    """Desapila el elemento en cima"""
    dato = pila.datos[pila.tope]
    pila.tope -= 1
    return dato


def pila_llena(pila):
    """Devuelve True si la pila esta llena"""
    return pila.tope + 1 == max


def pila_vacia(pila):
    """Devuelve True si la pila esta vacia"""
    return pila.tope == -1


def tamanio(pila):
    """Devuelve tamaño de pila"""
    return pila.tope + 1


def cima(pila):
    """Devuelve elemento de la cima"""
    return pila.datos[pila.tope]


def barrido(pila):
    """Muestra todos elementos en pila"""
    paux = Pila()
    while not pila_vacia(pila):
        dato = desapilar(pila)
        print(dato)
        apilar(paux, dato)
    while not pila_vacia(paux):
        apilar(pila, desapilar(paux))


def invertir(pila1):
    """Devuelve la pila invertida"""
    pila2 = Pila()
    while not pila_vacia(pila1):
        apilar(pila2, desapilar(pila1))
    return pila2


def randString(largo=1):
    """Devuelve una cadena aleatoria"""
    valores = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return '' .join(random.choice(valores) for i in range(largo))


def stringToPila(palabra):
    """Devuelve pila del string ingresado"""
    pila = Pila()
    for elemento in palabra:
        apilar(pila, elemento)
    return pila


def ordenPilaCrec(pila):
    """Devuelve pila ordenada"""
    aux = Pila()

    while not pila_vacia(pila):
        cont = 0
        dato = desapilar(pila)

        while not pila_vacia(aux) and (cima(aux) >= dato):
            apilar(pila, desapilar(aux))
            cont += 1
        apilar(aux, dato)

        for i in range(0, cont):
            apilar(aux, desapilar(pila))

    return aux


def ordenPilaDecr(pila):
    """Devuelve pila ordenada"""
    aux = Pila()

    while not pila_vacia(pila):
        cont = 0
        dato = desapilar(pila)

        while not pila_vacia(aux) and (cima(aux) <= dato):
            apilar(pila, desapilar(aux))
            cont += 1
        apilar(aux, dato)

        for i in range(0, cont):
            apilar(aux, desapilar(pila))

    return aux


def fibonacciPila(n):  # Falta terminar
    """Devuelve sucesion de Fibonacci de numero ingresado"""

    p = Pila()
    apilar(p, 0)
    apilar(p, 1)

    while not pila_vacia(p):
        dato = desapilar(p)
        if dato == 0 or dato == 1:
            return x
        else:
            apilar(p, n-1)
            apilar(p, n-2)


def comprobarOrdenAsc(lista):
    """Comprueba que la lista este ordenada ascendentemente"""
    band = True
    i = 0
    while band and (i < len(lista) - 1):
        if (lista[i] > lista[i + 1]):
            band = False
        i += 1
    return band
