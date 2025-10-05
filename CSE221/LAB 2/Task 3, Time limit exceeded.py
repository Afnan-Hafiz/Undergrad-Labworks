#task 3 time limit exceed, code okay
p=input().split()
Ain=input().split()
n=int(p[0])
sum=int(p[1])
arr=[]
for i in range(n):
  arr.append(int(Ain[i]))

i=0
j=0
k=n-1
flag=False
while i<n and k>=0:
  curr=arr[i]+arr[k]
  j=sum-curr
  for kamikaze in range(i+1,k):
    if arr[kamikaze]==j:
      flag=True
      print(i+1,kamikaze+1,k+1)
      break

  if curr>sum:
    k-=1
  elif curr<sum:
    i+=1
if flag==False:
  print(-1)
