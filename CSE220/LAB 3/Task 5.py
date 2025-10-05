#Task 05: Game Arena

def play_game(arena):
  row=len(arena)
  col=len(arena[0])
  sum=0
  for irow in range(row):
    for jcol in range(col):
      if arena[irow][jcol]%50==0:
        if arena[irow][jcol]!=0 and 1:
          if irow>0:
            if arena[irow-1][jcol]==2:
              sum+= 2
          if irow<row-1:
            if arena[irow+1][jcol]==2:
              sum+= 2
          if jcol>0:
            if arena[irow][jcol-1]==2:
              sum+= 2
          if jcol<col-1:
            if arena[irow][jcol+1]==2:
              sum+= 2

  if sum<10:
    print(f"Points Gained: {sum} . Your team is out.")
  else:
    print(f"Points Gained: {sum} . Your team has survived the game.")



#DO NOT CHANGE THE CODE BELOW
arena=np.array([[0,2,2,0],
                [50,1,2,0],
                [2,2,2,0],
                [1,100,2,0]
                ])
print_matrix(arena)
play_game(arena)
#This should print
#Points Gained: 6. Your team is out.
print(".....................")
arena=np.array([[0,2,2,0,2],
                [1,50,2,1,100],
                [2,2,2,0,2],
                [0,200,2,0,0]
                ])
print_matrix(arena)
play_game(arena)
#This should print
#Points Gained: 14. Your team has survived the game.
