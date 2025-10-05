def username_generator(first_name, last_name, student_id, middle_name=""):
  user_name=""

  for i in range(3):
    if len(user_name)==len(first_name):
      break
    else:
      if 97<=ord(first_name[i])<=122:
        user_name+=chr(ord(first_name[i])-32)
      else:
        user_name+=first_name[i]
  user_name+=middle_name

  for i in range(len(last_name)-3,len(last_name)):
    user_name+=last_name[i]

  user_name+="_"
  str_student_id=str(student_id)

  for i in range(len(str_student_id)-4, len(str_student_id)):
    user_name+=str(str_student_id[i])

  return user_name

first_name, middle_name, last_name, student_id= input ("First Name:"), input ("Middle Name:"), input ("Last Name:"), int (input ("Student ID:"))
print(username_generator(first_name, last_name, student_id, middle_name))