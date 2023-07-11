import numpy as np

#x = np.array([[0,1,0], [1,0,0],[0,0,1]])
x = np.array([[0,1,0,0], [1,0,0,0], [0,0,1,0], [0,1,0,1]])

xSz = x.shape

print()
print('  x  ')
for i in range(xSz[0]):
	for ii in range(xSz[1]):
		print(x[i][ii], end = " ")
	print()
print()

oneRows, oneColumns = np.where(x)

print()
print('oneRows       : ', oneRows)
print('oneColumns    : ', oneColumns)
print()

islandSize = [0 for i in range(len(oneRows))]
nOnes = len(oneRows)
for i in range(nOnes):
	if ((oneRows[i]-1) >= 0):
		ii = oneRows[i]-1
	else:
		ii = oneRows[i]
	while ((ii < xSz[0])& (ii <= oneRows[i]+1)):
		if ((oneColumns[i]-1) >= 0):
			iii = oneColumns[i]-1
		else:
			iii = oneColumns[i]
		while ((iii < xSz[1]) & (iii <= oneColumns[i]+1)) :
			print('\tIndex : ', i, '\tx : ', x[ii][iii], '\tRow :', ii, 'Column : ', iii)
			islandSize[i] = islandSize[i] + x[ii][iii]  
			iii+=1
		ii+=1



print()
print('Island size vector  : ', islandSize)
print()
print('Maximum island size : ', np.max(islandSize))
print()
