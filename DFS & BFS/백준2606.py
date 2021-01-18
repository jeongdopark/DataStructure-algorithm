# 신종 바이러스인 웜 바이러스는 네트워크를 통해 전파된다. 한 컴퓨터가 웜 바이러스에 걸리면 
# 그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸리게 된다.
# 예를 들어 7대의 컴퓨터가 <그림 1>과 같이 네트워크 상에서 연결되어 있다고 하자. 
# 1번 컴퓨터가 웜 바이러스에 걸리면 웜 바이러스는 2번과 5번 컴퓨터를 거쳐 3번과 6번 컴퓨터까지 전파되어 2, 3, 5, 6 
# 네 대의 컴퓨터는 웜 바이러스에 걸리게 된다. 
# 하지만 4번과 7번 컴퓨터는 1번 컴퓨터와 네트워크상에서 연결되어 있지 않기 때문에 영향을 받지 않는다.


n = int(input())
m = int(input())

graph = [[0] * (n+1) for _ in range(n+1)]


for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

visited = [False] * (n+1)
count = 0
def dfs(f):
    global count
    visited[f] = True
    for i in range(1, n+1):
        if(graph[f][i] == 1 and not visited[i]):
            dfs(i)
            count += 1


dfs(1)
print(count)