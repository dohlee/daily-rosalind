##################################################
# Reconstruct a String from its Genome Path
#
# http://rosalind.info/problems/BA3B/
# 
# Given: A sequence of k-mers Pattern1, ... , Patternn
#  such that the last k - 1 symbols of Patterni
#  are equal to the first k - 1 symbols of Patterni+1
#  for i from 1 to n-1.
# 
# Return: A string Text of length k+n-1 where the
#  i-th k-mer in Text is equal to Patterni for all
#  i.
#
# AUTHOR : dohlee
##################################################

# Your imports here


# Your codes here
def reconstruct_from_genome_path(kmers):
    """Return the original string reconstructed from kmers.""" 
    seq = [kmers[0]]
    for kmer in kmers[1:]:
        seq.append(kmer[-1])

    return ''.join(seq)

if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_BA3B.txt') as inFile:
        kmers = [line.strip() for line in inFile.readlines()]

    # Print output
    with open('../../answers/rosalind_BA3B_out.txt', 'w') as outFile:
        print(reconstruct_from_genome_path(kmers), file=outFile)

