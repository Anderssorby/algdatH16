from sys import stdin
from operator import attrgetter

Inf = float(1e3000)

class Edge:
    #edge to put in set of edges
    def __init__(self, U, V, W):
        self.u = U
        self.v = V
        self.w = W

class Node:
    #Node for all the vertices in graph
    def __init__ (self, label):
        self.label = label
    def __str__(self):
        return self.label


def mst(nNodes, V, E):
    # Finds heaviest edge in minimal span tree
    # given nNodes number of nodes,
    # V set of vertices
    # E set of Edge-object sets


    #Find MST
    T = []
    for e in E:
        if find(e.u) is not find(e.v):
            T.append(e)
            union(e.u, e.v)

    #Find largest weight in MST = weight of last element of T
    return T[-1].w

"""
MakeSet(x) initializes disjoint set for object x
Find(x) returns representative object of the set containing x
Union(x,y) makes two sets containing x and y respectively into one set

Some Applications:
- Kruskal's algorithm for finding minimal spanning trees
- Finding connected components in graphs
- Finding connected components in images (binary)
"""

def makeSet(x):
     x.parent = x
     x.rank   = 0

def union(x, y):
     xRoot = find(x)
     yRoot = find(y)
     if xRoot.rank > yRoot.rank:
         yRoot.parent = xRoot
     elif xRoot.rank < yRoot.rank:
         xRoot.parent = yRoot
     elif xRoot != yRoot: # Unless x and y are already in same set, merge them
         yRoot.parent = xRoot
         xRoot.rank = xRoot.rank + 1

def find(x):
     if x.parent == x:
        return x
     else:
        x.parent = find(x.parent)
        return x.parent



lines = []
for str in stdin:
    lines.append(str)
n = len(lines)
nodes = set([i for i in range(n+1)])
node = 0
V = [Node(i) for i in range(n+1)]
[makeSet(node) for node in V]
E = []
for line in lines:
    for k in line.split():
        data = k.split(':')
        neighbour = int(data[0])
        weight = int(data[1])
        E.append(Edge(V[node], V[neighbour], weight))
    node += 1
E.sort(key = attrgetter('w'))
#E.sort(key=lambda x: x.w)
#E = E[1::2]

print (mst(node, V, E))