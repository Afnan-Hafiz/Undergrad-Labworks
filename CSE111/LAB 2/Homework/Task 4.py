def username_generator(first, last, id, middle = ""):
  username = ""
  #Adding first name
  if len(first) <= 3:
    username += first.upper()
  else:
    username += first[:3].upper()

  #Adding middle name
  username += middle

  #Adding last name
  username += last[-3:].lower()

  #Adding id
  id = str(id)
  username += "_" + id[-4:]

  return username

first_name, middle_name, last_name, student_id= input ("First Name: "), input("Middle Name: "), input ("Last Name: "), int (input ("Student ID: "))

print(username_generator(first_name, last_name, student_id, middle_name))