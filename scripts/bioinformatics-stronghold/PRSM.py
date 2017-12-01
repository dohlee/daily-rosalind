##################################################
# Matching a Spectrum to a Protein
#
# http://rosalind.info/problems/PRSM/
# 
# Given: A positive integer n followed by a collection
#  of n protein strings s_1, s_2, ..., s_n and a
#  multiset R of positive numbers (corresponding
#  to the complete spectrum of some unknown protein
#  string).
# 
# Return: The maximum multiplicity of R \ominus
#  S[s_k] taken over all strings s_k, followed by
#  the string s_k for which this maximum multiplicity
#  occurs (you may output any such value if multiple
#  solutions exist).
#
# AUTHOR : dohlee
##################################################

# Your imports here
from PRTM import massTable
from collections import Counter

# Your codes here
def weight(peptide):
	"""Return the weight of the peptide."""
	return sum(massTable[aa] for aa in peptide)

def complete_spectrum(peptide):
	"""Return the complete spectrum of the peptide.
	Complete spectrum is a multiset of weights of all 
	prefixes and suffixes occurring in peptide.
	"""
	spectrum = []
	for i in range(len(peptide)):
		spectrum.append(weight(peptide[:i]))
		spectrum.append(weight(peptide[i:]))
	
	return spectrum

if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_PRSM.txt') as inFile:
        n = int(inFile.readline())
        peptides = [inFile.readline().strip() for _ in range(n)]
        R = list(map(float, inFile.readlines()))

    # Print output
    with open('../../answers/rosalind_PRSM_out.txt', 'w') as outFile:
    	maxMultiplicity = 0
    	for peptide in peptides:
    		spectrum = complete_spectrum(peptide)
    		minkowskiDifference = Counter([round(abs(b - a), 5) for b in R for a in spectrum])

    		multiplicity = minkowskiDifference.most_common(1)[0][1]
    		if multiplicity >= maxMultiplicity:
    			maxMultiplicity = multiplicity
    			answer = peptide

    	print(maxMultiplicity, file=outFile)
    	print(answer, file=outFile)
