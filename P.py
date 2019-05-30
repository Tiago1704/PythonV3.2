
Max = 10
import random

class Pila():
    def __init__(self):
        self.Tope, self.Datos = -1,[]

def crearpila(P):
    P.Tope = -1
    for I in range (0,Max):
        P.Datos.append(None)

def apilar(P,x):
    P.Tope = P.Tope + 1
    P.Datos[P.Tope]=x
  
def desapilar(P):
    x = P.Datos[P.Tope]
    P.Tope = P.Tope - 1
    return (x)

def pilallena(P):
    return  (P.Tope == Max-1)
    
def pilavacia(P):
    return  (P.Tope == -1)
        
def tamanopila(P): 
    return (P.Tope+1)

def cargar_random(P):
    while (not pilallena(P)):
        apilar(P,(random.randrange(0,10)))
