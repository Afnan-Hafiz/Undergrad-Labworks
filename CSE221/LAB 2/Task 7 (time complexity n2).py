n=input().split()
length=int(n[0])
query=int(n[1])
arr1=input().split()
for i in range(length):
  arr1[i]=int(arr1[i])

for i in range(query):
  arr2=input().split()
  lower=int(arr2[0])
  upper=int(arr2[1])
  count=0
  for j in range(length):
    if lower<=arr1[j]<=upper:
      count+=1
  print(count)