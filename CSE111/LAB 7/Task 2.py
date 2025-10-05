#task 2
class Triangle:
    def __init__(self,b,h):
        self.__base=b
        self.__height=h

    def getBase(self):
        return self.__base

    def getHeight(self):
        return self.__height

    def setBase(self,s):
        self.__base=s
        return self.__base

    def setHeight(self,s):
        self.__height=s
        return self.__height

    def area(self):
        area= 0.5 * self.__base * self.__height
        return area
t1 = Triangle(10, 5)
print("First Triangle Base:" , t1.getBase())
print("First Triangle Height:" , t1.getHeight())
print("First Triangle area:" ,t1.area())


t2 = Triangle(5, 3)
print("Second Triangle Base:" , t2.getBase())
print("Second Triangle Height:" , t2.getHeight())
print("Second Triangle area:" ,t2.area())