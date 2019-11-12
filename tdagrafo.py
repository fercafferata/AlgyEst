from tdacola import *
from tda_lista import *
from tda_heap import *
from tdapila import *


class NodoArista():
    info, sig, peso = None, None, 0


class Arista():
    inicio, tamanio = None, 0


class NodoVertice():
    info, sig, adyacentes, visitado = None, None, Arista(), False

    def __init__(self, info):
        self.info = info
        self.sig = None
        self.visitado = False
        self.adyacente = lista_arista()


class Grafo():
    inicio, tamanio, dirigido = None, 0, True

    def __init__(self, dirigido):
        self.inicio = None
        self.tamanio = 0
        self.dirigido = dirigido


def insertar_v(g, dato):
    nodo = NodoVertice()
    nodo.info = dato
    if g.inicio is None or nodo.info < g.inicio.info:
        nodo.sig = g.inicio
        g.inicio = nodo
    else:
        act = g.inicio.sig
        ant = g.inicio
        while act is not None and act.info <= nodo.info:
            act = act.sig
            ant = ant.sig
        nodo.sig = act
        ant.sig = nodo
    g.tamanio += 1


def eliminar_v(g, clave):
    x = None
    if g.inicio.info == clave:
        x = g.inicio.info
        g.inicio = g.inicio.sig
        g.tamanio -= 1
    else:
        ant = g.inicio
        act = g.inicio.sig
        while (act is not None) and (act.info != clave):
            ant = act
            act = act.sig
        if (act is not None):
            x = act.info
            ant.sig = act.sig
            g.tamanio -= 1
    if x is not None:
        aux = g.inicio
        while aux is not None:
            eliminar_a(aux.adyacentes, x)
    return x


def eliminar_a(vertice, clave):
    x = None
    if vertice.inicio.info == clave:
        x = vertice.inicio.info
        vertice.inicio = vertice.inicio.sig
        vertice.tamanio -= 1
    else:
        ant = vertice.inicio
        act = vertice.inicio.sig
        while (act is not None) and (act.info != clave):
            ant = act
            act = act.sig
        if (act is not None):
            x = act.info
            ant.sig = act.sig
            vertice.tamanio -= 1
    return x


def agregar_arista(g, dato):
    nodo = Arista()
    nodo.info = dato
    if g.inicio is None or nodo.info < g.inicio.info:
        nodo.sig = g.inicio
        g.inicio = nodo
    else:
        act = g.inicio.sig
        ant = g.inicio
        while act is not None and act.info <= nodo.info:
            act = act.sig
            ant = ant.sig
        nodo.sig = act
        ant.sig = nodo
    g.tamanio += 1


def insertar_a(g, dato, origen, destino):
    if(g.dirigido):
        agregar_arista(origen.adyacentes, dato, destino.info)
    else:
        agregar_arista(origen.adyacentes, dato, destino.info)
        agregar_arista(destino.adyacentes, dato, origen.info)


def buscar_arista(vertice, buscado):
    aux = vertice.adyacentes.inicio
    while(aux is not None and aux.destino != buscado):
        aux = aux.sig
    return aux


def buscar_vertice(g, buscado):
    aux = g.adyacentes.inicio
    while(aux is not None and aux.destino != buscado):
        aux = aux.sig
    return aux


def barrido_profundidad(g, vertice):
    while vertice is not None:
        if not vertice.visitado:
            vertice.visitado = True
            print(vertice.info)
            adyacentes = vertice.adyacentes.inicio
            while adyacentes is not None:
                adyacentes = buscar_vertice(grafo, adyacentes.destino)
                if not adyacentes.visitado:
                    barrido_profundidad(grafo, adyacentes)
                adyacentes = adyacentes.sig
    vertice = vertice.sig


def barrido_amplitud(g, vertice):
    cola = Cola()
    while vertice is not None:
        if not vertice.visitado:
            vertice.visitado = True
            arribo(cola, vertice)
            while not cola_vacia(cola):
                nodo = atencion(cola)
                print(nodo.inicio)
                adyacentes = nodo.adyacentes.inicio
                while adyacentes is not None:
                    adyacente = buscar_vertice(g, adyacentes.destino)
                    if not adyacente.visitado:
                        adyacente.visitado = True
                        arribo(cola, adyacente)
                    adyacentes = adyacentes.sig
    vertice = vertice.sig


'''def existe_paso(g, origen, destino):
    resultado = False
    if not origen.visitado:
        origen.visitado = True
        vadyacentes = origen.adyacentes.inicio
        while vadyacentes is not None and not resultado:
            adyacente = buscar_vertice(g, vadyacentes.origen)
            if(adyacentes.info = destino)'''


def marcar_no_visitados(g):
    aux = g.inicio
    while aux is not None:
        aux.visitado = False
    aux = aux.sig


def dijkstra(g, origen, destino):
    no_visitados = Heap(tamanio(g))
    camino = Pila()
    aux = g.inicio
    while aux is not None:
        if(aux.info == origen):
            arribo_h(no_visitados, [aux, None], 0)
        else:
            arribo_h(no_visitados, [aux, None], inf)
        aux = aux.sig
    while(not heap_vacio(no_visitados)):
        dato = atencion_h(no_visitados)
        apilar(camino, dato)
        aux = dato[1][0].adyacentes.inicio
        while aux is not None:
            pos = buscar_h(no_visitados, aux.destino)
            if(no_visitados.vector[pos][0] > dato[0] + aux.info):
                no_visitados.vector[pos][1][1] = dato[1][0].info
                cambiar_prioridad(no_visitados, pos, dato[0] + aux.info)
            aux = aux.sig
    return camino


def kruskal(grafo):
    bosque = []
    aristas = Heap(tamanio(grafo)**2)
    aux = grafo.inicio
    while aux is not None:
        bosque.append([aux.info])
        vadyacentes = aux.adyacentes.inicio
        while vadyacentes is not None:
            arribo_H(arista, [aux.info, vadyacentes.destino], vadyacentes.info)
            vadyacentes = vadyacentes.sig
        aux = aux.sig
    while len(bosque[0]) == 1 and not heap_vacio(aristas):
        dato = atencion_h(aristas)
        origen = None
        for elemento in bosque:
            if dato[1][0] in elemento:
                origen = bosque.pop(bosque.index(elemento))
        destino = None


'''cuando dijkstra'''
'''
fin = 's'
while not pila_vacia(camino):
    dato = desapilar(camino)
    if fin == dato[1][0].info,'hasta', dato[1][1], dato[0]:
        fin = dato[1][1]'''