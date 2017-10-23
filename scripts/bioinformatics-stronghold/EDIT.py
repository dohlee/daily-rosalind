##################################################
# Edit Distance
#
# http://rosalind.info/problems/EDIT/
# 
# Given: Two protein strings s and t in FASTA format
#  (each of length at most 1000 aa).
# 
# Return: The edit distance d_(\textrm(E))(s, t).
#
# AUTHOR : dohlee
##################################################

# Your imports here
from GC import Fasta
from GLOB import DPMatrix

# Your codes here
def recurrence_relation(i, j, self):
    """Recurrence relation for computing edit distance between
    two sequences.
    """
    candidates = [self.mat[i-1][j-1] + [self.mismatch, self.match][self.seq1[i-1] == self.seq2[j-1]],
                    self.mat[i-1][j] + self.gap,
                    self.mat[i][j-1] + self.gap]

    return min(enumerate(candidates), key=lambda x: x[1])

if __name__ == '__main__':
    # Load the data.
    seq1, seq2 = [seq for header, seq in Fasta('../../datasets/rosalind_EDIT.txt')]
    mat = DPMatrix(seq1, seq2, match=0, mismatch=1, gap=1)
    mat.set_recurrence_relation(recurrence_relation)
    mat.fill()

    # Print output
    with open('../../answers/rosalind_EDIT_out.txt', 'w') as outFile:
        print(mat[len(seq1)][len(seq2)], file=outFile)

