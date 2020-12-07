

# deque

import collections

a = input()

def isPalindrome(s:str):
    
    str = collections.deque()
    for i in s:
        if(i.isalnum()):
            str.append(i.lower())

    while(len(str) > 1):
        if(str.popleft() != str.pop()):
            return False

    return True        

if(isPalindrome(a)):
    print('palindrome')
else:
    print('not palindrome')
