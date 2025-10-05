class SultansDine:
  branch=0
  total=0
  name=[]
  def __init__(self,n):
    self.name=n
    self.total=0
    SultansDine.branch+=1
    SultansDine.name.append(self)
  def sellQuantity(self,q):
    self.quantity=q
    if q<10:
      self.total+= q*300
      SultansDine.total+=q*300
    elif 10<=q<=20:
      self.total+=q*350
      SultansDine.total+=q*350
    else:
      self.total+=q*400
      SultansDine.total+=q*400

  def branchInformation(self):
    print(f"Branch Name: {self.name}")
    print(f"Branch Sell: {self.total} Taka")

  @classmethod
  def details(cls):
    print(f"Total Number of branch(s): {cls.branch}")
    print(f"Total Sell: {cls.total} Taka")

    for i in cls.name:
      print(f"Branch Name: {i.name}, Branch Sell: {i.total} Taka")
      print(f"Branch consists of total sell's: {((i.total/cls.total)* 100):.2f} %")


#DRIVER CODE
SultansDine.details()
print('########################')
dhanmondi = SultansDine('Dhanmondi')
dhanmondi.sellQuantity(25)
dhanmondi.branchInformation()
print('-----------------------------------------')
SultansDine.details()
print('========================')
baily_road = SultansDine('Baily Road')
baily_road.sellQuantity(15)
baily_road.branchInformation()
print('-----------------------------------------')
SultansDine.details()
print('========================')
gulshan = SultansDine('Gulshan')
gulshan.sellQuantity(9)
gulshan.branchInformation()
print('-----------------------------------------')
SultansDine.details()