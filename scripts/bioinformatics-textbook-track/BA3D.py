##################################################
# Construct the De Bruijn Graph of a String
#
# http://rosalind.info/problems/BA3D/
# 
# Given: An integer k and a string Text.
# 
# Return:DeBruijnk(Text), in the form of an adjacency
#  list.
#
# AUTHOR : dohlee
##################################################

# Your imports here
from BA1E import enumerate_kmers
from collections import Counter, defaultdict

# Your codes here
class DeBruijnNode:
    def __init__(self, label):
        self.label = label
        self.parents = Counter()
        self.children = Counter()

    def add_parent(self, parent):
        """Add new parent to the node. 
        Note that self.parents can have multiple identical
        parent nodes at the same time.
        """
        self.parents[parent] += 1

    def add_child(self, child):
        """Add new child to the node."""
        self.children[child] += 1

    def __hash__(self):
        """Make de Bruijn node hashable since it will be used
        as a key of Counter object.
        """
        return hash(self.label)

class DeBruijnGraph:
    def __init__(self, string, k):
        """Construct de Bruijn graph for string with k-mers.
        Each node is labeled with (k-1)-mers, and each edge represents
        every k-mers in the string.
        """
        self.nodes = dict()
        self.graph = self._construct_graph(string, k)

    def _construct_graph(self, string, k):
        graph = defaultdict(list)
        for i, kmer in enumerate_kmers(string, k):
            if kmer[:-1] in self.nodes:
                u = self.nodes[kmer[:-1]]
            else:
                u = DeBruijnNode(kmer[:-1])
                self.nodes[kmer[:-1]] = u

            if kmer[1:] in self.nodes:
                v = self.nodes[kmer[1:]]
            else:
                v = DeBruijnNode(kmer[1:])
                self.nodes[kmer[1:]] = v
            graph[u].append(v)

        return graph

    def __getitem__(self, u):
        return self.graph[u]

    def __iter__(self):
        return iter(self.graph.keys())

if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_BA3D.txt') as inFile:
        k = int(inFile.readline())
        string = inFile.readline().strip()

    # Print output
    with open('../../answers/rosalind_BA3D_out.txt', 'w') as outFile:
        deBruijnGraph = DeBruijnGraph(string, k)
        for u in deBruijnGraph:
            print('%s -> %s' % (u.label, ','.join(map(lambda x: x.label, deBruijnGraph[u]))), file=outFile)

