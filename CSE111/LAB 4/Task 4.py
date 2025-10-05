class StudentDatabase:
  def __init__(self,name,id):
    self.name=name
    self.id=id
    self.grades={}

  def calculateGPA(self,mylist,session):
    dict1={}

    a=": ".join(mylist)
    b=a.split(": ")

    list1=[]
    for i in b[::2]:
      list1.append(i)
    list1=tuple(list1)

    cgpa=0
    for i in b[1::2]:
      cgpa+=float(i)*3
    cgpa=cgpa/(len(mylist)*3)
    cgpa=round(cgpa,2)

    dict1[list1]=cgpa
    self.grades[session]=dict1

  def printDetails(self):
    print(f"Name: {self.name}")
    print(f"ID: {self.id}")
    for i in range(len(self.grades)):
        session=list(self.grades.keys())[i]
        print(f"Courses taken in {session}:")
        a=self.grades[session]
        b=list(a.keys())[0]
        for j in b:
            print(j)
        print(f"GPA: {a[b]}")






#DRIVER CODE STARTS///////////////////////////////////////////////////
s1 = StudentDatabase('Pietro', '10101222')
s1.calculateGPA(['CSE230: 4.0', 'CSE220: 4.0','MAT110: 4.0'], 'Summer2020')
s1.calculateGPA(['CSE250: 3.7', 'CSE330: 4.0'],
'Summer2021')
print(f'Grades for {s1.name}\n{s1.grades}')
print('---------------------------------')
s1.printDetails()
s2 = StudentDatabase('Wanda', '10103332')
s2.calculateGPA(['CSE111: 3.7', 'CSE260: 3.7','ENG101: 4.0'], 'Summer2022')
print('---------------------------------')
print(f'Grades for {s2.name}\n{s2.grades}')
print('---------------------------------')
s2.printDetails()
#DRIVER CODE ENDS///////////////////////////////////////////////////
