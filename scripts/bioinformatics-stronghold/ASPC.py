##################################################
# Introduction to Alternative Splicing
#
# http://rosalind.info/problems/ASPC/
# 
# Given: Positive integers n and m with 0 <=q m
#  <=q n <=q 2000.
# 
# Return: The sum of combinations C(n, k) for all
#  k satisfying m <=q k <=q n, modulo 1,000,000.
#   In shorthand, \sum_(k=m)^(n)(\binom(n)(k)).
#
# AUTHOR : dohlee
##################################################

# Your imports here
from math import factorial

# Your codes here
def combination(n, r):
	"""Return nCr."""
	return factorial(n) // factorial(n-r) // factorial(r)

if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_ASPC.txt') as inFile:
        n, k = map(int, inFile.readline().split())

    # Print output
    with open('../../answers/rosalind_ASPC_out.txt', 'w') as outFile:
        print(sum(combination(n, i) for i in range(k, n+1)) % 1000000)

