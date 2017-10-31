##################################################
# Find Patterns Forming Clumps in a String
#
# http://rosalind.info/problems/BA1E/
# 
# Given: A string Genome, and integers k, L, and t.
# 
# Return: All distinct k-mers forming (L, t)-clumps
#  in Genome.
#
# AUTHOR : dohlee
##################################################

# Your imports here
from collections import Counter

# Your codes here
def enumerate_kmers(string, k):
    """Generate all k-mers within a string."""
    for i in range(0, len(string) - k + 1):
        yield string[i:i+k]


def add_clump_forming_kmers(counts, clumpFormingKmers):
    for kmer in counts:
        if counts[kmer] >= t:
            clumpFormingKmers.add(kmer)

    return clumpFormingKmers


def clump_forming_kmers(string, k, l, t):
    """Return k-mers in string which appear at least t times
    within the window of length l.
    """
    clumpFormingKmers = set()
    # Initial counts of k-mers within length l window starting from the first
    # chracter of the string.
    counts = Counter(enumerate_kmers(string[:l], k))
    clumpFormingKmers = add_clump_forming_kmers(counts, clumpFormingKmers)

    for i in range(1, len(string) - l + 1):
        counts[string[i-1:i-1+k]] -= 1
        counts[string[i+l-k:i+l]] += 1
        clumpFormingKmers = add_clump_forming_kmers(counts, clumpFormingKmers)

    return list(clumpFormingKmers)

if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_BA1E.txt') as inFile:
        string = inFile.readline().strip()
        k, l, t = map(int, inFile.readline().split())

    # Print output
    with open('../../answers/rosalind_BA1E_out.txt', 'w') as outFile:
        print(' '.join(clump_forming_kmers(string, k, l, t)), file=outFile)

