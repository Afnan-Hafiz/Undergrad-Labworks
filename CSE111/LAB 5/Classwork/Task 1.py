class Student:
  def __init__(self,name,id,dept="CSE"):
    self.names=name
    self.id=id
    self.dept=dept
    self.suggestion=""
  def dailyEffort(self,hours):
    self.hours=hours
    if hours<=2:
      self.suggestion= 'Should give more effort!'
    elif  hours <= 4 :
      self.suggestion= 'Keep up the good work!'
    else:
      self.suggestion=  'Excellent! Now motivate others.'

  def  printDetails(self):
    print(f"Name: {self.names}\nID: {self.id}\nDepartment: {self.dept}\nDaily Effort: {self.hours} hour(s) \nSuggestion: {self.suggestion}")

#DRIVER CODE STARTS/////////////////////////////////////////////////
harry = Student('Harry Potter', 123)
harry.dailyEffort(3)
harry.printDetails()
print('========================')
john = Student("John Wick", 456, "BBA")
john.dailyEffort(2)
john.printDetails()
print('========================')
naruto = Student("Naruto Uzumaki", 777,
"Ninja")
naruto.dailyEffort(6)
naruto.printDetails()
#DRIVER CODE ENDS/////////////////////////////////////////////////
