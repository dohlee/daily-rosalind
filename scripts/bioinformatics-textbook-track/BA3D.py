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
from BA3F import find_eulerian_cycle
from BA3G import find_eulerian_path
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
    def __init__(self, string=None, kmers=None, k=None):
        """Construct de Bruijn graph for string with k-mers.
        Each node is labeled with (k-1)-mers, and each edge represents
        every k-mers in the string.
        """
        self.nodes = dict()
        if string is not None and kmers is not None:
            raise ValueError("You cannot construct de Bruijn graph with a string and k-mers at the same time.")
        if string is None and kmers is None:
            raise ValueError("You should give string or k-mers to build de Bruijn graph.")

        if string is not None:
            if k is None:
                raise ValueError("You should specify the length of k-mers to build de Bruijn graph.")
            else:
                self.graph = self._construct_graph_from_string(string, k)
        elif kmers is not None:
            self.graph = self._construct_graph_from_kmers(kmers)

    def _construct_graph_from_string(self, string, k):
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

    def _construct_graph_from_kmers(self, kmers):
        graph = defaultdict(list)
        for kmer in kmers:
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

    def reconstruct(self, cyclic=False):
        """Reconstruct original string from de bruijn graph."""
        graph = self.graph.copy()
        if cyclic:
            path = find_eulerian_cycle(graph, start=list(self.graph.keys())[0])
            reconstructed = [path[0].label]
            k = len(path[0].label)
            for node in path[1:-k]:
                reconstructed.append(node.label[-1])
        else:
            path = find_eulerian_path(graph)
            reconstructed = [path[0].label]
            for node in path[1:]:
                reconstructed.append(node.label[-1])

        return ''.join(reconstructed)

    def __getitem__(self, u):
        return self.graph[u]

    def __iter__(self):
        return iter(self.graph.keys())

    def __str__(self):
        s = []
        for u in self.graph:
            s.append('%s -> %s' % (u.label, ','.join(map(lambda x: x.label, self.graph[u]))))

        return '\n'.join(s)

if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_BA3D.txt') as inFile:
        k = int(inFile.readline())
        string = inFile.readline().strip()

    # Print output
    with open('../../answers/rosalind_BA3D_out.txt', 'w') as outFile:
        deBruijnGraph = DeBruijnGraph(string=string, k=k)
        for u in deBruijnGraph:
            print('%s -> %s' % (u.label, ','.join(map(lambda x: x.label, deBruijnGraph[u]))), file=outFile)

