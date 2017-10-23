##################################################
# Transitions and Transversions
#
# http://rosalind.info/problems/TRAN/
# 
# Given: Two DNA strings s_1 and s_2 of equal length
#  (at most 1 kbp).
# 
# Return: The transition/transversion ratio R(s_1,
#  s_2).
#
# AUTHOR : dohlee
##################################################

# Your imports here
from GC import Fasta

# Your codes here
def is_transition(base1, base2):
    """Return whether substitution between base1 and base2 is transition."""
    purines = {'A', 'G'}
    pyrimidines = {'C', 'T'}

    if (base1 in purines and base2 in purines) or (base1 in pyrimidines and base2 in pyrimidines):
        return True
    else:
        return False
def transition_transversion_ratio(seq1, seq2):
    """Given two DNA sequences of equal length,
    return the transition(G<->A, C<->T)/transversion(else) ratio.
    """
    transitionCount, transversionCount = 0.0, 0.0
    for base1, base2 in zip(seq1, seq2):
        if base1 != base2:
            if is_transition(base1, base2):
                transitionCount += 1
            else:
                transversionCount += 1
    return transitionCount / transversionCount

if __name__ == '__main__':
    # Load the data.
    seq1, seq2 = [seq for header, seq in Fasta('../../datasets/rosalind_TRAN.txt')]

    # Print output
    with open('../../answers/rosalind_TRAN_out.txt', 'w') as outFile:
        print('%.11f' % transition_transversion_ratio(seq1, seq2), file=outFile)

