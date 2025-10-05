## 10 23241004 CSE-09E-21L-42 23241004
def bfs(graph, start):
    g = len(graph)
    distance = [-1] * (g+1)
    parent = [-1] * (g+1)
    q = [start]
    front = 0
    distance[start] = 0
    while front < len(q):
        u = q[front]
        front +=1

        for i in graph[u]:
            if distance[i] == -1:
                distance[i] = distance[u] + 1
                parent[i] = u
                q.append(i)
    return distance, parent

def build(parent,end):
    path = []
    current = end
    while current != -1:
        path.append(current)
        current = parent[current]
    path.reverse()
    return path

test= int(input())
for i in range(test):
    N , M, S, D, K = map(int, input().split())
    graph={i : [] for i in range(1, N+1)}
    for i in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)

    s_distance , s_parameter = bfs(graph, S)
    k_distance , k_parameter = bfs(graph, K)
    if s_distance[K] == -1 or k_distance[D] == -1:
        print(-1)
    else:
        first = build(s_parameter, K)
        second = build(k_parameter, D)
        path = first + second[1:]
        length = len(path)-1
        print(length)
        print(" ".join(map(str,path)))
