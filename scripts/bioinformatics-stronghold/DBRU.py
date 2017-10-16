##################################################
# Constructing a De Bruijn Graph
#
# http://rosalind.info/problems/DBRU/
# 
# Given: A collection of up to 1000 (possibly repeating)
#  DNA strings of equal length (not exceeding 50
#  bp) corresponding to a set S of (k+1)-mers.
# 
# Return: The adjacency list corresponding to the
#  de Bruijn graph corresponding to S \cup S^(\textrm(rc)).
#
# AUTHOR : dohlee
##################################################

# Your imports here
from REVC import reverse_complement

# Your codes here
def de_bruijn_graph(seqs):
	"""Construct de Bruijn Graph from a set of sequences."""
	seqs = set(seqs).union(set(reverse_complement(seq) for seq in seqs))
	adjacencyList = [(seq[:-1], seq[1:]) for seq in seqs]
	return adjacencyList

if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_DBRU.txt') as inFile:
        seqs = [line.strip() for line in inFile.readlines()]

    # Print output
    with open('../../answers/rosalind_DBRU_out.txt', 'w') as outFile:
        for u, v in de_bruijn_graph(seqs):
        	print('(%s, %s)' % (u, v), file=outFile)

