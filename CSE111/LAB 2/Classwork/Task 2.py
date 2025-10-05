def order(name,place="Mohakhali"):
  # name=input()
  # place=input()

  if name=="BBQ Chicken Cheese Burger":
    meal_cost=250
  elif name=="Beef Burger":
    meal_cost=170


  elif name=="Naga Drums":
    meal_cost=200


  if place=="Mohakhali":
    delivery_charge=40

  else:
    delivery_charge=60

  total=meal_cost + delivery_charge +(meal_cost*8/100)
  return total
a=order("Beef Burger","Dhanmondi")
print(a)