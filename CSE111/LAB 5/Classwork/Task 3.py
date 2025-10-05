class TaxiLagbe:
  def __init__(self,n,c):
    self.number=n
    self.coverage=c
    self.count=0
    self.name=()
    self.fare=0

  def addPassenger(self,*info):
    for i in info:
      name, fare=i.split('_')
      if len(self.name)<4:
        self.name+=(name,)
        self.fare+=int(fare)
        self.count+=1
        print(f'Dear {name}! Welcome to TaxiLagbe.')
      else:
        print('Taxi Full! No more passengers can be added.')

  def printDetails(self):
    name=''
    for i in self.name:
      if name=='':
        name+=i
      else:
        name+=', '+i
    print(f'Trip info for Taxi number: {self.number}')
    print(f'This taxi can only cover the {self.coverage} area.')
    print(f'Total passengers: {self.count}')
    print('Passenger lists:')
    print(name)
    print(f'Total collected fare: {self.fare} Taka')

#DRIVER CODE STARTS/////////////////////////////////////////////////
taxi1 = TaxiLagbe('1010-01', 'Dhaka')
print('-------------------------------')
taxi1.addPassenger('Walker_100',
'Wood_200','Matt_100')
taxi1.addPassenger('Wilson_105')
print('-------------------------------')
taxi1.printDetails()
print('-------------------------------')
taxi1.addPassenger('Karen_200')
print('-------------------------------')
taxi1.printDetails()
print('-------------------------------')
taxi2 = TaxiLagbe('1010-02', 'Khulna')
taxi2.addPassenger('Ronald_115', 'Parker_215')
print('-------------------------------')
taxi2.printDetails()
#DRIVER CODE ENDS/////////////////////////////////////////////////
