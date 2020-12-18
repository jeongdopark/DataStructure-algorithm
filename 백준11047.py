# 준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.

# 동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.


# n, m = map(int, input().split())
# money = [int(input()) for _ in range(n)]

# def check(d):
#     cash = m
#     cnt = 0
#     k = d
#     while cash != 0:
#         cnt += (cash // money[k])
#         cash = (cash % money[k])
#         if(cash == 0):
#             break
#         for i in range(n):
#             if(money[i] > cash):
#                 k = i-1
#                 break
#             elif(money[i] == cash):
#                 k = i
#                 break
#     return cnt


# for i in range(n):
#     if(money[i] > m):
#         print(check(i-1))
#         break
#     elif(money[i] == m):
#         print(1)
#         break


# n, m = map(int, input().split())
# money = [int(input()) for _ in range(n)]
# cnt = 0
# while m != 0:
#     for i in range(n):
#         if(money[i] > m):
#             cnt += (m // money[i-1])
#             m = (m % money[i-1])
#             if(m == 0):
#                 break
#         elif(money[i] == m):
#             cnt += 1
#             break

# print(cnt)

n, m = map(int, input().split())
money = [int(input()) for _ in range(n)]
cnt = 0

for i in range(1, n+1):
    coin = money[-i]
    if(m >= coin):
        cnt += (m // coin)
        m %= coin
        if(m == 0):
            print(cnt)
            break
        
        