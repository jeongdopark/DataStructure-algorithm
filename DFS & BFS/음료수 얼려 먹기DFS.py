
n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
ctn = 0


def dfs(x, y):
    if(0 <= x < n and 0 <= y < m and graph[x][y] == 0):
        graph[x][y] = 1
        dfs(x+1, y)
        dfs(x-1 ,y)
        dfs(x, y+1)
        dfs(x, y-1)
    else:
        return False


for i in range(n):
    for j in range(m):
        if(graph[i][j] == 0):
            dfs(i, j)
            print(i, j)

            ctn += 1
print(ctn)