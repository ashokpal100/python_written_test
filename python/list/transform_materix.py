# Python Program - Subtract Two Matrices
		
matrix1 = [[10, 11, 12],
           [13, 14, 15],
	       [16, 17, 18]
	      ]

for x in matrix1:
	print (x)

matrix = [[1, 2],
	      [3, 4],
	      [5, 6]]
rmatrix = [[0, 0, 0],
	       [0, 0, 0]]
	       
for i in range(len(matrix)):
	for j in range(len(matrix[0])):
		rmatrix[j][i] = matrix[i][j]

		
for r in rmatrix:
	print(r)