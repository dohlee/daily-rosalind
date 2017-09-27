##################################################
# GenBank Introduction
#
# http://rosalind.info/problems/GBK/
# 
# Given: A genus name, followed by two dates in
#  YYYY/M/D format.
# 
# Return: The number of Nucleotide GenBank entries
#  for the given genus that were published between
#  the dates specified.
#
# AUTHOR : dohlee
##################################################

# Your imports here
from Bio import Entrez
Entrez.email = 'apap950419@gmail.com'

# Your codes here
def get_genbank_nucleotide_records(query):
    """Return genbank nucleotide records given query."""
    handle = Entrez.esearch(db='nucleotide', term=query)
    records = Entrez.read(handle)
    return records

if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_GBK.txt') as inFile:
        genus = inFile.readline().strip()
        startDate = inFile.readline().strip()
        endDate = inFile.readline().strip()

        # PDAT is search field term for publication date
        query = '%s[Organism] AND %s:%s[PDAT]' % (genus, startDate, endDate)

    # Print output
    with open('../../answers/rosalind_GBK_out.txt', 'w') as outFile:
        print(get_genbank_nucleotide_records(query)['Count'], file=outFile)
