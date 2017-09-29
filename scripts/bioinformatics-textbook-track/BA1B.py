##################################################
# Find the Most Frequent Words in a String
#
# http://rosalind.info/problems/BA1B/
# 
# Given:  A DNA string Text and an integer k.
# 
# Return: All most frequent k-mers in Text (in any
#  order).
#
# AUTHOR : dohlee
##################################################

# Your imports here
from collections import Counter

# Your codes here
def most_frequent_kmer(seq, k):
	"""Return all most frequent k-mers in seq."""
	count = Counter([seq[i:i+k] for i in range(len(seq) - k + 1)])
	mostFrequentCount = max(count.values())
	return [kmer for kmer in count if count[kmer] == mostFrequentCount]	

if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_BA1B.txt') as inFile:
        seq = inFile.readline().strip()
        k = int(inFile.readline())

    # Print output
    with open('../../answers/rosalind_BA1B_out.txt', 'w') as outFile:
        print(' '.join(sorted(most_frequent_kmer(seq, k=k))), file=outFile)

