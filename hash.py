from tda_lista import *
import random 
import math


def crearTablaAbierta(tamanio):
    tabla = []
    for i in range(0, tamanio):
        tabla.append(Lista())
    return tabla


def crearTablaCerrada(tamanio):
    tabla = []
    for i in range(0, tamanio):
        tabla.append(None)
    return tabla


def barridoHashAbierta(tabla):
    for lista in tabla:
        if lista.tamanio != 0:
            barrido(lista)


def barridoHashCerrada(tabla):
    for elemento in tabla:
        if elemento is not None:
            print(elemento)


def rehash(tabla, original):
    indice = original + 1
    if indice == len(tabla):
        indice = 0
    while (tabla[indice] is not None) and (indice != original):
        indice += 1
        if indice == len(tabla):
            indice = 0
    if indice == original:
        indice = None
    return indice


# Ej 1
'''tabla = crearTablaAbierta(28)'''


def hash(palabra):
    if len(palabra) > 0:
        clave = ord(palabra[0].capitalize()) - 65
        return clave


def insertarPalabra(tabla, palabra, descripcion):
    clave = hash(palabra)
    indice = clave % len(tabla)
    inserCampo(tabla[indice], [palabra, descripcion], 0)


def busquedaPalabra(tabla, palabra):
    indice = hash(palabra)
    return busquedaListaCampo(tabla[indice], palabra, 0)


def eliminarPalabra(tabla, palabra):
    indice = hash(palabra)
    if busquedaListaCampo(tabla[indice], palabra, 0) is not None:
        eliminarCampo(tabla[indice], palabra, 0)


# A
'''
insertarPalabra(tabla, 'mate', 'descripcion de mate')
insertarPalabra(tabla, 'auto', 'descripcion de auto')
insertarPalabra(tabla, 'libro', 'descripcion de libro')
'''
# B
'''
buscado = busquedaPalabra(tabla, 'libro')
if buscado is not None:
    print('Palabra encontrada: ' + str(buscado.info))
else:
    print('La palabra que desea buscar no se encuntra en el diccionario')
'''

# C No anda
'''
print('Diccionario completo')
barridoHashAbierta(tabla)
eliminarPalabra(tabla, 'mate')
print('Diccionario Actualizado')
barridoHashAbierta(tabla)
'''


# Ej 2
def insertarNum(tabla, numero, nya, dir):
    clave = hash(numero)
    indice = clave % len(tabla)
    inserCampo(tabla[indice], [numero, nya, dir], 0)


'''
insertarNum(tabla, str(random.randint(1500, 8000)), 'Pepito', 'Calle falsa 123')
insertarNum(tabla, str(random.randint(1500, 8000)), 'Lisa', 'Av.SiempreViva 730')
print('Guia telefonica')
barridoHashAbierta(tabla)
'''


# Ej 3
'''
def buscarcatedra(tabla, catedra):
    clave = hash(catedra[0])
    indice = clave % len(tabla)
    if tabla[indice][1] != catedra[1]:
        indice = rehash(tabla, indice)
    return indice


def nuevacat():
    doc = Lista()
    cod = random.randint(100, 200)
    nom = 'Catedra' + str(random.randint(0, 50))
    mod = random.choice(['Anual', 'Cuatrimestral'])
    horas = random.randint(5, 10)
    catedra = [cod, nom, mod, horas, doc]
    return catedra


def agregardocente(tabla, catedra):
    nombre = 'Docente' + str(random.randint(0, 15))
    docente = [docente]
    indice = buscarcatedra(tabla, catedra)
    if indice is not None:
        insertar(tabla[indice][4], docente)


tabla = crearTablaCerrada(10)


def hash(codigo):
    return codigo*3


def insertarcatedra(tabla, dato):
    clave = hash(dato)
    indice = clave % len(tabla)
    if tabla[indice] is None:
        tabla[indice] = dato
    else:
        indice = rehash(tabla, indice)
        if indice is not None:
            tabla[indice] = dato
        else:
            print('no hay mas lugares en la tabla')


def cantidadcargados(tabla):
    cont = 0
    for elemento in tabla:
        if elemento is not None:
            cont += 1
    return cont


cantidad_insertar = 5
for i in range(0, cantidad_insertar):
    catedra = nuevacat()
    insertarcatedra(tabla, catedra)


barridoHashCerrada(tabla)
print('Lugares ocupados: ' + str(cantidadcargados(tabla)))
'''
