def username_generator(first, last, id, middle = ""):
  username = ""
  
  if len(first) <= 3:
    username += first.upper()
  else:
    username += first[:3].upper()

  username += middle
  username += last[-3:].lower()

  id = str(id)
  username += "_" + id[-4:]

  return username

first_name, middle_name, last_name, student_id= input ("First Name: "), input("Middle Name: "), input ("Last Name: "), int (input ("Student ID: "))


print(username_generator(first_name, last_name, student_id, middle_name))
