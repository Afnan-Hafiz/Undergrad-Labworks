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
i=0
j=0
while i<n and j<m:
  if arr1[i]<=arr2[j]:
    merge.append(arr1[i])
    i+=1
  else:
    merge.append(arr2[j])
    j+=1

while i<n:
    merge.append(arr1[i])
    i+=1

while j<m:
    merge.append(arr2[j])
    j+=1

for i in range(len(merge)):
  print(merge[i], end=" ")