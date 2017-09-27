##################################################
# Data Formats
#
# http://rosalind.info/problems/FRMT/
# 
# Given: A collection of n (n <=q 10) GenBank entry
#  IDs.
# 
# Return: The shortest of the strings associated
#  with the IDs in FASTA format.
#
# AUTHOR : dohlee
##################################################

# Your imports here
from Bio import Entrez
from Bio import SeqIO
Entrez.email = 'apap950419@gmail.com'

# Your codes here
def get_genbank_fasta(ids):
    handle = Entrez.efetch(db='nucleotide', id=ids, rettype='fasta')
    records = list(SeqIO.parse(handle, format='fasta'))
    return records

if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_FRMT.txt') as inFile:
        ids = inFile.readline().split()
        records = get_genbank_fasta(ids)

    # Print output
    with open('../../answers/rosalind_FRMT_out.txt', 'w') as outFile:
        shortest = min(records, key=lambda x: len(x.seq))
        print('>' + shortest.description, file=outFile)
        print('\n'.join(str(shortest.seq[i:i+70]) for i in range(0, len(shortest.seq), 70)), file=outFile)
