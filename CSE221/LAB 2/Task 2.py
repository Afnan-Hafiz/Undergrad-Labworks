p=input().split()
n=int(p[0])
m=int(p[1])
k=int(p[2])
A=[]
B=[]
Ain=input().split()
Bin=input().split()
for i in range(n):
  A.append(int(Ain[i]))
for i in range(m):
  B.append(int(Bin[i]))

i=0
j=m-1

storedDiff=float('infinity')
besti=0
bestj=0
while i<n and j>=0:
  sum=A[i]+B[j]
  diff= abs(A[i] + B[j]-k)

  if diff<storedDiff:
    storedDiff=diff
    besti=i
    bestj=j
  if sum>k:
    j-=1
  elif sum<k:
    i+=1
  else:
    besti=i
    bestj=j
    break

print(besti+1,bestj+1)