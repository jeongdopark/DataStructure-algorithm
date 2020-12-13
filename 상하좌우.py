#  여행가 A는 N x N 크기의 정사각형 공간 위에 서 있다. 이 공간은 1 x 1 크기의 정사각형으로 나누어져 있다.
# 가장 왼쪽 위 좌표는 (1, 1)이며, 가장 오른쪽 아래 좌표는 (N, N)에 해당한다. 여행가 A는 상, 하, 좌, 우 방향으로 이동할 수 있으며,
# 시작 좌표는 항상 (1, 1)이다.


# 나의 풀이
# n = int(input())
# mapList = list(map(str, input().split()))

# x = 1
# y = 1

# for i in mapList:
#     if(i == 'R'):
#         if(y < len(mapList)):
#             y += 1
#         else:
#             continue
#     elif(i == 'L'):
#         if(y > 1):
#             y -= 1
#         else:
#             continue
#     elif(i == 'U'):
#         if(x > 1):
#             x -= 1
#         else:
#             continue
#     elif(i == 'D'):
#         if(x < len(mapList)):
#             x += 1
#         else:
#             continue

# print(x, y)


#책 풀이

n = int(input())

x, y = 1, 1

mapList = input().split() 

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for move in mapList:
    for i in range(len(move_types)):   
        if(move == move_types[i]):
            nx = x + dx[i]
            ny = y + dy[i]
    if( nx < 1 or ny < 1 or nx > n or ny > n):
        continue
    x, y = nx, ny

print(x ,y)


