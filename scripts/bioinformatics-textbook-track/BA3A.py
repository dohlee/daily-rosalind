##################################################
# Generate the k-mer Composition of a String
#
# http://rosalind.info/problems/BA3A/
# 
# Given: An integer k and a string Text.
# 
# Return: Compositionk(Text) (the k-mers can be
#  provided in any order).
#
# AUTHOR : dohlee
##################################################

# Your imports here
from BA1E import enumerate_kmers

# Your codes here
if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_BA3A.txt') as inFile:
        k = int(inFile.readline())
        text = inFile.readline().strip()

    # Print output
    with open('../../answers/rosalind_BA3A_out.txt', 'w') as outFile:
        for i, kmer in sorted(enumerate_kmers(text, k), key=lambda x: x[1]):
            print(kmer, file=outFile)

