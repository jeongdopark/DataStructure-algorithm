# 도현이의 집 N개가 수직선 위에 있다. 각각의 집의 좌표는 x1, ..., xN이고, 집 여러개가 같은 좌표를 가지는 일은 없다.

# 도현이는 언제 어디서나 와이파이를 즐기기 위해서 집에 공유기 C개를 설치하려고 한다. 
# 최대한 많은 곳에서 와이파이를 사용하려고 하기 때문에, 
# 한 집에는 공유기를 하나만 설치할 수 있고, 가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치하려고 한다.
# C개의 공유기를 N개의 집에 적당히 설치해서, 가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램을 작성하시오.

# 첫째 줄에 집의 개수 N (2 ≤ N ≤ 200,000)과 공유기의 개수 C (2 ≤ C ≤ N)이 하나 이상의 빈 칸을 사이에 두고 주어진다.
# 둘째 줄부터 N개의 줄에는 집의 좌표를 나타내는 xi (0 ≤ xi ≤ 1,000,000,000)가 한 줄에 하나씩 주어진다.


n, m = map(int, input().split())
num = list(int(input()) for _ in range(n))
num.sort()


def count(len):
    cnt = 1
    ep = num[0]
    for i in range(1, n):
        if(num[i] - ep >= len):
            cnt += 1
            ep = num[i]
    return cnt
lt = 1
rt = num[-1]
ans = 0
while lt <= rt:
    mid = (lt + rt) // 2
    if(count(mid) >= m):
        lt = mid + 1
        ans = mid
    else:
        rt = mid - 1
print(ans)
