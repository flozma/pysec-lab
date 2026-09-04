# 정수 제곱근 판별 [연습문제]

from math import sqrt


def solution(n):
  answer = 0
  sqrted = int(sqrt(n))

  for item in range(1, sqrted + 1):
    if item**2 == n:
      answer = (item + 1) ** 2
    else:
      answer = -1

  return answer


def solution2(n):
  return -1 if not sqrt(n).is_integer() else (sqrt(n) + 1) ** 2
