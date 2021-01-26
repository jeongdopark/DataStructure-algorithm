
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
    test = deque()
    test.append(v)
    visited[v] = True
    while test:
        num = test.popleft()
        print(num, end = ' ')
        for i in graph[num]:
            if(visited[i] == False):
                test.append(i)
                visited[i] = True
            
bfs(graph, 1, visited)
