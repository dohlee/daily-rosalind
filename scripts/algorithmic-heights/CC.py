##################################################
# Connected Components
#
# http://rosalind.info/problems/CC/
# 
# Given: A simple graph with n <= 10^3 vertices
#  in the edge list format.
# 
# Return: The number of connected components in
#  the graph.
#
# AUTHOR : dohlee
##################################################

# Your imports here
from queue import Queue
from collections import defaultdict

# Your codes here
def bfs(graph, root, visited):
    q = Queue()
    q.put(root)
    visited[root] = True

    while not q.empty():
        curr = q.get()
        for v in graph[curr]:
            if not visited[v]:
                q.put(v)

            visited[v] = True

def count_connected_components(graph, vertexCount):
    """Return the number of connected components of the graph.
    Use BFS.
    """
    visited = [False] * vertexCount

    connectedComponentCount = 0
    while not all(visited):
        connectedComponentCount += 1

        # find unvisited node.
        for root in range(vertexCount):
            if not visited[root]:
                break

        # mark nodes as visited while doing BFS.
        bfs(graph, root, visited)

    return connectedComponentCount

if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_CC.txt') as inFile:
        graph = defaultdict(list)
        vertexCount, edgeCount = map(int, inFile.readline().split())
        for line in inFile.readlines():
            u, v = map(int, line.split())
            graph[u-1].append(v-1)
            graph[v-1].append(u-1)

    # Print output
    with open('../../answers/rosalind_CC_out.txt', 'w') as outFile:
        print(count_connected_components(graph, vertexCount), file=outFile)

