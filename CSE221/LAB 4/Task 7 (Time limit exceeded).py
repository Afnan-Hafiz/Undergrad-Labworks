n, m, k = map(int, input().split())
knight = []
for i in range(k):
  a, b = map(int, input().split())
  knight.append((a, b))

possible_moves=[
    (2, 1), (2, -1), (-2, 1), (-2, -1),
    (1, 2), (1, -2), (-1, 2), (-1, -2)
]

flag = False
for a, b in knight:
  for u,v in possible_moves:
    na = a + u
    nb = b + v
    if (na,nb) in knight:
      flag = True
      break
  if flag:
    break

if flag:
  print("YES")
else:
  print("NO")