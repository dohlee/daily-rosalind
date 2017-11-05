##################################################
# Align Two Strings Using Linear Space
#
# http://rosalind.info/problems/BA5L/
# 
# Given: Two long amino acid strings (of length
#  approximately 10,000).
# 
# Return: The maximum alignment score of these strings,
#  followed by an alignment achieving this maximum
#  score. Use the BLOSUM62 scoring matrix and indel
#  penalty  = 5.
#
# AUTHOR : dohlee
##################################################

# Your imports here


# Your codes here
def Fasta(filePath):
    """Read fasta file and generate header and seq, one by one."""
    with open(filePath) as inFile:
        # read in the first sequence.
        header, seqs = inFile.readline()[1:].strip(), []

        for line in inFile.readlines():
            # if new header appears, yield header and sequence.
            if line.startswith('>'):
                yield header, ''.join(seqs)
                header, seqs = line[1:].strip(), []
            else:
                seqs.append(line.strip())

        # do not forget to yield the last sequence.
        yield header, ''.join(seqs)

def blosum62_matrix():
    """Parse and return BLOSUM62 matrix."""
    blosum62 = """A  C  D  E  F  G  H  I  K  L  M  N  P  Q  R  S  T  V  W  Y
A  4  0 -2 -1 -2  0 -2 -1 -1 -1 -1 -2 -1 -1 -1  1  0  0 -3 -2
C  0  9 -3 -4 -2 -3 -3 -1 -3 -1 -1 -3 -3 -3 -3 -1 -1 -1 -2 -2
D -2 -3  6  2 -3 -1 -1 -3 -1 -4 -3  1 -1  0 -2  0 -1 -3 -4 -3
E -1 -4  2  5 -3 -2  0 -3  1 -3 -2  0 -1  2  0  0 -1 -2 -3 -2
F -2 -2 -3 -3  6 -3 -1  0 -3  0  0 -3 -4 -3 -3 -2 -2 -1  1  3
G  0 -3 -1 -2 -3  6 -2 -4 -2 -4 -3  0 -2 -2 -2  0 -2 -3 -2 -3
H -2 -3 -1  0 -1 -2  8 -3 -1 -3 -2  1 -2  0  0 -1 -2 -3 -2  2
I -1 -1 -3 -3  0 -4 -3  4 -3  2  1 -3 -3 -3 -3 -2 -1  3 -3 -1
K -1 -3 -1  1 -3 -2 -1 -3  5 -2 -1  0 -1  1  2  0 -1 -2 -3 -2
L -1 -1 -4 -3  0 -4 -3  2 -2  4  2 -3 -3 -2 -2 -2 -1  1 -2 -1
M -1 -1 -3 -2  0 -3 -2  1 -1  2  5 -2 -2  0 -1 -1 -1  1 -1 -1
N -2 -3  1  0 -3  0  1 -3  0 -3 -2  6 -2  0  0  1  0 -3 -4 -2
P -1 -3 -1 -1 -4 -2 -2 -3 -1 -3 -2 -2  7 -1 -2 -1 -1 -2 -4 -3
Q -1 -3  0  2 -3 -2  0 -3  1 -2  0  0 -1  5  1  0 -1 -2 -2 -1
R -1 -3 -2  0 -3 -2  0 -3  2 -2 -1  0 -2  1  5 -1 -1 -3 -3 -2
S  1 -1  0  0 -2  0 -1 -2  0 -2 -1  1 -1  0 -1  4  1 -2 -3 -2
T  0 -1 -1 -1 -2 -2 -2 -1 -1 -1 -1  0 -1 -1 -1  1  5  0 -2 -2
V  0 -1 -3 -2 -1 -3 -3  3 -2  1  1 -3 -2 -2 -3 -2  0  4 -3 -1
W -3 -2 -4 -3  1 -2 -2 -3 -3 -2 -1 -4 -4 -2 -3 -3 -2 -3 11  2
Y -2 -2 -3 -2  3 -3  2 -1 -2 -1 -1 -2 -3 -1 -2 -2 -2 -1  2  7
"""
    matrix = dict()
    lines = blosum62.splitlines()
    aas = lines[0].split()
    for line in lines[1:]:
        tokens = line.strip().split()
        aa = tokens[0]
        values = map(int, tokens[1:])
        matrix[aa] = dict(zip(aas, values))

    return matrix

class DPMatrix:
    def __init__(self, seq1, seq2, match, mismatch, gap):
        """Initialize 2-dimensional DP matrix which can be used for
        various alignment tasks.
        Basically it performs pairwise global alignment.
        """
        self.DIAG, self.UP, self.LEFT, self.DONE = 0, 1, 2, 3
        self.seq1, self.seq2 = seq1, seq2
        self.mat = [[0] * (len(seq2) + 1) for _ in range(len(seq1) + 1)]
        self.backtrackMat = [[0] * (len(seq2) + 1) for _ in range(len(seq1) + 1)]
        self.match, self.mismatch, self.gap = match, mismatch, gap

        if self.match is None or self.mismatch is None:
            self.scoringMatrix = blosum62_matrix()
            self.recurrenceRelation = lambda i, j, self: max(enumerate([self.mat[i-1][j-1] + self.scoringMatrix[self.seq1[i-1]][self.seq2[j-1]], 
                                                            self.mat[i-1][j] + self.gap, 
                                                            self.mat[i][j-1] + self.gap]),
                                                            key=lambda x: x[1])
        else:
            self.recurrenceRelation = lambda i, j, self: max(enumerate([self.mat[i-1][j-1] + [self.mismatch, self.match][self.seq1[i-1] == self.seq2[j-1]], 
                                                            self.mat[i-1][j] + self.gap, 
                                                            self.mat[i][j-1] + self.gap]),
                                                            key=lambda x: x[1])

    def set_recurrence_relation(self, recurrenceRelation):
        """Set recurrence relation which is used for filling DP matrix."""
        self.recurrenceRelation = recurrenceRelation

    def set_scoring_matrix(self, scoringMatrix):
        """Set user-defined scoring matrix"""
        self.scoringMatrix = scoringMatrix

    def set_backtrack_starting_point(self, func):
        """Set user-defined backtrack starting point."""
        self.backtrack_starting_point = func

    def set_initializer(self, func):
        """Set user-defined matrix initializer."""
        self.initialize = func

    def initialize(self, self_):
        """Matrix initilizer."""
        for i in range(len(self.seq1) + 1):
            self.mat[i][0] = self.gap * i
            self.backtrackMat[i][0] = self.UP
        for j in range(len(self.seq2) + 1):
            self.mat[0][j] = self.gap * j
            self.backtrackMat[0][j] = self.LEFT

    def backtrack_starting_point(self, self_):
        """Dynamically define starting point of the backtracking."""
        return len(self.seq1), len(self.seq2)

    def fill(self):
        """Fill DP matrix with given recurrence relation."""
        self.initialize(self)

        for i in range(1, len(self.seq1) + 1):
            for j in range(1, len(self.seq2) + 1):
                direction, score = self.recurrenceRelation(i, j, self)
                self.mat[i][j] = score
                self.backtrackMat[i][j] = direction

    def augmented_sequences(self):
        """Return augmented sequences."""
        i, j = self.backtrack_starting_point(self)
        augmentedSeq1, augmentedSeq2 = [], []

        while not (i == 0 and j == 0):
            if self.backtrackMat[i][j] == self.DIAG:
                augmentedSeq1.append(self.seq1[i-1])
                augmentedSeq2.append(self.seq2[j-1])
                i -= 1
                j -= 1
            elif self.backtrackMat[i][j] == self.UP:
                augmentedSeq1.append(self.seq1[i-1])
                augmentedSeq2.append('-')
                i -= 1
            elif self.backtrackMat[i][j] == self.LEFT:
                augmentedSeq1.append('-')
                augmentedSeq2.append(self.seq2[j-1])
                j -= 1
            else:
                break

        return ''.join(augmentedSeq1[::-1]), ''.join(augmentedSeq2[::-1])

    def __getitem__(self, i):
        return self.mat[i] 





if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_BA5L.txt') as inFile:
        seq1, seq2 = [line.strip() for line in inFile.readlines()]
        mat = DPMatrix(seq1, seq2, match=None, mismatch=None, gap=-5)
        mat.fill()

    # Print output
    with open('../../answers/rosalind_BA5L_out.txt', 'w') as outFile:
        print(mat[len(seq1)][len(seq2)], file=outFile)
        print('\n'.join(mat.augmented_sequences()), file=outFile)

