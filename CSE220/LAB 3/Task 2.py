#Task 02: Decryption Process

def decrypt_matrix(matrix):
  row=len(matrix)
  col=len(matrix[0])
  diff=np.zeros(col-1,dtype=int)
  sum=np.zeros(col,dtype=int)

  for c in range(col):
    for r in range(row):
      sum[c]+=matrix[r][c]
  for i in range(1,col,1):
    diff[i-1]= sum[i]-sum[i-1]
  return diff

#DO NOT CHANGE THE CODE BELOW
matrix=np.array([[1,3,1],
                 [6,4,2],
                 [5,1,7],
                 [9,3,3],
                 [8,5,4]
                 ])

returned_array=decrypt_matrix(matrix)
print(returned_array)
#This should print [-13, 1]