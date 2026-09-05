# 숫자의 표현 [연습문제]

def solution(n):
    answer = 0
    
    # n의 홀수인 약수의 개수
    for item in range(1, n+1):
        if n % item == 0 and item % 2 == 1:
            answer += 1
            
    return answer