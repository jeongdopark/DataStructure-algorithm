
#  Depth First Search 
#  틀린 답이다 이건.

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):
    if x >= 0 or x < n or y >= 0 or y < m:
        if graph[x][y] == 0:
            graph[x][y] = 1
            dfs(x - 1, y)
            dfs(x, y -1)
            dfs(x + 1 , y)
            dfs(x, y + 1)
            

result = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            result += 1

print(result)