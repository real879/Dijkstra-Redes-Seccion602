# Dijkstra-Redes-Seccion602
 Trabajo para el curso de Redes- seccion 602
 
 Implementacion del algoritmo de Dijkstra en python.
 
 Se utilizaron 3 grafos diferentes para la experimentacion

Para poder utilizarlo primer se debe de ingresar la informacion del grafo en un diccionario
de forma que:

grafo={

    'nodo':{'nodo_a':distancia_hacia_a,'nodo_b':distancia_hacia_b} 

}
 
 donde "nodo_a" y "nodo_b" son los nodos a los cuales "nodo" esta conectado
 
 Finalmente llamar a la funcion "Dijkstra" de la forma:
 
 Dijkstra(grafo , nodo_inicial, nodo_final) 
 
 donde "grafo" es el grafo donde se buscara el recorrido,
 "nodo_inicial" es el nodo donde se inicia el recorrido y
 "nodo_final" es el nodo de destino.
 
