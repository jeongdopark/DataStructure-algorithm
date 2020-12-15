
#  Depth First Search 
#  틀린 답이다 이건.
# return True의 의미 , 
n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

def check(x, y):
    if(x < 0 or y < 0 or x >= n or y >= m):
        return False
    elif(graph[x][y] == 1):
        return False
    elif(graph[x][y] == 0):
        graph[x][y] = 1
        check(x+1, y)
        check(x-1, y)
        check(x, y+1)
        check(x, y-1)
        return True
count = 0
for i in range(n):
    for j in range(m):
        if(check(i, j) == True):
            count += 1
print(count)