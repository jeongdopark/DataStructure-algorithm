
from collections import deque

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

def bfs(graph, v, visited):
    bfsList = deque()
    bfsList.append(v)
    visited[v] = True

    while bfsList:
        num = bfsList.popleft()
        print(num, end = ' ')
        for i in graph[num]:
            if(visited[i] == False):
                bfsList.append(i)
                visited[i] = True

bfs(graph, 1, visited)
        