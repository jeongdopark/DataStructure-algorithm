

n = int(input())

for _ in range(n):
    total = 0
    add = 0
    ox = list(input())
    for i in ox:
        if(i == 'O'):
            add += 1
            total += add
        else:
            add = 0            
    print(total)