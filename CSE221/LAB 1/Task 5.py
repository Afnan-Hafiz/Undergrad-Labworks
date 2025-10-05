m=int(input())
arrInput=input().split()
arr=[]
for i in arrInput:
  arr.append(int(i))

even=[]
odd=[]
merged=[]
for i in range(m):
    if i%2==0:
      even.append(arr[i])
    else:
      odd.append(arr[i])

sortedeven=sorted(even)
sortedodd=sorted(odd)
oddidx=0
evenidx=0
for i in range(m):
  if i%2==0:
      merged.append(sortedeven[evenidx])
      evenidx+=1
  else:
      merged.append(sortedodd[oddidx])
      oddidx+=1

flag=True
for i in range(m-1):
  if merged[i]>merged[i+1]:
    flag=False
    break

if flag==True:
  print("YES")
else:
  print("NO")

