


n = int(input())
cnt = 1
classList = []

for _ in range(n):
    classList.append(list(map(int, input().split())))
# 시작 시간과 끝나는 시간이 같은데 왜 ? 처음에 시작지점을 기준으로 정렬을 해주는 것일까?
classList = sorted(classList, key=lambda x : x[0])
classList = sorted(classList, key=lambda x : x[1]) 

b = 0
for i in range(1, n):
    start = classList[i][0]
    end = classList[b][1]
    if(start >= end):
        cnt += 1
        b = i
print(cnt)