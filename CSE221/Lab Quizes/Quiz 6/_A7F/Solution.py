import sys
import heapq
input = sys.stdin.readline
x = int(input())
for i in range(x):
    N, M, S, D = map(int, input().split())
    
    graph = [[] for i in range(N+1)]
    for i in range(M):
        u, v ,w= map(int, input().split())
        graph[u].append((v, w))
        graph[v].append((u, w))

    INF = 10**18
    first = [INF] * (N+1)
    second = [INF] * (N+1)
    first[S] = 0
    heap = [(0,S)]
    while heap:
        d, node = heapq.heappop(heap)
        for v, weight in graph[node]:
            nd= d + weight
            if nd < first[v]:
                second[v] = first[v]
                first[v] = nd
                heapq.heappush(heap, (nd,v))
            elif first[v] < nd < second[v]:
                second[v]= nd
                heapq.heappush(heap, (nd,v))

    print(-1 if second[D]==INF else second[D])