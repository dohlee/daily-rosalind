##################################################
# Construct the De Bruijn Graph of a Collection of k-mers
#
# http://rosalind.info/problems/BA3E/
# 
# Given: A collection of k-mers Patterns.
# 
# Return: The de Bruijn graph DeBruijn(Patterns),
#  in the form of an adjacency list.
#
# AUTHOR : dohlee
##################################################

# Your imports here
from BA3D import DeBruijnGraph

# Your codes here
if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_BA3E.txt') as inFile:
        kmers = [line.strip() for line in inFile.readlines()]

    # Print output
    with open('../../answers/rosalind_BA3E_out.txt', 'w') as outFile:
        deBruijnGraph = DeBruijnGraph(kmers=kmers)
        for u in deBruijnGraph:
            print('%s -> %s' % (u.label, ','.join(map(lambda x: x.label, deBruijnGraph[u]))), file=outFile)
