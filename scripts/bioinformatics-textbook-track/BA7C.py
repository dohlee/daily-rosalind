##################################################
# Implement AdditivePhylogeny
#
# http://rosalind.info/problems/BA7C/
# 
# Given: n and a tab-delimited n x n additive matrix.
# 
# Return: A weighted adjacency list for the simple
#  tree fitting this matrix.
#
# AUTHOR : dohlee
##################################################

# Your imports here
from BA7B import limb_length

# Your codes here
def delete_edge(graph, src, dst):
    """Delete an edge (src, dst) from graph."""
    for i, (neighbor, length) in enumerate(graph[src]):
        if neighbor == dst:
            break
    del graph[src][i]

    for i, (neighbor, length) in enumerate(graph[dst]):
        if neighbor == src:
            break
    del graph[dst][i]

def get_path(graph, src, dst, visited):
    """Return a path from src to dst by DFS.
    Path will be like [(src, w1), (v1, w2), ..., (v_k-1, w_k), (dst, 0)].
    """
    visited[src] = True
    for v, w in graph[src]:
        if visited[v]:
            continue

        # if dst is found, return a single edge (src, dst).
        if v == dst:
            return [(src, w), (dst, 0)]

        # recursively call get_path with v as src and see if v is on the path to dst.
        path = get_path(graph, v, dst, visited)
        if path is not None:
            return [(src, w)] + path

    # if src is not on the path to dst, return None.
    return None

def insert_new_node(graph, src, dst, distance, visited, nodeName):
    """ Insert new node named nodeName between the path (src, ..., dst).
    The new node will be at distance 'distance' from src on the path between src and dst.
    """
    path = get_path(graph, src, dst, visited)

    curr = 0  # pointer to the node on the path.
    edgeLength = path[0][1]
    remainingLength = distance

    # find appropriate position to insert the new node.
    while remainingLength >= edgeLength:
        remainingLength -= edgeLength
        curr += 1
        edgeLength = path[curr][1]

    # edge (currNode, nextNode) will be split.
    # new node will be put at distance 'remainingLength' from currNode.
    currNode = path[curr][0]
    nextNode = path[curr+1][0]

    # insert new node.
    graph[currNode].append((nodeName, remainingLength))
    graph[nextNode].append((nodeName, edgeLength - remainingLength))
    graph[nodeName] = [(currNode, remainingLength), (nextNode, edgeLength - remainingLength)]
    # and delete split edge.
    delete_edge(graph, currNode, nextNode)

def additive_phylogeny(distanceMatrix, n):
    """Find the simple tree fitting an n x n additive distance matrix D."""
    return additive_phylogeny_helper(distanceMatrix, n, nodeName=len(distanceMatrix))

def additive_phylogeny_helper(distanceMatrix, n, nodeName):
    """Helper for additive_phylogeny which will be recursively called."""
    # return simple graph with node 0 and 1, and a single edge.
    if n == 2:
        distance = distanceMatrix[0][1]
        return { 0:[(1, distance)], 1:[(0, distance)] }

    # limb length of the leaf n-1.
    limbLength = limb_length(distanceMatrix, n=n, j=n-1)
    for i in range(n-1):
        distanceMatrix[i][n-1] -= limbLength
        distanceMatrix[n-1][i] = distanceMatrix[i][n-1]

    # find degenerate triples which satisfies
    # Di,j = Di,n-1 + Dj,n-1
    for i in range(n-1):
        for j in range(i+1, n-1):
            if distanceMatrix[i][j] == distanceMatrix[i][n-1] + distanceMatrix[j][n-1]:
                x = distanceMatrix[i][n-1]
                src, dst = i, j  # store i, j in src, dst
                break
    
    # recursively call the function to get smaller graph first.
    graph = additive_phylogeny_helper(distanceMatrix, n-1, nodeName=nodeName+1)

    # insert new node on the path (src, ..., dst).
    visited = [False] * (2 * len(distanceMatrix))
    insert_new_node(graph, src, dst, x, visited, nodeName)

    # add leaf n-1 back to new node by creating a limb of length limbLength.
    graph[n-1] = [(nodeName, limbLength)]
    graph[nodeName].append((n-1, limbLength))
    
    return graph


if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_BA7C.txt') as inFile:
        n = int(inFile.readline())
        distanceMatrix = [list(map(int, line.split())) for line in inFile.readlines()]
        graph = additive_phylogeny(distanceMatrix, n)

    # Print output
    with open('../../answers/rosalind_BA7C_out.txt', 'w') as outFile:
        for src in graph:
            for dst, length in graph[src]:
                print('%d->%d:%d' % (src, dst, length), file=outFile)

