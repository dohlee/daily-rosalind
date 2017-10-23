##################################################
# Local Alignment with Scoring Matrix
#
# http://rosalind.info/problems/LOCA/
# 
# Given: Two protein strings s and t in FASTA format
#  (each having length at most 1000 aa).
# 
# Return: A maximum alignment score along with substrings
#  r and u of s and t, respectively, which produce
#  this maximum alignment score (multiple solutions
#  may exist, in which case you may output any one).
#  Use:
#
# AUTHOR : dohlee
##################################################

# Your imports here
from GC import Fasta
from GLOB import DPMatrix

# Your codes here
def pam250_matrix():
    """Parse and return PAM250 matrix."""
    pam250 = """A  C  D  E  F  G  H  I  K  L  M  N  P  Q  R  S  T  V  W  Y
A  2 -2  0  0 -3  1 -1 -1 -1 -2 -1  0  1  0 -2  1  1  0 -6 -3
C -2 12 -5 -5 -4 -3 -3 -2 -5 -6 -5 -4 -3 -5 -4  0 -2 -2 -8  0
D  0 -5  4  3 -6  1  1 -2  0 -4 -3  2 -1  2 -1  0  0 -2 -7 -4
E  0 -5  3  4 -5  0  1 -2  0 -3 -2  1 -1  2 -1  0  0 -2 -7 -4
F -3 -4 -6 -5  9 -5 -2  1 -5  2  0 -3 -5 -5 -4 -3 -3 -1  0  7
G  1 -3  1  0 -5  5 -2 -3 -2 -4 -3  0  0 -1 -3  1  0 -1 -7 -5
H -1 -3  1  1 -2 -2  6 -2  0 -2 -2  2  0  3  2 -1 -1 -2 -3  0
I -1 -2 -2 -2  1 -3 -2  5 -2  2  2 -2 -2 -2 -2 -1  0  4 -5 -1
K -1 -5  0  0 -5 -2  0 -2  5 -3  0  1 -1  1  3  0  0 -2 -3 -4
L -2 -6 -4 -3  2 -4 -2  2 -3  6  4 -3 -3 -2 -3 -3 -2  2 -2 -1
M -1 -5 -3 -2  0 -3 -2  2  0  4  6 -2 -2 -1  0 -2 -1  2 -4 -2
N  0 -4  2  1 -3  0  2 -2  1 -3 -2  2  0  1  0  1  0 -2 -4 -2
P  1 -3 -1 -1 -5  0  0 -2 -1 -3 -2  0  6  0  0  1  0 -1 -6 -5
Q  0 -5  2  2 -5 -1  3 -2  1 -2 -1  1  0  4  1 -1 -1 -2 -5 -4
R -2 -4 -1 -1 -4 -3  2 -2  3 -3  0  0  0  1  6  0 -1 -2  2 -4
S  1  0  0  0 -3  1 -1 -1  0 -3 -2  1  1 -1  0  2  1 -1 -2 -3
T  1 -2  0  0 -3  0 -1  0  0 -2 -1  0  0 -1 -1  1  3  0 -5 -3
V  0 -2 -2 -2 -1 -1 -2  4 -2  2  2 -2 -1 -2 -2 -1  0  4 -6 -2
W -6 -8 -7 -7  0 -7 -3 -5 -3 -2 -4 -4 -6 -5  2 -2 -5 -6 17  0
Y -3  0 -4 -4  7 -5  0 -1 -4 -1 -2 -2 -5 -4 -4 -3 -3 -2  0 10
"""
    matrix = dict()
    lines = pam250.splitlines()
    aas = lines[0].split()
    for line in lines[1:]:
        tokens = line.strip().split()
        aa = tokens[0]
        values = map(int, tokens[1:])
        matrix[aa] = dict(zip(aas, values))

    return matrix
    

def recurrence_relation(i, j, self):
    """Recurrence relation for local pairwise sequence alignment."""
    candidates = [self.mat[i-1][j-1] + self.scoringMatrix[self.seq1[i-1]][self.seq2[j-1]],
                    self.mat[i-1][j] + self.gap,
                    self.mat[i][j-1] + self.gap,
                    0]
    return max(enumerate(candidates), key=lambda x: x[1])

def max_score(mat):
    """Return the maximum score in DP matrix."""
    maxScore = 0
    for i in range(len(mat.seq1) + 1):
        for j in range(len(mat.seq2) + 1):
            if mat[i][j] > maxScore:
                maxScore = mat[i][j]

    return maxScore

def initialize(self):
    """Initializer for local sequence alignment DP Matrix."""
    for i in range(len(self.seq1) + 1):
        self.mat[i][0] = 0  # Should be initialized to 0.
        self.backtrackMat[i][0] = self.DONE
    for j in range(len(self.seq2) + 1):
        self.mat[0][j] = 0  # Should be initialized to 0.
        self.backtrackMat[0][j] = self.DONE

def backtrack_starting_point(self):
    """Backtrack starting point of local sequence alignment should be 
    the cell with maximum score over the whole matrix.
    """
    maxScore, startingPoint = 0, (0, 0)
    for i in range(len(self.seq1) + 1):
        for j in range(len(self.seq2) + 1):
            if self.mat[i][j] > maxScore:
                maxScore = self.mat[i][j]
                startingPoint = (i, j)

    return startingPoint

if __name__ == '__main__':
    # Load the data.
    seq1, seq2 = [seq for header, seq in Fasta('../../datasets/rosalind_LOCA.txt')]
    mat = DPMatrix(seq1, seq2, match=None, mismatch=None, gap=-5)
    mat.set_scoring_matrix(pam250_matrix())
    mat.set_recurrence_relation(recurrence_relation)
    mat.set_backtrack_starting_point(backtrack_starting_point)
    mat.fill()

    # Print output
    with open('../../answers/rosalind_LOCA_out.txt', 'w') as outFile:
        print(max_score(mat), file=outFile)
        print('\n'.join(map(lambda s: s.replace('-', ''), mat.augmented_sequences())), file=outFile)

