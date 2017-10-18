##################################################
# Open Reading Frames
#
# http://rosalind.info/problems/ORF/
# 
# Given: A DNA string s of length at most 1 kbp
#  in FASTA format.
# 
# Return: Every distinct candidate protein string
#  that can be translated from ORFs of s. Strings
#  can be returned in any order.
#
# AUTHOR : dohlee
##################################################

# Your imports here
from PROT import translate
from GC import Fasta
from REVC import reverse_complement as rev_comp

# Your codes here
def get_orfs(rna, shift, reverse_complement):
    """Return open reading frames of RNA sequence."""
    rna = [rna[shift:], rev_comp(rna, rna=True)[shift:]][reverse_complement]
    stopCodons = set(['UAA', 'UGA', 'UAG'])

    orfs, orfCodons, isInOrf = [], [], False
    for i in range(0, len(rna), 3):
        codon = rna[i:i+3]

        if not len(codon) == 3:
            break

        if codon == 'AUG':
            for c in orfCodons:
                c.append(codon)
            orfCodons.append([codon])
            isInOrf = True

        elif isInOrf and codon in stopCodons:
            for c in orfCodons:
                c.append(codon)
                orfs.append(''.join(c))
            orfCodons = []
            isInOrf = False

        elif isInOrf:
            for c in orfCodons:
                c.append(codon)

    return orfs

def candidate_protein(rna):
    """Return distinct candidate protein that can be made from
    the RNA, by examining all six open reading frames.
    """
    candidates = set()
    for reverseComplement in [False, True]:
        for shift in range(3):
            orfs = get_orfs(rna, shift=shift, reverse_complement=reverseComplement)

            candidates = candidates.union(set(translate(orf) for orf in orfs))

    return candidates


if __name__ == '__main__':
    # Load the data.
    rna = [s for h, s in Fasta('../../datasets/rosalind_ORF.txt')][0].replace('T', 'U')

    # Print output
    with open('../../answers/rosalind_ORF_out.txt', 'w') as outFile:
        for candidate in candidate_protein(rna):
            print(candidate, file=outFile)

