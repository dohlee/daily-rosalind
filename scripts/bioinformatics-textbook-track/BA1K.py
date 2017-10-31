##################################################
# Generate the Frequency Array of a String
#
# http://rosalind.info/problems/BA1K/
# 
# Given: A DNA string Text and an integer k.
# 
# Return: The frequency array of k-mers in Text.
#
# AUTHOR : dohlee
##################################################

# Your imports here
from BA1L import pattern2num

# Your codes here
def frequency_array(dna, k):
    """Generate frequency array of k-mers in DNA."""
    frequencyArray = [0] * (4**k)
    for i in range(0, len(dna) - k + 1):
        frequencyArray[pattern2num(dna[i:i+k])] += 1

    return frequencyArray


if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_BA1K.txt') as inFile:
        dna = inFile.readline().strip()
        k = int(inFile.readline())

    # Print output
    with open('../../answers/rosalind_BA1K_out.txt', 'w') as outFile:
        print(' '.join(map(str, frequency_array(dna, k))), file=outFile)
