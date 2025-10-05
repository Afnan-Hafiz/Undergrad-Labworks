d1 = {"a": 100, "b": 100, "c": 200, "d": 300}
d2 = {"a": 300, "b": 200, "d": 400, "e": 200}
lst = []
for k in d2.keys():
  if k in d1:
    d1[k] = d1[k] + d2[k]
  else:
    d1[k] = d2[k]
for v in d1.values():
  lst.append(v)
for i in lst:
  for j in range(len(lst)-1):
    if lst[j] > lst[j+1]:
      lst[j],lst[j+1] = lst[j+1],lst[j]
unique_dict = {}
for v in lst:
  unique_dict[v] = None
unique_dict = tuple(unique_dict.keys())
print(d1)
print("Values:",unique_dict)