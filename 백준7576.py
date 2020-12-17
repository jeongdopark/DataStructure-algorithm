
from collections import deque

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(m) ]
apple = deque()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(apple):
    while apple:
        x, y = apple.popleft()
        
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if(0 <= nx < m and 0 <= ny < n and graph[nx][ny] == 0):
                graph[nx][ny] = graph[x][y] + 1 
                apple.append((nx, ny))
        
for i in range(m):
    for j in range(n):
        if(graph[i][j] == 1):
            apple.append((i, j))

bfs(apple)

result = -2

check_tot = False

for i in graph:
    for j in i:
        if(j == 0):
            check_tot = True
        result = max(result, j)
        
if check_tot:
    print(-1)
elif result == -1:
    print(0)
else:
    print(result - 1)

    
# def check():
#     check = False
#     result = -2
#     for i in range(m):
#         for j in range(n):
#             if(graph[i][j] == 1):
#                 apple.append((i, j))
#             elif(graph[i][j] == 0):
#                 check = True
#     if(not check):
#         return 0
#     elif(check):
#         bfs(apple)
#         for i in graph:
#             for j in i:
#                 if(j == 0):
#                     return -1
#                 else:
#                     result = max(result, j)
#     return result

# print(check())

    
    
    