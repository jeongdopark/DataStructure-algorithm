
# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 
# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 
# 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다
# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 
# 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 
# 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다.
#  입력으로 주어지는 간선은 양방향이다.

from collections import deque

n, m, start = map(int, input().split())

graph = [[0]*(n+1) for i in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

visited = [False] * (n+1)

def dfs(v):
    visited[v] = True
    print(v, end =' ')
    for i in range(1, n+1):
        for j in str(graph[v][i]):
            if(j == '1' and not visited[i]):
                dfs(i)
stack = deque()  

def bfs(v):
    stack.append(v)
    while stack:
        cur = stack.popleft()
        print(cur, end =' ')
        visited[cur] = False
        for i in range(1, n+1):
            if(graph[cur][i] == 1 and visited[i]):
                stack.append(i)
                visited[i] = False                            

dfs(start)
print()
bfs(start)

        
