d = {"key1" : "value1", "key2" : "value2", "key3" : "value1"}
new_d = {}
for k,v in d.items():
  if v not in new_d:
    new_d[v] = [k]
  else:
    new_d[v].append(k)
print(new_d)