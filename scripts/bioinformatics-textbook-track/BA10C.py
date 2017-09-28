##################################################
# Implement the Viterbi Algorithm
#
# http://rosalind.info/problems/BA10C/
# 
# Given: A string x, followed by the alphabet 
#  from which x was constructed, followed by the
#  states States, transition matrix Transition,
#  and emission matrix Emission of an HMM (, States,
#  Transition, Emission).
# 
# Return: A path that maximizes the (unconditional)
#  probability Pr(x, ) over all possible paths .
#
# AUTHOR : dohlee
##################################################

# Your imports here
from BA10A import generate_mapping
from BA10A import parse_transition_matrix
from BA10B import parse_emission_matrix


# Your codes here
def backtrack(V, BT, S):
    """Given Viterbi matrix V and backtrack matrix BT,
    find the most probable path by backtracking BT.
    """
    res = []
    inverseS = dict((v, k) for k, v in S.items())

    stateIndex = max(range(len(S)), key=lambda l: V[l][-1])
    for i in range(len(V[0]) - 1, -1, -1):
        res.append(inverseS[stateIndex])
        stateIndex = BT[stateIndex][i]

    return res[::-1]


def decode(X, Z, S, A, E):
    """Given observation sequence X, alphabet Z,
    states S, state transition matrix A, emmision matrix E,
    estimate the most probable state path by Viterbi algorithm.
    """
    # initialize Viterbi matrix and backtrack matrix.
    V = [[0] * len(X) for _ in range(len(S))]
    BT = [[0] * len(X) for _ in range(len(S))]
    for k in range(len(S)):
        V[k][0] = 1.0 / len(S) * E[k][Z[X[0]]]

    # Fill in Viterbi matrix.
    for i in range(len(X) - 1):
        for k in range(len(S)):
            V[k][i+1] = E[k][Z[X[i+1]]] * max(V[l][i] * A[l][k] for l in range(len(S)))
            BT[k][i+1] = max(range(len(S)), key=lambda l: V[l][i] * A[l][k])

    return backtrack(V, BT, S)


if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_BA10C.txt') as inFile:
        X = inFile.readline().strip()
        inFile.readline()
        Z = generate_mapping(inFile)
        inFile.readline()
        S = generate_mapping(inFile)
        inFile.readline()
        A = parse_transition_matrix(inFile)
        inFile.readline()
        E = parse_emission_matrix(inFile)

    # Print output
    with open('../../answers/rosalind_BA10C_out.txt', 'w') as outFile:
        print(''.join(decode(X, Z, S, A, E)), file=outFile)
