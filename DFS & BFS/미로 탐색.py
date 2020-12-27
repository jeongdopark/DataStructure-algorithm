# DFS 탐색
from collections import deque
n, m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(input()))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

stack = deque()
def bfs(x, y):
    stack.append((x,y))
    while stack:
        x, y = stack.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if(nx < 0 or ny < 0 or nx >= n or ny >= m):
                continue
            if(graph[nx][ny] == '1'):
                continue
            if(graph[nx][ny] == '0'):
                graph[x][y] = 1
                stack.append((nx, ny))
            if(graph[nx][ny] == 'x'):
                return print('탈출 성공')
    return print('탈출 실패')


for i in range(n):
    for j in range(m):
        if(graph[i][j] == 'e'):
            bfs(i ,j)
    
        

