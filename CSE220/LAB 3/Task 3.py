# Task 03: Row Rotation Policy of BRACU Classroom
def row_rotation(exam_week, seat_status):
  row=len(seat_status)
  col=len(seat_status[0])
  arr=np.zeros((row,col),dtype=seat_status.dtype)

  for i in range(row):
    change=seat_status[((i+exam_week+1)%row)]
    arr[i]= change

  print_matrix(arr)
  return exam_week%row-1

#DO NOT CHANGE THE CODE BELOW
seat_status = np.array([[ 'A' , 'B' , 'C' , 'D' , 'E'],
                  ['F' , 'G' , 'H' , 'I' , 'J'],
                  ['K' , 'L' , 'M' , 'N' , 'O'],
                  ['P' , 'Q' , 'R' , 'S' , 'T'],
                  ['U' , 'V' , 'W' , 'X' , 'Y'],
                  ['Z' , 'AA' , 'BB' , 'CC' , 'DD']])
exam_week=3
print_matrix(seat_status)
print()

row_number=row_rotation(exam_week, seat_status) #This should print modified seat status after rotation and return the row number
print(f'Your friend AA will be on row {row_number}') #This should print Your friend AA will be on row 2