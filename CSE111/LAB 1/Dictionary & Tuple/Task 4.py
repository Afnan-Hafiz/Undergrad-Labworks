d = {}
inp = input()
inp = inp.lower()
for i in inp:
  c = 1
  if i == " ":
    continue
  elif i not in d.keys():
    d[i] = c
  else:
    c = d[i]+1
    d[i] = c
print(d)