n=input().split()
length=int(n[0])
sum=int(n[1])
arr=input().split()
for i in range(length):
  arr[i]=int(arr[i])

idx1=0
idx2=length-1
flag=False
while idx1<idx2:
  current=arr[idx1]+arr[idx2]
  if current==sum:
    print(idx1+1,idx2+1)
    flag=True
    break
  elif current<sum:
    idx1+=1
  else:
    idx2-=1

if flag==False:
  print(-1)