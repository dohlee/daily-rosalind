##################################################
# Computing GC Content
#
# http://rosalind.info/problems/GC/
# 
# Given: At most 10 DNA strings in FASTA format
#  (of length at most 1 kbp each).
# 
# Return: The ID of the string having the highest
#  GC-content, followed by the GC-content of that
#  string. Rosalind allows for a default error of
#  0.001 in all decimal answers unless otherwise
#  stated; please see the note on absolute error
#  below.
#
# AUTHOR : dohlee
##################################################

# Your imports here


# Your codes here
def Fasta(filePath):
    """Read fasta file and generate header and seq, one by one."""
    with open(filePath) as inFile:
        # read in the first sequence.
        header, seqs = inFile.readline()[1:].strip(), []

        for line in inFile.readlines():
            # if new header appears, yield header and sequence.
            if line.startswith('>'):
                yield header, ''.join(seqs)
                header, seqs = line[1:].strip(), []
            else:
                seqs.append(line.strip())

        # do not forget to yield the last sequence.
        yield header, ''.join(seqs)

def gc_content(seq):
    """Compute GC content of sequence."""
    from collections import Counter
    c = Counter(seq)
    return (c['G'] + c['C']) / float(sum(c.values()))

if __name__ == '__main__':
    # get the sequence with the highest GC content.
    highestGC, answer = 0, None
    for header, seq in Fasta('../../datasets/rosalind_GC.txt'):
        gc = gc_content(seq)
        if gc > highestGC:
            highestGC, answer = gc, header

    # Print output
    with open('../../answers/rosalind_GC_out.txt', 'w') as outFile:
        print(answer, file=outFile)
        print('%.6f' % (100 * gc), file=outFile)

