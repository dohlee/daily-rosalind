##################################################
# Generate the d-Neighborhood of a String
#
# http://rosalind.info/problems/BA1N/
# 
# Given: A DNA string Pattern and an integer d.
# 
# Return: The collection of strings Neighbors(Pattern,
#  d).
#
# AUTHOR : dohlee
##################################################

# Your imports here


# Your codes here
def neighbors_helper(pattern, d):
    if d == 0:
        return [pattern]
    if len(pattern) == 1 and d >= 1:
        return [base for base in 'ATGC']

    res = []
    for base in 'ATGC':
        if pattern[0] != base:
            res.extend(base + suffix for suffix in neighbors_helper(pattern[1:], d-1))
        else:
            res.extend(base + suffix for suffix in neighbors_helper(pattern[1:], d))

    return res

def neighbors(pattern, d):
    """Return d-neighbors of the pattern."""
    return neighbors_helper(pattern, d)

if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_BA1N.txt') as inFile:
        pattern = inFile.readline().strip()
        d = int(inFile.readline())

    # Print output
    with open('../../answers/rosalind_BA1N_out.txt', 'w') as outFile:
        print('\n'.join(neighbors(pattern, d)), file=outFile)

