d1 = {"a":10,"b": 20,"c": 20,"d": 30,"e": 10,"f": 50,"g": 90}
lst = []
for v in d1.values():
  lst.append(v)
d1 = {}
for i in lst:
  if i in d1:
    d1[i] += 1
  else:
    d1[i] = 1
for num, freq in d1.items():
  print(num,"-", freq, "times")