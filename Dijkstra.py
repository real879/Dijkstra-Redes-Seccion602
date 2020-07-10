#Algoritmo de Dijkstra - Redes - 602

#Primer grafo
grafo1 ={

'a':{'b':5,'c':3},
'b':{'e':1},
'c':{'d':1,'f':3},
'd':{'f':1, 'g':1},
'e':{'d':3, 'g':1},
'f':{},
'g':{}
} 

#Segundo grafo
grafo2={
'a':{'b':2,'c':1},
'b':{'d':1},
'c':{'d':3,'e':4},
'd':{'f':2},
'e':{'f':2},
'f':{},
}

#Tercer grafo
grafo3={
'a':{'b':3,'c':1},
'b':{'a':3,'d':1,'g':5},
'c':{'a':1,'d':2,'f':5},
'd':{'b':1,'c':2,'e':4,'f':2},
'e':{'d':4,'g':2,'h':1},
'f':{'c':5,'d':2,'h':3},
'g':{'b':5,'e':2},
'h':{'f':3,'e':1}
}


def dijkstra(grafo,inicio,destino):
    caminoMasCorto = {} #Se inicializa un diccionario para guardar los caminos mas cortos de cada nodo
    nodoAnterior = {} #Se inicializa un diccionario para guardar el nodo anterior que tuvo el menor camino por cada nodo
    nodosSinVer = grafo #una variable para guardar los nodos que aun no se recorren
    camino = [] #Para guardar el camino recorrido

    #Se recorre el grafo para asignar un valor grande al camino de todos los nodos menos al nodo inicial

    for nodo in nodosSinVer:  
        caminoMasCorto[nodo] = 99999
    caminoMasCorto[inicio] = 0
 
    #Se recorre el grafo mientras exista un nodo sin ser visto
    while nodosSinVer:
        minNodo = None

        #Se encuentra el nodo con menor camino y se le guarda
        for nodo in nodosSinVer:

          #Si es el primer recorrido se asigna el nodo inicial por tener menor recorrido
            if minNodo is None: 
                minNodo = nodo
            elif caminoMasCorto[nodo] < caminoMasCorto[minNodo]:
                minNodo = nodo
        
        #Se obtienen los nodos adyacentes del nodo con menor camino
        for nodoAdyacente, peso in grafo[minNodo].items():

          #Se evalua el peso que cuesta llegar al proximo nodo y si es menor se actualiza el camino mas corto del proximo nodo
            if peso + caminoMasCorto[minNodo] < caminoMasCorto[nodoAdyacente]:
                caminoMasCorto[nodoAdyacente] = peso + caminoMasCorto[minNodo]
                nodoAnterior[nodoAdyacente] = minNodo

        #Se saca de la lista al nodo que ya fue revisado
        nodosSinVer.pop(minNodo)

    #Para obtener el recorrido se debe de empezar del destino hacia el origen
    #Empezamos con el ultimo nodo
    nodoActual = destino
    
    #se recorre el camino hasta que se llegue al nodo inicial
    while nodoActual != inicio:
        camino.insert(0,nodoActual)
        nodoActual = nodoAnterior[nodoActual]
 
    camino.insert(0,inicio)

    #Si se encontro un camino se imprime la distancia y el camino
    if caminoMasCorto[destino] != 99999:
        print('La distancia mas corta entre "'+inicio+'" y "' +destino+ '" es: ' + str(caminoMasCorto[destino]))
        print('El camino es: ' + str(camino))
 

print("Grafo1: ")
dijkstra(grafo1, 'a', 'e') #Se busca el camino mas optimo desde "a" hacia "e" en el grafo1
print()
print("Grafo2: ")
dijkstra(grafo2, 'a', 'b') #Se busca el camino mas optimo desde "a" hacia "e" en el grafo2
print()
print("Grafo3:")
dijkstra(grafo3, 'c', 'h') #Se busca el camino mas optimo desde "a" hacia "e" en el grafo3