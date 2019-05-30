import C

def mostrar_contenido(cola):
    for i in range(1,11):
        x = C.supresion(cola)
        print (x)

cola = C.Cola()
C.crearcola(cola)
C.cargar_random(cola)
print (cola.datos)
mostrar_contenido(cola)