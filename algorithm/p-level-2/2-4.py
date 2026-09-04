# JadenCase 문자열 만들기 [연습문제]

def solution(s):
    new_list = list(s.split(" "))
    
    return " ".join([word.capitalize() for word in new_list ])