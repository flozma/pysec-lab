# 점프와 순간 이동 [Summer/Winter Coding]
# Greedy Algorithm



def solution(n):
    usage_of_battery = 0
    
    # 점프 => K칸 이동 => 건전지 - K
    # 순간이동 => 현재까지 온거리 x 2 => 건전지 감소 x
    # 건전지 사용 최소화를 위해 점프로 이동 최소

    # Think of it in a reverse way
    
    while n > 0:
        if n % 2 == 0:
            n = n // 2
        elif n % 2 != 0:
            n -= 1
            usage_of_battery += 1     
        

    return usage_of_battery