##################################################
# Perfect Matchings and RNA Secondary Structures
#
# http://rosalind.info/problems/PMCH/
# 
# Given: An RNA string s of length at most 80 bp
#  having the same number of occurrences of 'A'
#  as 'U' and the same number of occurrences of
#  'C' as 'G'.
# 
# Return: The total possible number of perfect matchings
#  of basepair edges in the bonding graph of s.
#
# AUTHOR : dohlee
##################################################

# Your imports here
from GC import Fasta

# Your codes here
def factorial(n):
	"""Return n!."""
	if n == 1:
		return 1
	return n * factorial(n-1)

def count_perfect_matchings(seq):
	"""Return the number of perfect matchings in the sequence."""
	return factorial(seq.count('A')) * factorial(seq.count('G'))

if __name__ == '__main__':
    # Load the data.
    seq = [seq for header, seq in Fasta('../../datasets/rosalind_PMCH.txt')][0]

    # Print output
    with open('../../answers/rosalind_PMCH_out.txt', 'w') as outFile:
        print(count_perfect_matchings(seq), file=outFile)

