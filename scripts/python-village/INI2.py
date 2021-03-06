##################################################
# Variables and Some Arithmetic
#
# http://rosalind.info/problems/INI2/
# 
# Given: Two positive integers a and b, each less
#  than 1000.
# 
# Return: The integer corresponding to the square
#  of the hypotenuse of the right triangle whose
#  legs have lengths a and b.
#
# AUTHOR : dohlee
##################################################

# Your imports here


# Your codes here






if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_INI2.txt') as inFile:
        a, b = map(int, inFile.readline().strip().split())

    # Print output
    with open('../../answers/rosalind_INI2_out.txt', 'w') as outFile:
        print(a**2 + b**2, file=outFile)

