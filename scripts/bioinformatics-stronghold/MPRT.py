##################################################
# Finding a Protein Motif
#
# http://rosalind.info/problems/MPRT/
# 
# Given: At most 15 UniProt Protein Database access
#  IDs.
# 
# Return: For each protein possessing the N-glycosylation
#  motif, output its given access ID followed by
#  a list of locations in the protein string where
#  the motif can be found.
#
# AUTHOR : dohlee
##################################################

# Your imports here
import re
import requests

# Your codes here
def get_uniprot_sequence(accession):
    """Given UniProt Protein Database accession,
    return the amino acid sequence of the protein.
    """
    response = requests.get('http://www.uniprot.org/uniprot/%s.fasta' % accession)
    return ''.join(line.strip() for line in response.text.splitlines()[1:])

def n_glycosylation_motifs(seq):
    """Find occurences of N-glycosylation motifs in the sequence,
    and return the starting index of the motif.
    """
    return [match.start() + 1 for match in re.finditer(r'(?=N[^P][ST][^P])', seq)]

if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_MPRT.txt') as inFile:
        accessions = [line.strip() for line in inFile.readlines()]

    # Print output
    with open('../../answers/rosalind_MPRT_out.txt', 'w') as outFile:
        for accession in accessions:
            seq = get_uniprot_sequence(accession)
            motifLocations = n_glycosylation_motifs(seq)
            if len(motifLocations) > 0:
                print(accession, file=outFile)
                print(' '.join(map(str, motifLocations)), file=outFile)
