##################################################
# Find All Approximate Occurrences of a Collection of Patterns in a String
#
# http://rosalind.info/problems/BA9O/
# 
# Given: A string Text, a collection of strings
#  Patterns, and an integer d.
# 
# Return: All positions in Text where a string from
#  Patterns appears as a substring with at most
#  d mismatches.
#
# AUTHOR : dohlee
##################################################

# Your imports here
from BA1H import find_approximate

# Your codes here
if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_BA9O.txt') as inFile:
        text = inFile.readline().strip()
        patterns = inFile.readline().strip().split()
        d = int(inFile.readline())

    # Print output
    with open('../../answers/rosalind_BA9O_out.txt', 'w') as outFile:
        positions = []
        for pattern in patterns:
            positions.extend(find_approximate(text, pattern, d))

        print(' '.join(map(str, list(sorted(positions)))), file=outFile)

