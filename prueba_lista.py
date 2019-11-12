from tda_lista import NodoLista, cargaAuto, insertar, eliminar, barrido
from tda_lista import lista_vacia, tamanio, Lista, eliminarNodo
from tda_lista import cargaString, insertar1, primo, busquedaLista
from tda_lista import inserCampo, entre
import math
import random
from random import randint
l1 = Lista()
l2 = Lista()
l3 = Lista()

'''cargaAuto(l1, 5)
barrido(l1)
while l1.inicio is not None:
    eliminarNodo(l1)
    print('l1')
    barrido(l1)'''


# ej1
'''cargaAuto(l1, 10)
barrido(l1)
print('El tamanio es: ' + str(l1.tamanio))'''

# ej2
'''cargaString(l1, 10)
barrido(l1)
aux1 = l1.inicio
aux = l1.inicio
while aux is not None:
    if ((aux.info == 'a') or (aux.info == 'e') or (aux.info == 'i') or
    (aux.info == 'o') or (aux.info == 'u') or (aux.info == 'A') or
    (aux.info == 'E') or (aux.info == 'I') or (aux.info == 'O') or
    (aux.info == 'U')):
        eliminar(l1, aux.info)
    aux = aux.sig
print('lista sin vocales')
barrido(l1)'''


# ej3
'''cargaAuto(l1, 10)
barrido(l1)
aux = l1.inicio
while aux is not None:
    if aux.info % 2 == 0:
        insertar(l2, aux.info)
    else:
        insertar(l3, aux.info)
    aux = aux.sig
print('Lista de numeros pares:')
barrido(l2)
print('Lista de numeros impares:')
barrido(l3)'''


# ej4
'''cargaAuto(l1, 10)
barrido(l1)
insertar1(l1, 100, 3)
print("Lista con elemente agregado")
barrido(l1)'''

# ej5
'''cargaAuto(l1, 10)
barrido(l1)
print()
aux = l1.inicio
while aux is not None:
    if primo(aux.info):
        eliminar(l1, aux.info)
    aux = aux.sig
print('Lista sin numeros primos:')
barrido(l1)'''


# ej6


# ej7
'''cargaAuto(l1, 5)
cargaAuto(l2, 5)
print('lista 1')
barrido(l1)
print('lista 2')
barrido(l2)
aux = l1.inicio
aux1 = l2.inicio
c = 0
while aux is not None:
    if aux.info != aux1.info:
        insertar(l3, aux.info)
        insertar(l3, aux1.info)
    else:
        c += 1
    aux = aux.sig
    aux1 = aux1.sig
print('listas unidas')
barrido(l3)
print('Hay ' + str(c) + ' elementos repetidos')
while not lista_vacia(l3):
    eliminarNodo(l3)
    print('Menos un nodo')
    barrido(l3)'''


# ej8 TERMINAR
'''while tamanio(l1) < 10:
    aleatorio = random.randint(-999, 999)
    if busquedaLista(l1, aleatorio) is None:
        if primo(aleatorio):
            #rango con anterior y siguiente +14
                insertar(l1, aleatorio)
        else:
            if aleatorio mod 2 != 0:
                #anterior y siguiente pares
                    insertar(l1, aleatorio)
barrido(l1)'''


# ej 9
'''artistas = ['Arctic Monkeys', "The strokes", "Miles Kane", "Oasis",
            "Radiohead", "The killers", "Coldplay", "Kings of leon",
            "The kooks", "Kasabian", "Josh Homme", "Foo fighters"]
for i in range(0, 10):
    nom = 'Nombre: ' + str(random.randint(0, 50))
    artis = random.choice(artistas)
    dur = random.randint(60, 180)
    reprod = random.randint(200, 1000)
    cancion = [nom, artis, dur, reprod]
    inserCampo(l1, cancion, 1)
barrido(l1)
aux = l1.inicio'''
'''clarga = aux
while aux is not None:
    if (aux.info[2] > clarga.info[2]):
        clarga = aux
    aux = aux.sig
print('La cancion mas larga es ' + str(clarga.info))
t1 = aux
t2, t3, t4, t5 = 0, 0, 0, 0
while aux is not None:
    if (aux.info[3] > t1)'''
# puedo ordenar de mayor a menor por reproducciones
# y mostrar los primeros 5/10/50


# Punto c
'''aux = l1.inicio
while aux is not None:
    if aux.info[1] == 'Arctic Monkeys':
        inserCampo(l2, aux.info, 1)
    aux = aux.sig
if l2.inicio is None:
    print('No hay canciones de Arctic Monkeys')
else:
    print('Canciones de Arctic Monkeys')
    barrido(l2)'''


# Ej10
'''Pers = ['Darth Vader', 'Chewbacca', 'Per1', 'Per2', 'Per3', 'Per4', 'Per5',
        'Per6', 'Per7', 'Per8']
Planetas = ['Alderan', 'Planet1', 'Planet2', 'Planet3', 'Planet4', 'Planet5',
            'Planet6']
esp = ['Droide', 'Humano', 'Esp1', 'Esp2', 'Esp3', 'Esp4', 'Esp5']
gen = ['f', 'm']
for i in range(0, 10):
    nombre = random.choice(Pers)
    altura = str(random.randint(50, 150))
    edad = str(random.randint(200, 1000))
    genero = random.choice(gen)
    especie = random.choice(esp)
    planeta = random.choice(Planetas)
    episodio = str(random.randint(1, 7))
    StarWars = [nombre, altura, edad, genero, especie, planeta, episodio]
    inserCampo(l1, StarWars, 0)
barrido(l1)
aux = l1.inicio
aux1 = l2.inicio
'''
# Punto A
'''while aux is not None:
    if aux.info[3] == 'f':
        inserCampo(l2, aux, 0)
    aux = aux.sig
if aux1 is None:
    print('No hay personajes femeninos')
else:
    print('Lista de personajes femeninos')
    barrido(l2)'''

# Punto B Sintaxis invalida en el condicional
'''while aux is not None:
    if (aux.info[4] == 'Droide') and (aux.info[6] == '1')
    and (aux.info[6] == '2') and (aux.info[6] == '3') and (aux.info[6] == '4')
    and (aux.info[6] == '5') and (aux.info[6] == '6'):
        inserCampo(l2, aux, 4)
    aux = aux.sig
if aux1 is None:
    print('No hay personajes de la especie Droide en los primeros 6 episodios')
else:
    print('Lista de personajes de la especie Droide que aparecen en los 
            primeros 6 episodios')
    barrido(l2)'''


# Punto C
'''if aux.info[0] is 'Darth Vader':
    print(aux.info)'''


# Punto D
'''while aux is not None:
    if aux.info[6] == '4' and aux.info[6] == '5' aux.info[6] == '6'
    and aux.info[6] == '7':
        inserCampo(l2, aux, 0)
    aux = aux.sig
Print('Lista de personajes que aparecen en el episodio7 y en los 3 anteriores')
barrido(l2)'''


# Punto E
'''may = aux
while aux is not None:
    if aux.info[2] >= '850':
        inserCampo(l2, aux, 0)
        if may < aux.info[2]:
            may = aux
    aux = aux.sig
print('Personajes mayores a 850 años')
barrido(l2)
print('Persoanje de mayo edad' + str(may))'''


# Punto G
'''while aux is not None:
    if aux.info[4] == 'Humano' and aux.info[5] == 'Alderan':
        inserCampo(l2, aux, 0)
    aux = aux.sig
print('lista de personajes de especie humana con planeta de origen: Alderan')
barrido(l2)'''


# Punto H
'''while aux is not None:
    if aux.info[1] <= '70':
        inserCampo(l2, aux, 0)
    aux = aux.sig
if aux1 is None:
    print('No hay personajes de altura menor o igual a 70')
else:
    print('Lista de personajes con altura menor o igual a 70')
    barrido(l2)'''


# Ej15
'''for i in range(1, 8):
    costo = randint(1500, 3500)
    tiempo = randint(2, 12)  # tiempo en horas
    dia = randint(1, 28)
    mes = randint(1, 12)
    anio = randint(2018, 2019)
    persona = 'Persona ' + str(i)
    tarea = [costo, tiempo, dia, mes, anio, persona]
    inserCampo(l1, tarea, 1)
barrido(l1)
aux = l1.inicio
'''
# Punto A
'''
a = 0
while aux is not None:
    a += aux.info[1]
    aux = aux.sig
prom = (a//7)
print('El tiempo promedio de tareas es de: ' + str(prom) + ' horas')
'''

# Punto B
'''
a = 0
while aux is not None:
    a += aux.info[0]
    aux = aux.sig
print('El costo total del proyecto es de: $' + str(a))
'''
# Punto C
'''
while aux is not None:
    if aux.info[5] == 'Persona 5':
        inserCampo(l2, aux.info, 5)
    aux = aux.sig
print('Actividades realizadas por Persona 5: ')
barrido(l2)
'''

# Punto D
'''
f1 = [7, 8, 2018]
f2 = [5, 9, 2019]
print('Tareas a realizar entre ' + str(f1) + ' y ' + str(f2) + ' : ')
while aux is not None:
    if entre(aux.info[2], f1[0], f2[0]) and entre(aux.info[3], f1[1], f2[1])
    and entre(aux.info[4], f1[2], f2[2]):
        print(aux.info)
    aux = aux.sig
'''

# Ej 16
'''for i in range(0, 7):
    emp = 'Empresa' + str(random.randint(1, 8))
    num = str(randint(1, 8))
    cant = randint(265, 500)
    dia = randint(1, 28)
    mes = randint(1, 12)
    ciudad = ['Buenos aires', 'Londres', 'Montevideo', 'Miami', 'Francia']
    origen = random.choice(ciudad)
    ciudad1 = ['Atenas', 'Bariloche', 'San Pablo', 'California', 'Sudafrica']
    destino = random.choice(ciudad1)
    km = randint(1000, 11000)
    numero = randint(1, 265)
    clas = ['Turista', 'Primera']
    clase = random.choice(clas)
    est = ['libre', 'ocupado']
    estado = random.choice(est)
    persona = 'Persona' + str(randint(1, 50))
    asiento = [numero, clase, estado, persona]
    vuelo = [emp, num, cant, dia, mes, origen, destino, km, asiento]
    inserCampo(l1, vuelo, 6)
barrido(l1)
aux = l1.inicio'''

# Punto A
'''while aux is not None:
    if aux.info[6] == 'Atenas':
        inserCampo(l2, aux.info, 6)
    aux = aux.sig
if l2.inicio is None:
    print('No hay vuelos con destino Atenas')
else:
    print('Lista de vuelos con destino Atenas')
    barrido(l2)'''

# Punto B
'''while aux is not None:
    if aux.info[8][1] == 'Turista':
        if aux.info[8][2] == 'libre':
            inserCampo(l2, aux.info, 6)
    aux = aux.sig
if l2.inicio is None:
    print('No hay vuelos con clase turista libre')
else:
    print('Lista de vuelos con clase turista libre')
    barrido(l2)
'''

# Punto C


# Punto D
'''while aux is not None:
    if (aux.info[3] == 23) and (aux.info[4] == 8):
        inserCampo(l2, aux.info, 6)
    aux = aux.sig
if l2.inicio is None:
    print('No hay vuelos programados para dicha fecha')
else:
    print('Lista de vuelos para dicha fecha')
    barrido(l2)
'''

# Punto E


# Ej20
'''
for i in range(0, 10):
    abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    nombre = random.choice(abc)
    precio = str(random.randint(200, 1000))
    calif = str(random.randint(1, 5))
    producto = [nombre, precio, calif]
    inserCampo(l1, producto, 2) # Podemos cambiar el orden modificando la ultima variable
barrido(l1)
aux = l1.inicio'''

# Punto A
'''
while aux is not None:
    if aux.info[0] == 'P':
        inserCampo(l2, aux.info, 0)
    aux = aux.sig
if l2.inicio is None:
    print('No hay productos con ese nombre')
else:
    print('Producto con dicho nombre')
    barrido(l2)'''


# Punto C
'''while aux is not None:
    inserCampo(l2, aux.info, 2)
    aux = aux.sig
print('lista ordenada de acuerdo a la clasificacion')
barrido(l2)'''

# Punto D
'''
menor = aux.info
while aux is not None:
    if aux.info[2] == '3':
        if menor[1] > aux.info[1]:
            menor = aux.info
    aux = aux.sig
print('Producto mas barato: ' + str(menor))
'''

# Punto E
'''while aux is not None:
    if aux.info[0] == 'H':
        inserCampo(l2, aux.info, 1)
    aux = aux.sig
if l2.inicio is None:
    print('No hay productos con la letra H')
else:
    print('Lista de precios de productos que comienzan con la letra H')
    barrido(l2)'''
