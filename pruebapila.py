from tdapila import Pila, apilar, desapilar, pila_llena, pila_vacia, tamanio
from tdapila import cima, barrido
import random

p = Pila()
p1 = Pila()
p2 = Pila()
p3 = Pila()

'''#Ej12

dato = [5]
apilar(p, dato)
dato = [3]
apilar(p, dato)
dato = [7]
apilar(p, dato)
print(p.datos)
aux = desapilar(p)
apilar(p1, aux)
print(p1.datos)
while not pila_vacia(p):
    aux1 = desapilar(p1)'''


#Ej14

dato = ['h']
apilar(p, dato)
dato = ['o']
apilar(p, dato)
dato = ['l']
apilar(p, dato)
dato = ['a']
apilar(p, dato)
dato = ['.']
apilar(p, dato)
print(p.datos)
while not pila_vacia(p):
    aux = desapilar(p)
    '''if (aux == 'a' or aux == 'e' or aux == 'i' or aux == 'o' or aux == 'u' or
    aux == 'A' or aux == 'E' or aux == 'I' or aux == 'O' or aux == 'U'):
        apilar(p1, aux)'''
    if (aux == '.' or aux == ','):
        apilar(p2, aux)
    else:
        apilar(p3, aux)
print(p1.datos)
print(p2.datos)
print(p3.datos)