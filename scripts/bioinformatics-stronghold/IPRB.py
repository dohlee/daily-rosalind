##################################################
# Mendel's First Law
#
# http://rosalind.info/problems/IPRB/
# 
# Given: Three positive integers k, m, and n, representing
#  a population containing k+m+n organisms: k individuals
#  are homozygous dominant for a factor, m are heterozygous,
#  and n are homozygous recessive.
# 
# Return: The probability that two randomly selected
#  mating organisms will produce an individual possessing
#  a dominant allele (and thus displaying the dominant
#  phenotype). Assume that any two organisms can
#  mate.
#
# AUTHOR : dohlee
##################################################

# Your imports here


# Your codes here
def dominant_probability(k, m, n):
	"""Return the probability of producing an 
	individual with dominant phenotype.
	"""
	total = float(k + m + n)
	# compute the probability of homozygous recessive.
	pRecessiveHomozygote = (n / total) * ((n-1) / (total-1)) + \
							2 * (m / total) * (n / (total-1)) * 0.5 + \
							(m / total) * ((m-1) / (total-1))  * 0.25
	# and subtract it from 1.
	return 1 - pRecessiveHomozygote

if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_IPRB.txt') as inFile:
        k, m, n = map(int, inFile.readline().split())

    # Print output
    with open('../../answers/rosalind_IPRB_out.txt', 'w') as outFile:
        print('%.5f' % dominant_probability(k, m, n), file=outFile)

