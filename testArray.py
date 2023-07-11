import numpy as np

na = np.array([[0,1,2], [3,4,5], [6,7,8]])

la = [[0,1,2], [3,4,5], [6,7,8]]

print()
print('na elements') 
naSz = na.shape
for i in range(naSz[0]):
	for ii in range(naSz[1]):
		print(na[i][ii], end= " ")
	print()

print()
print('la elements')
for r in na:
	for c in r :
		print(c, end = " ")
	print()

print()

