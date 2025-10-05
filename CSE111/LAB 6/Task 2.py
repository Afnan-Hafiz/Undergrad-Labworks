class Student:
  def __init__(self,name,id,cg):
    self.name=name
    self.id=id
    self.cg=cg
  def setId(self,update):
    self.id=update
class Department:
  def __init__(self,dept):
    self.dept=dept
    self.stud={}
  def addStudent(self,*args):
    for i in args:
      if int(i.id) in self.stud.keys():
        print("Student with the same ID already exists, Please try with another ID")
      else:
        self.stud[int(i.id)]=[i.name,i.cg]
        print(f"Welcome to {self.dept} department, {i.name}")
  def findStudent(self,id):
    if id in self.stud.keys():
      print("Student info:")
      print(f"Student Name: {self.stud[id][0]}")
      print(f"ID: {id}")
      print(f"CGPA: {self.stud[id][1]}")
    else:
      print(f"Student with this ID doesn't exist, Please give a valid ID")
  def details(self):
    print(f"Department Name: {self.dept}")
    print(f"Number of student:{len(self.stud)}")
    print("Details of the students:")
    for k,v in self.stud.items():
      print(f"Student name: {self.stud[k][0]}, ID:{k}, cgpa:{self.stud[k][1]}")
#DRIVER CODE STARTS/////////////////////////////////////////////////

s1 = Student("Akib", 22301010, 3.29)
s2 = Student("Reza", 22101010, 3.45)
s3 = Student("Ruhan", 23101934, 4.00)
print("1==================================")
cse = Department("CSE")
cse.findStudent(22112233)
print("2==================================")
cse.addStudent(s1,s2,s3)
print("3==================================")
cse.details()
print("4==================================")
cse.findStudent(22301010)
print("5==================================")
s4 = Student("Nakib",22301010,3.22)
cse.addStudent(s4)
print("6==================================")
s4.setId(21201220)
cse.addStudent(s4)
print("7==================================")
cse.details()
print("8==================================")
s5 = Student("Sakib",22201010,2.29)
cse.addStudent(s5)
print("9==================================")
cse.details()

#DRIVER CODE ENDS/////////////////////////////////////////////////