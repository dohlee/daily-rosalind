##################################################
# Finding a Motif in DNA
#
# http://rosalind.info/problems/SUBS/
# 
# Given: Two DNA strings s and t (each of length
#  at most 1 kbp).
# 
# Return: All locations of t as a substring of s.
#
# AUTHOR : dohlee
##################################################

# Your imports here
import re

# Your codes here
def find(seq, motif):
    # refer to:
    # https://stackoverflow.com/questions/4664850/find-all-occurrences-of-a-substring-in-python
    # note that lookahead is required to capture overlapping matches.
    return [m.start() + 1 for m in re.finditer('(?=%s)' % motif, seq)]

if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_SUBS.txt') as inFile:
        seq = inFile.readline().strip()
        motif = inFile.readline().strip()

    # Print output
    with open('../../answers/rosalind_SUBS_out.txt', 'w') as outFile:
        print(' '.join(map(str, find(seq, motif))), file=outFile)

