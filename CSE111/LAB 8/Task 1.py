class Student:
  ID = 0
  def __init__(self,name,dept,age,cgpa):
    Student.ID += 1
    self.name = name
    self.cgpa = cgpa
    self.dept = dept
    self.age = age
  def showDetails(self):
    print(f"Id: {Student.ID}")
    print(f"Name: {self.name}")
    print(f"Department: {self.dept}")
    print(f"Age: {self.age}")
    print(f"CGPA: {self.cgpa}")
  @classmethod
  def from_String(cls,string):
    cls.ID += 1
    lst = string.split("-")
    name = lst[0]
    dept = lst[1]
    age = lst[2]
    cgpa = lst[3]
    return cls(name,dept,age,cgpa)

    
s1 = Student("Samin", "CSE", 21, 3.91)
s1.showDetails()
print("-----------------------")
s2 = Student("Fahim", "ECE", 21, 3.85)
s2.showDetails()
print("-----------------------")
s3 = Student("Tahura", "EEE", 22, 3.01)
s3.showDetails()
print("-----------------------")
s4 = Student.from_String("Sumaiya-BBA-23-3.96")
s4.showDetails()