##################################################
# Find All Approximate Occurrences of a Pattern in a String
#
# http://rosalind.info/problems/BA1H/
# 
# Given: Strings Pattern and Text along with an
#  integer d.
# 
# Return: All starting positions where Pattern appears
#  as a substring of Text with at most d mismatches.
#
# AUTHOR : dohlee
##################################################

# Your imports here
from BA1G import hamming_distance
from BA1E import enumerate_kmers

# Your codes here
def find_approximate(text, pattern, d):
    """Return indices of all d-approximate occurences of the pattern."""
    k = len(pattern)
    return [i for i, kmer in enumerate_kmers(text, k) if hamming_distance(pattern ,kmer) <= d]

if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_BA1H.txt') as inFile:
        pattern = inFile.readline().strip()
        text = inFile.readline().strip()
        d = int(inFile.readline())

    # Print output
    with open('../../answers/rosalind_BA1H_out.txt', 'w') as outFile:
        print(' '.join(map(str, find_approximate(text, pattern, d))), file=outFile)

