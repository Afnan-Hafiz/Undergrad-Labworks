def is_james_bond(n):
  str1=''
  for i in n:
    if i==0 or 7:
      str1+=str(i)
    else:
      continue
  if str1=="007":
    return True
  else:
    return False
a= is_james_bond( [1, 2, 4, 0, 0, 7, 5] )
print(a)