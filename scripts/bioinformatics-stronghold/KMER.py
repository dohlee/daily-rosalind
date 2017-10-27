##################################################
# k-Mer Composition
#
# http://rosalind.info/problems/KMER/
# 
# Given: A DNA string s in FASTA format (having
#  length at most 100 kbp).
# 
# Return: The 4-mer composition of s.
#
# AUTHOR : dohlee
##################################################

# Your imports here
from LEXF import lexicographic_kmers
from GC import Fasta
from collections import Counter

# Your codes here

if __name__ == '__main__':
    # Load the data.
    seq = [s for h, s in Fasta('../../datasets/rosalind_KMER.txt')][0]

    # Print output
    with open('../../answers/rosalind_KMER_out.txt', 'w') as outFile:
        counter = Counter([seq[i:i+4] for i in range(0, len(seq) - 3)])
        print(' '.join(map(str, [counter[kmer] for kmer in lexicographic_kmers('ATGC', k=4)])), file=outFile)

