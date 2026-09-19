# 할인 행사 [연습문제]


def solution(want, number, discount):
  answer = 0

  target_array = []

  for key, value in enumerate(discount):
    array = discount[key : key + 10]

    if len(array) != 10:
      continue

    count = 0

    for item, counter in list(zip(want, number)):
      if array.count(item) != counter:
        break

      count += 1

    if count == len(want):
      target_array.append(array)
      answer += 1

  return answer
