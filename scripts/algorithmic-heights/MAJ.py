##################################################
# Majority Element
#
# http://rosalind.info/problems/MAJ/
# 
# Given: A positive integer k <= 20, a positive
#  integer n <= 10^4, and k arrays of size n containing
#  positive integers not exceeding 10^5.
# 
# Return: For each array, output an element of this
#  array occurring strictly more than n/2 times
#  if such element exists, and "-1" otherwise.
#
# AUTHOR : dohlee
##################################################

# Your imports here


# Your codes here
def majority_element(arr):
	"""Find majority element through Boyer-Moore majority voting algorithm.
	Return the majority element if exists, otherwise -1.
	"""
	candidate, count = arr[0], 0
	for v in arr:
		count += [-1, 1][v == candidate]
		if count == 0:
			candidate, count = v, 1 

	return [-1, candidate][arr.count(candidate) > len(arr) / 2.0]

if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_MAJ.txt') as inFile:
        arrayCount, size = map(int, inFile.readline().split())
        arrays = [list(map(int, line.split())) for line in inFile.readlines()]

    # Print output
    with open('../../answers/rosalind_MAJ_out.txt', 'w') as outFile:
        print(' '.join(map(str, [majority_element(arr) for arr in arrays])), file=outFile)

