class Department:
  def __init__(self,name="ChE Department",sec=int(5)):
    self.name=name
    self.sec=sec
    self.stud=[]
    self.sum=0
    print(f"The {self.name} Department has {self.sec} sections.")
  def add_students(self,*args):
    if self.sec==len(args):
      for i in args:
        self.stud.append(i)
        self.sum+=i
      print(f"The {self.name} has an average of {round(self.sum/len(self.stud),2)} students in each section.")
    else:
      print(f"The {self.name} doesn't have {len(args)} sections.")
  def merge_Department(self,*args):
    for i in args:
      self.stud.extend(i.stud)
      print(f"{i.name} is merged to {self.name} Department.")
      self.sum+=i.sum
    return(f"Now The {self.name} has an average of {round(self.sum/(self.sec),2)} students in each section.")

#DRIVER CODE
d1 = Department()
print('1-----------------------------')
d2 = Department('MME Department')
print('2-----------------------------')
d3 = Department('NCE Department', 8)
print('3-----------------------------')
d1.add_students(12, 23, 12, 34, 21)
print('4-----------------------------')
d2.add_students(40, 30, 21)
print('5-----------------------------')
d3.add_students(12, 34, 41, 17, 30, 22, 32, 51)
print('6-----------------------------')
mega = Department('Engineering Department', 10)
print('7-----------------------------')
mega.add_students(21,30,40,36,10,32,27,51,45,15)
print('8-----------------------------')
print(mega.merge_Department(d1, d2))
print('9-----------------------------')
print(mega.merge_Department(d3))