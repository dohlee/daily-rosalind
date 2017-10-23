##################################################
# Maximizing the Gap Symbols of an Optimal Alignment
#
# http://rosalind.info/problems/MGAP/
# 
# Given: Two DNA strings s and t in FASTA format
#  (each of length at most 5000 bp).
# 
# Return: The maximum number of gap symbols that
#  can appear in any maximum score alignment of
#  s and t with score parameters satisfying m >
#  0, d < 0, and g < 0.
#
# AUTHOR : dohlee
##################################################

# Your imports here
from GC import Fasta
from LCSQ import longest_common_subsequence

# Your codes here

if __name__ == '__main__':
    # Load the data.
    seq1, seq2 = [seq for header, seq in Fasta('../../datasets/rosalind_MGAP.txt')]

    # Print output
    with open('../../answers/rosalind_MGAP_out.txt', 'w') as outFile:
        print(len(seq1) + len(seq2) - 2 * len(longest_common_subsequence(seq1, seq2)), file=outFile)        

