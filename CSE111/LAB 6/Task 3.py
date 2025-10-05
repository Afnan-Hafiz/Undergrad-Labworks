class Vaccine:
    def __init__(self,vaccine,country,interval):
        self.vaccine=vaccine
        self.interval=interval
        self.country=country
class Person:
    def __init__(self,name,age,type="General Citizen"):
        self.name=name
        self.age=age
        self.type=type
        self.given=""
        self.first="Not Given"
        self.second="Not Given"
    def pushVaccine(self,vac,dose="1st dose"):
      if self.type=="Student" or self.age>=25:
           if dose=="1st dose":
            self.given=vac.vaccine
            self.first="Given"
            self.second=f"Please come after {vac.interval} days"
            print(f"1st dose done for {self.name}")
           else:
              if vac.vaccine==self.given:
                  self.second="Given"
                  print(f"2nd dose done for {self.name}")
              else:
                  print(f"Sorry {self.name}, you can’t take 2 different vaccines")
      else:
          print(f"Sorry {self.name}, Minimum age for taking vaccines is 25 years now.")
    def showDetail(self):
        print(f"Name: {self.name} Age: {self.age} Type:{self.type}")
        print(f"Vaccine name: {self.given}")
        print(f"1st dose:{self.first}")
        print(f"2nd dose: {self.second}")




#DRIVER CODE STARTS/////////////////////////////////////////////////
astra = Vaccine("AstraZeneca", "UK", 60)
modr = Vaccine("Moderna", "UK", 30)
sin = Vaccine("Sinopharm", "China", 30)
p1 = Person("Bob", 21, "Student")
print("=================================")
p1.pushVaccine(astra)
print("=================================")
p1.showDetail()
print("=================================")
p1.pushVaccine(sin, "2nd Dose")
print("=================================")
p1.pushVaccine(astra, "2nd Dose")
print("=================================")
p1.showDetail()
p2 = Person("Carol", 23, "Actor")
print("=================================")
p2.pushVaccine(sin)
print("=================================")
p3 = Person("David", 34)
print("=================================")
p3.pushVaccine(modr)
print("=================================")
p3.showDetail()
print("=================================")
p3.pushVaccine(modr, "2nd Dose")
#DRIVER CODE ENDS/////////////////////////////////////////////////