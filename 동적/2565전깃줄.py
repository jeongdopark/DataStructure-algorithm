# 전깃줄이 전봇대에 연결되는 위치는 전봇대 위에서부터 차례대로 번호가 매겨진다. 
# 전깃줄의 개수와 전깃줄들이 두 전봇대에 연결되는 위치의 번호가 주어질 때, 
# 남아있는 모든 전깃줄이 서로 교차하지 않게 하기 위해 없애야 하는 전깃줄의 최소 개수를 구하는 프로그램을 작성하시오.

# 첫째 줄에는 두 전봇대 사이의 전깃줄의 개수가 주어진다. 전깃줄의 개수는 100 이하의 자연수이다. 
# 둘째 줄부터 한 줄에 하나씩 전깃줄이 A전봇대와 연결되는 위치의 번호와 B전봇대와 연결되는 위치의 번호가 차례로 주어진다. 
# 위치의 번호는 500 이하의 자연수이고, 같은 위치에 두 개 이상의 전깃줄이 연결될 수 없다.

# 첫째 줄에 남아있는 모든 전깃줄이 서로 교차하지 않게 하기 위해 없애야 하는 전깃줄의 최소 개수를 출력한다.

n = int(input())

num = [list(map(int, input().split())) for _ in range(n)]
num = sorted(num, key = lambda x : x[0])
ans = 0
mm = [0] * (n+1)
mm[1] = 1
for i in range(1, n):
    max = 0
    for j in range(i):
        if(num[j][1] < num[i][1] and max < mm[j+1]):
            max = mm[j+1]
    mm[i+1] = max + 1
    if(ans < mm[i+1]):
        ans = mm[i+1]
print(n-ans)
