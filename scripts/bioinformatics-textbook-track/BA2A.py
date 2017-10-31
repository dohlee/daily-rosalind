##################################################
# Implement MotifEnumeration
#
# http://rosalind.info/problems/BA2A/
# 
# Given: Integers k and d, followed by a collection
#  of strings Dna.
# 
# Return: All (k, d)-motifs in Dna.
#
# AUTHOR : dohlee
##################################################

# Your imports here
from BA1E import enumerate_kmers
from BA1N import neighbors
from collections import Counter

# Your codes here
def find_motif(dnas, k, d):
    """Return the list of (k, d)-motifs in DNAs."""
    # Hash all occurences of k-mers (including d-neighbors) in each DNA string.
    motifCounts = [Counter() for _ in range(len(dnas))]
    for count, dna in zip(motifCounts, dnas):
        for i, kmer in enumerate_kmers(dna, k):
            for neighbor in neighbors(kmer, d):
                count[neighbor] += 1

    # Find motif that occurs in all DNAs.
    motives = []
    for motif in motifCounts[0]:
        if all(count[motif] > 0 for count in motifCounts[1:]):
            motives.append(motif)

    return motives

if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_BA2A.txt') as inFile:
        k, d = map(int, inFile.readline().split())
        dnas = [line.strip() for line in inFile.readlines()]

    # Print output
    with open('../../answers/rosalind_BA2A_out.txt', 'w') as outFile:
        print(' '.join(find_motif(dnas, k, d)), file=outFile)

