from tdapila import Pila, apilar, desapilar, pila_llena, pila_vacia, tamanio
from tdapila import cima, barrido, cargaAutoInt, invertir, randString, stringToPila
from tdapila import ordenPilaCrec, cargaAutoStr, factorialPila, fibonacciPila 
from tdapila import quicksortPila, listaRandom, comprobarOrdenAsc
import random

p = Pila()
p1 = Pila()
p2 = Pila()
p3 = Pila()
p4 = Pila()


# Ej1
'''cargaAutoInt(p)
barrido(p)

num = 1
cont = 0

paux = Pila()
while not pila_vacia(p):
    dato = desapilar(p)
    if (dato == num):
        cont += 1
    apilar(paux, dato)

print('El numero ' + str(num) + ' se encuentra ' + str(cont) + ' veces en la lista')'''


# Ej2
'''cargaAutoInt(p)
print("Todos:")
barrido(p)
while not pila_vacia(p):
    dato = desapilar(p)
    if (dato % 2 == 0):
        apilar(p1, dato)
p = invertir(p1)
print('Solo pares:')
barrido(p)'''


# Ej3
'''num = 3
reemplazo = 100
cargaAutoInt(p)
print("Pila:")
barrido(p)
while not pila_vacia(p):
    dato = desapilar(p)
    if dato == num:
        dato = reemplazo
    apilar(p1, dato)
p = invertir(p1)
print("Pila con el numero " + str(num) + " reemplazado por el " + str(reemplazo))
barrido(p)'''


# Ej4
'''cargaAutoInt(p)
barrido(p)
p = invertir(p)
print("Pila anterior invertida:")
barrido(p)'''

# Ej5
'''palindr = True
palabra = 'ala'
# palabra = 'hola'
for elemento in palabra:
    apilar(p, elemento)

while not pila_vacia(p):
    dato = desapilar(p)
    apilar(p1, dato)
    apilar(p2, dato)

p = invertir(p2)

while not pila_vacia(p):
    dato1 = desapilar(p)
    dato2 = desapilar(p1)
    if dato1 != dato2:
        palindr = False
    apilar(p2, dato2)

if palindr:
    print('Palindromo')
else:
    print('No palindromo')'''


# Ej6
'''palabra = randString(3)
p = stringToPila(palabra)

print('Pila normal:')
barrido(p)

p1 = invertir(p)
print('Pila invertida')
barrido(p1)'''


# Ej7
'''cargaAutoInt(p)
i = 3
print('Pila:')
barrido(p)

if (i < tamanio(p)):
    while not pila_vacia(p):
        aux = desapilar(p)
        if i != p.tope + 1:
            apilar(p1, aux)

    p = invertir(p1)
    print('Pila con elemento en posicion ' + str(i) + ' eliminado')
    barrido(p)
else:
    print("El numero ingresado existe el limite de la pila")'''


# Ej8
'''palos = ['Oro', 'Basto', 'Copa', 'Espada']
while not pila_llena(p):
    num = random.randint(1, 13)
    palo = random.choice(palos)
    apilar(p, [num, palo])

while not pila_vacia(p):
    carta = desapilar(p)
    if carta[1] == 'Oro':
        apilar(p1, carta)
    elif carta[1] == 'Basto':
        apilar(p2, carta)
    elif carta[1] == 'Copa':
        apilar(p3, carta)
    elif carta[1] == 'Espada':
        apilar(p4, carta)

print('Oro:')
barrido(p1)
print('Basto:')
barrido(p2)
print('Copa:')
barrido(p3)
print('Espada:')
barrido(p4)

p1 = ordenPilaCrec(p1)
print('Oro ordenado crecientemente:')
barrido(p1)
while not pila_llena(p):
    num = random.randint(1, 12)
    palo = random.choice(palos)
    apilar(p, [num, palo])

while not pila_vacia(p):
    carta = desapilar(p)
    if carta[1] == 'Oro':
        apilar(p1, carta)
    elif carta[1] == 'Basto':
        apilar(p2, carta)
    elif carta[1] == 'Copa':
        apilar(p3, carta)
    elif carta[1] == 'Espada':
        apilar(p4, carta)

print('Oro:')
barrido(p1)
print('Basto:')
barrido(p2)
print('Copa:')
barrido(p3)
print('Espada:')
barrido(p4)

p1 = ordenPilaCrec(p1)
print('Oro ordenado crecientemente:')
barrido(p1)'''


# Ej9
'''print(str(factorialPila(5)))'''


# Ej10
'''cargaAutoInt(p)
barrido(p)
while not pila_vacia(p):
    dato = desapilar(p)
    if dato % 2 == 0:
        apilar(p1, dato)
    else:
        apilar(p2, dato)
print('Pila par:')
barrido(p1)
print('Pila impar:')
barrido(p2)'''


# Ej11
'''vocales = 'aeiouAEIOU'
palabra = 'Algoritmos'
cont = 0
p = stringToPila(palabra)

while not pila_vacia(p):
    dato = desapilar(p)
    if dato in vocales:
        cont += 1
    apilar(p1, dato)
print('Hay ' + str(cont) + ' vocales')

p = invertir(p1)
barrido(p)'''


# Ej12
'''num = int(input('Ingrese un numero: '))
while num != 0:
    if not pila_llena(p):
        while not pila_vacia(p) and (cima(p) >= num):
            apilar(p1, desapilar(p))
        apilar(p, num)
        while not pila_vacia(p1):
            apilar(p, desapilar(p1))
    else:
        print('Pila llena')
    barrido(p)
    num = int(input('Ingrese un numero: '))'''


# Ej13
'''z = 100
cant_orden = 0
no_orden = []

for k in range(0, z):
    lista = listaRandom(14)

    quicksortPila(lista, 0, len(lista) - 1)
    print(lista)
    ordenado = comprobarOrdenAsc(lista)
    if ordenado:
        cant_orden += 1

print("Se ordenaron correctamente: " + str(cant_orden) + " de " + str(z))'''


# Ej14
'''num = '0123456789'
parrafo = 'Hoy, en mi casa hay 3 perros.'
voc = 'aeiouAEIOU'
cons = 'bcdfghjklmnñpqrstvwxyzBCDFGHJKLMNÑPQRSTVWXYZ'
for elemento in parrafo:
    if elemento in voc:
        apilar(p1, elemento)
    else:
        if elemento in cons:
            apilar(p2, elemento)
        else:
            apilar(p3, elemento)
# Parte A
print('Cantidad de vocales: ' + str(tamanio(p1)))
print('Cantidad de consonantes: ' + str(tamanio(p2)))
print('Cantidad de signos o numeros: ' + str(tamanio(p3)))

# Parte B
c_espacios = 0
while not pila_vacia(p3):
    aux = desapilar(p3)
    if aux == ' ':
        c_espacios += 1
print('Cantidad de espacios: ' + str(c_espacios))

# Parte C
c_total = (tamanio(p1) + tamanio(p2) + tamanio(p3))
por_voc = (tamanio(p1) * 100) / c_total
por_con = (tamanio(p2) * 100) / c_total
print('Porcentaje de vocales: ' + str(por_voc))
print('Porcentaje de consonantes: ' + str(por_con))


# Parte D
c_numeros = 0
while not pila_vacia(p3):
    aux = desapilar(p3)
    if aux == num:
        c_numeros += 1
print('Cantidad de numeros: ' + str(c_numeros))


# Parte E
if tamanio(p1) == tamanio(p3):
    print('Tienen cantidades iguales')
else:
    print('No tienen cantidades iguales')


# Parte F
while not pila_vacia(p2):
    dat = desapilar(p3)
    if dat == 'z' or dat == 'Z':
        print('Existe al menos una z en el parrafo')
    else:
        print('No existe una z en el parrafo')'''


# Ej15
'''objetos = ['monitor', 'teclado', 'silla', 'lampara', 'pisapapeles', 'basurero',
           'cinta adhesiva', 'carpetas', 'grapadora']
while not pila_llena(p):
    peso = random.randint(1, 13)
    objeto = random.choice(objetos)
    apilar(p, [peso, objeto])

print('Pila desordenada:')
barrido(p)
p = ordenPilaCrec(p)
print('Pila ordenada:')
barrido(p)'''


# Ej16
'''def dirToNum(direccion):
    num = 0
    if (direccion == "norte"):
        num = 8
    elif (direccion == "sur"):
        num = 2
    elif (direccion == "oeste"):
        num = 4
    elif (direccion == "este"):
        num = 6
    elif (direccion == "noreste"):
        num = 9
    elif (direccion == "noroeste"):
        num = 7
    elif (direccion == "sureste"):
        num = 3
    elif (direccion == "suroeste"):
        num = 1
    return num


def NumToDir(numero):
    dir = ""
    if (numero == 1):
        dir = "suroeste"
    elif (numero == 2):
        dir = "sur"
    elif (numero == 3):
        dir = "sureste"
    elif (numero == 4):
        dir = "oeste"
    elif (numero == 6):
        dir = "este"
    elif (numero == 7):
        dir = "noroeste"
    elif (numero == 8):
        dir = "norte"
    elif (numero == 9):
        dir = "noreste"
    return dir


movimientos = ['norte', 'sur', 'este', 'oeste', 'noreste', 'sureste',
               'noroeste', 'suroeste']
lista_movs = []
lista_movs_rev = []

while not pila_llena(p):
    mov = random.choice(movimientos)
    lista_movs.append(mov)
    apilar(p, dirToNum(mov))

while not pila_vacia(p):
    num = 10 - desapilar(p)
    lista_movs_rev.append(NumToDir(num))

print("Movimientos realizados por el robot: ")
print(lista_movs)

print("Movimientos inversos, para volver a punto de partida: ")
print(lista_movs_rev)'''


# Ej17
'''print(fibonacciPila(1))'''
    

# Ej18
'''TMedia = 0
cmen = 0
cmay = 0
cargaAutoInt(p)
tmayor = cima(p)
tmenor = cima(p)
while not pila_vacia(p):
    dato = desapilar(p)
    TMedia += dato
    if dato < tmenor:
        tmenor = dato
    if dato > tmayor:
        tmayor = dato
    apilar(p1, dato)
print('Temperatura menor: ' + str(tmenor))
print('Temperatura mayor: ' + str(tmayor))
TMedia = round(TMedia / tamanio(p1))
print('Temperatura media: ' + str(TMedia))

while not pila_vacia(p1):
    dato = desapilar(p1)
    if dato >= TMedia:
        cmay += 1
    else:
        cmen += 1
    apilar(p, dato)
print('Cantidad de temperaturas mayores a la media: ' + str(cmay))
print('Cantidad de temperaturas menores a la media: ' + str(cmen))'''


# Ej19
'''cargaAutoStr(p)
while not pila_vacia(p):
    dato = desapilar(p)
    if len(dato) > 7:
        print(dato)
    apilar(p1, dato)
p = invertir(p1)
'''


# Ej20
'''cargaAutoInt(p)
barrido(p)
while not pila_vacia(p):
    dato = desapilar(p)
    if (dato % 2 == 0) or (dato % 3 == 0) or (dato % 5 == 0):
        apilar(p1, dato)
p1 = invertir(p1)
print('Pila con multiplos')
barrido(p1)'''