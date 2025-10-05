class Contacts:
    def __init__(self,names,num,d={}):
        self.name=names
        self.numbers=num
        self.contactDict=d
        if len(self.name)==len(self.numbers):
            for i in range(len(self.name)):
                self.contactDict[self.name[i]]= self.numbers[i]
            print('Contacts saved successfully.')
        else:
            print('Contacts cannot be saved. Length Mismatch!')


#DRIVER CODE STARTS////////////////////////////////////////
names = ["Emergency", "Father", "Bestie"]
numbers = ["999", "01xx23", "01xx87", "01xx65", "01xx43"]

m1 = Contacts(names, numbers)
print("Saved Contacts:", m1.contactDict)
print("---------------------------------------------")
print('reference of m1 :',m1)

names.append("Mother")
numbers.pop()

m2 = Contacts(names, numbers)
print("Saved Contacts:", m2.contactDict)
print("---------------------------------------------")
#DRIVER CODE ENDS//////////////////////////////////////////


#taskoption
m1 = Contacts(names, numbers)
print('Changed:',m1)