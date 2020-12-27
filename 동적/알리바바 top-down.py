


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

m = [[0] * n for _ in range(n)]

def DFS(x, y):
    if(x == 0 and y == 0):
        return graph[0][0]
    else:
        if y == 0:
            m[x][y] = DFS(x-1, y) + graph[x][y]
        elif x == 0:
            m[x][y] = DFS(x, y-1) + graph[x][y]
        else:
            m[x][y] = min(DFS(x-1, y), DFS(x, y-1))
        return m[x][y]
        
DFS(n-1, n-1)