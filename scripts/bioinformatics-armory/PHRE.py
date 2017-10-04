##################################################
# Read Quality Distribution
#
# http://rosalind.info/problems/PHRE/
# 
# Given: A quality threshold, along with FASTQ entries
#  for multiple reads.
# 
# Return: The number of reads whose average quality
#  is below the threshold.
#
# AUTHOR : dohlee
##################################################

# Your imports here

# Your codes here
def Fastq_fp(inFile):
    """Read fastq file and generate header, seq, comment, and quality, one by one."""
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

def below_threshold(qualities, threshold):
    """Return True if average quality of the sequence is
    below the threshold. Otherwise, return False.
    It assumes Phred33 scoring scheme.
    """
    quals = [ord(c) - 33 for c in qualities]
    return sum(quals) / float(len(quals)) < threshold

if __name__ == '__main__':
    # Load the data.
    c = 0
    with open('../../datasets/rosalind_PHRE.txt') as inFile:
        threshold = int(inFile.readline())
        for header, seq, comment, quality in Fastq_fp(inFile):
            if below_threshold(quality, threshold):
                c += 1

    # Print output
    with open('../../answers/rosalind_PHRE_out.txt', 'w') as outFile:
        print(c, file=outFile)

