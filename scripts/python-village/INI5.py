##################################################
# Working with Files
#
# http://rosalind.info/problems/INI5/
# 
# Given: A file containing at most 1000 lines.
# 
# Return: A file containing all the even-numbered
#  lines from the original file.  Assume 1-based
#  numbering of lines.
#
# AUTHOR : dohlee
##################################################

# Your imports here


# Your codes here






if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_INI5.txt') as inFile:
        evenNumberedLines = [line for i, line in enumerate(inFile.readlines()) if i % 2 == 1]

    # Print output
    with open('../../answers/rosalind_INI5_out.txt', 'w') as outFile:
        print(''.join(evenNumberedLines), file=outFile)

