##################################################
# Error Correction in Reads
#
# http://rosalind.info/problems/CORR/
#
# Given: A collection of up to 1000 reads of equal
#  length (at most 50 bp) in FASTA format. Some
#  of these reads were generated with a single-nucleotide
#  error. For each read s in the dataset, one of
#  the following applies:
#
# Return: A list of all corrections in the form
#  "[old read]->[new read]".  (Each correction must
#  be a single symbol substitution, and you may
#  return the corrections in any order.)
#
# AUTHOR : dohlee
##################################################

# Your imports here
from GC import Fasta
from REVC import reverse_complement
from HAMM import hamming_distance
from collections import Counter

# Your codes here
def get_correctly_sequenced_read_set(reads):
    counter = Counter()
    for read in reads:
        counter[read] += 1
        counter[reverse_complement(read)] += 1

    # Return sequences appearing more than 1 time.
    return set([read for read, count in counter.items() if count > 1])


def get_error_corrections(reads):
    correct_read_set = get_correctly_sequenced_read_set(reads)
    error_corrections = []
    for read in reads:
        if read in correct_read_set or reverse_complement(read) in correct_read_set:
            continue
        else:
            for reference_read in correct_read_set:
                if hamming_distance(read, reference_read) == 1:
                    error_corrections.append((read, reference_read))
                    break

    return error_corrections


if __name__ == '__main__':
    # Load the data.
    reads = [seq for _, seq in Fasta('../../datasets/rosalind_CORR.txt')]

    # Print output
    error_corrections = get_error_corrections(reads)
    with open('../../answers/rosalind_CORR_out.txt', 'w') as outFile:
        for read, reference_read in error_corrections:
            print('%s->%s' % (read, reference_read), file=outFile)
