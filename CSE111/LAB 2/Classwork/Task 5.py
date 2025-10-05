def days(n):
  year=n//365
  remaining=n%365
  months=remaining//30
  days=remaining%30
  return (f"{year} years, {months} months and {days} days")
print(days(4320))
