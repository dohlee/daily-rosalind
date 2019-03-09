##################################################
# Construct the Graph of a Spectrum
#
# http://rosalind.info/problems/BA11A/
# 
# Given: A space-delimited list of integers Spectrum.
# 
# Return: Graph(Spectrum).
#
# AUTHOR : dohlee
##################################################

# Your imports here
from collections import defaultdict

# Your codes here
massTable = """
A   71
C   103
D   115
E   129
F   147
G   57
H   137
I   113
K   128
L   113
M   131
N   114
P   97
Q   128
R   156
S   87
T   101
V   99
W   186
Y   163
X   4
Z   5
""".split()
aa2mass = dict(zip(massTable[::2], map(int,massTable[1::2])))
mass2aa = dict(zip(map(int,massTable[1::2]), massTable[::2]))

def graph(spectrum):
    spectrum = [0] + spectrum
    l = len(spectrum)
    adj_list = defaultdict(list)

    for i in range(l):
        for j in range(i+1, l):
            diff = spectrum[j] - spectrum[i]
            if diff in mass2aa:
                adj_list[spectrum[i]].append((spectrum[j], mass2aa[diff]))
    
    return adj_list

if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_BA11A.txt') as inFile:
        spectrum = list(map(int, inFile.readline().strip().split()))

    adj_list = graph(spectrum)
    # Print output
    with open('../../answers/rosalind_BA11A_out.txt', 'w') as outFile:
        for u in sorted(adj_list.keys()):
            vs = adj_list[u]
            for v, aa in vs:
                print('%d->%d:%s' % (u, v, aa), file=outFile)
