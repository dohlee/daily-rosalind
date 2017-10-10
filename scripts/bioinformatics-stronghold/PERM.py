##################################################
# Enumerating Gene Orders
#
# http://rosalind.info/problems/PERM/
# 
# Given: A positive integer n <=q 7.
# 
# Return: The total number of permutations of length
#  n, followed by a list of all such permutations
#  (in any order).
#
# AUTHOR : dohlee
##################################################

# Your imports here


# Your codes here
def permutation_helper(lst):
    """Helper function for recursive call."""
    if len(lst) == 1:
        return [lst]

    p = []
    for i in range(len(lst)):
        p.extend([[lst[i]] + perm for perm in permutation_helper(lst[:i] + lst[i+1:])])
    return p

def permutation(l):
    """Return the list of all permutations of length n."""
    lst = [x for x in range(1, l+1)]
    return permutation_helper(lst)

if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_PERM.txt') as inFile:
        l = int(inFile.readline())

    # Print output
    with open('../../answers/rosalind_PERM_out.txt', 'w') as outFile:
        perm = permutation(l)
        print(len(perm), file=outFile)
        for p in perm:
            print(' '.join(map(str, p)), file=outFile)

