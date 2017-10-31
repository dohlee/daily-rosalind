##################################################
# Find the Most Frequent Words with Mismatches in a String
#
# http://rosalind.info/problems/BA1I/
# 
# Given: A string Text as well as integers k and d.
# 
# Return: All most frequent k-mers with up to d
#  mismatches in Text.
#
# AUTHOR : dohlee
##################################################

# Your imports here
from BA1E import enumerate_kmers
from BA1N import neighbors
from collections import Counter

# Your codes here
def most_frequent_words_with_mismatches(string, k, d):
    """Return the list of the most frequent k-mers when at most 
    d mismatches are allowed.
    """
    counter = Counter()
    for i, kmer in enumerate_kmers(string, k):
        for neighbor in neighbors(kmer, d):
            counter[neighbor] += 1

    maxCount = max(counter.values())
    return [kmer for kmer in counter if counter[kmer] == maxCount]

if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_BA1I.txt') as inFile:
        string = inFile.readline().strip()
        k, d = map(int, inFile.readline().split())

    # Print output
    with open('../../answers/rosalind_BA1I_out.txt', 'w') as outFile:
        print(' '.join(most_frequent_words_with_mismatches(string, k, d)), file=outFile)
