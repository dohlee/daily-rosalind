##################################################
# Reconstruct a String from its k-mer Composition
#
# http://rosalind.info/problems/BA3H/
# 
# Given: An integer k followed by a list of k-mers
#  Patterns.
# 
# Return: A string Text with k-mer composition equal
#  to Patterns. (If multiple answers exist, you
#  may return any one.)
#
# AUTHOR : dohlee
##################################################

# Your imports here
from BA3D import DeBruijnGraph

# Your codes here
if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_BA3H.txt') as inFile:
        k = int(inFile.readline())
        kmers = [line.strip() for line in inFile.readlines()]
        deBruijnGraph = DeBruijnGraph(kmers=kmers)

    # Print output
    with open('../../answers/rosalind_BA3H_out.txt', 'w') as outFile:
        print(deBruijnGraph.reconstruct(), file=outFile)

