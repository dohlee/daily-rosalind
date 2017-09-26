##################################################
# Breadth-First Search
#
# http://rosalind.info/problems/BFS/
# 
# Given: A simple directed graph with n <= 10^3
#  vertices in the edge list format.
# 
# Return: An array D[1..n] where D[i] is the length
#  of a shortest path from the vertex 1 to the vertex
#  i (D[1]=0). If i is not reachable from 1 set
#  D[i] to -1.
#
# AUTHOR : dohlee
##################################################

# Your imports here
from queue import Queue
from collections import defaultdict

# Your codes here
def get_depths(graph, n):
    """Return the length of shortest path to each vertex from vertex 0.
    If the vertex is not reachable, -1 is returned.
    """
    depths = [0] + [-1] * (n-1)
    visited = [True] + [False] * (n-1)

    q = Queue()
    # enqueue tuple (vertex, depth)
    for v in graph[0]:
        visited[v] = True
        q.put((v, 1))

    while not q.empty():
        u, depth = q.get()
        depths[u] = depth

        # enqueue tuple (vertex, depth+1)
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                q.put((v, depth+1))

    return depths

if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_BFS.txt') as inFile:
        graph = defaultdict(list)
        vertexCount, edgeCount = map(int, inFile.readline().split())
        for _ in range(edgeCount):
            u, v = map(int, inFile.readline().split())
            graph[u - 1].append(v - 1)


    # Print output
    with open('../../answers/rosalind_BFS_out.txt', 'w') as outFile:
        print(' '.join(map(str, get_depths(graph, vertexCount))), file=outFile)

