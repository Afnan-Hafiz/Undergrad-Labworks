n=list(map(int,input().split()))
num=list(map(int,input().split()))
dic={}
max=0
left=0
for right in range(n[0]):
  if num[right] in dic:
    dic[num[right]]+=1
  else:
    dic[num[right]] = 1
  while len(dic)>n[1]:
    dic[num[left]]-=1
    if dic[num[left]]==0:
      dic.pop(num[left])
    left+=1
  if max<right-left+1:
    max = right-left+1
print(max)