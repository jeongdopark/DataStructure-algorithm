#  BFS : Breath First Search '너비 우선 탐색' 가까운 노드부터 탐색하는 알고리즘이다. 

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

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:

        cur = queue.popleft()
        print(cur, end = ' ')

        for i in graph[cur]:
            if(not visited[i]):
                queue.append(i)
                visited[i] = True
        
bfs(graph, 1, visited)


