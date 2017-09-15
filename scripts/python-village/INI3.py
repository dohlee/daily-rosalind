##################################################
# Strings and Lists
#
# http://rosalind.info/problems/INI3/
# 
# Given: A string s of length at most 200 letters
#  and four integers a, b, c and d.
# 
# Return: The slice of this string from indices
#  a through b and c through d (with space in between),
#  inclusively.  In other words, we should include
#  elements s[b] and s[d] in our slice.
#
# AUTHOR : dohlee
##################################################

# Your imports here


# Your codes here



if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_INI3.txt') as inFile:
        string = inFile.readline().strip()
        a, b, c, d = map(int, inFile.readline().strip().split())

    # Print output
    with open('../../answers/rosalind_INI3_out.txt', 'w') as outFile:
        print(string[a:b+1], string[c:d+1], file=outFile)

