##################################################
# Compute the Probability of a Hidden Path
#
# http://rosalind.info/problems/BA10A/
# 
# Given: A hidden path  followed by the states
#  States and transition matrix Transition of an
#  HMM (, States, Transition, Emission).
# 
# Return: The probability of this path, Pr(). You
#  may assume that initial probabilities are equal.
#
# AUTHOR : dohlee
##################################################

# Your imports here


# Your codes here
def generate_mapping(inFile):
    """Return state/alphabet-index mapping dictionary."""
    return dict((state, i) for i, state in enumerate(inFile.readline().split()))


def parse_transition_matrix(inFile):
    """Return state transition matrix."""
    states = inFile.readline().split()
    transitionMatrix = [list(map(float, inFile.readline().split()[1:])) for _ in range(len(states))]
    return transitionMatrix


def state_path_probability(PI, S, A):
    """Given a state sequence PI, a set of state S,
    and a matrix of state transition probabilities A,
    return the probability of state sequence.
    """
    # assume initial probabilities are equal.
    p = 1.0 / len(S)

    # multiply transition probabilities from start to end.
    for s1, s2 in zip(PI[:-1], PI[1:]):
        p *= A[S[s1]][S[s2]]

    return p

if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_BA10A.txt') as inFile:
        PI = inFile.readline().strip()
        inFile.readline()
        S = generate_mapping(inFile)
        inFile.readline()
        A = parse_transition_matrix(inFile)

    # Print output
    with open('../../answers/rosalind_BA10A_out.txt', 'w') as outFile:
        print('%.12g' % state_path_probability(PI, S, A), file=outFile)
