n = input()
list = []
stack = []

for i in n:
    list.append(i)

sum = 0
for j in range(len(list)):
    if(n[j] == '(' ):
        stack.append(n[j])
    else:
        if(n[j-1] == '('):
            stack.pop()
            sum += len(stack)
        elif(n[j-1] == ')'):
            stack.pop()
            sum += 1
    
prin(sum)