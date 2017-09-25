##################################################
# Merge Two Sorted Arrays
#
# http://rosalind.info/problems/MER/
# 
# Given: A positive integer n <= 10^5 and a sorted
#  array A[1..n] of integers from -10^5 to 10^5,
#  a positive integer m <= 10^5 and a sorted array
#  B[1..m] of integers from -10^5 to 10^5.
# 
# Return: A sorted array C[1..n+m] containing all
#  the elements of A and B.
#
# AUTHOR : dohlee
##################################################

# Your imports here


# Your codes here
def merge(arr1, arr2):
    i, j = 0, 0
    merged = []
    while i != len(arr1) and j != len(arr2):
        if arr1[i] <= arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    if i == len(arr1):
        merged.extend(arr2[j:])
    else:
        merged.extend(arr1[i:])

    return merged

if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_MER.txt') as inFile:
        n = int(inFile.readline())
        arr1 = list(map(int, inFile.readline().split()))
        m = int(inFile.readline())
        arr2 = list(map(int, inFile.readline().split()))

    # Print output
    with open('../../answers/rosalind_MER_out.txt', 'w') as outFile:
        print(' '.join(map(str, merge(arr1, arr2))), file=outFile)

