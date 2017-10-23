##################################################
# Counting Optimal Alignments
#
# http://rosalind.info/problems/CTEA/
# 
# Given: Two protein strings s and t in FASTA format,
#  each of length at most 1000 aa.
# 
# Return: The total number of optimal alignments
#  of s and t with respect to edit alignment score,
#  modulo 134,217,727 (227-1).
#
# AUTHOR : dohlee
##################################################

# Your imports here
from GC import Fasta
from GLOB import DPMatrix

# Your codes here
def initialize(self):
    """Initializer for counting optimal alignments."""
    for i in range(len(self.seq1) + 1):
        self.mat[i][0] = (self.gap * i, 1)
        self.backtrackMat[i][0] = self.DONE  # We don't need backtracking
    for j in range(len(self.seq2) + 1):
        self.mat[0][j] = (self.gap * j, 1)
        self.backtrackMat[0][j] = self.DONE  # We don't need backtracking

def recurrence_relation(i, j, self):
    """Recurrence relation for counting optimal alignments."""
    candidates = [self.mat[i-1][j-1][0] + [self.mismatch, self.match][self.seq1[i-1] == self.seq2[j-1]],
                    self.mat[i-1][j][0] + self.gap,
                    self.mat[i][j-1][0] + self.gap]
    alignmentCounts = [self.mat[i-1][j-1][1], self.mat[i-1][j][1], self.mat[i][j-1][1]]

    alignmentCount = 0
    minScore = min(candidates)
    for i in range(3):
        if candidates[i] == minScore:
            alignmentCount += alignmentCounts[i]

    return (self.DONE, (minScore, alignmentCount))

if __name__ == '__main__':
    # Load the data.
    seq1, seq2 = [seq for header, seq in Fasta('../../datasets/rosalind_CTEA.txt')]
    mat = DPMatrix(seq1, seq2, match=0, mismatch=1, gap=1)
    mat.set_initializer(initialize)
    mat.set_recurrence_relation(recurrence_relation)
    mat.fill()
    # Print output
    with open('../../answers/rosalind_CTEA_out.txt', 'w') as outFile:
        print(mat[len(seq1)][len(seq2)][1] % 134217727, file=outFile)

