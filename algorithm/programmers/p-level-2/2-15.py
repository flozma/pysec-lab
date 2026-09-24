# 행렬의 곱셈 [연습문제]

def solution(arr1, arr2):
    m = len(arr1)
    n = len(arr1[0])
    r = len(arr2[0])
    
    answer = [[0 for _ in range(r)] for i in range(m)]
    
    for i in range(m):
        for k in range(r):
            for j in range(n):
                answer[i][k] += arr1[i][j] * arr2[j][k] 
    
    return answer