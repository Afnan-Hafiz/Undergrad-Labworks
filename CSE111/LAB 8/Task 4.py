#4
class Student:
  total=0
  BracStudents=0
  otherStudents=0
  def __init__(self,n,d,uni="BRAC University"):
    self.name=n
    self.dept=d
    self.uni=uni
    Student.total+=1
    if self.uni=="BRAC University":
      Student.BracStudents+=1
    else:
      Student.otherStudents+=1




  def individualDetail(self):
    print(f"Name: {self.name}")
    print(f"Department: {self.dept}")
    print(f"Institution: {self.uni}")



  @classmethod
  def printDetails(cls):
    print(f"Total Student(s):{cls.total}")
    print(f"BRAC University Student(s): {cls.BracStudents}")
    print(f"Other Institution Student(s):{cls.otherStudents}")

  @classmethod
  def createStudent(cls,p,d,uni="BRAC University"):
    return cls(p,d,uni)


Student.printDetails()
print('#########################')

mikasa = Student('Mikasa Ackerman', "CSE")
mikasa.individualDetail()
print('------------------------------------------')
Student.printDetails()

print('========================')

harry = Student.createStudent('Harry Potter', "Defence Against Dark Arts", "Hogwarts School")
harry.individualDetail()
print('-------------------------------------------')
Student.printDetails()

print('=========================')

levi = Student.createStudent("Levi Ackerman", "CSE")
levi.individualDetail()
print('--------------------------------------------')
Student.printDetails()

