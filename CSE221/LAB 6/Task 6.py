from collections import deque

N, M, S, Q = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

sources = list(map(int, input().split()))
destinations = list(map(int, input().split()))

dist = [-1] * (N + 1)
q = deque()

for s in sources:
    dist[s] = 0
    q.append(s)

while q:
    node = q.popleft()
    for k in graph[node]:
        if dist[k] == -1:
            dist[k] = dist[node] + 1
            q.append(k)

ans = [str(dist[d]) for d in destinations]
print(' '.join(ans))