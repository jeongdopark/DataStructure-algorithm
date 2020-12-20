# N개의 자연수로 이루어진 수열이 주어졌을 때, 그 중에서 가장 길게 증가하는(작은 수에서 큰 수로) 원소들의 집합을 찾는 프로그램을 작성하라. 
# 예를 들어, 원소가 2, 7, 5, 8, 6, 4, 7, 12, 3 이면 가장 길게 증가하도록 원소들을 차례대로 뽑아내면 2, 5, 6, 7, 12를 
# 뽑아내어 길이가 5인 최대 부분 증가수열을 만들 수 있다.

# n = int(input())
# num = list(map(int, input().split()))

# dy = [0] * (n)
# dy[0] = 1
# ans = 1
# for i in range(1, n):
#     for j in range(i):
#         if(num[j] < num[i]):
#             if(dy[j] >= dy[i]):
#                 dy[i] = dy[j] + 1
#                 if(ans < dy[i]):
#                     ans = dy[i]
#         else:
#             continue
# print(ans)


n = int(input())
num = list(map(int, input().split()))

dy = [0] * (n)
dy[0] = 1
ans = 0
for i in range(1, n):
    max = 0
    for j in range(i):
        if(num[j] < num[i] and dy[j] > max):
                max = dy[j]
    dy[i] = max + 1
    if(dy[i] > ans):
        ans = dy[i]
print(ans)
