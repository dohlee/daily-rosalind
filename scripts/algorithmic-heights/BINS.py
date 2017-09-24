##################################################
# Binary Search
#
# http://rosalind.info/problems/BINS/
# 
# Given: Two positive integers n <=q 10^5 and m
#  <=q 10^5, a sorted array A[1..n] of integers
#  from -10^5 to 10^5 and a list of m integers -10^5
#  <=q k_1, k_2, \dots, k_m <=q 10^5.
# 
# Return: For each k_i, output an index 1 <= j <=
#  n s.t. A[j]=k_i or "-1" if there is no such index.
#
# AUTHOR : dohlee
##################################################

# Your imports here


# Your codes here
def binary_search(arr, k):
	"""If k is in arr, return the index of k in arr, otherwise return -1."""
	return binary_search_helper(arr, k, 0, len(arr))

def binary_search_helper(arr, k, n, m):
	"""Helper function for binary_search"""
	# if no element is left in the range, return -1.
	if n >= m:
		return -1

	# if only one element is left,
	elif n == m-1:
		# if the element is k, return the index (1-based).
		if arr[n] == k:
			return n+1
		# else return -1.
		else:
			return -1

	# if two or more elements are left, set midpoint and call the function recursively.
	mid = (n + m) // 2 
	if arr[mid] > k:
		return binary_search_helper(arr, k, n, mid)
	else:
		return binary_search_helper(arr, k, mid, m)

if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_BINS.txt') as inFile:
        n = int(inFile.readline())
        m = int(inFile.readline())
        arr = list(map(int, inFile.readline().split()))
        ks = list(map(int, inFile.readline().split()))

    # Print output
    with open('../../answers/rosalind_BINS_out.txt', 'w') as outFile:
        print(' '.join(map(str, [binary_search(arr, k) for k in ks])), file=outFile)

