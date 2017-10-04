##################################################
# FASTQ format introduction
#
# http://rosalind.info/problems/TFSQ/
# 
# Given: FASTQ file
# 
# Return: Corresponding FASTA records
#
# AUTHOR : dohlee
##################################################

# Your imports here


# Your codes here
def Fastq(filePath):
    """Read fastq file and generate header, seq, comment, and quality, one by one."""
    with open(filePath) as inFile:
        for i, line in enumerate(inFile.readlines()):
            if i % 4 == 0:
                header = line.strip()[1:]
            elif i % 4 == 1:
                seq = line.strip()
            elif i % 4 == 2:
                comment = line.strip()[1:]
            else:
                quality = line.strip()
                yield header, seq, comment, quality

if __name__ == '__main__':
    # Load the data.
    headers, seqs = [], []
    for header, seq, comment, quality in Fastq('../../datasets/rosalind_TFSQ.txt'):
        headers.append(header)
        seqs.append(seq)

    # Print output
    with open('../../answers/rosalind_TFSQ_out.txt', 'w') as outFile:
        for header, seq in zip(headers, seqs):
            print('>' + header, file=outFile)
            print(seq, file=outFile)

