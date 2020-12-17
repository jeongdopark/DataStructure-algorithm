
from collections import deque
n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

stack = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ctn = 0

def bfs(x, y):
    stack.append((x, y))
    graph[x][y] = 1
    while stack:
        x, y = stack.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if(0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0):
                graph[nx][ny] = 1
                stack.append((nx, ny))

for i in range(n):
    for j in range(m):
        if(graph[i][j] == 0):
            print(i, j)
            bfs(i, j)
            ctn += 1
print(ctn)

            