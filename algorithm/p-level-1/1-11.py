# 음양 더하기

def solution1(absolutes, signs):
    answer = 0
    
    for key, value in enumerate(signs):
        print(key, value)
        if value == True:
            answer += absolutes[key] * 1
        else:
            answer += absolutes[key] * -1
        
        
    return answer


def solution2(absolutes, signs):
    for absolute, sign in zip(absolutes, signs):
        if sign:
            answer += absolute
        else:
            answer -= absolute
            
    return answer