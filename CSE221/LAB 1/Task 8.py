n=int(input())
final=[]
for i in range(n):
  p=input()
  m=p.split()
  name=m[0]
  time=m[6]
  time1,time2=time.split(":")
  newTime=int(time1)*60 + int(time2)
  a=(name,-newTime,i,p)
  final.append(a)

sortedFinal=sorted(final)
for i in sortedFinal:
  print(i[3])