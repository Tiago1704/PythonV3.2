import P,C

def moverPaC ():
    pila = P.Pila()
    P.crearpila(pila)
    P.cargar_random(pila)
    print ("Pila: ",pila.Datos)
    cola = C.Cola()
    C.crearcola(cola)
    paux = P.Pila()    
    P.crearpila(paux)
    while (not P.pilavacia(pila)):
        x = P.desapilar(pila)
        P.apilar(paux,x)
    if (not P.pilavacia(paux)):
        while (not P.pilavacia(paux)) or (not C.colallena(cola)):
            x = P.desapilar(paux)
            C.insertarcola(cola,x)
        print("Cola: ",cola.datos)
    else:
        print ("La pila está vacía")

def moverCaP ():
    cola = C.Cola()
    C.crearcola(cola)
    C.cargar_random(cola)
    print("Cola: ",cola.datos)
    pila = P.Pila()
    P.crearpila(pila)
    if (not C.colavacia(cola)):
        while (not C.colavacia(cola)) or (not P.pilallena(pila)):    
            x = C.supresion(cola)
            P.apilar(pila,x)
        print ("Pila: ",pila.Datos)
    else:
        print ("La cola está vacía")

def PaP1():
    pila1 = P.Pila()
    P.crearpila(pila1)
    P.cargar_random(pila1)
    print ("Contenido de pila 1: ",pila1.Datos)
    paux = P.Pila()
    P.crearpila(paux)
    pila2 = P.Pila()
    P.crearpila(pila2)
    while (not P.pilavacia(pila1)):
        x = P.desapilar(pila1)
        P.apilar(paux,x)
    while (not P.pilavacia(paux)):
        x = P.desapilar(paux)
        P.apilar(pila2,x)
    print ("Contenido de pila 2: ",pila2.Datos)    

def PaP2():
    pila1 = P.Pila()
    P.crearpila(pila1)
    P.cargar_random(pila1)
    print ("Contenido de pila 1: ",pila1.Datos)
    pila2 = P.Pila()
    P.crearpila(pila2)
    while (not P.pilavacia(pila1)):
        x = P.desapilar(pila1)
        P.apilar(pila2,x)
    print ("Contenido de pila 2: ",pila2.Datos)

def InvertirCporP ():
    cola = C.Cola()
    C.crearcola(cola) 
    pila = P.Pila()
    P.crearpila(pila)
    C.cargar_random(cola)
    print ("Cola original: ",cola.datos)    
    while (not C.colavacia(cola)) or (not P.pilallena(pila)):
        y = C.supresion(cola)
        P.apilar(pila,y)
    while (not P.pilavacia(pila)) or (not C.colallena(cola)):
        z = P.desapilar(pila)
        C.insertarcola(cola,z)
    print("Cola invertida por pila: ",cola.datos)

def InvertirPporC ():
    cola = C.Cola()
    C.crearcola(cola) 
    pila = P.Pila()
    P.crearpila(pila)
    P.cargar_random(pila)
    print ("Pila original: ",pila.Datos)    
    while (not P.pilavacia(pila)) or (not C.colallena(cola)):
        z = P.desapilar(pila)
        C.insertarcola(cola,z)
    while (not C.colavacia(cola)) or (not P.pilallena(pila)):
        y = C.supresion(cola)
        P.apilar(pila,y)
    print("Pila invertida por cola: ",cola.datos)
    

print("----------------------------------------------------------")
print ("Moviendo de Pila a Cola")
moverPaC()
print("----------------------------------------------------------")
print ("Moviendo de Cola a Pila")
moverCaP()
print("----------------------------------------------------------")
print ("Moviendo de Pila a Pila manteniendo el orden")
PaP1()
print("----------------------------------------------------------")
print ("Moviendo de Pila a Pila invirtiendo el orden")
PaP2()
print("----------------------------------------------------------")
print ("Pila invirtiendo el orden de cola")
InvertirCporP()
print("----------------------------------------------------------")
print ("Cola invirtiendo el orden de pila")
InvertirPporC ()
print("----------------------------------------------------------")