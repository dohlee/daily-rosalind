##################################################
# Compute the Hamming Distance Between Two Strings
#
# http://rosalind.info/problems/BA1G/
# 
# Given: Two DNA strings.
# 
# Return: An integer value representing the Hamming
#  distance.
#
# AUTHOR : dohlee
##################################################

# Your imports here


# Your codes here
def hamming_distance(seq1, seq2):
    """Return hamming distance of two sequence."""
    # note that hamming distance is defined for two sequences
    # with the same length.
    assert len(seq1) == len(seq2)
    # count the number of mismatching characters in pythonic way!
    return sum(c1 != c2 for c1, c2 in zip(seq1, seq2))

if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_BA1G.txt') as inFile:
        seq1 = inFile.readline().strip()
        seq2 = inFile.readline().strip()

    # Print output
    with open('../../answers/rosalind_BA1G_out.txt', 'w') as outFile:
        print(hamming_distance(seq1, seq2), file=outFile)

