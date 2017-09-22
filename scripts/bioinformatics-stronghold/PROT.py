##################################################
# Translating RNA into Protein
#
# http://rosalind.info/problems/PROT/
# 
# Given: An RNA string s corresponding to a strand
#  of mRNA (of length at most 10 kbp).
# 
# Return: The protein string encoded by s.
#
# AUTHOR : dohlee
##################################################

# Your imports here


# Your codes here

# this elegant snippet to make codon table is from Ben Usman's solution.
tokens = """UUU F      CUU L      AUU I      GUU V
UUC F      CUC L      AUC I      GUC V
UUA L      CUA L      AUA I      GUA V
UUG L      CUG L      AUG M      GUG V
UCU S      CCU P      ACU T      GCU A
UCC S      CCC P      ACC T      GCC A
UCA S      CCA P      ACA T      GCA A
UCG S      CCG P      ACG T      GCG A
UAU Y      CAU H      AAU N      GAU D
UAC Y      CAC H      AAC N      GAC D
UAA Stop   CAA Q      AAA K      GAA E
UAG Stop   CAG Q      AAG K      GAG E
UGU C      CGU R      AGU S      GGU G
UGC C      CGC R      AGC S      GGC G
UGA Stop   CGA R      AGA R      GGA G
UGG W      CGG R      AGG R      GGG G""".split()

# worth noting this.
CODON_TABLE = dict(zip(tokens[0::2], tokens[1::2]))

def translate(rna):
	aas = []
	# read sequence three by three.
	for i in range(0, len(rna), 3):
		codon = rna[i:i+3]
		# if we met stop codon, immediately stop translating.
		if CODON_TABLE[codon] == 'Stop':
			break
		# append new amino acids to aa	
		aas.append(CODON_TABLE[codon])

	return ''.join(aas)

if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_PROT.txt') as inFile:
        rna = inFile.readline().strip()

    # Print output
    with open('../../answers/rosalind_PROT_out.txt', 'w') as outFile:
        print(translate(rna), file=outFile)

