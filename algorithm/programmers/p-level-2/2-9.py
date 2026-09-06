# 피보나치 수 [연습문제]


def solution(n):
  fibonacci = [0, 1]
  MOD = 1234567

  for index in range(2, n + 1):
    fibonacci.append(fibonacci[index - 2] + fibonacci[index - 1])
    # fibonacci[index] = fibonacci[index - 2] + fibonacci[index - 1]
    # 이는 index = 2라면 2일 때 이미 존재하는 위치의 값을 바꾼다는 의미
    # - 위 코드는 python에서는 없는 index를 새로 만드는 문법이 아님

  return fibonacci[n] % MOD
