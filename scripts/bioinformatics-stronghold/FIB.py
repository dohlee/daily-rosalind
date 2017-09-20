##################################################
# Rabbits and Recurrence Relations
#
# http://rosalind.info/problems/FIB/
# 
# Given: Positive integers n <=q 40 and k <=q 5.
# 
# Return: The total number of rabbit pairs that
#  will be present after n months, if we begin with
#  1 pair and in each generation, every pair of
#  reproduction-age rabbits produces a litter of
#  k rabbit pairs (instead of only 1 pair).
#
# AUTHOR : dohlee
##################################################

# Your imports here


# Your codes here

if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_FIB.txt') as inFile:
        n, k = map(int, inFile.readline().split())
        # a represents the number of newborn rabbits.
        # b represents the number of reproduction-age rabiits.
        a, b = [1], [0]

        for _ in range(n-1):
            a.append(k * b[-1])
            b.append(b[-1] + a[-2])

    # Print output
    with open('../../answers/rosalind_FIB_out.txt', 'w') as outFile:
        print(a[-1] + b[-1], file=outFile)

