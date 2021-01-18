# 7
# 6
# 1 2
# 2 3
# 1 5
# 5 2
# 5 6
# 4 7


from collections import deque

com = int(input())
line = int(input())

graph = [[0] * (com + 1) for _ in range(com + 1)]
visited = [False] * (com+1)
for i in range(line):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1


def BFS(start):
    cnt = -1
    queue = deque()
    queue.append(start)
    visited[start] = True
    while queue:
        add = queue.popleft()
        cnt += 1
        for i in range(1, com+1):
            if(graph[add][i] == 1 and visited[i] == False):
                queue.append(i)
                visited[i] = True
    return cnt

print(BFS(1))
