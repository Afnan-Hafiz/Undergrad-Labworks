#5
inp = input()
low = []
upp = []
even = []
odd = []
ans = []
for i in inp:
  if ord("a")<=ord(i)<=ord("z"):
    low.append(i)
  elif ord("A")<=ord(i)<=ord("Z"):
    upp.append(i)
  elif int(i) % 2 != 0:
    odd.append(i)
  else:
    even.append(i)
for i in range(len(low)-1):
    for j in range(len(low)-1):
      if low[j] > low[j+1]:
        low[j],low[j+1] = low[j+1],low[j]
for i in range(len(upp)-1):
    for j in range(len(upp)-1):
      if upp[j] > upp[j+1]:
        upp[j],upp[j+1] = upp[j+1],upp[j]
for i in range(len(even)-1):
    for j in range(len(even)-1):
      if even[j] > even[j+1]:
        even[j],even[j+1] = even[j+1],low[j]
for i in range(len(odd)-1):
    for j in range(len(odd)-1):
      if odd[j] > odd[j+1]:
        odd[j],odd[j+1] = odd[j+1],odd[j]
for i in low:
  ans.append(i)
for i in upp:
  ans.append(i)
for i in odd:
  ans.append(i)
for i in even:
  ans.append(i)
for i in ans:
  print(i,end="")