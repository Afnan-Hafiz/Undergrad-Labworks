#Task 04: Matrix Compression

def compress_matrix(mat):
  row=len(mat)
  col=len(mat[0])
  arr=np.zeros((2,2),dtype=int)
  for i in range(0,row,2):
    for j in range(0,col,2):
      sum=mat[i][j]+mat[i+1][j]+mat[i][j+1]+mat[i+1][j+1]
      arr[i//2][j//2]=sum

  return arr


#DO NOT CHANGE THE CODE BELOW
matrix=np.array([[1,2,3,4],
                 [5,6,7,8],
                 [1,3,5,2],
                 [-2,0,6,-3]
                 ])
print_matrix(matrix)
print("...............")
returned_array=compress_matrix(matrix)
print_matrix(returned_array)
#This should print

#|  14  |  22 |
#--------------
#|  2  |  10  |
#--------------