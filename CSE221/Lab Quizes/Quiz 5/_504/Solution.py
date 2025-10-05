import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    index = 1
    results = []
    
    for _ in range(t):
        N = int(data[index])
        M = int(data[index + 1])
        index += 2
        
       
        graph = [[] for _ in range(N + 1)]
        for _ in range(M):
            u = int(data[index])
            v = int(data[index + 1])
            index += 2
            graph[u].append(v)
            graph[v].append(u)
        
        
        visited = [False] * (N + 1)
        parent = [-1] * (N + 1)
        cycles = 0
        
        for i in range(1, N + 1):
            if not visited[i]:
                stack = [i]
                visited[i] = True
                parent[i] = -1
                
                while stack:
                    node = stack.pop()
                    
                    for neighbor in graph[node]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            parent[neighbor] = node
                            stack.append(neighbor)
                        elif neighbor != parent[node]:
                            
                            cycles += 1


        visited = [False] * (N + 1)
        components = 0
        for i in range(1, N + 1):
            if not visited[i]:
                components += 1
                queue = deque([i])
                visited[i] = True
                while queue:
                    node = queue.popleft()
                    for neighbor in graph[node]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append(neighbor)
        
        edges_to_remove = M - N + components
        results.append(str(edges_to_remove))
    
    print("\n".join(results))

if __name__ == "__main__":
    main()

