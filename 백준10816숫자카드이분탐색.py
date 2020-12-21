

# 숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다. 정수 M개가 주어졌을 때, 
# 이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하는 프로그램을 작성하시오.
# 첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)이 주어진다.
# 둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다. 숫자 카드에 적혀있는 수는 -10,000,000보다 크거나 같고,
# 10,000,000보다 작거나 같다.
# 셋째 줄에는 M(1 ≤ M ≤ 500,000)이 주어진다. 넷째 줄에는 상근이가 몇 개 가지고 있는 숫자 카드인지 구해야 할 M개의 정수가 주어지며,
# 이 수는 공백으로 구분되어져 있다. 이 수도 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.

# n = int(input())
# num1 = list(map(int, input().split()))
# num1.sort()
# m = int(input())
# num2 = list(map(int, input().split()))
# ans = []
# count = 0
# def minus(x):
#     global count
#     global i 
#     if(num1[x] == i):
#         count += 1
#         if(x > 0):
#             minus(x-1)
#     else:
#         return count
# def plus(x):
#     global count
#     global i 
#     if(num1[x] == i):
#         count += 1
#         if(x < n - 1):
#             plus(x + 1)
#     else:
#         return count


# for i in num2:
#     lt = 0
#     rt = n - 1
#     while lt <= rt:
#         mid = (lt + rt) // 2
        
#         if(num1[mid] > i):
#             rt = mid - 1
#         elif(num1[mid] == i):
#             count += 1
#             if(0 < mid < n - 1):
#                 plus(mid+1)
#                 minus(mid-1)
#             elif(mid == n-1):
#                 minus(mid-1)
#             elif(mid == 0):
#                 plus(mid+1)
#             break
#         else:
#             lt = mid + 1
#     ans.append(count)
#     count = 0

# for i in ans:
#     print(i, end = ' ')



# from collections import Counter
# import sys
# input = sys.stdin.readline
# n = int(input())
# s = list(map(int, input().split()))
# m = int(input())
# s_ = list(map(int, input().split()))
# s = Counter(s)

# for i in s_:
#     print(s[i], end = ' ')

import sys
input = sys.stdin.readline
n = int(input())
num1 = list(map(int, input().split()))
num1.sort()
m = int(input())
num2 = list(map(int, input().split()))
ans = []
for i in num2:
    lt = 0
    rt = n - 1
    while lt <= rt:
        mid = (lt + rt) // 2
        if(num1[mid] > i):
            rt = mid - 1
        elif(num1[mid] == i):
            count = num1.count(i)
            break
        else:
            lt = mid + 1
    print(count, end = ' ')
    