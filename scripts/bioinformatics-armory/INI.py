##################################################
# Introduction to the Bioinformatics Armory
#
# http://rosalind.info/problems/INI/
# 
# Given: A DNA string s of length at most 1000 bp.
# 
# Return: Four integers (separated by spaces) representing
#  the respective number of times that the symbols
#  'A', 'C', 'G', and 'T' occur in s. Note: You
#  must provide your answer in the format shown
#  in the sample output below.
#
# AUTHOR : dohlee
##################################################

# Your imports here
from Bio.Seq import Seq

# Your codes here
def base_composition(dna):
	"""Return the base composition ('A', 'C', 'G', 'T') of dna."""
	seq = Seq(dna)
	return seq.count('A'), seq.count('C'), seq.count('G'), seq.count('T')

if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_INI.txt') as inFile:
        dna = inFile.readline().strip()

    # Print output
    with open('../../answers/rosalind_INI_out.txt', 'w') as outFile:
        print(' '.join(map(str, base_composition(dna))), file=outFile)

