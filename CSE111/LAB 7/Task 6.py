class Library:
    def __init__(self, n, d1):
        self.name = n
        self.dict1 = d1
        self.borrower = {}

    def details(self):
        print(f'{self.name} Library details')
        print(f'Borrower details: \n{self.borrower}')
        print(f'Books availability:\n{self.dict1}')


class Reader:
    def __init__(self, n):
        self.name = n
        self.count = 0
        self.d1 = {}

    def borrow(self, l, *books):
        for i in books:
            if self.count < 5:
                if l.dict1[i] != 0:
                    l.dict1[i] -= 1
                    print(f'{i} book is borrowed successfully')
                    self.count += 1
                    if i not in self.d1:
                        self.d1[i] = 1
                    else:
                        self.d1[i] += 1
                else:
                    print(f'{i} books are not available at the moment')
            else:
                print('You cannot borrow more than 5 books.')

        if self.name not in l.borrower:
            l.borrower[self.name] = self.count

    def readerInfo(self, n=''):
        if n == '':
            print(f'{self.name}, you have {self.count} book(s) with you')
            for i in self.d1:
                print(f'Books on {i}: {self.d1[i]}')
        else:
            print(f'{self.name}, you have {self.d1[n]} {n} book(s) with you')




#Driver Code
L1=Library('Dhaka',{'Arts':15,'Fiction':135,'Politics':2,'Science':11,'Poetry':15})
L1.details()
print("1----------------------")
r1=Reader('Aladdin')
r1.borrow(L1,'Arts','Fiction','Fiction','Politics')
print("2----------------------")
r1.borrow(L1,'Politics','Fiction')
print("3----------------------")
r1.readerInfo()
print("4----------------------")
r1.readerInfo('Fiction')
print("5----------------------")
L1.details()
print("6----------------------")
r2=Reader('Jasmine')
r2.borrow(L1,'Politics','Poetry')
print("7----------------------")
r2.readerInfo()    #preader
print("8----------------------")
L1.details()