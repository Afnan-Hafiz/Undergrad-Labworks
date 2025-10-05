#Tracing
class A:
 temp = 4
 def __init__(self):
  self.y = self.temp - 2
  self.sum = self.temp + 1
  A.temp -= 2
  self.methodA(3, 4)
 def methodA(self, m, n):
  x = 0
  self.y = self.y + m + (self.temp)
  A.temp += 1
  x = x + 1 + n
  self.sum = self.sum + x + self.y
  print(x, self.y, self.sum)

class B:
 x = 0
 def __init__(self, b = None):
    self.y, self.temp, self.sum = 5, -5, 2

    if b == None:
      self.y = self.temp + 3

      self.sum = 3 + self.temp + 2
      self.temp -= 2
    else:
      self.sum = b.sum
      B.x = b.x
      b.methodB(2, 3)
 def methodA(self, m, n):
  x = 2
  self.y = self.y + m + (self.temp)
  self.temp += 1
  x = x + 5 + n
  self.sum = self.sum + x + self.y
  print(x, self.y, self.sum)
 def methodB(self, m, n):
  y = 0
  y = y + self.y
  B.x = self.y + 2 + self.temp
  self.methodA(self.x, y)
  self.sum = self.x + y + self.sum
  print(self.x, y, self.sum)
a1 = A()
b1 = B()
b2 = B(b1)
b1.methodA(1,2)
b2.methodB(3,2)