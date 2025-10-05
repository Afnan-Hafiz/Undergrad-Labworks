class Patient:
  #write a constructor
  def __init__(self, id, name, age, bloodgroup, next, prev):
    self.id = id
    self.name = name
    self.age = age
    self.bloodgroup = bloodgroup
    self.next = next
    self.prev = prev


class WRM:

  def __init__(self):
    #Creating the dummy head
    self.dh = Patient(None,None,None,None,None,None)
    self.dh.next = self.dh
    self.dh.prev = self.dh
    self.current=self.dh

  def registerPatient(self,id, name, age, bloodgroup):
    newPatient= Patient(id, name, age, bloodgroup,self.dh,self.current)
    self.current.next=newPatient
    self.dh.prev=newPatient
    self.current=newPatient
    print("Patient registered successfully!")

  def servePatient(self):
    currentPatient=self.dh.next
    if currentPatient==self.dh:
      print("No more patient to serve!")
    else:
      print(f"{currentPatient.name} is now being served!")
      self.dh.next=currentPatient.next
      currentPatient= self.dh


  def showAllPatient(self):
    if self.dh.next==self.dh:
      print("No patient")
    else:
      currentPatient=self.dh.next
      while currentPatient!=self.dh:
        print(f"ID: {currentPatient.id}")
        currentPatient=currentPatient.next


  def canDoctorGoHome(self):
    if self.dh.next!=self.dh:
      print("Doctors can't go home")
    else:
      print("Doctors can go home")

  def cancelAll(self):
    self.dh.next=self.dh
    self.dh.prev=self.dh



  def ReverseTheLine(self):
    currentPatient=self.dh.next
    if currentPatient==self.dh:
      print("No more patient to serve!")
    else:
      while currentPatient!=self.dh:
        temp=currentPatient.next
        currentPatient.next= currentPatient.prev
        currentPatient.prev=temp
        currentPatient=temp

      temp=self.dh.next
      self.dh.next=self.dh.prev
      self.dh.prev=temp

    return currentPatient




#Write a Tester Code in this cell
print("**Welcome to Waiting Room Management System**")
wrm=WRM()
n=True
while n!=7:
  print("=========================")
  print()
  print("==Choose an option==\n1. RegisterPatient()\n2. ServePatient()\n3. CancelAll()\n4. CanDoctorGoHome()\n5. ShowAllPatient()\n6. ReverseTheLine\n7. Exit\n =====================")
  n=int(input("Enter what you need to know: "))
  if n==1:
    print("Executing RegisterPatient()...")
    id=int(input("Enter ID: "))
    name=input("Enter Name: ")
    age=int(input("Enter age: "))
    bloodgroup=input("Enter bloodgroup: ")
    wrm.registerPatient(id,name,age,bloodgroup)

  elif n==2:
    wrm.servePatient()

  elif n==3:
    print("Doctors are on a lunch break")
    wrm.cancelAll()

  elif n==4:
    wrm.canDoctorGoHome()

  elif n==5:
    print("The patient list are: ")
    wrm.showAllPatient()

  elif n==6:
    wrm.ReverseTheLine()

  elif n==7:
    break

  else:
    print("Invalid choice!")