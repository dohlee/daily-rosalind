##################################################
# Counting Disease Carriers
#
# http://rosalind.info/problems/AFRQ/
#
# Given: An array A for which A[k] represents the
#  proportion of homozygous recessive individuals
#  for the k-th Mendelian factor in a diploid population.
#  Assume that the population is in genetic equilibrium
#  for all factors.
#
# Return: An array B having the same length as A
#  in which B[k] represents the probability that
#  a randomly selected individual carries at least
#  one copy of the recessive allele for the k-th
#  factor.
#
# AUTHOR : dohlee
##################################################

# Your imports here
from math import sqrt

# Your codes here
if __name__ == '__main__':
    # Load the data.
    q_squares = map(float, open('../../datasets/rosalind_AFRQ.txt').read().strip().split())
    ps = [1 - sqrt(q_square) for q_square in q_squares]

    # Print output
    with open('../../answers/rosalind_AFRQ_out.txt', 'w') as outFile:
        print(' '.join(map(lambda p: '%.3g' % (1 - p**2), ps)), file=outFile)
