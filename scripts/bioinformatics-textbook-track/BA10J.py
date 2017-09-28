##################################################
# Solve the Soft Decoding Problem
#
# http://rosalind.info/problems/BA10J/
# 
# Given: A string x, followed by the alphabet 
#  from which x was constructed, followed by the
#  states States, transition matrix Transition,
#  and emission matrix Emission of an HMM (, States,
#  Transition, Emission).
# 
# Return: The probability Pr(i = k|x) that the
#  HMM was in state k at step i (for each state
#  k and each step i). 
#
# AUTHOR : dohlee
##################################################

# Your imports here
from BA10A import generate_mapping
from BA10A import parse_transition_matrix
from BA10B import parse_emission_matrix
from BA10D import forward_matrix

# Your codes here
def backward_matrix(X, Z, S, A, E):
	"""Return backward matrix of sequence X with current HMM model."""
	# initialize backward matrix.
	B = [[0] * len(X) for _ in range(len(S))]
	for k in range(len(S)):
		B[k][-1] = 1

	# fill backward matrix.
	for i in range(len(X)-1, 0, -1):
		for k in range(len(S)):
			B[k][i-1] = sum(A[k][l] * E[l][Z[X[i]]] * B[l][i] for l in range(len(S)))

	return B


def soft_decode(F, B, X, Z, k, i):
	"""Given Forward matrix F and Backward matrix B,
	return the probability that the HMM was in state k at step i.
	"""
	numState = len(F)
	denom1 = sum(F[l][-1] for l in range(numState))
	return F[k][i] * B[k][i] / denom1 

if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_BA10J.txt') as inFile:
        X = inFile.readline().strip()
        inFile.readline()
        Z = generate_mapping(inFile)
        inFile.readline()
        S = generate_mapping(inFile)
        inFile.readline()
        A = parse_transition_matrix(inFile)
        inFile.readline()
        E = parse_emission_matrix(inFile)

        states = list(sorted(S.keys(), key=lambda x: S[x]))
        F = forward_matrix(X, Z, S, A, E)
        B = backward_matrix(X, Z, S, A, E)

    # Print output
    with open('../../answers/rosalind_BA10J_out.txt', 'w') as outFile:
        print('\t'.join(states), file=outFile)
        for i in range(len(X)):
        	for k in range(len(S)):
        		v = soft_decode(F, B, X, Z, k, i)
        		print(('%.4f' % v).rstrip('0'), end=' ', file=outFile)
        	print(file=outFile)	


