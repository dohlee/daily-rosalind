##################################################
# 2-Way Partition
#
# http://rosalind.info/problems/PAR/
# 
# Given: A positive integer n <= 10^5 and an array
#  A[1..n] of integers from -10^5 to 10^5.
# 
# Return: A permuted array B[1..n] such that it
#  is a permutation of A and there is an index 1
#  <= q <= n such that B[i] <= A[1] for all 1 <=
#  i <= q-1, B[q]=A[1], and B[i] > A[1] for all
#  q+1 <= i <= n.
#
# AUTHOR : dohlee
##################################################

# Your imports here


# Your codes here
def partition(arr):
	"""Partition array with the first element as a pivot."""
	pivot = arr[0]
	p, q = 1, len(arr) - 1

	while p < q:
		while arr[p] <= pivot: p += 1
		while arr[q] > pivot: q -= 1

		arr[p], arr[q] = arr[q], arr[p]

	arr[p], arr[q] = arr[q], arr[p]	

	# place pivot element in the middle.
	arr[0], arr[q] = arr[q], arr[0]
	return arr

if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_PAR.txt') as inFile:
        inFile.readline()
        arr = list(map(int, inFile.readline().split()))

    # Print output
    with open('../../answers/rosalind_PAR_out.txt', 'w') as outFile:
        print(' '.join(map(str, partition(arr))), file=outFile)

