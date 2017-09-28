##################################################
# Compute the Probability of an Outcome Given a Hidden Path
#
# http://rosalind.info/problems/BA10B/
# 
# Given: A string x, followed by the alphabet 
#  from which x was constructed, followed by a hidden
#  path , followed by the states States and emission
#  matrix Emission of an HMM (, States, Transition,
#  Emission).
# 
# Return: The conditional probability Pr(x|) that
#  string x will be emitted by the HMM given the
#  hidden path .
#
# AUTHOR : dohlee
##################################################

# Your imports here
from BA10A import generate_mapping

# Your codes here
def parse_emmision_matrix(inFile):
    """Parse emmision matrix and return the matrix.
    It assumes emmision matrix comes at the last.
    """
    inFile.readline()
    E = [list(map(float, line.split()[1:])) for line in inFile.readlines()]
    return E

def probability_of_observation_sequence(X, PI, Z, S, E):
    """Given observation X, state sequence PI, alphabet Z,
    states S, emmision matrix E, compute the probability of
    observation X.
    """
    p = 1
    for x, s in zip(X, PI):
        # multiply the probabiilty of emitting x from state s.
        p *= E[S[s]][Z[x]]
    return p

if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_BA10B.txt') as inFile:
        X = inFile.readline().strip()
        inFile.readline()
        Z = generate_mapping(inFile)
        inFile.readline()
        PI = inFile.readline().strip()
        inFile.readline()
        S = generate_mapping(inFile)
        inFile.readline()
        E = parse_emmision_matrix(inFile)

    # Print output
    with open('../../answers/rosalind_BA10B_out.txt', 'w') as outFile:
        print('%.12g' % probability_of_observation_sequence(X, PI, Z, S, E), file=outFile)
