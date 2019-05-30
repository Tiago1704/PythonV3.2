# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 04:55:02 2018

@author: Tiago Ibacache

La lista es una estructura que almacena elementos (Generalmente nodos) los nodos pueden almacenar datos variados.
Son estructuras dinamicas (pueden guardar varios tipos de datos y se puede expandir y contraer para almacenar mas o menos información).
Los nodos poseen dos campos: informacion y enlace.

    estaVacia(): devuelve verdadero si la lista esta vacía, falso en caso contrario.
    insertar(x, k): inserta el elemento x en la k-ésima posición de la lista.
    buscar(x): devuelve la posición en la lista del elemento x.
    buscarK(k): devuelve el k-ésimo elemento de la lista.
    eliminar(x): elimina de la lista el elemento x. 
"""
class Lista:
    def __init__(self):
        self.nodo = None
        self.cabecera = None 
        
    def CrearLista (l):
        l.nodo = 0
        l.cabecera = 0
        
    def Estavacia ():
        if l.cabecera.siguiente == None:
            return True;
        else:
            return False; 
    
    def insertar (self = o, o, iter = i):
        if (i != None and it.act != None):
            i.act.sig = nodo(o,i.act.sig)
    
    def eliminar (self = 0):
        if i.act.sig != None:
            i.act.sig = i.act.sig.sig
            
    
    
            
        
        
        
    

