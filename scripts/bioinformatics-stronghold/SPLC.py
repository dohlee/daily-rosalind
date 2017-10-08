##################################################
# RNA Splicing
#
# http://rosalind.info/problems/SPLC/
# 
# Given: A DNA string s (of length at most 1 kbp)
#  and a collection of substrings of s acting as
#  introns.  All strings are given in FASTA format.
# 
# Return: A protein string resulting from transcribing
#  and translating the exons of s. (Note: Only one
#  solution will exist for the dataset provided.)
#
# AUTHOR : dohlee
##################################################

# Your imports here
from PROT import translate
from GC import Fasta

# Your codes here
def splice_translate(seq, introns):
    """Translate sequence after splicing introns out."""
    # map each intron to the sequence to get their coordinates.
    intronCoordinates = sorted([(seq.index(intron), seq.index(intron) + len(intron)) for intron in introns], \
                                key=lambda x: x[0])
    intronCoordinates = [(0, 0)] + intronCoordinates + [(len(seq), len(seq))]

    # from coordinates of introns, get coordinates of exons.
    exonCoordinates = [(x[1], y[0]) for x, y in zip(intronCoordinates[:-1], intronCoordinates[1:])]

    # convert sequence into rna and return translated amino acid sequence.
    rna = ''.join([seq[start:end] for start, end in exonCoordinates]).replace('T', 'U')
    return translate(rna)

if __name__ == '__main__':
    # Load the data.
    seqs = [seq for header, seq in Fasta('../../datasets/rosalind_SPLC.txt')]
    seq = seqs[0]
    introns = seqs[1:]

    # Print output
    with open('../../answers/rosalind_SPLC_out.txt', 'w') as outFile:
        print(splice_translate(seq, introns), file=outFile)

