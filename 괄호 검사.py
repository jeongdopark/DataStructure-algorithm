

n = input()

stack = []


def stackTest(test):
    leftCount = 0
    rightCount = 0
    for i in test:
        print(i)
        if(i == '{' or i == '(' or i == '['):
            stack.append(i)
            leftCount += 1
        if(i == '}' or i == ')' or i == ']'):
            if(len(stack) == 0):
                return False
            cur = stack.pop()
            rightCount += 1
            if(cur == '{'):
                if(i != '}'):
                    return False
            if(cur == '('):
                if(i != ')'):
                    return False
            if(cur == '['):
                if(i != ']'):
                    return False
    if(leftCount != rightCount):
        return False
    print(leftCount, rightCount)
    return True    

print(stackTest(n))