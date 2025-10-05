class Spaceship:
    def __init__(self,n,c):
        self.name=n
        self.capacity=c
        self.l1=[]
        self.c_w=0
        self.x=self.capacity

    def load_cargo(self,x):
        a=self.capacity
        b=x.getWeight()
        if (a-b) >=0:
            self.l1.append(x.getName())
            self.x=self.x-b
            self.c_w+=b
        else:
            print(f'Warning: Unable to load {x.getName()} inside\n{self.name}. Exceeds capacity by {b-self.x}')

    def display_details(self):
        print(f'Spaceship Name: {self.name}')
        print(f'Capacity: {self.capacity}')
        print(f'Current Cargo Weight: {self.c_w}')
        print(f'Cargo: {self.l1}')

class Cargo:
    def __init__(self,n,w):
        self.__name= n
        self.__weight= w

    def getWeight(self):
        return self.__weight

    def getName(self):
        return self.__name

# Creating spaceships
falcon = Spaceship("Falcon", 50000)
apollo = Spaceship("Apollo", 100000)
enterprise = Spaceship("Enterprise", 220000)
print("1.===================================")
# Creating cargo
gold = Cargo("Gold", 20000)
platinum = Cargo("Platinum", 25000)
dilithium = Cargo("Dilithium", 50000)
trilithium = Cargo("Trilithium", 70000)
neutronium = Cargo("Neutronium", 80000)
print("2.===================================")
# Loading cargo onto spaceships
falcon.load_cargo(gold)
falcon.load_cargo(platinum)
falcon.display_details()
print("3.===================================")
apollo.load_cargo(gold)  # Apollo will not reach its total capacity
apollo.display_details()
print("4.===================================")
falcon.load_cargo(neutronium)  # This should exceed Falcon's capacity
print("5.===================================")
enterprise.load_cargo(dilithium)
enterprise.load_cargo(trilithium)
enterprise.load_cargo(neutronium)  # This should not exceed Enterprise's capacity
enterprise.display_details()

