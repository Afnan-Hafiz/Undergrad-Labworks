class Tournament:
    def __init__(self,name='Default'):
        self.__name = name
    def set_name(self,name):
        self.__name = name
    def get_name(self):
        return self.__name
class Cricket_Tournament(Tournament):
  def __init__(self,name='Default',n_team = 0,tpe = "No type"):
    super().__init__(name)
    self.n_team = n_team
    self.tpe = tpe
  def detail(self):
    return f"Cricket Tournament Name: {super().get_name()}\nNumber of Teams: {self.n_team}\nType: {self.tpe}"
class Tennis_Tournament(Tournament,):
  def __init__(self,name='Default',n_player = 0):
    super().__init__(name)
    self.n_player = n_player
  def detail(self):
    return f'Tennis Tournament Name: {super().get_name()}\nNumber of Players: {self.n_player}'
ct1 = Cricket_Tournament()
print(ct1.detail())
print("-----------------------")
ct2 = Cricket_Tournament("IPL",10,"t20")
print(ct2.detail())
print("-----------------------")
tt = Tennis_Tournament("Roland Garros",128)
print(tt.detail())


