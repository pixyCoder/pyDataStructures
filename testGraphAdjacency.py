
import numpy as np
import testGraphVisual

# Inputs
N = 6
adjacency_list = [[10, 0, 1],
			[8, 1, 2],
			[4, 1, 3],
			[5, 3, 4],
			[16, 4, 5],
			[4, 2, 5]]
filename = "externalTestGraph.png"
saveFile = 1


if __name__ == '__main__':
	adjacency_matrix = np.zeros([N,N]) + 999.0

	for i in range(0,N):
		adjacency_matrix[adjacency_list[i][1]][adjacency_list[i][2]] = adjacency_list[i][0]

	testGraphVisual.plot_weighted_graph(N, adjacency_list, filename, saveFile)

	print()
	print('\t   Adj matrix   ')
	for i in range(0,N):
		for ii in range(0,N):
			print(adjacency_matrix[i][ii], end=" ")
		print()
	print()
