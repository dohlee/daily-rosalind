##################################################
# Complementing a Strand of DNA
#
# http://rosalind.info/problems/REVC/
# 
# Given: A DNA string s of length at most 1000 bp.
# 
# Return: The reverse complement s^(\textrm(c))
#  of s.
#
# AUTHOR : dohlee
##################################################

# Your imports here


# Your codes here
COMPLEMENT_TABLE_DNA = str.maketrans('ATGC', 'TACG')
COMPLEMENT_TABLE_RNA = str.maketrans('AUGC', 'UACG')

def reverse_complement(string, rna=False):
	if rna:
		return string[::-1].translate(COMPLEMENT_TABLE_RNA)
	else:
		return string[::-1].translate(COMPLEMENT_TABLE_DNA)

if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_REVC.txt') as inFile:
        string = inFile.readline().strip()

    # Print output
    with open('../../answers/rosalind_REVC_out.txt', 'w') as outFile:
        print(reverse_complement(string), file=outFile)

