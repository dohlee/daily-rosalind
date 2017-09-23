##################################################
# Fibonacci Numbers
#
# http://rosalind.info/problems/FIBO/
# 
# Given: A positive integer n <= 25.
# 
# Return: The value of F_n.
#
# AUTHOR : dohlee
##################################################

# Your imports here


# Your codes here
def fib(n):
	"""Return nth fibonacci number."""
	if n == 0:
		return 0
	elif n == 1:
		return 1

	a, b = 0, 1
	for _ in range(n-1):
		a, b = b, a + b

	return b

if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_FIBO.txt') as inFile:
        n = int(inFile.readline())

    # Print output
    with open('../../answers/rosalind_FIBO_out.txt', 'w') as outFile:
        print(fib(n), file=outFile)

