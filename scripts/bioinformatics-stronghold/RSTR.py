##################################################
# Matching Random Motifs
#
# http://rosalind.info/problems/RSTR/
#
# Given: A positive integer N <=q 100000, a number
#  x between 0 and 1, and a DNA string s of length
#  at most 10 bp.
#
# Return: The probability that if N random DNA strings
#  having the same length as s are constructed with
#  GC-content x (see Introduction to Random Strings),
#  then at least one of the strings equals s. We
#  allow for the same random string to be created
#  more than once.
#
# AUTHOR : dohlee
##################################################

# Your imports here


# Your codes here
if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_RSTR.txt') as inFile:
        N, x = inFile.readline().strip().split()
        N, x = int(N), float(x)
        seq = inFile.readline().strip()
        p = 1
        for c in seq:
            if c in 'AT':
                p *= (1 - x) / 2.
            else:
                p *= x / 2.

    # Print output
    with open('../../answers/rosalind_RSTR_out.txt', 'w') as outFile:
        print('%.3f' % (1 - (1 - p)**N), file=outFile)
