##################################################
# Edit Distance Alignment
#
# http://rosalind.info/problems/EDTA/
# 
# Given: Two protein strings s and t in FASTA format
#  (with each string having length at most 1000 aa).
# 
# Return: The edit distance d_(\textrm(E))(s, t)
#  followed by two augmented strings s' and t' representing
#  an optimal alignment of s and t.
#
# AUTHOR : dohlee
##################################################

# Your imports here
from GC import Fasta
from GLOB import DPMatrix
from EDIT import recurrence_relation

# Your codes here

if __name__ == '__main__':
    # Load the data.
    seq1, seq2 = [seq for header, seq in Fasta('../../datasets/rosalind_EDTA.txt')]
    mat = DPMatrix(seq1, seq2, match=0, mismatch=1, gap=1)
    mat.set_recurrence_relation(recurrence_relation)
    mat.fill()

    # Print output
    with open('../../answers/rosalind_EDTA_out.txt', 'w') as outFile:
        print(mat[len(seq1)][len(seq2)], file=outFile)
        print('\n'.join(mat.augmented_sequences()), file=outFile)
