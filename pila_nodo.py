import random


class NodoPila():
    info, sig = None, None


class Pila():
    def __init__(self):
        self.tope = None
        self.tamanio = 0

def apilar(pila, dato):
    aux = NodoPila()
    aux.info = dato
    aux.sig = pila.tope
    pila.tope = aux
    pila.tamanio += 1

def desapilar(pila):
    dato = pila.tope.info
    pila.tope = pila.tope.sig
    pila.tamanio -= 1
    return dato

def pila_vacia(pila):
    pila.tamanio == 0

def tamanio(pila):
    return pila.tamanio

def cargaAutoInt(pila, num):
    for i in range (0, num):
        dato = random.randint(0, 10)
        apilar(pila, dato)
