class Student:
    def __init__(self,name,cg,course):
        self.name=name
        self.cgpa=cg
        self.courses_taken=course
        self.student_status=''
        self.advising_status=''
        if self.cgpa>3.00:
            self.student_status+='Regular'
            self.advising_status+='Approved'
            print('All the best, Clark, for the upcoming semester.')
        elif 2.00<self.cgpa<3.00:
            self.advising_status+='Denied'
            self.courses_taken=0
            print('Hello Diana, You are a regular student and have to take between 3 to 5 courses.')
        elif 1.60<self.cgpa<2.00:
            self.student_status+='Probation'
            self.advising_status+='Approved'
            print('Study hard this time, Barry.')
        elif self.cgpa<1.60:
            self.advising_status+='Denied'
            self.courses_taken=0
            print('Sorry, Bruce, you are on probation and cannot take more than 2 courses.')


#DRIVER CODE STARTS////////////////////////////////////////
s1 = Student("Clark", 3.45, 4)
print(f"Name: {s1.name}\nCGPA: {s1.cgpa}\nCourses Taken: {s1.courses_taken}")
print(f"Student Status: {s1.student_status}\nAdvising Status: {s1.advising_status}")
print("--------------------------------------------------------------------------------")
s2 = Student("Barry", 1.93, 2)
print(f"Name: {s2.name}")
print(f"Student Status: {s2.student_status}\nAdvising Status: {s2.advising_status}")
print("--------------------------------------------------------------------------------")
s3 = Student("Diana", 2.91, 2)
print(f"Advising Status: {s3.advising_status}\nCourses Taken: {s3.courses_taken}")
print("--------------------------------------------------------------------------------")
s4 = Student("Bruce", 1.52, 5)
print(f"Advising Status: {s4.advising_status}\nCourses Taken: {s4.courses_taken}")
#DRIVER CODE ENDS//////////////////////////////////////////