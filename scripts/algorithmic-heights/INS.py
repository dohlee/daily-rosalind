##################################################
# Insertion Sort
#
# http://rosalind.info/problems/INS/
# 
# Given: A positive integer n <= 10^3 and an array
#  A[1..n] of integers.
# 
# Return: The number of swaps performed by insertion
#  sort algorithm on A[1..n].
#
# AUTHOR : dohlee
##################################################

# Your imports here


# Your codes here
def insertion_sort_swap_count(arr):
	"""Return the number of swaps when doing insertion sort."""
	swapCount = 0

	for i in range(1, len(arr)):
		k = i
		# move down with swapping until the right position is found.
		while k > 0 and arr[k] < arr[k-1]:
			arr[k], arr[k-1] = arr[k-1], arr[k]
			swapCount += 1
			k -= 1

	return swapCount

if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_INS.txt') as inFile:
        n = int(inFile.readline())
        arr = list(map(int, inFile.readline().split()))

    # Print output
    with open('../../answers/rosalind_INS_out.txt', 'w') as outFile:
        print(insertion_sort_swap_count(arr), file=outFile)

