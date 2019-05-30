import random
Max = 10

class ColaNodo():
    def __init__(self):
        self.final = None
        self.datos = []
        self.frente = None
        self.tam = None
  
def crearcola(q):
    q.frente= 0
    q.final= -1
    q.tam = 0
    for I in range (0,Max):
        q.datos.append(None)

def insertarcola(q,x):
    if q.final == Max-1:
        q.final = 0
    else:
        q.final= q.final + 1
    q.datos[q.final]= x
    q.tam= q.tam + 1

def supresion (q):
    x= q.datos[q.frente]
    if q.frente == Max-1:
        q.frente = 0
    else:
        q.frente = q.frente + 1
    q.tam=  q.tam - 1
    return x

def colavacia(q):
    return(q.tam == 0)
    
def colallena(q):
    return(q.tam == Max )

def tamcola(q):
    return(q.tam)

def moveralfinal (q):
    if (not colavacia(q)):
        x = supresion(q)
        insertarcola(q,x)
        
def cargar_random(q):
    while (not colallena(q)):
        insertarcola(q,(random.randrange(0,10)))

