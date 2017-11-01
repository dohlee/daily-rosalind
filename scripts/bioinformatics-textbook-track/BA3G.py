##################################################
# Find an Eulerian Path in a Graph
#
# http://rosalind.info/problems/BA3G/
# 
# Given: A directed graph that contains an Eulerian
#  path, where the graph is given in the form of
#  an adjacency list.
# 
# Return: An Eulerian path in this graph.
#
# AUTHOR : dohlee
##################################################

# Your imports here
from BA3F import parse_adjacency_list, find_eulerian_cycle
from collections import Counter

# Your codes here
def add_imaginary_edge(graph):
    """Add imaginary edge (start, end), where start is the node
    with surplus incoming edges, and end is the node with surplus
    outgoing edges.
    """
    outgoingEdgeCounts, incomingEdgeCounts = Counter(), Counter()
    for u in graph:
        outgoingEdgeCounts[u] += len(graph[u])
        for v in graph[u]:
            incomingEdgeCounts[v] += 1 

    start = list((incomingEdgeCounts - outgoingEdgeCounts).keys())[0]
    end = list((outgoingEdgeCounts - incomingEdgeCounts).keys())[0]

    # Add imaginary edge.
    graph[start].append(end)
    return start, end

def find_eulerian_path(graph):
    """Return an eulerian path of the graph."""
    start, end = add_imaginary_edge(graph)
    cycle = find_eulerian_cycle(graph, start=end)[:-1]
    for i in range(len(cycle)):
        if cycle[i] == start and cycle[(i+1) % len(cycle)] == end:
            path = cycle[i+1:] + cycle[:i+1]

    return path

if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_BA3G.txt') as inFile:
        graph = parse_adjacency_list(inFile)

    # Print output
    with open('../../answers/rosalind_BA3G_out.txt', 'w') as outFile:
        print('->'.join(map(str, find_eulerian_path(graph))), file=outFile)
