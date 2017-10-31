##################################################
# Find Frequent Words with Mismatches and Reverse Complements
#
# http://rosalind.info/problems/BA1J/
# 
# Given: A DNA string Text as well as integers k
#  and d.
# 
# Return: All k-mers Pattern maximizing the sum
#  Countd(Text, Pattern) + Countd(Text, Pattern)
#  over all possible k-mers.
#
# AUTHOR : dohlee
##################################################

# Your imports here
from BA1E import enumerate_kmers
from BA1N import neighbors
from collections import Counter

# Your codes here
COMPLEMENT_TABLE_DNA = str.maketrans('ATGC', 'TACG')
COMPLEMENT_TABLE_RNA = str.maketrans('AUGC', 'UACG')

def reverse_complement(string, rna=False):
    if rna:
        return string[::-1].translate(COMPLEMENT_TABLE_RNA)
    else:
        return string[::-1].translate(COMPLEMENT_TABLE_DNA)

def most_frequent_words_with_mismatches(string, k, d):
    """Return the list of the most frequent k-mers when at most 
    d mismatches are allowed.
    """
    counter = Counter()
    for i, kmer in enumerate_kmers(string, k):
        for neighbor in neighbors(kmer, d):
            counter[neighbor] += 1
        for neighbor in neighbors(reverse_complement(kmer), d):
            counter[neighbor] += 1

    maxCount = max(counter.values())
    return [kmer for kmer in counter if counter[kmer] == maxCount]

if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_BA1J.txt') as inFile:
        string = inFile.readline().strip()
        k, d = map(int, inFile.readline().split())

    # Print output
    with open('../../answers/rosalind_BA1J_out.txt', 'w') as outFile:
        print(' '.join(map(str, most_frequent_words_with_mismatches(string, k, d))), file=outFile)

