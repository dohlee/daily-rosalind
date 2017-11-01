##################################################
# Find a k-Universal Circular String
#
# http://rosalind.info/problems/BA3I/
# 
# Given: An integer k.
# 
# Return: A k-universal circular string. (If multiple
#  answers exist, you may return any one.)
#
# AUTHOR : dohlee
##################################################

# Your imports here
from BA3D import DeBruijnGraph

# Your codes here
def binary_rep(i, k):
	"""Return binary representation of decimal number i,
	with zero-paddings to make the length of the representation k.
	"""
	b = bin(i)[2:]
	return '0' * (k - len(b)) + b

def binary_kmers(k):
	"""Return all binary k-mers."""
	return [binary_rep(i, k) for i in range(2**k)]

if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_BA3I.txt') as inFile:
        k = int(inFile.readline())
        kmers = binary_kmers(k)

    # Print output
    with open('../../answers/rosalind_BA3I_out.txt', 'w') as outFile:
        deBruijnGraph = DeBruijnGraph(kmers=kmers)
        # print(deBruijnGraph)
        print(deBruijnGraph.reconstruct(cyclic=True), file=outFile)

