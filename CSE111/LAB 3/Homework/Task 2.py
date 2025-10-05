class Pokemon:
  def __init__(self, name1, name2, power1, power2, damageRate):
    self.pokemon1_name= name1
    self.pokemon2_name= name2
    self.pokemon1_power= power1
    self.pokemon2_power= power2
    self.damage_rate=  damageRate
    pika_combined_power = (self.pokemon1_power + self.pokemon2_power) * self.damage_rate

#DRIVER CODE STARTS///////////////////////////////
team_pika = Pokemon('pikachu', 'charmander', 90, 60, 10)
print('=======Team 1=======')
print('Pokemon 1:',team_pika.pokemon1_name,
team_pika.pokemon1_power)
print('Pokemon 2:',team_pika.pokemon2_name,
team_pika.pokemon2_power)
pika_combined_power = (team_pika.pokemon1_power +
team_pika.pokemon2_power) * team_pika.damage_rate
print('Combined Power:', pika_combined_power)
#DRIVER CODE ENDS///////////////////////////////////



#SUBTASK
team_bulb = Pokemon('bulbasaur', 'squirtle', 80, 70, 9)
team_bulb.combined_power = (team_bulb.pokemon1_power + team_bulb.pokemon2_power) * team_bulb.damage_rate

print('=======Team 2=======')
print('Pokemon 1:', team_bulb.pokemon1_name, team_bulb.pokemon1_power)
print('Pokemon 2:', team_bulb.pokemon2_name, team_bulb.pokemon2_power)
print('Combined Power:', team_bulb.combined_power)