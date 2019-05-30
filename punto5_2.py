import C
def puntos(palabra):
    contador = 0    
    for i in palabra:
        if(i == ':'):
            contador = contador +1
    if (contador>0):
        return True
    else:
        return False

def carga_cola(c1,c2,palabra):
    i = 1
        
    if palabra[0] != ':':
        C.insertarcola(c1,palabra[0])    
        while(palabra[i]!= ":" and i<len(palabra)-1):
            C.insertarcola(c1,palabra[i])
            i = i+1
        i = i+1

        while(i<len(palabra)):
            C.insertarcola(c2,palabra[i])
            i = i+1    
    else:
        i = 1        
        while(i<len(palabra)):
            C.insertarcola(c2,palabra[i])
            i = i+1

def tam_iguales(c1,c2):
    if C.tamcola(c1) == C.tamcola(c2):
        return True
    else:
        return False

def mayor(c1,c2):
        
    may = C.tamcola(c1)
    if C.tamcola(c2) > may:
        print("Segundoa palabra es mas grande que la primera")
    else:
        print("La primera palabra es mas grande que la segunda")
    
def identicas(c1,c2):
    con_igual = 0    
    tam_ini = C.tamcola(c1)
    while(not C.colavacia(c1)):
        x = C.supresion(c1)
        y = C.supresion(c2)
        if (x == y):
            con_igual = con_igual + 1
    if con_igual == tam_ini:
        return True
    else:
        return False
        
c1 = C.Cola()
C.crearcola(c1)

c2 = C.Cola()
C.crearcola(c2)



palabra = input("INGRESE 2 PALABRAS SEPARADAS POR "":"" PUNTOS")
if puntos(palabra):
    carga_cola(c1,c2,palabra)
    if tam_iguales(c1,c2):
        if identicas(c1,c2):
            print("Las palabras son identicas. Tienen los mismos caracteres")
        else:
            print("Las palabras tienen el mismos tamaño, pero diferentes caracteres")
    else:
        mayor(c1,c2)

else:
    print("La palabra no tiene 2 puntos.")

    
