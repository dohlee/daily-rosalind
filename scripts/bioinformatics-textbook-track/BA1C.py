##################################################
# Find the Reverse Complement of a String
#
# http://rosalind.info/problems/BA1C/
# 
# Given: A DNA string Pattern.
# 
# Return: Pattern, the reverse complement of Pattern.
#
# AUTHOR : dohlee
##################################################

# Your imports here


# Your codes here
# Define complementing bases.
COMPLEMENT_TABLE = str.maketrans('ATGC', 'TACG')

def reverse_complement(seq):
	"""Return the reverse complement of seq."""
	return seq[::-1].translate(COMPLEMENT_TABLE)

if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_BA1C.txt') as inFile:
        seq = inFile.readline().strip()

    # Print output
    with open('../../answers/rosalind_BA1C_out.txt', 'w') as outFile:
        print(reverse_complement(seq), file=outFile)

