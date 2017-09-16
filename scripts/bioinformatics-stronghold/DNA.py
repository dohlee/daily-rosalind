##################################################
# Counting DNA Nucleotides
#
# http://rosalind.info/problems/DNA/
# 
# Given: A DNA string s of length at most 1000 nt.
# 
# Return: Four integers (separated by spaces) counting
#  the respective number of times that the symbols
#  'A', 'C', 'G', and 'T' occur in s.
#
# AUTHOR : dohlee
##################################################

# Your imports here
from collections import Counter

# Your codes here






if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_DNA.txt') as inFile:
        counter = Counter(inFile.readline().strip())

    # Print output
    with open('../../answers/rosalind_DNA_out.txt', 'w') as outFile:
        print(counter['A'], counter['C'], counter['G'], counter['T'], file=outFile)

