# 최솟값 만들기

def solution(A,B):
    zip_arr = zip(sorted(A), sorted(B, reverse=True))
    return sum([num1 * num2 for num1, num2 in zip_arr])