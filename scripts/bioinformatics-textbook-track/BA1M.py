##################################################
# Implement NumberToPattern
#
# http://rosalind.info/problems/BA1M/
# 
# Given: Integers index and k.
# 
# Return: NumberToPattern(index, k).
#
# AUTHOR : dohlee
##################################################

# Your imports here


# Your codes here
def num2pattern(index, k):
    """Convert an integer into a dna string of length k."""
    d = dict(zip('0123', 'ACGT'))
    c = []
    while index > 4:
        c.append(index % 4)
        index //= 4
    c.append(index)
    c += [0] * (k - len(c))
    return ''.join(map(lambda x: d[str(x)], c[::-1]))

if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_BA1M.txt') as inFile:
        index = int(inFile.readline())
        k = int(inFile.readline())

    # Print output
    with open('../../answers/rosalind_BA1M_out.txt', 'w') as outFile:
        print(num2pattern(index, k), file=outFile)

