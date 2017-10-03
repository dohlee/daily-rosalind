##################################################
# Overlap Graphs
#
# http://rosalind.info/problems/GRPH/
# 
# Given: A collection of DNA strings in FASTA format
#  having total length at most 10 kbp.
# 
# Return: The adjacency list corresponding to (O)_3.
#   You may return edges in any order.
#
# AUTHOR : dohlee
##################################################

# Your imports here
from GC import Fasta
from collections import defaultdict

# Your codes here
def overlap_graph(filePath, k=3):
    prefix = defaultdict(list)
    suffix = defaultdict(list)

    for header, seq in Fasta(filePath):
        prefix[seq[:k]].append(header)
        suffix[seq[-k:]].append(header)

    overlapGraph = []
    for kmer in prefix:
        for h in prefix[kmer]:
            for s in suffix[kmer]:
                if h != s:
                    overlapGraph.append((s, h))

    return overlapGraph

if __name__ == '__main__':
    # Load the data.
    overlapGraph = overlap_graph('../../datasets/rosalind_GRPH.txt')        

    # Print output
    with open('../../answers/rosalind_GRPH_out.txt', 'w') as outFile:
        print('\n'.join([' '.join([src, dst]) for src, dst in overlapGraph]), file=outFile)
