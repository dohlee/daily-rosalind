##################################################
# Implement UPGMA
#
# http://rosalind.info/problems/BA7D/
# 
# Given: An integer n followed by a space-delimited
#  n x n distance matrix.
# 
# Return: An adjacency list for the ultrametric
#  tree output by UPGMA. Weights should be accurate
#  to three decimal places.
#
# AUTHOR : dohlee
##################################################

# Your imports here


# Your codes here
class Cluster(object):
    """docstring for Cluster"""
    def __init__(self, id, age, nodes):
        self.id = id
        self.age = age
        self.nodes = nodes
    
    def compute_distance_with_cluster(self, cluster, distanceMatrix):
        distanceSum = sum(distanceMatrix[i][j] for i in self.nodes for j in cluster.nodes)
        return distanceSum / float(len(self.nodes) * len(cluster.nodes))

def merge_clusters(c1, c2, id, age):
    """Merge two clusters and return new cluster with |c1| + |c2| elements."""
    return Cluster(id, age, c1.nodes + c2.nodes)

def find_closest_clusters(clusterList, clusters, distanceMatrix):
    """Find closest clusters given distance matrix."""
    c1, c2 = min([(c1, c2) for c1 in clusters for c2 in clusters if c1 != c2], key=lambda tup: clusterList[tup[0]].compute_distance_with_cluster(clusterList[tup[1]], distanceMatrix))
    return clusterList[c1], clusterList[c2]

def connect_nodes(graph, parent, child):
    """Connet parent and child node."""
    distance = parent.age - child.age

    graph[parent.id].append((child.id, distance)) 
    graph[child.id].append((parent.id, distance))

def update_distance_matrix(newCluster, clusterList, distanceMatrix):
    """append the new row and column for new cluster."""
    distances = [newCluster.compute_distance_with_cluster(cluster, distanceMatrix) for cluster in clusterList]

    # append new column.
    for i in range(len(distanceMatrix)):
        distanceMatrix[i].append(distances[i])

    # append new row.
    distanceMatrix.append(distances + [0])

def upgma(distanceMatrix, n):
    """UPGMA clustering algorithm."""
    from collections import defaultdict

    # we need to maintain the list of clusters to access them by index.
    clusterList = [Cluster(id, age=0, nodes=[id]) for id in range(n)]
    # the set of remaining clusters.
    clusters = set([id for id in range(n)])
    # the graph to be returned.
    graph = defaultdict(list)
    # id of the new node.
    currentId = n

    while len(clusters) > 1:  # while there is more than one cluster
        c1, c2 = find_closest_clusters(clusterList, clusters, distanceMatrix)

        # age = D(c1, c2) / 2.
        age = c1.compute_distance_with_cluster(c2, distanceMatrix) / 2

        # merge two child clusters and make new node.
        newCluster = merge_clusters(c1, c2, currentId, age=age)
        currentId += 1

        # connect parent node with two child clusters.
        connect_nodes(graph, newCluster, c1)
        connect_nodes(graph, newCluster, c2)

        # remove child clusters from remaining clusters, and add parent cluster to remaining clusters.
        clusters.remove(c1.id)
        clusters.remove(c2.id)
        clusters.add(newCluster.id)
        clusterList.append(newCluster)

        update_distance_matrix(newCluster, clusterList, distanceMatrix)


    return graph

if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_BA7D.txt') as inFile:
        n = int(inFile.readline())
        distanceMatrix = [list(map(int, inFile.readline().split())) for _ in range(n)]

        T = upgma(distanceMatrix, n)
    # Print output
    with open('../../answers/rosalind_BA7D_out.txt', 'w') as outFile:
        nodeCount = len(T)
        for u in range(nodeCount):
            for v, w in T[u]:
                print('%d->%d:%.3f' % (u, v, w), file=outFile)
