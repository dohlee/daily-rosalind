##################################################
# Construct the Overlap Graph of a Collection of k-mers
#
# http://rosalind.info/problems/BA3C/
# 
# Given: A collection Patterns of k-mers.
# 
# Return: The overlap graph Overlap(Patterns), in
#  the form of an adjacency list.
#
# AUTHOR : dohlee
##################################################

# Your imports here
from collections import defaultdict

# Your codes here
def overlap_graph(kmers):
    """Return the overlap graph of given k-mers."""
    overlapGraph = defaultdict(list)
    prefixDict = defaultdict(list)
    suffixDict = defaultdict(list) 
    for kmer in kmers:
        prefixDict[kmer[:-1]].append(kmer)
        suffixDict[kmer[1:]].append(kmer)

    for suffix in suffixDict:
        if suffix not in prefixDict:
            continue
        for u in suffixDict[suffix]:
            for v in prefixDict[suffix]:
                overlapGraph[u].append(v)

    return overlapGraph

if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_BA3C.txt') as inFile:
        kmers = [line.strip() for line in inFile.readlines()]

    # Print output
    with open('../../answers/rosalind_BA3C_out.txt', 'w') as outFile:
        overlapGraph = overlap_graph(kmers)
        for u in overlapGraph:
            for v in overlapGraph[u]:
                print('%s -> %s' % (u, v), file=outFile)


