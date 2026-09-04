# 콜라츠 추측 [연습문제]

def solution(num):
    result = 0
    iteration = 0
    
    while num != 1:
        if iteration == 500:
            break
        else:            
            if num % 2 == 0:
                num /= 2
            else:
                num = num * 3 + 1
            
            iteration += 1
    
    return -1 if iteration == 500 else iteration



def solution2(num):
    if num == 1:
        return 0
    
    for iteration in range(500):
        num = num // 2 if num % 2 == 0 else (num * 3 + 1)
    
        if num == 1:
            return iteration + 1

    return -1