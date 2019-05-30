import P,C

def cargar_palabra(pila):
    for i in palabra:
        
       P.apilar(pila,i)

def insertar_palabra (cola):
    for i in palabra:
        C.insertarcola(cola,i)
        
def invertir_orden(pila):
    paux = P.Pila()
    P.crearpila(paux)
    while (not P.pilavacia(pila)):
        x = P.desapilar(pila)
        P.apilar(paux,x)
    return paux

palabra = input("Ingrese palabra : ")
palabra = palabra.lower()
pila = P.Pila()
P.crearpila(pila)
cola = C.Cola()
C.crearcola(cola)
cargar_palabra(pila)
insertar_palabra(cola)
paux = invertir_orden(pila)
if (paux.Datos == cola.datos):
    print ("Es palíndromo")
else:
    print ("No es palíndromo")
