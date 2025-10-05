n=input().split()
length=int(n[0])
query=int(n[1])
arr1=input().split()
for i in range(length):
  arr1[i]=int(arr1[i])

def binary_search(arr1,target,up):
  low=0
  high=len(arr1)

  while low<high:
    mid=(low+high)//2
    if up:
      if arr1[mid]<=target:
        low=mid+1
      else:
        high=mid
    else:
      if arr1[mid]<target:
        low=mid+1
      else:
        high=mid
  return low

for i in range(query):
  arr2=input().split()
  small=int(arr2[0])
  big=int(arr2[1])
  lower=binary_search(arr1,small,False)
  upper=binary_search(arr1,big,True)
  print(upper-lower)