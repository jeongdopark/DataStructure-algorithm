

n = 9
num = list(int(input()) for _ in range(n))
maxim = 0
ans = 0
for i in range(n):
    if(maxim < num[i]):
       maxim = num[i]
       ans = i
print(maxim)
print(ans+1) 
