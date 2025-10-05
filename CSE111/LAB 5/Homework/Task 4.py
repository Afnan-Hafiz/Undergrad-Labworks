class Shopidify:
  def __init__(self,n=None):
    self.name = n
    self.item_list = {}
    self.transaction = 0
    if self.name == None:
      print("Welcome to Shopidify")
    else:
      print(f'Welcome {self.name} to Shopidify')

  def add_to_cart(self,i,a = 1):
    if type(i) != list:
      self.item = i
      self.amount = a
      self.item_list[self.item] = self.amount
      self.transaction+=1
    else:
      for j in range(len(i)-1):
        if j%2==0:
          self.item = i[j]
          self.amount = i[j+1]
          self.item_list[self.item] = self.amount
      self.transaction+=1

  def display_cart(self):
    if self.name == None:
      print('Items in the cart for Guest:')
    else:
      print(f'Items in the cart for {self.name}:')
    for key,value in self.item_list.items():
      print(f'- {key}: {value}x')

  def checkout(self):
    if self.name == None:
      print("Checkout completed for Guest")
    else:
      print(f'Checkout completed for {self.name}')

  def display_history(self):
    if self.name ==None:
      print("Purchase history for Guest:")
      print("Transaction 1:")
      for key,value in self.item_list.items():
        print(f'- {key}: {value}x')
    else:
      print(f'Purchase history for {self.name}')
      print(f'Transaction {self.transaction}:')
      for key,value in self.item_list.items():
        print(f'- {key}: {value}x')


#DRIVER CODE
guest_account = Shopidify()
print("1xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
john_account = Shopidify("John")
print("2xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
guest_account.add_to_cart("Air Jordan", 2)
guest_account.add_to_cart("Luffy Action Figure")
guest_account.display_cart()
print("3xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
john_account.add_to_cart(["Chocolate Chip Cookies", 3,"Goku Action Figure",2,"Dumbbells-5kg",2])
john_account.display_cart()
print("4xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
guest_account.add_to_cart("Air Jordan")
guest_account.display_cart()
print("5xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
guest_account.checkout()
print("6xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
print("6xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
guest_account.display_history()
print("7xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
john_account.checkout()
print("8xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
john_account.display_history()
print("9xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")