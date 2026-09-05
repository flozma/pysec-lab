# 이진 변환 반복하기 [월간 코드 챌린지 시즌 1]

# bin_s = bin(int(s))
# int_s = int(bin_s, 2)

def solution(s):
    counter = 0
    removal_zero_sum = 0
    new_str = s
    
    while(1):
        if new_str == "1":
            break
        
        new_str_len = len(new_str)
        list_s = [char for char in new_str.split("0") if char != ""]
        joined_str = "".join(list_s)
        joined_str_len = len(joined_str)     

        new_str = bin(joined_str_len).lstrip("0b")
        
        counter += 1
        removal_zero_sum += new_str_len - joined_str_len
        
    return [counter, removal_zero_sum]


def solution2(s):
    new_str = s
    iteration = 0
    counter = 0
    
    while new_str != "1":
        iteration += 1
        counter += new_str.count('0')
        new_str = bin(new_str.count('1'))[2:]
        
        
    return [iteration, counter]


