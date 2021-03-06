##################################################
# Genome Assembly with Perfect Coverage and Repeats
#
# http://rosalind.info/problems/GREP/
# 
# Given: A list S_(k+1) of error-free DNA (k+1)-mers
#  (k <=q 5) taken from the same strand of a circular
#  chromosome (of length <=q 50).
# 
# Return: All circular strings assembled by complete
#  cycles in the de Bruijn graph B_k of S_(k+1).
#  The strings may be given in any order, but each
#  one should begin with the first (k+1)-mer provided
#  in the input.
#
# AUTHOR : dohlee
##################################################

# Your imports here
from PCOV import DeBruijnGraph

# Your codes here
if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_GREP.txt') as inFile:
        kmers = [line.strip() for line in inFile.readlines()]

    # Print output
    with open('../../answers/rosalind_GREP_out.txt', 'w') as outFile:
        dbg = DeBruijnGraph(kmers=kmers)
        reconstructed = dbg.reconstruct_all(cyclic=True, start=dbg.nodes[kmers[0][:-1]])

        print('\n'.join([s for s in reconstructed if s.startswith(kmers[0])]), file=outFile)
