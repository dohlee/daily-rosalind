##################################################
# Implement PatternToNumber
#
# http://rosalind.info/problems/BA1L/
# 
# Given: A DNA string Pattern.
# 
# Return: PatternToNumber(Pattern).
#
# AUTHOR : dohlee
##################################################

# Your imports here


# Your codes here
def pattern2num(pattern):
    """Convert DNA string pattern into number."""
    d = dict(zip('ACGT', '0123'))
    return int(''.join(d[c] for c in pattern) , 4)

if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_BA1L.txt') as inFile:
        pattern = inFile.readline().strip()

    # Print output
    with open('../../answers/rosalind_BA1L_out.txt', 'w') as outFile:
        print(pattern2num(pattern), file=outFile)

