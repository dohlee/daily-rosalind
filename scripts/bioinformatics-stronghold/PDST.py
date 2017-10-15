##################################################
# Creating a Distance Matrix
#
# http://rosalind.info/problems/PDST/
# 
# Given: A collection of n (n <=q 10) DNA strings
#  s_1, ..., s_n of equal length (at most 1 kbp).
#  Strings are given in FASTA format.
# 
# Return: The matrix D corresponding to the p-distance
#  d_p on the given strings.  As always, note that
#  your answer is allowed an absolute error of 0.001.
#
# AUTHOR : dohlee
##################################################

# Your imports here
from GC import Fasta

# Your codes here
def p_distance(s1, s2):
	"""Return the proportion of corresponding symbols that differ
	between s1 and s2.
	"""
	assert len(s1) == len(s2), "The length of two strings should be equal."
	return sum(c1 != c2 for c1, c2 in zip(s1, s2)) / len(s1)

def distance_matrix(seqs):
	"""Given the list of genetic strings, return the distance matrix
	of the strings.
	"""
	seqCount = len(seqs)
	distanceMatrix = [[0] * seqCount for _ in range(seqCount)]
	for i in range(seqCount):
		for j in range(i+1, seqCount):
			distanceMatrix[i][j] = distanceMatrix[j][i] = p_distance(seqs[i], seqs[j])

	return distanceMatrix

if __name__ == '__main__':
    # Load the data.
    seqs = [seq for header, seq in Fasta('../../datasets/rosalind_PDST.txt')]

    # Print output
    with open('../../answers/rosalind_PDST_out.txt', 'w') as outFile:
        distanceMatrix = distance_matrix(seqs)
        for row in distanceMatrix:
        	print(' '.join(map(lambda x: '%.5f' % x, row)), file=outFile)

