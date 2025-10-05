# Task 01: Zigzag Walk

def walk_zigzag(floor):
  row=len(floor)
  col=len(floor[0])

  for i in range(col):
    if i%2==0:
      for j in range(0,row,2):
        change=floor[j][i]
        print(change, end= " ")
    else:
      if row%2!=0:
        for k in range(row-2,0,-2):
          change=floor[k][i]
          print(change, end= " ")
      else:
        for k in range(row-1,0,-2):
          change=floor[k][i]
          print(change, end= " ")
    print("\n")


#DO NOT CHANGE THE CODE BELOW
floor = np.array([[ '3' , '8' , '4' , '6' , '1'],
                  ['7' , '2' , '1' , '9' , '3'],
                  ['9' , '0' , '7' , '5' , '8'],
                  ['2' , '1' , '3' , '4' , '0'],
                  ['1' , '4' , '2' , '8' , '6']]
                )

print_matrix(floor)
print('Walking Sequence:')
walk_zigzag(floor)
#This should print
# 3 9 1
# 1 2
# 4 7 2
# 4 9
# 1 8 6
print('################')
floor = np.array([[ '3' , '8' , '4' , '6' , '1'],
                  ['7' , '2' , '1' , '9' , '3'],
                  ['9' , '0' , '7' , '5' , '8'],
                  ['2' , '1' , '3' , '4' , '0']]
                )

print_matrix(floor)
print('Walking Sequence:')
walk_zigzag(floor)
#This should print
# 3 9
# 1 2
# 4 7
# 4 9
# 1 8