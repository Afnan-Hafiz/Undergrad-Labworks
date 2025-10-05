def replace_domain(email,newDomain, fixed="kaaj.com"):
  rep=email.split("@")
  temp=''
  if rep[1]==fixed:
    temp=rep[0]+"@"+newDomain
    return (f"Changed: {temp}")
  else:
    return (f"Unchanged: {email}")
a=replace_domain("alice@kaaj.com","sheba.xyz")
b=replace_domain("bob@sheba.xyz","sheba.xyz")
print(a)
print(b)
