# TRACING
class Student:
  def init(self):
    self.name = None
    self.cgpa = 0.0
s1 = Student()
s2 = Student()
s3 = None
print(s3)
s1.name = "Student One"
s1.cgpa = 2.3
s3 = s1
s2.name = "Student Two"
s2.cgpa = s3.cgpa + 1
s3.name = "New Student"
print(s1.name)
print(s2.name)
print(s3.name)
print(s1.cgpa)
print(s2.cgpa)
print(s3.cgpa)
s3 = s2
s1.name = "old student"
s2.name = "older student"
s3.name = "oldest student"
s2.cgpa = s1.cgpa - s3.cgpa + 4.5
print(s1.name)
print(s2.name)
print(s3.name)
print(s1.cgpa)
print(s2.cgpa)
print(s3.cgpa)