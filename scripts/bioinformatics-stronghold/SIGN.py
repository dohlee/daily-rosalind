##################################################
# Enumerating Oriented Gene Orderings
#
# http://rosalind.info/problems/SIGN/
# 
# Given: A positive integer n <=q 6.
# 
# Return: The total number of signed permutations
#  of length n, followed by a list of all such permutations
#  (you may list the signed permutations in any
#  order).
#
# AUTHOR : dohlee
##################################################

# Your imports here
from itertools import permutations

# Your codes here
def signed_permutation(n):
    """Return signed permutation of length n."""
    return [x for x in permutations([i for i in range(-n, n+1) if i != 0], n) if set(range(1, n+1)) == set(map(abs, x))]

if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_SIGN.txt') as inFile:
        n = int(inFile.readline())

    # Print output
    with open('../../answers/rosalind_SIGN_out.txt', 'w') as outFile:
        signedPermutation = signed_permutation(n)
        print(len(signedPermutation), file=outFile)
        for perm in signedPermutation:
            print(' '.join(map(str, perm)), file=outFile)

