def bmi(hcm,weight):
  heightm=hcm/100
  BMI=weight/(heightm**2)
  if BMI<18.5:
    what="underweight"
  elif 18.5<=BMI<=24.9:
    what="Normal"
  elif 25<=BMI<=30:
    what="overweight"
  elif 30<=BMI:
    what="OBESE"
  return (f"score is {BMI:.1f}.You are {what}")
a=bmi(175,96)
print(a)