##################################################
# Compute Limb Lengths in a Tree
#
# http://rosalind.info/problems/BA7B/
# 
# Given: An integer n, followed by an integer j
#  between 0 and n - 1, followed by a space-separated
#  additive distance matrix D (whose elements are
#  integers).
# 
# Return: The limb length of the leaf in Tree(D)
#  corresponding to row j of this distance matrix
#  (use 0-based indexing).
#
# AUTHOR : dohlee
##################################################

# Your imports here


# Your codes here
def limb_length(distanceMatrix, n, j):
	return min(distanceMatrix[i][j] + distanceMatrix[k][j] - distanceMatrix[i][k] \
		for i in range(n) for k in range(n) if i != j and k != j) // 2






if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_BA7B.txt') as inFile:
        n = int(inFile.readline())
        j = int(inFile.readline())
        distanceMatrix = [list(map(int, inFile.readline().split())) for _ in range(n)]

    # Print output
    with open('../../answers/rosalind_BA7B_out.txt', 'w') as outFile:
        print(limb_length(distanceMatrix, n, j), file=outFile)

