import sys
import queue

class Graph:
 
    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = []
        # to store graph
 
    # function to add an edge to graph
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])
 
    # A utility function to find set of an element i
    # (truly uses path compression technique)
    def find(self, parent, i):
        if parent[i] != i:
          # Reassignment of node's parent to root node as
          # path compression requires
            parent[i] = self.find(parent, parent[i])
        return parent[i]
 
    # A function that does union of two sets of x and y
    # (uses union by rank)
    def union(self, parent, rank, x, y):
        
        # Attach smaller rank tree under root of
        # high rank tree (Union by Rank)
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x
 
        # If ranks are same, then make one as root
        # and increment its rank by one
        else:
            parent[y] = x
            rank[x] += 1
 
    # The main function to construct MST using Kruskal's
        # algorithm
    def KruskalMST(self):
 
        result = []  # This will store the resultant MST
 
        # An index variable, used for sorted edges
        i = 0
 
        # An index variable, used for result[]
        e = 0
 
        # Step 1:  Sort all the edges in
        # non-decreasing order of their
        # weight.  If we are not allowed to change the
        # given graph, we can create a copy of graph
        # self.graph = sorted(self.graph,
        #                     key=lambda item: item[2])
 
        parent = []
        rank = []
 
        # Create V subsets with single elements
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
 
        # Number of edges to be taken is equal to V-1
        while e < self.V - 1:
 
            # Step 2: Pick the smallest edge and increment
            # the index for next iteration
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
 
            # If including this edge doesn't
            # cause cycle, then include it in result
            # and increment the index of result
            # for next edge
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
            # Else discard the edge
 
        minimumCost = 0
        # print("Edges in the constructed MST")
        for u, v, weight in result:
            minimumCost += weight
        #     print("%d -- %d == %d" % (u, v, weight))
        # print("Minimum Spanning Tree", minimumCost)
        #print(minimumCost)
        return minimumCost

def sortKey(item):
    return (item[2], item[3])

def sortList(arr):
    arr.sort(key=lambda x: sortKey(x))
    return arr

def main(input):
    vertexNames = []
    edges = []
    
    for line in input[1:]:
        line = line.strip()
        if line == "":
            continue
        else:
            line = line.split()
            if not line[0] in vertexNames:
                vertexNames.append(line[0])
            if not line[1] in vertexNames:
                vertexNames.append(line[1])

    vertexNames.sort()
    g = Graph(len(vertexNames))
    adjacentMatrix = [[] for x in range( len(vertexNames))]
    adjacentEdgeSums = [0] * len(vertexNames)
    for line in input[1:]:
        line = line.strip()
        if line == "":
            continue
        else:
            line = line.split()

            if line[0] < line[1]:
                edge = [vertexNames.index(line[0]), vertexNames.index(line[1]), int(line[2]) , int(line[3]) ]
            else:
                edge = [vertexNames.index(line[1]), vertexNames.index(line[0]), int(line[2]) , int(line[3]) ]
            edges.append(edge)
            adjacentMatrix[vertexNames.index(line[0])].append(vertexNames.index(line[1]))
            adjacentMatrix[vertexNames.index(line[1])].append(vertexNames.index(line[0]))
            if int(line[3]) == 1:
                adjacentEdgeSums[vertexNames.index(line[0])] += int(line[2])
                adjacentEdgeSums[vertexNames.index(line[1])] += int(line[2])

    
    
    upgrade = adjacentEdgeSums.index(max(adjacentEdgeSums))

    prunedList = []
    for e in edges:
        if (e[0] not in adjacentMatrix[upgrade] and e[1] not in adjacentMatrix[upgrade]) or e[0] == upgrade or e[1] == upgrade:
            prunedList.append(e)            
    prunedList = sortList(prunedList)
    for edge in prunedList:
            g.addEdge(edge[0], edge[1], edge[2])
            print(vertexNames[edge[0]], vertexNames[edge[1]], edge[2])     

    result = g.KruskalMST()
    print(result + 10000)

    

input = ['11', 'alpha beta 3000 0', 'alpha gamma 2000 0', 'gamma epsilon 7000 0', 'beta delta 5000 1', 'delta epsilon 8000 1', 'beta epsilon 5000 1', 'epsilon zeta 9000 1', 'zeta delta 4000 1', 'zeta eta 5000 0', 'zeta theta 8000 1', 'eta theta 6500 1']

if __name__ == '__main__':
    #input = []
    #for line in sys.stdin:
    #    input.append(line.strip(" \r\n"))
    main(input)
