def key_generator(*args):
  keys = []
  for i in args:
    final = ""
    final += i[0].lower()

    for j in range(-2, -len(i), -1):
      final += str(ord(i[j]))

    final+=i[-1].upper()
    keys.append(final)
  return (f'Encrypted Keys: {keys}')

key_list = key_generator ("Alex", "Bob", "Trudy")
print(key_list)