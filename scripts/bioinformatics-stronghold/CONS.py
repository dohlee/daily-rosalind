##################################################
# Consensus and Profile
#
# http://rosalind.info/problems/CONS/
# 
# Given: A collection of at most 10 DNA strings
#  of equal length (at most 1 kbp) in FASTA format.
# 
# Return: A consensus string and profile matrix
#  for the collection. (If several possible consensus
#  strings exist, then you may return any one of
#  them.)
#
# AUTHOR : dohlee
##################################################

# Your imports here
from GC import Fasta

# Your codes here
NUC2NUM = {'A':0, 'C':1, 'G':2, 'T':3}
NUM2NUC = {0:'A', 1:'C', 2:'G', 3:'T'}

def make_profile(seqs):
    """Make profile with a set of sequence."""
    profile = [[0] * len(seqs[0]) for _ in range(len(seqs))]

    for seq in seqs:
        for i, nuc in enumerate(seq):
            profile[NUC2NUM[nuc]][i] += 1

    return profile

def consensus(profile):
    """Return one of the consensus sequences of the profile."""
    argmax = lambda x: max(enumerate(x), key=lambda t: t[1])[0]
    return ''.join(map(lambda col: NUM2NUC[argmax(col)], [[profile[i][j] for i in range(4)] for j in range(len(profile[0]))]))

def print_summary(profile, file):
    """Print summary of the profile."""
    for i in range(4):
        print('%s: %s' % (NUM2NUC[i], ' '.join(map(str, profile[i]))), file=file)

if __name__ == '__main__':
    # Load the data.
    seqs = [seq for header, seq in Fasta('../../datasets/rosalind_CONS.txt')]
    profile = make_profile(seqs)

    # Print output
    with open('../../answers/rosalind_CONS_out.txt', 'w') as outFile:
        print(consensus(profile), file=outFile)
        print_summary(profile, file=outFile)

