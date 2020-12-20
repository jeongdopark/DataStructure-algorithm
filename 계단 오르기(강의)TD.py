


n = int(input())
dy = [0] * (n+1)
dy[1] = 1
dy[2] = 2

def DFS(num):
    if(dy[num] > 0):
        return dy[num]
    if(num == 1 or num == 2):
        return dy[num]
    dy[num] = DFS(num -1) + DFS(num -2)
    return dy[num]

print(DFS(n))