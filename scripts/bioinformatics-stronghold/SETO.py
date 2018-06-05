##################################################
# Introduction to Set Operations
#
# http://rosalind.info/problems/SETO/
#
# Given: A positive integer n (n <=q 20,000) and
#  two subsets A and B of \(1, 2, ..., n\).
#
# Return: Six sets: A \cup B, A \cap B, A - B, B
#  - A, A^(\textrm(c)), and B^(\textrm(c)) (where
#  set complements are taken with respect to \(1,
#  2, ..., n\)).
#
# AUTHOR : dohlee
##################################################

# Your imports here


# Your codes here
if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_SETO.txt') as inFile:
        n = int(inFile.readline().strip())
        u = set(range(1, n + 1))
        a = set(map(int, inFile.readline().strip()[1:-1].split(',')))
        b = set(map(int, inFile.readline().strip()[1:-1].split(',')))

    # Print output
    with open('../../answers/rosalind_SETO_out.txt', 'w') as outFile:
        print(a.union(b), file=outFile)
        print(a.intersection(b), file=outFile)
        print(a.difference(b), file=outFile)
        print(b.difference(a), file=outFile)
        print(u.difference(a), file=outFile)
        print(u.difference(b), file=outFile)
