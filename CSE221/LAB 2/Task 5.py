n=input().split()
length=int(n[0])
sum=int(n[1])
arr=input().split()
for i in range(length):
  arr[i]=int(arr[i])

arrsum=0
new=[]
max=0
j=0
for i in range(length):
  arrsum+=arr[i]
  if arrsum<=sum:
    new.append(arr[i])
    if len(new)-j>max:
      max=len(new)-j
  else:
    while arrsum>sum:
      arrsum-=arr[j]
      j+=1
    new.append(arr[i])


print(max)