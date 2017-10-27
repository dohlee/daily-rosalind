##################################################
# Expected Number of Restriction Sites
#
# http://rosalind.info/problems/EVAL/
# 
# Given: A positive integer n (n <=q 1,000,000),
#  a DNA string s of even length at most 10, and
#  an array A of length at most 20, containing numbers
#  between 0 and 1.
# 
# Return:  An array B having the same length as
#  A in which B[i] represents the expected number
#  of times that s will appear as a substring of
#  a random DNA string t of length n, where t is
#  formed with GC-content A[i] (see Introduction
#  to Random Strings).
#
# AUTHOR : dohlee
##################################################

# Your imports here


# Your codes here
EPSILON = 1e-5
def probability(seq, gcContent):
	p = 1
	for c in seq:
		if c in 'AT':
			p *= (1 - gcContent) / 2
		else:
			p *= gcContent / 2

	return p

if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_EVAL.txt') as inFile:
        n = int(inFile.readline())
        s = inFile.readline().strip()
        A = list(map(float, inFile.readline().split()))

    # Print output
    with open('../../answers/rosalind_EVAL_out.txt', 'w') as outFile:
    	B = [probability(s, gcContent) * (n - len(s) + 1) for gcContent in A]
    	print(' '.join(map(lambda x: '%.3f' % (x + EPSILON), B)), file=outFile)

