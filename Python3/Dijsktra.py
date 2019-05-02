import math
import random as rn
import networkx

g = networkx.Graph()
# import sys
# grafo = [[0, 1, 4, 0, 0, 0, 0, 0],
#         [1, 0, 0, 0, 0, 2, 0, 0],
#         [4, 0, 0, 5, 0, 0, 0, 0],
#         [0, 0, 5, 0, 1, 3, 0, 0],
#         [0, 0, 0, 1, 0, 0, 2, 3],
#         [0, 2, 0, 3, 0, 0, 0, 0],
#         [0, 0, 0, 0, 2, 0, 0, 4],
#         [0, 0, 0, 0, 3, 0, 4, 0]]
print("inserire grandezza matrice")
dimGrafo = int(input())
print("inserire percentuale zeri")
percentualeZeri = (100 - int(input())) / 100
# percentualeZeri = int((dimGrafo*int(input()))/100)
# print(percentualeZeri)
grafo = []
for c in range(dimGrafo):
    grafo.append([math.inf] * dimGrafo)
    g.add_node(c)
for r in range(dimGrafo):
    for c in range(dimGrafo):
        if r == c:
            grafo[r][c] = 0
        elif r < c:
            numeroRandom = rn.randrange(11)
            grafo[r][c] = numeroRandom
            grafo[c][r] = numeroRandom
            g.add_weighted_edges_from([r, c], numeroRandom)
            g.add_weighted_edges_from([c, r], numeroRandom)
        elif rn.random() < percentualeZeri:
            grafo[r][c] = 0
            grafo[c][r] = 0
for stamp in range(dimGrafo):
    print(grafo[stamp])

labelList = [math.inf] * len(grafo)  # inizializzazione
labelList[0] = 0  # distanza da nodo sorgente uguale a 0
nodiDaEsplorare = list(range(dimGrafo))
cntPasso = 0
while len(nodiDaEsplorare) > 0:
    # stampo il numero del passo e la labelList (lista con i pesi del percorso per raggiungere quel nodo)
    print("Passo numero: %d", cntPasso)
    print("Nodiinesplorati: ", nodiDaEsplorare)
    print("Lista delle label: ", labelList)
    print("-----------------------------------------------------------------------")
    # trovo il nodo con la label più piccola in labelList e rimuovo il nodo da nodiDaEsplorare.
    lblMinore = math.inf
    nodoMinore = math.inf
    for indice, contenuto in enumerate(labelList):
        if indice in nodiDaEsplorare:
            if lblMinore > contenuto:
                lblMinore = contenuto
                nodoMinore = indice
    print(nodoMinore)
    if nodoMinore != math.inf:
        nodiDaEsplorare.remove(nodoMinore)
        # inserisco nella labelList i nodi collegati al nodo estratto
        for indice, contenuto in enumerate(grafo[nodoMinore]):
            if contenuto > 0:
                if indice in nodiDaEsplorare:
                    if labelList[indice] > contenuto + lblMinore:
                        labelList[indice] = contenuto + lblMinore
        cntPasso = cntPasso + 1
    else:
        nodiDaEsplorare = []

networkx.draw(g)