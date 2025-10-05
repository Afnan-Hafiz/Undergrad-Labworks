class Exam:
  def __init__(self,marks):
    self.marks = marks
    self.time = 60
  def examSyllabus(self):
    return "Maths , English"
  def examParts(self):
    return "Part 1 - Maths\nPart 2 - English\n"

class ScienceExam(Exam):
  def __init__(self,marks,time,*args):
    super().__init__(marks)
    self.time=time
    self.subject=args

  def examSyllabus(self):
    a=super().examSyllabus()
    if self.subject:
      b=", ".join(self.subject)
      return f"{a} {b}"
    else:
      return a

  def examParts(self):
    a= super().examParts()
    for i in range(len(self.subject)):
       a+= f"Part {i+3} - {self.subject[i]}\n"
    return a

  def __str__(self):
    return f"Marks: {self.marks} Time: {self.time} minutes Numberof Parts: {len(self.subject)+2}"



engineering = ScienceExam(100,90,"Physics","HigherMaths")
print(engineering)
print('----------------------------------')
print(engineering.examSyllabus())
print(engineering.examParts())
print('==================================')
architecture =ScienceExam(100,120,"Physics","HigherMaths","Drawing")
print(architecture)
print('----------------------------------')
print(architecture.examSyllabus())
print(architecture.examParts())