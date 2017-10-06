##################################################
# Merge Sort
#
# http://rosalind.info/problems/MS/
# 
# Given: A positive integer n <= 10^5 and an array
#  A[1..n] of integers from -10^5 to 10^5.
# 
# Return: A sorted array A[1..n].
#
# AUTHOR : dohlee
##################################################

# Your imports here
from MER import merge

# Your codes here
def merge_sort(arr):
    """Mergesort arr."""
    if len(arr) == 1:
        return arr

    mid = len(arr) // 2
    arr1 = merge_sort(arr[:mid])
    arr2 = merge_sort(arr[mid:])

    return merge(arr1, arr2)

if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_MS.txt') as inFile:
        inFile.readline()
        arr = list(map(int, inFile.readline().split()))

    # Print output
    with open('../../answers/rosalind_MS_out.txt', 'w') as outFile:
        print(' '.join(map(str, merge_sort(arr))), file=outFile)

