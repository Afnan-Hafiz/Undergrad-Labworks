# Task 3
class Team:
    def __init__(self,n=''):
        self.__name=n
        self.__l1=[]

    def setName(self,s):
        self.__name=s
        return self.__name

    def addPlayer(self,x):
        self.__l1.append(x.name)

    def printDetail(self):
        print('=====================')
        print(f'Team: {self.__name}')
        print(f'List of Players: \n{self.__l1}')
        print('=====================')


class Player:
    def __init__(self,n):
        self.name=n

b = Team()
b.setName('Bangladesh')
mashrafi = Player("Mashrafi")
b.addPlayer(mashrafi)
tamim = Player("Tamim")
b.addPlayer(tamim)
b.printDetail()
a = Team("Australia")
ponting = Player("Ponting")
a.addPlayer(ponting)
lee = Player("Lee")
a.addPlayer(lee)
a.printDetail()