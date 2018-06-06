##################################################
# The Wright-Fisher Model of Genetic Drift
#
# http://rosalind.info/problems/WFMD/
#
# Given: Positive integers N (N <=q 7), m (m <=q
#  2N), g (g <=q 6) and k (k <=q 2N).
#
# Return: The probability that in a population of
#  N diploid individuals initially possessing m
#  copies of a dominant allele, we will observe
#  after g generations at least k copies of a recessive
#  allele. Assume the Wright-Fisher model.
#
# AUTHOR : dohlee
##################################################

# Your imports here
from ASPC import combination

# Your codes here
if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_WFMD.txt') as inFile:
        N, m, g, k = map(int, inFile.readline().strip().split())
        p = m / (2 * N)

    # Probabilities of having x donimant alleles in 1st generation.
    p_dominant_alleles = [combination(2 * N, i) * p**i * (1 - p)**(2 * N - i) for i in range(2 * N + 1)]
    for _ in range(g - 1):
        temp = [0] * (2 * N + 1)
        for i in range(2 * N + 1):
            for j, p in enumerate(p_dominant_alleles):
                temp[i] += p * combination(2 * N, i) * (j / (2 * N))**i * (1 - (j / (2 * N)))**(2 * N - i)
        p_dominant_alleles = temp

    # Print output
    with open('../../answers/rosalind_WFMD_out.txt', 'w') as outFile:
        print('%.3f' % sum(p_dominant_alleles[:-k]), file=outFile)
