##################################################
# Finding a Shared Spliced Motif
#
# http://rosalind.info/problems/LCSQ/
# 
# Given: Two DNA strings s and t (each having length
#  at most 1 kbp) in FASTA format.
# 
# Return: A longest common subsequence of s and
#  t. (If more than one solution exists, you may
#  return any one.)
#
# AUTHOR : dohlee
##################################################

# Your imports here
from GC import Fasta
from GLOB import DPMatrix

# Your codes here
def longest_common_subsequence(seq1, seq2):
    """Return the longest common subsequence of two sequences."""
    mat = DPMatrix(seq1, seq2, match=1, mismatch=0, gap=0)
    mat.fill()

    lcs = []
    augSeq1, augSeq2 = mat.augmented_sequences()
    for c1, c2 in zip(augSeq1, augSeq2):
        if c1 == c2:
            lcs.append(c1)

    return ''.join(lcs)

if __name__ == '__main__':
    # Load the data.
    seq1, seq2 = [seq for header, seq in Fasta('../../datasets/rosalind_LCSQ.txt')]

    # Print output
    with open('../../answers/rosalind_LCSQ_out.txt', 'w') as outFile:
        print(longest_common_subsequence(seq1, seq2), file=outFile)

