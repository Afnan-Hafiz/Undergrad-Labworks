def hospital_fee(**kwargs):
  highest=0
  payer=""
  for key,value in kwargs.items():
    if value>=highest:
      highest=value
  for key,value in kwargs.items():
    if highest==value:
      payer+=f'{key},'
  return highest, payer[:len(payer)-1]

max_amount, max_payer = hospital_fee(Mashrafe = 400, Bumrah = 900, Steyn = 1200, Cummins = 900, Wood = 400, Marsh = 700)
print(f'Highest fee was {max_amount}tk which was paid by {max_payer}.')