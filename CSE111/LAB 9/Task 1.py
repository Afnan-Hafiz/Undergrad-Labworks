#1
class NikeBangladesh:
  branch=[]
  total=0
  stocks={'Air Jordan': 0, 'Cortez': 0, 'Zoom Kobe': 0}

  def __init__(self,n):
    self.name=n
    self.instock={'Air Jordan': 0, 'Cortez': 0, 'Zoom Kobe': 0}
    self.total=0
    NikeBangladesh.branch.append(n)

  def details(self):
    print(f"Nike {self.name} outlet:")
    print("Products Currently Stocked:")
    print(f"{self.instock}")
    print(f"Sold: {self.total}")

  def restockProducts(self,r):
    for k,v in r.items():
      self.instock[k]+=v
      NikeBangladesh.stocks[k]+=v

  def productSold(self,p):
    for k,v in p.items():
      self.instock[k]-=v
      NikeBangladesh.stocks[k]-=v
      NikeBangladesh.total+=v
      self.total+=v



  @classmethod
  def status(cls):
    print("Nike Bangladesh Status:")
    print(f"Branches Opened: {cls.branch}")
    print("Currently Stocked")
    print(f"{cls.stocks}")
    print(f"Sold: {cls.total}")


#DRIVER CODE
print("xxxxxxxxxxxxxx1xxxxxxxxxxxxxxxx")
NikeBangladesh.status()
dhaka = NikeBangladesh("Dhaka Banani")
chittagong = NikeBangladesh("Chittagong GEC")
print("xxxxxxxxxxxxxx2xxxxxxxxxxxxxxxx")
dhaka.details()
print("xxxxxxxxxxxxxx3xxxxxxxxxxxxxxxx")
chittagong.details()
print("xxxxxxxxxxxxxx4xxxxxxxxxxxxxxxx")
dhaka.restockProducts(
{"Air Jordan":1200,"Cortez":200,"Zoom Kobe":200})
chittagong.restockProducts(
{"Air Jordan":1000,"Cortez":250,"Zoom Kobe":100})
print("xxxxxxxxxxxxxx5xxxxxxxxxxxxxxxx")
NikeBangladesh.status()
print("xxxxxxxxxxxxxx6xxxxxxxxxxxxxxxx")
dhaka.productSold({"Air Jordan":760,"Cortez":90})
chittagong.productSold({"Air Jordan":520,"Zoom Kobe":70})
print("xxxxxxxxxxxxxx7xxxxxxxxxxxxxxxx")
NikeBangladesh.status()