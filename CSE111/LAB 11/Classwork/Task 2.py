class Point:
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y
    self.area = 0


  def calculate_area(self):
    return self.area


  def print_details(self):
    print("--------- Printing details ----------")
    print(f'Co-ordinate: ({self.x},{self.y})')
    print(f'Area: {self.area}')

class Circle(Point):
  def __init__(self,r, x=0, y=0):
    super().__init__(x,y)
    self.r = r
    self.area = 3.1416*(r)**2
  def print_details(self):
    super().print_details()
    print(f"Radius: {self.r}")
class Sphere(Circle):
  def __init__(self,r, x=0, y=0):
    super().__init__(r,x,y)
    self.area *= 4

print("--------------1---------------")
p1 = Point(2,3)
print(f'Area of p1: {p1.calculate_area()}')
print("--------------2---------------")
p1.print_details()
print("--------------3---------------")
p2 = Point()
p2.print_details()
print("--------------4---------------")
c1 = Circle(4,0,3)
print(f'Area of c1: {c1.calculate_area()}')
print("--------------5---------------")
c1.print_details()
print("--------------6---------------")
c2 = Circle(7)
print(f'Area of c2: {c2.calculate_area()}')
print("--------------7---------------")
sph1 = Sphere(3,0,2)
print(f'Area of sph1: {sph1.calculate_area()}')
print("--------------8---------------")
sph1.print_details()
print("--------------9---------------")
sph2 = Sphere(6)
print(f'Area of sph2: {sph2.calculate_area()}')
