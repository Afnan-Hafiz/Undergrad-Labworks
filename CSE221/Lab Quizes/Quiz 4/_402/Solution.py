import sys
sys.setrecursionlimit(10**6+50)
input = sys.stdin.readline
n = int(input())
def dfs(node , parent):
    subtree[node] = 0
    for i in graph[node]:
        if i != parent:
            dfs(i, node)
            subtree[node] = max(subtree[node], 1+subtree[i])
        

for k in range(n):
    N, M = map(int, input().split())
    graph= [[] for i in range(N+1)]
    for i in range(N-1):
        u,v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    subtree = [-1]* (N+1)
    dfs(M, -1)
    Q = int(input())
    for i in range(Q):
        x = int(input())
        print(subtree[x])