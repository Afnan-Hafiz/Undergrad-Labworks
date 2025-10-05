class Sphere:
  def __init__(self,name,r=1, color="White"):
    self.name=name
    self.color=color
    self.radius=r
    self.volume=((4/3)*3.1416*(self.radius**3))

  def merge_sphere(self,*args):
    list1=[]
    for i in args:
      self.volume+=i.volume
      list1.append(i.color)
    for i in list1:
      if i!="White" or self.color!="White":
        self.color="Mixed Color"
    print("Spheres are being merged")


  def printDetails(self):
    print(f"Spherer ID: {self.name}")
    print(f"Color: {self.color}")
    print(f"Volume: {self.volume}")

#DRIVER CODE STARTS/////////////////////////////////////////////////
sphere1 = Sphere("Sphere 1")
print("1***************")
sphere1.printDetails()
print("2***************")
sphere2 = Sphere("Sphere 2", 3)
print("3***************")
sphere2.printDetails()
print("4***************")
sphere3 = Sphere("Sphere 3", 2)
print("5***************")
sphere3.printDetails()
print("6***************")
sphere3.merge_sphere(sphere1,sphere2)
print("7***************")
sphere3.printDetails()
print("8***************")
sphere4 = Sphere("Sphere 4", 5, "Purple")
print("9***************")
sphere4.merge_sphere(sphere3)
print("10***************")
sphere4.printDetails()

#DRIVER CODE ENDS/////////////////////////////////////////////////
