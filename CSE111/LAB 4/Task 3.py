class GreenPhone:
  def __init__(self,m,v,c):

    self.model=m
    self.version=v
    self.camera=c

    self.a=2
    self.m=3
    self.u=4
    self.x=0

  def showSpecification(self):
    print("Phone Company: GreenPhone")
    print(f"Model Name: {self.model}")
    print(f"Android Version: {self.version}")
    print(f"Number of Cameras: {self.camera}")

  def updatePhone(self):
    if self.model[0]=="A":
      if self.x<self.a:
        print(f"Your phone Greenphone {self.model} is upgraded to Android Version: {self.version+1}.")
        self.x+=1
        self.version+=1
      else:
        print(f'Your phone Greenphone {self.model} is already up to date.')

    elif self.model[0]=='M':
        if self.x<self.m:
                print(f'Your phone Greenphone {self.model} is upgraded to Android Version: {self.version+1}.')
                self.x+=1
                self.version+=1
        else:
            print(f'Your phone Greenphone {self.model} is already up to date.')

    elif self.model[0]=='U':
        if self.x<self.u:
                print(f'Your phone Greenphone {self.model} is upgraded to Android Version: {self.version+1}.')
                self.x+=1
                self.version+=1
        else:
            print(f'Your phone Greenphone {self.model} is already up to date.')
#DRIVER CODE STARTS///////////////////////////////////////////////////
print('1=======================')
p1 = GreenPhone('A1', 12, 3)
p2 = GreenPhone('M11', 12, 4)
p3 = GreenPhone('U20', 12, 5)
p1.showSpecification()
print('2=======================')
p2.showSpecification()
print('3=======================')
p1.updatePhone()
print('4=======================')
p1.updatePhone()
p2.updatePhone()
p3.updatePhone()
print('5=======================')
p1.updatePhone()
p2.updatePhone()
p3.updatePhone()
print('6=======================')
p2.updatePhone()
p3.updatePhone()
print('7=======================')
p1.showSpecification()
p3.showSpecification()
#DRIVER CODE ENDS///////////////////////////////////////////////////
