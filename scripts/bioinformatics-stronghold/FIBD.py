##################################################
# Mortal Fibonacci Rabbits
#
# http://rosalind.info/problems/FIBD/
# 
# Given: Positive integers n <=q 100 and m <=q 20.
# 
# Return: The total number of pairs of rabbits that
#  will remain after the n-th month if all rabbits
#  live for m months.
#
# AUTHOR : dohlee
##################################################

# Your imports here


# Your codes here
def fibd(n, m):
	"""Return the total number of rabbits that will remain
	after the n-th month if all rabbits live for m months.
	"""
	mat = [[0] * m for _ in range(n)]
	mat[0][0] = 1

	for month in range(1, n):
		mat[month][0] = sum(mat[month-1][1:])
		for j in range(m-1):
			mat[month][j+1] = mat[month-1][j]	

	return sum(mat[n-1])

if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_FIBD.txt') as inFile:
    	n, m = map(int, inFile.readline().split())

    # Print output
    with open('../../answers/rosalind_FIBD_out.txt', 'w') as outFile:
        print(fibd(n, m), file=outFile)

