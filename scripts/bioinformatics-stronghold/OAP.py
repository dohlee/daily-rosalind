##################################################
# Overlap Alignment
#
# http://rosalind.info/problems/OAP/
# 
# Given: Two DNA strings s and t in FASTA format,
#  each having length at most 10 kbp.
# 
# Return: The score of an optimal overlap alignment
#  of s and t, followed by an alignment of a suffix
#  s' of s and a prefix t' of t achieving this optimal
#  score. Use an alignment score in which matching
#  symbols count +1, substitutions count -2, and
#  there is a linear gap penalty of 2.  If multiple
#  optimal alignments exist, then you may return
#  any one.
#
# AUTHOR : dohlee
##################################################

# Your imports here
from GC import Fasta

# Your codes here
INF = 12345679
DIAG, UP, LEFT, DONE = 1, 2, 4, 8

def initialize_matrix(mat, backtrackMat, seq1, seq2, gap):
    """Initialize matrices for overlap alignment."""
    for i in range(len(seq1) + 1):
        mat[i][0] = gap * i
        backtrackMat[i][len(seq2)] = UP
    for j in range(len(seq2) + 1):
        mat[0][j] = 0
        backtrackMat[0][j] = LEFT


def overlap_alignment(seq1, seq2, match, mismatch, gap):
    """Return the score and augmented sequences of overlap alignment of two sequences.
    Pruning the DP matrix cell (which is hopeless to give better score) gives slight performance improvement 
    so that it finishes within 5 minutes."""

    # Initialization.
    mat = [[-INF] * (len(seq2) + 1) for _ in range(len(seq1) + 1)]
    backtrackMat = [[0] * (len(seq2) + 1) for _ in range(len(seq1) + 1)]
    initialize_matrix(mat, backtrackMat, seq1, seq2, gap)

    # Limit coordinates for pruning.
    limit = [len(seq2) + 1] * (len(seq1) + 1)
    maxScore = -INF

    # Fill DP matrix.
    for i in range(1, len(seq1) + 1):
        if (i+1) % 100 == 0:
            print(i+1)
        j = 1
        while j < limit[i]:
            candidates = [mat[i-1][j-1] + [mismatch, match][seq1[i-1] == seq2[j-1]],
                            mat[i-1][j] + gap,
                            mat[i][j-1] + gap]

            score = max(candidates)
            # Fill DP matrix.
            mat[i][j] = score

            # Fill backtrack matrix.
            for k, candidate in enumerate(candidates):
                if candidate == score:
                    backtrackMat[i][j] += [DIAG, UP, LEFT][k]

            # Pruning.
            if score < maxScore - match * (len(seq2) - j):
                x, y = i + 1, j + 1
                while x < len(seq1) + 1 and y < len(seq2) + 1:
                    limit[x] = y
                    x += 1
                    y += 1

            # Replace max score if needed.
            if j == len(seq2) and score > maxScore:
                maxScore = score

            j += 1
    
    # Backtrack and get augmented sequences.
    augSeq1, augSeq2 = augmented_sequences(mat, backtrackMat, maxScore, seq1, seq2)

    return maxScore, augSeq1, augSeq2


def initialize(self):
    """Initializer for fitting alignment."""
    for i in range(len(self.seq1) + 1):
        self.mat[i][0] = 0  # Should be initialized to 0.
        self.backtrackMat[i][0] = self.DONE
    for j in range(len(self.seq2) + 1):
        self.mat[0][j] = 0  # Should be initialized to 0.
        self.backtrackMat[0][j] = self.DONE


def backtrack_starting_point(mat, maxScore, seq1, seq2):
    """Backtrack starting point for semiglobal alignment."""
    for x in range(len(seq1) + 1):
        if mat[x][len(seq2)] == maxScore:
            i, j = x, len(seq2)
            break

    return i, j


def augmented_sequences(mat, backtrackMat, maxScore, seq1, seq2):
    """Return augmented sequences representing optimal semiglobal alignment."""
    i, j = backtrack_starting_point(mat, maxScore, seq1, seq2)

    augmentedSeq1, augmentedSeq2 = [], []
    while not (i == 0 or j == 0):
        if (backtrackMat[i][j] >> 0) & 1 == 1:
            augmentedSeq1.append(seq1[i-1])
            augmentedSeq2.append(seq2[j-1])
            i -= 1
            j -= 1
        elif (backtrackMat[i][j] >> 1) & 1 == 1:
            augmentedSeq1.append(seq1[i-1])
            augmentedSeq2.append('-')
            i -= 1
        elif (backtrackMat[i][j] >> 2) & 1 == 1:
            augmentedSeq1.append('-')
            augmentedSeq2.append(seq2[j-1])
            j -= 1
        else:
            break

    return ''.join(augmentedSeq1[::-1]), ''.join(augmentedSeq2[::-1])





if __name__ == '__main__':
    # Load the data.
    seq2, seq1 = [seq for header, seq in Fasta('../../datasets/rosalind_OAP.txt')]
    score, augSeq1, augSeq2 = overlap_alignment(seq1, seq2, match=+1, mismatch=-2, gap=-2)
    # Print output
    with open('../../answers/rosalind_OAP_out.txt', 'w') as outFile:
        print(score, file=outFile)
        print(augSeq2, file=outFile)
        print(augSeq1, file=outFile)
