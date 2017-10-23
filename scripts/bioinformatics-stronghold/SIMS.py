##################################################
# Finding a Motif with Modifications
#
# http://rosalind.info/problems/SIMS/
# 
# Given: Two DNA strings s and t, where s has length
#  at most 10 kbp and t represents a motif of length
#  at most 1 kbp.
# 
# Return: An optimal fitting alignment score with
#  respect to the mismatch score defined above,
#  followed by an optimal fitting alignment of a
#  substring of s against t. If multiple such alignments
#  exist, then you may output any one.
#
# AUTHOR : dohlee
##################################################

# Your imports here
from GC import Fasta
from GLOB import DPMatrix

# Your codes here
def initialize(self):
    """Initializer for fitting alignment."""
    for i in range(len(self.seq1) + 1):
        self.mat[i][0] = 0  # Should be initialized to 0.
        self.backtrackMat[i][0] = self.DONE
    for j in range(len(self.seq2) + 1):
        self.mat[0][j] = self.gap * j
        self.backtrackMat[0][j] = self.DONE

def backtrack_starting_point(self):
    """Backtrack starting point for fitting alignment."""
    maxScore, startingPoint = -12345679, (0, 0)
    for i in range(len(self.seq1) + 1):
        if self.mat[i][len(self.seq2)] > maxScore:
            maxScore = self.mat[i][len(self.seq2)]
            startingPoint = (i, len(self.seq2))

    return startingPoint

def get_max_score(mat):
    """Return the max score over the rightmost column of the DP matrix."""
    return max(mat[i][len(mat.seq2)] for i in range(len(mat.seq1) + 1))

if __name__ == '__main__':
    # Load the data.
    seq1, seq2 = [seq for header, seq in Fasta('../../datasets/rosalind_SIMS.txt')]
    mat = DPMatrix(seq1, seq2, match=+1, mismatch=-1, gap=-1)
    mat.set_initializer(initialize)
    mat.set_backtrack_starting_point(backtrack_starting_point)
    mat.fill()

    # Print output
    with open('../../answers/rosalind_SIMS_out.txt', 'w') as outFile:
        print(get_max_score(mat), file=outFile)
        print('\n'.join(mat.augmented_sequences()), file=outFile)

