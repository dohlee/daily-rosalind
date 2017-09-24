##################################################
# Double-Degree Array
#
# http://rosalind.info/problems/DDEG/
# 
# Given: A simple graph with n <= 10^3 vertices
#  in the edge list format.
# 
# Return: An array D[1..n] where D[i] is the sum
#  of the degrees of i's neighbors.
#
# AUTHOR : dohlee
##################################################

# Your imports here
from collections import defaultdict

# Your codes here
def add_edge(graph, u, v):
    """Add edge (u, v) to the graph."""
    graph[u].append(v)
    graph[v].append(u)

def double_degree(graph, u):
    """Return the sum of the degrees of u's neighbors"""
    return sum(len(graph[neighbor]) for neighbor in graph[u])

if __name__ == '__main__':
    # Load the data.
    graph = defaultdict(list)
    with open('../../datasets/rosalind_DDEG.txt') as inFile:
        vertexCount, edgeCount = map(int, inFile.readline().split())
        for line in inFile.readlines():
            u, v = map(int, line.split())
            add_edge(graph, u, v)

    # Print output
    with open('../../answers/rosalind_DDEG_out.txt', 'w') as outFile:
        print(' '.join(map(str, [double_degree(graph, u) for u in range(1, vertexCount+1)])), file=outFile)

