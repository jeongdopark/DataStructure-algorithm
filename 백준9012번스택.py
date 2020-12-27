

n = int(input())

def check(argument):
    stack = []
    for i in argument:
        if i in ('(', '{', '['):
            stack.append(i)
        else:
            if(len(stack) > 0):
                if(i == ')' and stack.pop() != '(') or        
                (i == '}' and stack.pop() != '{') or 
                (i == ']' and stack.pop() != '['):
                    return 'NO'
            else:
                return 'NO'
    if(len(stack) == 0):
        return 'YES'
    else:
        return 'NO'

for _ in range(n):
    test = list(str(input()))
    print(check(test))
