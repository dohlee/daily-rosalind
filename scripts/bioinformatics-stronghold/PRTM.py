##################################################
# Calculating Protein Mass
#
# http://rosalind.info/problems/PRTM/
# 
# Given: A protein string P of length at most 1000
#  aa.
# 
# Return: The total weight of P.  Consult the monoisotopic
#  mass table.
#
# AUTHOR : dohlee
##################################################

# Your imports here


# Your codes here
massTable = """
A   71.03711
C   103.00919
D   115.02694
E   129.04259
F   147.06841
G   57.02146
H   137.05891
I   113.08406
K   128.09496
L   113.08406
M   131.04049
N   114.04293
P   97.05276
Q   128.05858
R   156.10111
S   87.03203
T   101.04768
V   99.06841
W   186.07931
Y   163.06333
""".split()
massTable = dict(zip(massTable[::2],map(float,massTable[1::2])))

def weight(peptide):
	return sum(massTable[aa] for aa in peptide)

if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_PRTM.txt') as inFile:
        peptide = inFile.readline().strip()

    # Print output
    with open('../../answers/rosalind_PRTM_out.txt', 'w') as outFile:
        print('%.3f' % weight(peptide), file=outFile)

