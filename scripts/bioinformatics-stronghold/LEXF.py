##################################################
# Enumerating k-mers Lexicographically
#
# http://rosalind.info/problems/LEXF/
# 
# Given: A collection of at most 10 symbols defining
#  an ordered alphabet, and a positive integer n
#  (n <=q 10).
# 
# Return: All strings of length n that can be formed
#  from the alphabet, ordered lexicographically
#  (use the standard order of symbols in the English
#  alphabet).
#
# AUTHOR : dohlee
##################################################

# Your imports here


# Your codes here
def lexicographic_kmers_helper(alphabets, k):
	"""Helper function for recursive call."""
	if k == 1:
		return alphabets

	res = []
	for x in alphabets:
		res.extend([x + result for result in lexicographic_kmers_helper(alphabets, k-1)])

	return res

def lexicographic_kmers(alphabets, k):
	"""Return lexicographically ordered k-mers."""
	alphabets = sorted(alphabets)
	return lexicographic_kmers_helper(alphabets, k)

if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_LEXF.txt') as inFile:
        alphabets = list(map(str, inFile.readline().split()))
        k = int(inFile.readline())

    # Print output
    with open('../../answers/rosalind_LEXF_out.txt', 'w') as outFile:
        print('\n'.join(lexicographic_kmers(alphabets, k)), file=outFile)

