n=int(input())
student=[]
swap=0
id=input().split()
marks=input().split()
validID=[]
validMark=[]
for i in id:
  validID.append(int(i))
for i in marks:
  validMark.append(int(i))

for i in range(n):
  a=(-validMark[i],validID[i],i)
  student.append(a)
sortedStudent=sorted(student)

loc=[0]*n
for i in range(n):
    j=sortedStudent[i][2]
    loc[j]=i

track=[False]*n
for i in range(n):
  if track[i] or loc[i]==i:
    continue
  size=0
  j=i
  while not track[j]:
      track[j] = True
      j = loc[j]
      size+=1

  if size>1:
    swap+=size-1

print(f"Minimum swaps: {swap}")
for i in range(n):
  print(f"ID: {sortedStudent[i][1]} Mark: {-sortedStudent[i][0]}")

