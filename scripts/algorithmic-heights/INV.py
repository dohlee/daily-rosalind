##################################################
# Counting Inversions
#
# http://rosalind.info/problems/INV/
# 
# Given: A positive integer n <= 10^5 and an array
#  A[1..n] of integers from -10^5 to 10^5.
# 
# Return: The number of inversions in A.
#
# AUTHOR : dohlee
##################################################

# Your imports here


# Your codes here
def merge(arr1, arr2):
    """Merge two arrays, also count the number of inversions 
    while merging.
    """
    i, j, inversionCount = 0, 0, 0
    merged = []
    # compare the smallest value from each array,
    # then append the smaller one to merged array.
    while i != len(arr1) and j != len(arr2):
        if arr1[i] <= arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            # remaining elements in arr1 will cause inversions.
            inversionCount += (len(arr1) - i)
            j += 1

    # extend the remaining array.
    if i == len(arr1):
        merged.extend(arr2[j:])
    else:
        merged.extend(arr1[i:])

    return merged, inversionCount

def count_inversions_helper(arr):
    """Helper function for recursive call."""
    if len(arr) == 1:
        return arr, 0

    mid = len(arr) // 2
    arr1, leftInversionCount = count_inversions_helper(arr[:mid])
    arr2, rightInversionCount = count_inversions_helper(arr[mid:])
    merged, inversionCount = merge(arr1, arr2)

    return merged, leftInversionCount + rightInversionCount + inversionCount
    
def count_inversions(arr):
    """Return the number of inversions in the array."""
    _, inversionCount = count_inversions_helper(arr)
    return inversionCount

if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_INV.txt') as inFile:
        inFile.readline()
        arr = list(map(int, inFile.readline().split()))

    # Print output
    with open('../../answers/rosalind_INV_out.txt', 'w') as outFile:
        print(count_inversions(arr), file=outFile)

