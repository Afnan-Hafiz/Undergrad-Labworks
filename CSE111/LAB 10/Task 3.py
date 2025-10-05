class KK_tea:
  dict1={}
  def __init__(self,p,t=50,n="Regular"):
    self.price=p
    self.name=f"KK {n} Tea"
    self.teabags=t
    self.weight= self.teabags*2
    self.status=False
    self.dict1[self.name]=0

  def product_detail(self):
    print(f"Name: {self.name}, Weight: {self.weight}")
    print(f"Tea Bags: {self.teabags}, Price: {self.price}")
    print(f"Status: {self.status}")

  @classmethod
  def total_sales(cls):
    print(f"Total sales: {cls.dict1}")

  @classmethod
  def update_sold_status_regular(cls, *args):
    for i in args:
      i.status=True
      cls.dict1[i.name]+=1

class KK_flavoured_tea (KK_tea):
  def __init__(self,f,p,t):
    super().__init__(p,t,f)

  @classmethod
  def update_sold_status_flavoured(cls, *args):
    for i in args:
      super().update_sold_status_regular(i)


t1 = KK_tea(250)
print("-----------------1-----------------")
t1.product_detail()
print("-----------------2-----------------")
KK_tea.total_sales()
print("-----------------3-----------------")
t2 = KK_tea(470, 100)
t3 = KK_tea(360, 75)
KK_tea.update_sold_status_regular(t1, t2, t3)
print("-----------------4-----------------")
t3.product_detail()
print("-----------------5-----------------")
KK_tea.total_sales()
print("-----------------6-----------------")
t4 = KK_flavoured_tea("Jasmine", 260, 50)
t5 = KK_flavoured_tea("Honey Lemon", 270, 45)
t6 = KK_flavoured_tea("Honey Lemon", 270, 45)
print("-----------------7-----------------")
t4.product_detail()
print("-----------------8-----------------")
t6.product_detail()
print("-----------------9-----------------")
KK_flavoured_tea.update_sold_status_flavoured(t4,
t5, t6)
print("-----------------10-----------------")
KK_tea.total_sales()
