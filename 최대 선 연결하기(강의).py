# 문제 알맹이는 최대 부분 증가수열과 동일 문제다 

# 왼쪽의 번호와 오른쪽의 번호가 있는 그림에서 같은 번호끼리 선으로 연결하려고 합니다. 
# 왼쪽번호는 무조건 위에서부터 차례로 1부터 N까지 오름차순으로 나열되어 있습니다. 
# 오른쪽의 번호 정보가 위부터 아래 순서로 주어지만 서로 선이 겹치지 않고 최대 몇 개의 선 을 연결할 수 있는 지 구하는 프로그램을 작성하세요.


n = int(input())
num = list(map(int, input().split()))

dy = [1] * (n)
ans = 0
for i in range(1, n):
    max = 0
    for j in range(i):
        if(num[j] < num[i] and dy[num[j]-1] > max):
                max = dy[j]
    dy[num[j]-1] = max + 1
    if(dy[num[j]-1] > ans):
        ans = dy[num[j]-1]
print(ans)
