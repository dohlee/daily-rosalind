##################################################
# Introduction to Protein Databases
#
# http://rosalind.info/problems/DBPR/
# 
# Given: The UniProt ID of a protein.
# 
# Return: A list of biological processes in which
#  the protein is involved (biological processes
#  are found in a subsection of the protein's "Gene
#  Ontology" (GO) section).
#
# AUTHOR : dohlee
##################################################

# Your imports here
from Bio import ExPASy
from Bio import SwissProt

# Your codes here
def extract_go_biological_process(accession):
    """Get GO Biological Process term of protein via SwissProt DB."""
    handle = ExPASy.get_sprot_raw(accession)
    record = SwissProt.read(handle)
    # the snippet below extracts GO Biological Process term from SwissProt record.
    return [tup[2][2:] for tup in record.cross_references if tup[0] == 'GO' and tup[2].startswith('P')]

if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_DBPR.txt') as inFile:
        accession = inFile.readline().strip()

    # Print output
    with open('../../answers/rosalind_DBPR_out.txt', 'w') as outFile:
        print('\n'.join(extract_go_biological_process(accession)), file=outFile)

