



n = int(input())
mm = [0] * 1000001
mm[1] = 0
mm[2] = 1
mm[3] = 1

if(n >= 4):
    for i in range(4, n+1):
        mm[i] = mm[i-1] + 1
        if(i % 2 == 0 and mm[i] > mm[i//2]+ 1):
            mm[i] = mm[i//2]+ 1
        if(i % 3 == 0 and mm[i] > mm[i//3] + 1):
            mm[i] = mm[i//3]+ 1

print(mm[n])
