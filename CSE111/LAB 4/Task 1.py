class Customer:
    def __init__(self):
        print("Welcome to ABC Memorial Park ")
        self.list1=[]
        self.list2=[]
    def buyTicket(self,n,a):
        self.list1.append(n)
        self.list2.append(a)
        if len(self.list1)>3:
            print('You cant buy more than 3 tickets')
            self.list2.pop()
        else:
            print(f'Successfully purchased a ticket for {n}!')
    def showDetails(self):
        if len(self.list1)>3:
            print(f'Amount of tickets: {3}')
        else:
            print(f'Amount of tickets: {2}')
        total=0
        for i in self.list2:
            if i>10:
                total+=100
            else:
                total+=50
        print(f'Total price: {total} Taka')



#DRIVER CODE STARTS///////////////////////////////////////////////////
print('1-------------------------')
customer1 = Customer()
print('2-------------------------')
customer1.buyTicket('Bob', 23)
customer1.buyTicket('Henry', 7)
customer1.buyTicket('Alexa', 30)
customer1.buyTicket('Jonas', 43)
print('3-------------------------')
customer1.showDetails()
print('4-------------------------')
customer2 = Customer()
print('5-------------------------')
customer2.buyTicket('Harry', 60)
customer2.buyTicket('Tomas', 28)
print('6-------------------------')
customer2.showDetails()
#DRIVER CODE ENDS///////////////////////////////////////////////////