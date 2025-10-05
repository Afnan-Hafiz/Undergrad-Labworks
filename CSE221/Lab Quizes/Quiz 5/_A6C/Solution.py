import sys
input= sys.stdin.readline
from collections import deque

n=int(input())
for i in range(n):
    N=int(input())
    x1, y1, x2, y2 = map(int, input().split())
    turns = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)]
    
    distance = [[-1] * (N + 1) for i in range(N+1)]
    distance[x1][y1] = 0
    queue = deque([(x1,y1)])

    while len(queue) != 0:
        x, y = queue.popleft()
        if (x,y) == (x2,y2):
            print(distance[x][y])
            break

        for dx, dy in turns:
            nx,ny = x + dx , y + dy
            if (1 <= nx <= N) and (1 <=ny <= N) and (distance[nx][ny] == -1):
                distance[nx][ny] = distance[x][y] + 1
                queue.append([nx,ny])
    if distance[x2][y2] == -1:
        print(-1) 