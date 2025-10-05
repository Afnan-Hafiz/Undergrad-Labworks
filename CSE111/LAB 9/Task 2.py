class Player:
  total=0
  temp=""
  def __init__(self,n=None,num=10,t=None):
    self.name=n
    self.number=num
    self.team=t
    Player.total+=1
    if n!=None:
      Player.temp+=n + ", "

  def set_name(self,p):
    self.name=p
    Player.temp+=p+", "

  def set_team(self,t):
    self.team=t
    return self.team

  def set_number(self,num):
    self.number=num
    return self.number

  def player_detail(self):
    return(f'Player Name: {self.name} \nJersey Number: {self.number} \nCountry: {self.team}')

  @classmethod
  def info(cls):
    print(f"Total number of players: {cls.total}")
    print(f"Players enlisted so far: {cls.temp[0:len(cls.temp)-2]}")



#DRIVER CODE
print("Total number of players:", Player.total)
print("---------------------------")
p1 = Player()
p1.set_name("Neymar")
p1.set_team("Brazil")
print(p1.player_detail())
print('========================')
Player.info()
print("---------------------------")
p2 = Player("Ronaldo")
p2.set_number(7)
p2.set_team("Portugal")
print(p2.player_detail())
print('========================')
Player.info()
print("---------------------------")
p3 = Player("Messi")
p3.set_team("Argentina")
print(p3.player_detail())
print('========================')
Player.info()
print("---------------------------")
p4 = Player("Mbappe", 10, "France")
print(p4.player_detail())
print('========================')
Player.info()