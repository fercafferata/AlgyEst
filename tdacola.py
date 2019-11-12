import random

max = 10


class Cola():
    def __init__(self):
        self.datos = []
        for i in range(0, max):
            self.datos.append(None)
        self.frente = -1
        self.final = -1
        self.tamanio = 0


def cargacaract(cola):
    caract = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ,.;:/*-+=%$?¿¡!'
    while not cola_llena(cola):
        arribo(cola, random.randint(0, 15000))
        arribo(cola, random.choice(caract))


def cargautomatica(cola):
    while not cola_llena(cola):
        dato = random.randint(0, 10)
        arribo(cola, dato)


def arribo(cola, dato):
    cola.final += 1
    if cola.final == max:
        cola.final = 0
    if cola.frente == -1:
        cola.frente = 0
    cola.datos[cola.final] = dato
    cola.tamanio += 1


def atencion(cola):
    aux = cola.datos[cola.frente]
    cola.frente += 1
    cola.tamanio -= 1
    if cola.frente == max:
        cola.frente = 0
    if cola.tamanio == 0:
        cola.frente == -1
        cola.final = -1
    return aux


def cola_vacia(cola):
    return cola.tamanio == 0


def cola_llena(cola):
    return cola.tamanio == max


def barrido(cola):
    caux = Cola()
    while not cola_vacia(cola):
        aux = atencion(cola)
        print(aux)
        arribo(caux, aux)
    while not cola_vacia(caux):
        aux = atencion(caux)
        arribo(cola, aux)


def moverAfinal(cola):
    aux = atencion(cola)
    arribo(cola, aux)


def cargaAutoStr(cola):
    abc = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    while not cola_llena(cola):
        arribo(cola, random.choice(abc))


def cargaAutoInt(cola):
    while not cola_llena(cola):
        dato = random.randint(0, 15000)
    arribo(cola, dato)


def primo(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def tamanio(cola):
    return cola.tamanio
    

def fibonacci(indice):
    c = Cola()
    c1 = Cola()

    arribo(c, 0)
    arribo(c, 1)

    if (indice < 1) and (indice >= 0):
        moverAfinal(c)
        atencion(c)
    elif (indice > 1):
        while tamanio(c) <= indice:
            while tamanio(c) > 2:
                arribo(c1, atencion(c))
            dato1 = atencion(c)
            dato2 = atencion(c)
            suma = 0
            suma = dato1 + dato2
            arribo(c1, dato1)
            arribo(c1, dato2)
            arribo(c1, suma)
            c, c1 = c1, c
    barrido(c)
