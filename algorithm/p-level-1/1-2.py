# 약수의 합 [연습문제]


def solution(n):
  answer = 0

  for item in range(1, n + 1):
    if n % item == 0:
      answer += item

  # answer = sum([item for item in range(1, n+1) if n % item == 0])

  return answer
