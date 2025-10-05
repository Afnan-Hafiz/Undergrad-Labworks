n, m = map(int, input().split())
adj_list = {}
for i in range(1, n + 1):
  adj_list[i] = []

u_list = list(map(int, input().split()))
v_list = list(map(int, input().split()))
w_list = list(map(int, input().split()))

for u, v, w in zip(u_list, v_list, w_list):
  adj_list[u].append((v, w))

for key,value in adj_list.items():
    print(f"{key}: ", end=" ")
    print(*value)