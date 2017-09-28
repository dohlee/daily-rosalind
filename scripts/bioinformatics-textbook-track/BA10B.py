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
from BA10A import parse_transition_matrix

# Your codes here






if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_BA10B.txt') as inFile:
        X = inFile.readline().strip()
        inFile.readline()
        Z = generate_mapping(inFile)
        inFile.readline()
        PI = inFile.readline().strip()


    # Print output
    with open('../../answers/rosalind_BA10B_out.txt', 'w') as outFile:
        pass

