import C,P

def Invertir (cola):
    pila = P.Pila()
    P.crearpila(pila)
    while (not C.colavacia(cola)) or (not P.pilallena(pila)):
        y = C.supresion(cola)
        P.apilar(pila,y)
    while (not P.pilavacia(pila)) or (not C.colallena(cola)):
        z = P.desapilar(pila)
        C.insertarcola(cola,z)


cola = C.Cola()
C.crearcola(cola)
C.cargar_random(cola)
print("Cola Original")
print(cola.datos)
Invertir(cola)
print("Cola Invertida")
print(cola.datos)
