import random
max = 100


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


def fibonacciPila(n):
    """Devuelve sucesion de Fibonacci de numero ingresado"""

    p = Pila()
    apilar(p, 0)

    if (n == 1):
        apilar(p, 1)
    elif (n > 1):
        apilar(p, 1)
        while not pila_llena(p) and tamanio(p) <= n:
            dato = desapilar(p)
            dato2 = cima(p)
            apilar(p, dato)
            apilar(p, (dato + dato2))
    print(p)



def comprobarOrdenAsc(lista):
    """Comprueba que la lista este ordenada ascendentemente"""
    band = True
    i = 0
    while band and (i < len(lista) - 1):
        if (lista[i] > lista[i + 1]):
            band = False
        i += 1
    return band


def factorialPila(n):
    """Devuelve factorial de numero introducido"""
    factorial = 1
    p = Pila()
    while n > 0:
        apilar(p, n)
        n -= 1
    while not pila_vacia(p):
        factorial *= desapilar(p)

    return factorial


def quicksortPila(vect, pri, ult):
    """Ordena lista por quicksort iterativo"""
    p = Pila()
    apilar(p, [pri, ult])
    datos = []

    while not pila_vacia(p):
        datos = desapilar(p)

        i = datos[0]
        j = datos[1] - 1
        pivot = datos[1]

        while (i < j):
            while (vect[i] <= vect[pivot]) and (i < j):
                i += 1
            while (vect[j] > vect[pivot]) and (i < j):
                j -= 1
            if i <= j:
                vect[i], vect[j] = vect[j], vect[i]
        if vect[pivot] < vect[i]:
            vect[pivot], vect[i] = vect[i], vect[pivot]

        if datos[0] < j:
            apilar(p, [datos[0], j])
        if datos[1] > i:
            apilar(p, [i+1, datos[1]])


def listaRandom(tamanio):
    """Devuelve lista random de tamanio indicado"""
    lista = []
    for i in range(0, tamanio):
        lista.append(random.randint(-1000, 1000))

    return lista