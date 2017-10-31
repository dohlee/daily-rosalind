##################################################
# Find a Position in a Genome Minimizing the Skew
#
# http://rosalind.info/problems/BA1F/
# 
# Given: A DNA string Genome.
# 
# Return: All integer(s) i minimizing Skew(Prefixi
#  (Text)) over all values of i (from 0 to |Genome|).
#
# AUTHOR : dohlee
##################################################

# Your imports here


# Your codes here
def skew_minimizing_positions(dna):
    """Return the positions that minimize the G-C skew of dna[:pos]."""
    minSkew, skew = 12345679, 0
    pos = []
    for i, base in enumerate(dna, 1):
        if base == 'C':
            skew -= 1
        elif base == 'G':
            skew += 1

        if skew < minSkew:
            minSkew = skew
            pos = [i]
        elif skew == minSkew:
            pos.append(i)

    return pos

if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_BA1F.txt') as inFile:
        dna = inFile.readline().strip()

    # Print output
    with open('../../answers/rosalind_BA1F_out.txt', 'w') as outFile:
        print(' '.join(map(str, skew_minimizing_positions(dna))), file=outFile)

