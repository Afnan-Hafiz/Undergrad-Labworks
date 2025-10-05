inp = input()
inp1 = input()
d1 = {}
d2 = {}
lst = []
lst1 = []
for i in inp:
  lst.append(i)
for k in lst:
  d1[k] = None
for i in inp1:
  lst1.append(i)
for k in lst1:
  d2[k] = None
if d1 == d2:
  print("They are anagrams")
else:
  print("They are not anagrams")