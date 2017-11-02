##################################################
# Character-Based Phylogeny
#
# http://rosalind.info/problems/CHBP/
# 
# Given: A list of n species (n <=q 80) and an n-column
#  character table C in which the jth column denotes
#  the jth species.
# 
# Return: An unrooted binary tree in Newick format
#  that models C.
#
# AUTHOR : dohlee
##################################################

# Your imports here


# Your codes here
def merge_two_nodes(characterTable, nodeNames, i, j):
	"""Merge two nodes."""
	assert i < j
	nodeNames[i] = '(%s,%s)' % (nodeNames[i], nodeNames[j])
	nodeNames.pop(j)

	for row in characterTable:
		row.pop(j)

	if len(characterTable) > 1:
		toRemove = [i for i, row in enumerate(characterTable) if row.count('1') == 1 or row.count('0') == 1]
		for i in toRemove:
			del characterTable[i]

def select_nodes_to_merge(characterTable):
	"""When characters of two nodes are consistent for all rows
	in character table, they are ready to be merged.
	"""
	for i in range(len(characterTable[0])):
		for j in range(i+1, len(characterTable[0])):
			if all(row[i] == row[j] for row in characterTable):
				return i, j

	return None, None

def reconstruct_tree(characterTable, nodeNames):
	"""Reconstruct unrooted binary tree from character table by
	iteratively merging two nodes.
	"""
	i, j = select_nodes_to_merge(characterTable)

	while not (i is None and j is None):
		merge_two_nodes(characterTable, nodeNames, i, j)
		i, j = select_nodes_to_merge(characterTable)

	return '(%s)' % ','.join(nodeNames)

if __name__ == '__main__':
    # Load the data.
    with open('../../datasets/rosalind_CHBP.txt') as inFile:
        nodeNames = inFile.readline().strip().split()
        characterTable = [list(line.strip()) for line in inFile.readlines()]

    # Print output
    with open('../../answers/rosalind_CHBP_out.txt', 'w') as outFile:
        print(reconstruct_tree(characterTable, nodeNames), file=outFile)
