##################################################
# Read Filtration by Quality
#
# http://rosalind.info/problems/FILT/
# 
# Given: A quality threshold value q, percentage
#  of bases p, and set of FASTQ entries. 
# 
# Return: Number of reads in filtered FASTQ entries
#
# AUTHOR : dohlee
##################################################

# Your imports here
from PHRE import Fastq_fp

# Your codes here
def filter(qualities, threshold, percentage):
	"""Return True if more than percentage(%) of bases
	have better or equal quality than specified threshold.
	"""
	return sum((ord(c) - 33) >= threshold for c in qualities) / len(qualities) >= percentage / 100

if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_FILT.txt') as inFile:
        threshold, percentage = map(int, inFile.readline().split())
        c = 0
        for header, seq, comment, quality in Fastq_fp(inFile):
        	if filter(quality, threshold, percentage):
        		c += 1

    # Print output
    with open('../../answers/rosalind_FILT_out.txt', 'w') as outFile:
        print(c, file=outFile)

