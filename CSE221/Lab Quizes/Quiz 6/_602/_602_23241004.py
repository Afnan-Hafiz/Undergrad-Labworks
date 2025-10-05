## 10 23241004 CSE-09E-21L-41 23241004
import sys
import heapq
input = sys.stdin.readline
x = int(input())

for _ in range(x):
    N, M= map(int, input().split())
    u = list(map(int, input().split()))
    v = list(map(int, input().split()))
    w = list(map(int, input().split()))
    graph = [[] for j in range(N+1)]
    for i in range(M):      
        graph[u[i]].append((v[i], w[i]))
    
    INF = 10**18
    dist = [[INF,INF] for j in range(N+1)]
    heap = [(0, 1, -1)]
    while heap:
        c, n, p0 = heapq.heappop(heap)
        for i, weight in graph[n]:
            p =  weight%2
            if (p0 == -1 or p0 == p) and c + weight < dist[i][p]:
                dist[i][p]= c + weight
                heapq.heappush(heap, (dist[i][p], i, p))
    res = min(dist[N])
    print(-1 if res == INF else res)