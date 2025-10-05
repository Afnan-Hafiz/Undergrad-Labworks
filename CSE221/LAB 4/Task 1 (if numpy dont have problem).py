import numpy as np
n, m = map(int, input().split())
mat = np.zeros((n, n), dtype=int)

for i in range(m):
  u, v, w = map(int, input().split())
  mat[u-1][v-1] = w

for row in mat:
  print(*row)