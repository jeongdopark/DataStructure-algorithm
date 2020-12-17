
from collections import deque
import sys
t = int(sys.stdin.readline())

dx = [-1, 1, 0 ,0]
dy = [0, 0, -1, 1]
stack = deque()
answer = []
def bfs(x, y):
    stack.append((x, y))
    while stack:
        x, y = stack.popleft()
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                stack.append((nx, ny))
         
for i in range(t):
    count = 0   
    m, n, k = map(int, sys.stdin.readline().split())
    graph = [[0] * (m) for _ in range(n)]
    for j in range(k):
        x, y = map(int, sys.stdin.readline().split())
        graph[y][x] = 1
    for a in range(n):
        for b in range(m):
            if(graph[a][b] == 1):
                count += 1
                bfs(a, b)
    print(count)
    
    


