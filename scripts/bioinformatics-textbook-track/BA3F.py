##################################################
# Find an Eulerian Cycle in a Graph
#
# http://rosalind.info/problems/BA3F/
# 
# Given: An Eulerian directed graph, in the form
#  of an adjacency list.
# 
# Return: An Eulerian cycle in this graph.
#
# AUTHOR : dohlee
##################################################

# Your imports here
from collections import defaultdict

# Your codes here
def parse_adjacency_list(inFile):
    """Parse adjacency list format [u -> v1,v2,v3]
    and return corresponding graph.
    """
    graph = defaultdict(list)
    for line in inFile.readlines():
        u, vs = line.strip().split(' -> ')
        u, vs = int(u), list(map(int, vs.split(',')))

        graph[u].extend(vs)

    return graph

def find_cycle(graph, start):
    """Return a sequence of nodes which form a cycle
    starting from a node 'start'.
    """
    cycle = []
    u = graph[start].pop()
    while u != start:
        cycle.append(u)
        u = graph[u].pop()
    cycle.append(u)

    # Clean up nodes which have no edges.
    toRemove = [k for k, v in graph.items() if not v]
    for k in toRemove:
        del graph[k]

    return cycle

def find_eulerian_cycle(graph, start=0):
    """Return an eulerian cycle of the graph."""
    cycle = [start] + find_cycle(graph, start)
    updated = True
    while updated:
        updated = False
        for i, start in enumerate(cycle):
            # If an edge starting from the node still exists,
            # insert new cycle.
            if start in graph:
                updated = True
                cycle = cycle[:i+1] + find_cycle(graph, start) + cycle[i+1:]
                break

    return cycle

if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_BA3F.txt') as inFile:
        graph = parse_adjacency_list(inFile)

    # Print output
    with open('../../answers/rosalind_BA3F_out.txt', 'w') as outFile:
        print('->'.join(map(str, find_eulerian_cycle(graph))), file=outFile)

