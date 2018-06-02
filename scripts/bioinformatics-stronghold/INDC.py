##################################################
# Independent Segregation of Chromosomes
#
# http://rosalind.info/problems/INDC/
#
# Given: A positive integer n <=q 50.
#
# Return: An array A of length 2n in which A[k]
#  represents the common logarithm of the probability
#  that two diploid siblings share at least k of
#  their 2n chromosomes (we do not consider recombination
#  for now).
#
# AUTHOR : dohlee
##################################################

# Your imports here
from ASPC import combination
import numpy as np

# Your codes here
if __name__ == '__main__':
    # Load the data.
    n = int(open('../../datasets/rosalind_INDC.txt').read())

    # Print output
    with open('../../answers/rosalind_INDC_out.txt', 'w') as outFile:
        answer = np.log10(np.array([combination(2 * n, i) * (0.5)**(2 * n) for i in range(2 * n, 0, -1)]).cumsum())[::-1]
        print(' '.join(map(lambda x: '%.4f' % x, answer)), file=outFile)
