#!/usr/bin/python3

from sys import stdin


function = stdin.readline()
number_of_nodes = int(stdin.readline())
s = int(stdin.readline())
r = int(stdin.readline())
if function[0] == 'v':
    m = [0] * number_of_nodes
    for line in stdin:
        number = line.split()
        p = int(number.pop(0))
        for n in number:
            m[int(n)] = p
    d = 0
    n = r
    while n != s:
        n = m[n]
        d += 1
    print(d)
    exit()
WHITE = 0
BLACK = 1

class Node:
    def __init__(self):
        self.children = []
        self.ratatosk = False
        self.next_child = 0
        self.color = WHITE
        # self.i = i
        self.d = 0


def dfs(root):
    # SKRIV DIN KODE HER
    stack = [root]
    while stack:
        node = stack.pop()
        # print("visiting", node.i)
        node.color = BLACK
        if node.ratatosk:
            return node.d
        for child in node.children:
            if child.color == WHITE:
                child.ancestor = node
                child.d = node.d + 1
                stack.append(child)



def bfs(root):
    from collections import deque
    # SKRIV DIN KODE HER
    queue = deque([root])
    while queue:
        node = queue.popleft()
        # visiting node
        node.color = BLACK
        if node.ratatosk:
            return node.d
        # Add children to queue
        for child in node.children:
            if child.color == WHITE and child not in queue:
                child.ancestor = node
                child.d = node.d + 1
                queue.append(child)

nodes = []
for i in range(number_of_nodes):
    nodes.append(Node())
start_node = nodes[s]
ratatosk_node = nodes[r]
ratatosk_node.ratatosk = True
for line in stdin:
    number = line.split()
    p = int(number.pop(0))
    temp_node = nodes[p]
    for child_number in number:
        n = nodes[int(child_number)]
        n.p = temp_node
        temp_node.children.append(n)

if function[0] == 'd':
    print(dfs(start_node))
elif function[0] == 'b':
    print(bfs(start_node))

