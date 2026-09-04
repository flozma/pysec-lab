# 없는 숫자 더하기

def solution(numbers):
    answer = 0
    
    original = list(range(0, 10))
    
    
    for num in original:
        if num not in numbers:
            answer += num
          
    return answer

def solution2(numbers):
    return 45 - sum(numbers)