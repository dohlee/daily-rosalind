##################################################
# Find All Occurrences of a Pattern in a String
#
# http://rosalind.info/problems/BA1D/
# 
# Given: Strings Pattern and Genome.
# 
# Return: All starting positions in Genome where
#  Pattern appears as a substring.  Use 0-based
#  indexing.
#
# AUTHOR : dohlee
##################################################

# Your imports here
from BA1A import find

# Your codes here
if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_BA1D.txt') as inFile:
    	motif = inFile.readline().strip()
    	seq = inFile.readline().strip()

    # Print output
    with open('../../answers/rosalind_BA1D_out.txt', 'w') as outFile:
        print(' '.join(map(str, find(seq, motif))), file=outFile)

