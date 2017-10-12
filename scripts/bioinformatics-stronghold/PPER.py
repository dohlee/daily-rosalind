##################################################
# Partial Permutations
#
# http://rosalind.info/problems/PPER/
# 
# Given: Positive integers n and k such that 100
#  >= n > 0 and 10 >= k > 0.
# 
# Return: The total number of partial permutations
#  P(n, k), modulo 1,000,000.
#
# AUTHOR : dohlee
##################################################

# Your imports here
from functools import reduce
import operator

# Your codes here
def prod(iterable):
	"""Return the product of elements in interable."""
	return reduce(operator.mul, iterable, 1)
	
def partial_permutation(n, r):
	"""Return nPr."""
	return prod(range(n, n-r, -1))

if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_PPER.txt') as inFile:
        n, r = map(int, inFile.readline().split())

    # Print output
    with open('../../answers/rosalind_PPER_out.txt', 'w') as outFile:
        print(partial_permutation(n, r) % 1000000, file=outFile)

