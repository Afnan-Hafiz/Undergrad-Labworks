n = int(input())
for i in range(n):
  m=int(input())
  arrInput=input().split()
  arr=[]
  for i in arrInput:
    arr.append(int(i))

  flag=True
  for i in range(len(arr)-1):
    if arr[i]>arr[i+1]:
      flag=False
      break

  if flag==True:
    print("YES")
  else:
    print("NO")