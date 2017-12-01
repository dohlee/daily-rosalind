##################################################
# Comparing Spectra with the Spectral Convolution
#
# http://rosalind.info/problems/CONV/
# 
# Given: Two multisets of positive real numbers
#  S_1 and S_2. The size of each multiset is at
#  most 200.
# 
# Return: The largest multiplicity of S_1 \ominus
#  S_2, as well as the absolute value of the number
#  x maximizing (S_1 \ominus S_2)(x) (you may return
#  any such value if multiple solutions exist).
#
# AUTHOR : dohlee
##################################################

# Your imports here
from collections import Counter

# Your codes here
if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_CONV.txt') as inFile:
        s1 = list(map(float, inFile.readline().split()))
        s2 = list(map(float, inFile.readline().split()))

    # Print output
    with open('../../answers/rosalind_CONV_out.txt', 'w') as outFile:
        minkowskiDifference = Counter([round(abs(a - b), 5) for a in s1 for b in s2])
        print('\n'.join(map(str, minkowskiDifference.most_common(1)[0][::-1])), file=outFile)

