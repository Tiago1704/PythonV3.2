class nodo:
    izq , der, dato = None, None, 0

 

def __init__(self, dato):
    self.izq = None
    self.der = None
    self.dato = dato

 

class arbolBinario:
    def __init__(self):
        self.raiz = None

 
def agregarNodo(self, dato):
    return nodo(dato)

 

def insertar(self, raiz, dato):
    if raiz == None:
        return self.agregarNodo(dato)
    else:
        if dato <= raiz.dato:
            raiz.izq = self.insertar(raiz.izq, dato)
        else:
                raiz.der = self.insertar(raiz.der, dato)
                return raiz