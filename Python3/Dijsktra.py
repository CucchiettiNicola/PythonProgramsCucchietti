import math

grafo = [[0, 1, 4, 0, 0, 0, 0, 0],
         [1, 0, 0, 0, 0, 2, 0, 0],
         [4, 0, 0, 5, 0, 0, 0, 0],
         [0, 0, 5, 0, 1, 3, 0, 0],
         [0, 0, 0, 1, 0, 0, 2, 3],
         [0, 2, 0, 3, 0, 0, 0, 0],
         [0, 0, 0, 0, 2, 0, 0, 4],
         [0, 0, 0, 0, 3, 0, 4, 0]]

labelList = [math.inf] * len(grafo)  # inizializzazione
labelList[0] = 0  # distanza da nodo sorgente uguale a 0
contatore = 0

nodiDaEsplorare = [0, 1, 2, 3, 4, 5, 6, 7]
while len(nodiDaEsplorare) > 0:
    print(labelList)
    # Scelgo il nodo che ha la label più piccola (k).
    nodoMinore = math.inf
    for k in labelList:
        if labelList.index(k) in nodiDaEsplorare:
            if nodoMinore > k:
                lblMinore = k
                nodoMinore = labelList.index(k)
    nodiDaEsplorare.remove(nodoMinore)
    # Ricerco i nodi collegati al nodo k -> ciclo for sulla riga k di grafo
    for k in grafo[nodoMinore]:
        if k > 0:
            if grafo[nodoMinore].index(k) in nodiDaEsplorare:
                if labelList[grafo[nodoMinore].index(k)] > k + lblMinore:
                    labelList[grafo[nodoMinore].index(k)] = k + lblMinore
