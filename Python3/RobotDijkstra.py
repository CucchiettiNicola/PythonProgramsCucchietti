import networkx as nx
import matplotlib.pyplot as plt
import math

WEIGHT_EDGE = 1

def floorMatrixCreator(dim, objectCoord_list):
    floor_mat = [[None for col in range(0,dim)] for row in range(0,dim)]

    for row,col in objectCoord_list:
        floor_mat[row][col] = "X"

    freeTileCounter = 0

    for row in range(0,dim):
        for col in range(0,dim):
            if floor_mat[row][col] != "X":
                floor_mat[row][col] = freeTileCounter
                freeTileCounter += 1
    
    return floor_mat

def adjDictCreator(floor_mat):
    adj_dict = {}

    for row in range(0,len(floor_mat)):
        for col in range(0, len(floor_mat[row])):
            if not floor_mat[row][col] == "X":
                adj_dict[floor_mat[row][col]] = neighborsListCreator(floor_mat, row, col)

    return adj_dict

def neighborsListCreator(floor_mat, row, col):
    neighbors_list = []
    dim = len(floor_mat)

    if row>0:
        if floor_mat[row-1][col]!="X":
            neighbors_list.append(floor_mat[row-1][col])

    if col>0:
        if floor_mat[row][col-1]!="X":
            neighbors_list.append(floor_mat[row][col-1])

    if col<dim-1:
        if floor_mat[row][col+1]!="X":
            neighbors_list.append(floor_mat[row][col+1])

    if row<dim-1:
        if floor_mat[row+1][col]!="X":
            neighbors_list.append(floor_mat[row+1][col])

    return neighbors_list

def convertToAdjMatrix(adj_dict):
    dim = len(adj_dict)
    adj_mat = [[0 for col in range(0,dim)] for row in range(0,dim)]

    for key, neighbors_list in adj_dict.items():
        for node in neighbors_list:
            adj_mat[key][node] = WEIGHT_EDGE

    return adj_mat

def indexMin(label_list, notVisited_list):
    infinite_list = [math.inf]*len(label_list)
    for i in notVisited_list:
        infinite_list[i] = label_list[i]

    minimum = min(infinite_list)
    
    if not minimum==math.inf:
        return infinite_list.index(minimum)
    
    return -1

def dijkstra(currentNode, previous_weight, graph, **other):
    if previous_weight == 0:
        label_list = [math.inf]*len(graph)
        notVisited_list = [a for a in range(0,len(graph))]
    else:
        label_list = other.get("label_list")
        notVisited_list = other.get("notVisited_list")

    label_list[currentNode] = previous_weight
    notVisited_list.remove(currentNode)

    if len(notVisited_list)==0:
        return label_list
    
    for node, weight in enumerate(graph[currentNode]):
        if weight!=0:
            if (node+weight)<label_list[node]:
                label_list[node] = previous_weight + weight

    indexNextNode = indexMin(label_list, notVisited_list)

    if not indexNextNode==-1:
        return dijkstra(indexNextNode, label_list[indexNextNode], graph, label_list=label_list, notVisited_list=notVisited_list)
    
    return label_list

floor_dim = 4

obs_list = [(0,0),(0,1),(0,2),(0,3),(1,0),(1,3),(2,1),(3,3)]
floor_mat = floorMatrixCreator(floor_dim, obs_list)

for tile_list in floor_mat:
    print(" ")
    for tile in tile_list:
        print("%3s" %tile, end=" ")

print("\n")

adj_dict = adjDictCreator(floor_mat)
print("\nAdjacency dictionary: " + str(adj_dict))
adj_mat = convertToAdjMatrix(adj_dict)

graph = nx.convert.from_dict_of_lists(adj_dict)

start_tile = int(input("\n> Start tile: "))
target_tile = int(input("\n> Target tile: "))

dist_list = dijkstra(start_tile, 0, adj_mat)

print("\n> Shortest paths from %d to others tile: " %start_tile, dist_list)
print("\n> Shortest path from %d to %d: %d" %(start_tile, target_tile, dist_list[target_tile]))

pos_dict = {}

for row,tile_list in enumerate(floor_mat):
    for col,tile in enumerate(tile_list):
        if tile != "X":
            pos_dict[tile] = (col, floor_dim-row)

_, path_list = nx.algorithms.shortest_paths.weighted.single_source_dijkstra(graph, start_tile, target_tile)

nx.draw(graph, pos=pos_dict, with_labels=True)
nx.draw(graph, pos=pos_dict, nodelist=path_list, node_color="yellow", with_labels=True)
nx.draw_networkx_nodes(graph, pos=pos_dict, nodelist=[start_tile], node_color="green", node_shape="D")
nx.draw_networkx_nodes(graph, pos=pos_dict, nodelist=[target_tile], node_color="red", node_shape="D")
plt.show()
