class Farmer:
  def __init__(self,n=None):
    self.unique=n
    if type(n)==str:
      print(f"Welcome to your farm, {self.unique}")
    elif type(n)==int:
      print(f"Welcome to your farm. Your farm ID is {self.unique}!")
    else:
      print("Welcome to your farm!")
    self.crop=[]
    self.fish=[]

  def addCrops(self,*args):
    q=len(args)
    if q==0:
      print("No crop(s) added.")
    else:
      print(f"{q} crop(s) added.")
    for i in args:
      self.crop.append(i)
  def addFishes(self,*args):
    w=len(args)
    if w==0:
      print("No fish added.")
    else:
      print(f"{w} fish(s) added.")
    for i in args:
      self.fish.append(i)
  def showGoods(self,*args):
    if len(self.crop)>0:
      print(f'You have {len(self.crop)} crop(s):')
      print(",".join(self.crop))
    else:
      print("You don't have any crop(s)")

    if len(self.fish)>0:
      print(f'You have {len(self.fish)} fish(s):')
      print(",".join(self.fish))
    else:
      print("You don't have any fish(s).")

#DRIVER CODE STARTS/////////////////////////////////////////////////
f1 = Farmer()
print("-------------------")
f1.addCrops('Rice', "Jute", "Cinnamon")
print("-------------------")
f1.addFishes()
print("-------------------")
f1.addCrops('Mustard')
print("-------------------")
f1.showGoods()
print("-------------------")
f2 = Farmer("Korim Mia")
print("-------------------")
f2.addFishes('Pangash', 'Magur')
print("-------------------")
f2.addCrops("Wheat", "Potato")
print("-------------------")
f2.addFishes("Koi", "Tuna", "Sardine")
print("-------------------")
f2.showGoods()
print("-------------------")
f3 = Farmer(2865127000)
print("-------------------")
f3.addCrops()
print("-------------------")
f3.addFishes("Katla")
print("-------------------")
f3.showGoods()
print("-------------------")
#DRIVER CODE ENDS/////////////////////////////////////////////////
