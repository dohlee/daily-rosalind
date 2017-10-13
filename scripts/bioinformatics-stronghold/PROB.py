##################################################
# Introduction to Random Strings
#
# http://rosalind.info/problems/PROB/
# 
# Given: A DNA string s of length at most 100 bp
#  and an array A containing at most 20 numbers
#  between 0 and 1.
# 
# Return: An array B having the same length as A
#  in which B[k] represents the common logarithm
#  of the probability that a random string constructed
#  with the GC-content found in A[k] will match
#  s exactly.
#
# AUTHOR : dohlee
##################################################

# Your imports here
from math import log10

# Your codes here
def log_probability_of_sequence(seq, gcContent):
	"""Given GC content, return the common logarithm of the probability of the sequence."""
	return sum(log10([(1 - gcContent) / 2, gcContent / 2][nuc in ['G', 'C']]) for nuc in seq)

if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_PROB.txt') as inFile:
        seq = inFile.readline().strip()
        gcContents = map(float, inFile.readline().split())

    # Print output
    with open('../../answers/rosalind_PROB_out.txt', 'w') as outFile:
        for gcContent in gcContents:
        	print('%.3f' % log_probability_of_sequence(seq, gcContent), end=' ', file=outFile)

