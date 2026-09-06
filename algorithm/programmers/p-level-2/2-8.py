# 다음 큰 숫자 [연습문제]


def solution(n):
  next_big_int = n

  while 1:
    next_big_int += 1

    if bin(next_big_int).split("0b")[1].count("1") == bin(n).split("0b")[1].count("1"):
      break

  return next_big_int
