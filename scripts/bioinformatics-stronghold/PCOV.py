##################################################
# Genome Assembly with Perfect Coverage
#
# http://rosalind.info/problems/PCOV/
# 
# Given: A collection of (error-free) DNA k-mers
#  (k <=q 50) taken from the same strand of a circular
#  chromosome. In this dataset, all k-mers from
#  this strand of the chromosome are present, and
#  their de Bruijn graph consists of exactly one
#  simple cycle.
# 
# Return: A cyclic superstring of minimal length
#  containing the reads (thus corresponding to a
#  candidate cyclic chromosome).
#
# AUTHOR : dohlee
##################################################

# Your imports here
from collections import Counter, defaultdict

# Your codes here
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

def enumerate_kmers(string, k, start=0):
    """Generate all k-mers within a string."""
    for i in range(0, len(string) - k + 1):
        yield start + i, string[i:i+k]

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
    with open('../../datasets/rosalind_PCOV.txt') as inFile:
        kmers = [line.strip() for line in inFile.readlines()]

    # Print output
    with open('../../answers/rosalind_PCOV_out.txt', 'w') as outFile:
        dbg = DeBruijnGraph(kmers=kmers)
        print(dbg.reconstruct(cyclic=True), file=outFile)

