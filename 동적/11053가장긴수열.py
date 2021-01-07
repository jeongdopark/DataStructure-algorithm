# 수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.
# 예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 
# A = {10, 20, 10, 30, 20, 50} 이고,길이는 4이다.
# 첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.
# 둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)
# 첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.


n = int(input())
num = list(map(int, input().split()))

mm = [0] * (n+1)
mm[1] = 1
ans = 1
for i in range(1, n):
    max = 0
    for j in range(i):
        if(num[i] > num[j] and max < mm[j+1]):
            max = mm[j+1]
    mm[i+1] = max + 1
    if(ans < mm[i+1]):
        ans = mm[i+1]

print(ans)