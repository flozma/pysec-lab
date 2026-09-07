# 카펫 [완전탐색 Brute-Force]
# Brute Force : 가능한 모든 경우의 수를 빠짐없이 전부 확인하여 정답을 찾는 단순하고 확실한 방법

def solution(brown, yellow):
    answer = [0, 0]
    sum = brown + yellow
    
    for width in range(sum - 1, 0, -1):
        if sum % width != 0:
            continue
        
        height = sum / width
        yellow_area = (width - 2) * (height - 2)
        brown_area = sum - yellow_area
        
        if yellow_area == yellow and brown_area == brown:
            answer[0] = width
            answer[1] = height
            break
    
    return answer
