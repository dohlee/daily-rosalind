##################################################
# 2SUM
#
# http://rosalind.info/problems/2SUM/
# 
# Given: A positive integer k <= 20, a positive
#  integer n <= 10^4, and k arrays of size n containing
#  integers from -10^5 to 10^5.
# 
# Return: For each array A[1..n], output two different
#  indices 1 <= p < q <= n such that A[p] = -A[q]
#  if exist, and "-1" otherwise.
#
# AUTHOR : dohlee
##################################################

# Your imports here


# Your codes here
def two_sum(arr):
	"""Return a pair of numbers in array which sums to 0 if exists,
	otherwise return a pair of -1's.
	"""
	negated = set(-i for i in arr)
	for i, value in enumerate(arr):
		if value in negated:
			try:
				j = arr.index(-value, i+1)
			except ValueError:
				continue

			return (i+1, j+1)

	return (-1, -1)

if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_2SUM.txt') as inFile:
        k, n = map(int, inFile.readline().split())
        arrays = [list(map(int, line.split())) for line in inFile.readlines()]

    # Print output
    with open('../../answers/rosalind_2SUM_out.txt', 'w') as outFile:
        for array in arrays:
        	p, q = two_sum(array)
        	if p == -1:
        		print(-1, file=outFile)
        	else:
        		print(p, q, file=outFile)

