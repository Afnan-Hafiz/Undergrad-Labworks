class Student:
  def __init__(self, name, cg, credit=9,dept="CSE"):
    self.name=name
    self.cg=float(cg)
    self.credit=int(credit)
    self.dept=dept


  def checkScholarshipEligibility(self):
     self.scholarship=""
     if self.cg >=3.5 and self.credit >10:
      if self.cg >=3.7:
        print(f"{self.name} is eligible for Merit based scholarship.")
        self.scholarship= "Merit-based scholarship"
      elif 3.5<= self.cg <3.7 :
        print(f"{self.name} is eligible for Need-based scholarship.")
        self.scholarship= "Need-basedscholarship"
     else:
      print(f"{self.name} is not eligible for scholarship.")
      self.scholarship= "No scholarship"

  def showDetails(self):
    print(f"Name: {self.name}")
    print(f"Department: {self.dept}")
    print(f"CGPA: {self.cg}")
    print(f"Number of Credits: {self.credit}")
    print(f"Scholarship Status: {self.scholarship}")

#DRIVER CODE STARTS/////////////////////////////////////////////////
print('--------------------------')
std1 = Student("Alif", 3.99, 12)
print('--------------------------')
std1.checkScholarshipEligibility()
print('--------------------------')
std1.showDetails()
print('--------------------------')
std2 = Student("Mim", 3.4)
std3 = Student("Henry", 3.5, 15,"BBA")
print('--------------------------')
std2.checkScholarshipEligibility()
print('--------------------------')
std3.checkScholarshipEligibility()
print('--------------------------')
std2.showDetails()
print('--------------------------')
std3.showDetails()
print('--------------------------')
std4 = Student("Bob", 4.0, 6, "CSE")
print('--------------------------')
std4.checkScholarshipEligibility()
print('--------------------------')
std4.showDetails()
#DRIVER CODE ENDS/////////////////////////////////////////////////