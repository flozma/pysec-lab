# 올바른 괄호 [스택 / 큐]

def solution(s):
    stack = list()
    
    for index in range(0, len(s)):
        if stack and stack[len(stack) - 1] == '(' and s[index] == ')':
            stack.pop()
        else:
            stack.append(s[index])
        
    return len(stack) == 0