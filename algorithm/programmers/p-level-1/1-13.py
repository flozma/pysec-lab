# 나누어 떨어지는 숫자 배열 [연습문제]

def solution(arr, divisor):
    new_list = [item for item in arr if item % divisor == 0]
    
    new_list.sort()
    
    return new_list if len(new_list) else [-1]