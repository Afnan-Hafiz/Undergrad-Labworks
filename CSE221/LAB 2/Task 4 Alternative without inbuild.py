n=int(input())
arr1in=input().split()
m=int(input())
arr2in=input().split()
arr1=[]
arr2=[]
for i in range(n):
  arr1.append(int(arr1in[i]))
for i in range(m):
  arr2.append(int(arr2in[i]))

merge=[]
for i in range(n):
  merge.append(arr1[i])

for i in range(m):
  merge.append(arr2[i])

merge.sort()

for i in range(len(merge)):
  print(merge[i], end=" ")