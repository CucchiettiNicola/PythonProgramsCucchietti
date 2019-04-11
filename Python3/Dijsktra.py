import math

grafo = [[0, 1, 4, 0, 0, 0, 0, 0],
         [1, 0, 0, 0, 0, 2, 0, 1],
         [4, 0, 0, 5, 0, 0, 0, 0],
         [0, 0, 5, 0, 1, 3, 0, 0],
         [0, 0, 0, 1, 0, 0, 2, 3],
         [0, 2, 0, 3, 0, 0, 0, 0],
         [0, 0, 0, 0, 2, 0, 0, 4],
         [0, 1, 0, 0, 3, 0, 4, 0]]

labelList = [math.inf] * len(grafo)  # inizializzazione
labelList[0] = 0  # distanza da nodo sorgente uguale a 0

nodiDaEsplorare = [0, 1, 2, 3, 4, 5, 6, 7]
while len(nodiDaEsplorare) > 0:
    # stampo la labelList (lista con i pesi del percorso per raggiungere quel nodo)
    print(labelList)
    # trovo il nodo con la label più piccola in labelList e rimuovo il nodo da nodiDaEsplorare.
    nodoMinore = math.inf
    for indice,contenuto in enumerate(labelList):
        if indice in nodiDaEsplorare:
            if nodoMinore > contenuto:
                lblMinore = contenuto
                nodoMinore = indice
    nodiDaEsplorare.remove(nodoMinore)
    # inserisco nella labelList i nodi collegati al nodo estratto
    for indice,contenuto in enumerate(grafo[nodoMinore]):
        if contenuto > 0:
            if indice in nodiDaEsplorare:
                if labelList[indice] > contenuto + lblMinore:
                    labelList[indice] = contenuto + lblMinore
