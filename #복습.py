

n = int(input())

num = [list(map(int,input().split())) for _ in range(n)]

num = sorted(num, key = lambda x : x[0])
print(num)
mm = [0] * (n+1)
mm[1] = num[0][1]

for i in range(2, n+1):
    for j in range(i-1, 0, -1):
        print(j)
        if(num[i-1][2] > num[j-1][2]):
            mm[i] = num[i-1][1] + mm[j]
            break
        
print(mm)