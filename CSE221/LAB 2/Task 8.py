n=int(input())
for i in range(n):
  m=input().split()
  k=int(m[0])
  x=int(m[1])
  if x==1:
    print(k)
  else:
    ans=k+(k-1)//(x-1)
    print(ans)
