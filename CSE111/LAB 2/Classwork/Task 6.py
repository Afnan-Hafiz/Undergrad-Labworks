def str1(x):
  temp1=""
  for i in range(len(x)):
    temp1+=chr(ord(x[i]-32))
    if x[i]=="i":
      temp1+=chr(ord(x[i]-32))
    elif x[i]=="." or "?":
      temp1+=chr(ord(x[i+2]-32))
    else:
      temp1+=i
    return temp
print(str("My fa"))