
n = int(input())

num = [list(map(int,input().split())) for _ in range(n)]

num = sorted(num, key = lambda x : x[0])

mm = [0] * (n+1)
mm[1] = num[0][1]
ans = 0
for i in range(2, n+1):
    for j in range(i-1, 0, -1):        
        if(num[i-1][2] > num[j-1][2]):
            mm[i] = num[i-1][1] + mm[j]
            if(mm[i] > ans ):
                ans = mm[i]
            break
    
        
print(ans)