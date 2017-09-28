##################################################
# Compute the Probability of a String Emitted by an HMM
#
# http://rosalind.info/problems/BA10D/
# 
# Given: A string x, followed by the alphabet 
#  from which x was constructed, followed by the
#  states States, transition matrix Transition,
#  and emission matrix Emission of an HMM (, States,
#  Transition, Emission).
# 
# Return: The probability Pr(x) that the HMM emits
#  x. 
#
# AUTHOR : dohlee
##################################################

# Your imports here
from BA10A import generate_mapping
from BA10A import parse_transition_matrix
from BA10B import parse_emission_matrix

# Your codes here
def forward_matrix(X, Z, S, A, E):
    """Return forward matrix of sequence X with current HMM model."""
    # initialize forward matrix.
    F = [[0] * len(X) for _ in range(len(S))]
    for k in range(len(S)):
        F[k][0] = 1.0 / len(S) * E[k][Z[X[0]]] # assume uniform initial probabilities.

    # fill Forward matrix.
    for i in range(len(X) - 1):
        for k in range(len(S)):
            F[k][i+1] = E[k][Z[X[i+1]]] * sum(F[l][i] * A[l][k] for l in range(len(S)))

    return F

if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_BA10D.txt') as inFile:
        X = inFile.readline().strip()
        inFile.readline()
        Z = generate_mapping(inFile)
        inFile.readline()
        S = generate_mapping(inFile)
        inFile.readline()
        A = parse_transition_matrix(inFile)
        inFile.readline()
        E = parse_emission_matrix(inFile)

        F = forward_matrix(X, Z, S, A, E) 

    # Print output
    with open('../../answers/rosalind_BA10D_out.txt', 'w') as outFile:
        print(sum(F[k][-1] for k in range(len(S))), file=outFile)

