class Author:
  def __init__(self,n=None):
    self.name = n
    self.book_list = {}
    self.total = 0

  def setName(self,a):
    self.name = a

  def addBook(self,b,t):
    if self.name == None:
      print("A book can not be added without author name")
    else:
      self.book = b
      self.btype = t
      if self.btype in self.book_list:
        self.book_list[self.btype].append(self.book)
      else:
        self.book_list[self.btype] = [self.book]
      self.total+=1

  def printDetail(self):
    print(f'Number of Book(s): {self.total}')
    print(f'Author Name: {self.name}')
    for key,value in self.book_list.items():
      print(f'{key}:',end=" ")
      for i in range(len(value)):
        if len(value) ==1:
          print(value[i])
        else:
          if i!=len(value):
            print(value[i]+",")
          else:
            print(value[i])

#DRIVER CODE
a1 = Author()
print("=================================")
a1.addBook("Ice", "Science Fiction")
print("=================================")
a1.setName("Anna Kavan")
a1.addBook("Ice", "Science Fiction")
a1.printDetail()
print("=================================")
a2 = Author("Humayun Ahmed")
a2.addBook("Onnobhubon", "Science Fiction")
a2.addBook("Megher Upor Bari", "Horror")
print("=================================")
a2.printDetail()
a2.addBook("Ireena", "Science Fiction")
print("=================================")
a2.printDetail()
print("=================================")