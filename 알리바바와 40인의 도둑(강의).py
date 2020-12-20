# 알리바바는 40인의 도둑으로부터 금화를 훔쳐 도망치고 있습니다.
# 알리바바는 도망치는 길에 평소에 잘 가지 않던 계곡의 돌다리로 도망가고자 한다. 계곡의 돌다리는 N×N개의 돌들로 구성되어 있다.
# 각 돌다리들은 높이가 서로 다릅니다.
# 해당 돌다리를 건널때 돌의 높이 만큼 에너지가 소비됩니다. 이동은 최단거리 이동을 합니다. 
# 즉 현재 지점에서 오른쪽 또는 아래쪽으로만 이동해야 합니다.
# N*N의 계곡의 돌다리 격자정보가 주어지면 (1, 1)격자에서 (N, N)까지 가는데 드는 에너지의 최소량을 구하는 프로그램을 작성하세요.


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    graph[0][i] += graph[0][i-1]

for i in range(1, n):
    graph[i][0] += graph[i-1][0] 

for i in range(1, n):
    for j in range(1, n):
        if(graph[j-1][i] >= graph[j][i-1]):
            graph[j][i] += graph[j][i-1]
        else:
            graph[j][i] += graph[j-1][i]
        
print(graph[n-1][n-1])











# n = int(input())

# graph = [list(map(int, input().split())) for _ in range(n)]
# energy = graph[0][0]

# def dy(x, y):
#     global energy
#     if(x == n-1 and y == n-1):
#         return energy
#     elif(x == n - 1):
#         energy += graph[x][y+1]
#         dy(x, y+1)
#     elif(y == n - 1):
#         energy += graph[x+1][y]
#         dy(x+1, y)
#     elif(graph[x+1][y] < graph[x][y+1]):
#         energy += graph[x+1][y]
#         dy(x+1, y)
#     elif(graph[x+1][y] > graph[x][y+1]):
#         energy += graph[x][y+1]
#         dy(x, y+1)

# print(dy(0, 0))