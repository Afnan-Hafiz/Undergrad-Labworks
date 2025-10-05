class Cakes:
  order_list={}
  feedback={}
  custom="Cake"
  def __init__(self,n,w):
    self.name=n
    self.weight=w
    self.order_list[f"{self.name} Cake {self.weight}gm"]=1
    self.price=1200*(self.weight/1000)
    self.sweetness="Moderate"
    self.cream="Whipped Cream"
    if self.custom=="Cheese Cake":
      self.price-=self.price*(10/100)

  def add_customization(self,s="Moderate sugar",t="Whipped Cream"):
    self.sweetness=s
    self.cream=t
    if self.custom=="Cheese Cake":
      print("Sorry! No customization available for cheese cakes.")

  @classmethod
  def give_feedbacks(cls,n,review):
    cls.name=n
    cls.review=review
    if cls.name in cls.feedback.keys():
      cls.feedback[cls.name].append(cls.review)
    else:
      cls.feedback[cls.name]=[cls.review]
    print("Thanks for your valuable feedback!")

  @classmethod
  def show_feedbacks(cls):
    print(cls.feedback)

  def cake_details(self):
    print(f"Flavor: {self.name} {self.custom}, Weight: {self.weight} gm")
    print(f"Sweetness: {self.sweetness} sugar, Cream Type: {self.cream}")
    if self.custom=="Cake":
     print(f"Price: {self.price} Taka")


class Cheese_Cakes(Cakes):
  custom="Cheese Cake"
  def __init__(self,n,w,ord='baked'):
    super().__init__(n,w)
    self.baketype=ord
    self.price=1500*(self.weight/1000)
    self.cream="Cream Cheese"

  def cake_details(self):
    super().cake_details()
    print(f"Cake Type:{self.baketype}, Price: {self.price} Taka")

  @classmethod
  def give_feedbacks(cls,n,review=None):
    cls.name=n
    cls.review=review
    super().give_feedbacks(n,review)
    print("You will get 10% discount for your next purchase!")

order_1=Cakes("Chocolate",500)
order_2=Cakes("Vanilla",800)
print("(1)**********************************")
order_1.cake_details()
print("(1.1)**********************************")
print(Cakes.order_list)
print("(2)**********************************")
order_2.add_customization("Zero","Butter Cream")
order_2.cake_details()
print("(3)**********************************")
Cakes.give_feedbacks("Chocolate Cake","Very Delicious")
Cakes.give_feedbacks("Chocolate Cake","Yummy")
print("(4)**********************************")
Cakes.show_feedbacks()
print("(5)**********************************")
ch_order1=Cheese_Cakes("Red velvet",700)
ch_order1.cake_details()
print("(6)**********************************")
ch_order1.add_customization()
print("(7)**********************************")
ch_order2=Cheese_Cakes("Blue Berry",900,"No Bake")
ch_order2.cake_details()
print("(8)**********************************")
print(Cakes.order_list)
print("(9)**********************************")
Cheese_Cakes.give_feedbacks("Red velvet Cheese Cake","Average")
Cheese_Cakes.give_feedbacks("Blue Berry Cheese Cake","Liked it")
print("(10)**********************************")
Cakes.show_feedbacks()