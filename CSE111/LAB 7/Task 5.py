class BracuStudent:
    def __init__(self, name, home):
        self.name = name
        self.home = home
        self.bus_pass = False

    def show_details(self):
        print(f"Student Name: {self.name}")
        print(f"Lives in {self.home}")
        print(f"Have Bus Pass? {self.bus_pass}")

    def get_pass(self):
        self.bus_pass = True
        return self.bus_pass



class BracuBus:
    def __init__(self, home, max_capacity=2):
        self.home = home
        self.max = max_capacity
        self.passengers = []

    def show_details(self):
        print(f"Bus Route: {self.home}")
        print(f"Passengers Count: {len(self.passengers)} (Max: {self.max})")
        print(f"Passengers On Board: {self.passengers}")

    def board(self, *students):
        if len(students)==0:
          print("No passengers!")

        else:
            for student in students:
                if student.home == self.home and student.bus_pass:
                    if len(self.passengers)<self.max:
                      self.passengers.append(student.name)
                      print(f"{student.name} boarded the bus.")
                    else:
                        print("Bus is full!")
                elif not student.bus_pass:
                    print(f"You don't have a bus pass!")
                    print(f"You got on the wrong bus!.")


#DRIVER CODE
st1 = BracuStudent("Afif", "Mirpur")
print("1===========================")
st2 = BracuStudent("Shanto", "Motijheel")
st3 = BracuStudent("Taskin", "Mirpur")
st1.show_details()
st2.show_details()
print("2===========================")
st3.show_details()
print("3===========================")
bus1 = BracuBus("Mirpur")
bus2 = BracuBus("Azimpur", 5)
bus1.show_details()
bus2.show_details()
print("4===========================")
st2.get_pass()
st3.get_pass()
print("5===========================")
st2.show_details()
st3.show_details()
print("6===========================")
bus1.board()
print("7===========================")
bus1.board(st1, st2)
print("8===========================")
st1.get_pass()
st2.home = "Mirpur"
st1.show_details()
st2.show_details()
print("9===========================")
bus1.board(st1, st2, st3)
print("10===========================")
bus1.show_details()