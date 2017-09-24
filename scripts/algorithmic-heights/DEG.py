##################################################
# Degree Array
#
# http://rosalind.info/problems/DEG/
# 
# Given: A simple graph with n <= 10^3 vertices
#  in the edge list format.
# 
# Return: An array D[1..n] where D[i] is the degree
#  of vertex i.
#
# AUTHOR : dohlee
##################################################

# Your imports here


# Your codes here






if __name__ == '__main__':
    from collections import Counter
    # Load the data.
    with open('../../datasets/rosalind_DEG.txt') as inFile:
        counter = Counter() 
        vertexCount, edgeCount = map(int, inFile.readline().split())
        for line in inFile.readlines():
            u, v = map(int, line.split())
            counter[u] += 1
            counter[v] += 1

    # Print output
    with open('../../answers/rosalind_DEG_out.txt', 'w') as outFile:
        print(' '.join(map(str, [counter[v] for v in range(1, vertexCount+1)])), file=outFile)

