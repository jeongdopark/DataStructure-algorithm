

a, b = map(int, input().split())
graph = []
count = 0

def dfs(i,j):
    if(0 <= i < a and 0 <= j < b):
        if(graph[i][j] == 0):
            graph[i][j] = 1
            dfs(i+1, j)
            dfs(i, j+1)
            dfs(i-1, j)
            dfs(i, j-1)
        else:
            return False
    else:
        return False
    
    

for _ in range(a):
    graph.append(list(map(int, input())))

for i in range(a):
    for j in range(b):
        if(graph[i][j] == 0):
            count += 1
            dfs(i,j)

print(count)

            
