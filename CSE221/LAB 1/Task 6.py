m=int(input())
arrInput=input().split()
arr=[]
for i in arrInput:
  arr.append(int(i))

flag=True
while flag:
  flag=False
  for i in range(len(arr)-1):
    if (arr[i]%2 == arr[i+1]%2) and (arr[i]>arr[i+1]):
      arr[i],arr[i + 1]=arr[i + 1],arr[i]
      flag=True

for i in arr:
  print(i, end=' ')