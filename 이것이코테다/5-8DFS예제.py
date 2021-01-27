
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

def dfs(start):
    visited[start] = True
    print(start, end = ' ')
    for i in graph[start]:
        if(visited[i] == False):
            dfs(i)
dfs(1)
