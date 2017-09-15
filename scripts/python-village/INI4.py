##################################################
# Conditions and Loops
#
# http://rosalind.info/problems/INI4/
# 
# Given: Two positive integers a and b (a < b <
#  10000).
# 
# Return: The sum of all odd integers from a through
#  b, inclusively.
#
# AUTHOR : dohlee
##################################################

# Your imports here


# Your codes here
def sum_odd_numbers(a, b):
	return sum(i for i in range(a, b+1) if i % 2 == 1)




if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_INI4.txt') as inFile:
        a, b = map(int, inFile.readline().strip().split())

    # Print output
    with open('../../answers/rosalind_INI4_out.txt', 'w') as outFile:
        print(sum_odd_numbers(a, b), file=outFile)

