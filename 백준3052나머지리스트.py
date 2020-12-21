
num = list(int(input()) for _ in range(10))
ans = []
for i in range(10):
    if(not (num[i] % 42 in ans)):
        ans.append(num[i] % 42)
print(len(ans))

