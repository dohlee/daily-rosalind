##################################################
# Inferring Protein from Spectrum
#
# http://rosalind.info/problems/SPEC/
# 
# Given: A list L of n (n <=q 100) positive real
#  numbers.
# 
# Return: A protein string of length n-1 whose prefix
#  spectrum is equal to L (if multiple solutions
#  exist, you may output any one of them).  Consult
#  the monoisotopic mass table.
#
# AUTHOR : dohlee
##################################################

# Your imports here
from PRTM import massTable

# Your codes here
massToAminoacid = dict((mass, aa) for aa, mass in massTable.items())

def get_amino_acid_given_mass(mass):
	minDiff = 12345679
	for key in massToAminoacid:
		diff = abs(mass - key)
		if diff < minDiff:
			minDiff = diff 
			aa = massToAminoacid[key]

	return aa

def infer_protein_from_spectrum(prefixSpectrum):
	"""Given prefix spectrum of a protein string,
	return one of the possible protein string which can
	generate the given prefix spectrum.
	"""
	masses = [b - a for a, b in zip(prefixSpectrum[:-1], prefixSpectrum[1:])]
	return ''.join([get_amino_acid_given_mass(mass) for mass in masses])

if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_SPEC.txt') as inFile:
        prefixSpectrum = list(map(float, inFile.readlines()))

    # Print output
    with open('../../answers/rosalind_SPEC_out.txt', 'w') as outFile:
        print(infer_protein_from_spectrum(prefixSpectrum), file=outFile)

