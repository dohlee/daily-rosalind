##################################################
# Compute the Number of Times a Pattern Appears in a Text
#
# http://rosalind.info/problems/BA1A/
# 
# Given: (DNA strings) Text and Pattern.
# 
# Return: Count(Text, Pattern).
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
    return [m.start() for m in re.finditer('(?=%s)' % motif, seq)]

if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_BA1A.txt') as inFile:
        seq = inFile.readline().strip()
        motif = inFile.readline().strip()

    # Print output
    with open('../../answers/rosalind_BA1A_out.txt', 'w') as outFile:
        print(len(find(seq, motif)), file=outFile)

