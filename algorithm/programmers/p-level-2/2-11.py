# 귤 고르기 [연습문제]


def solution(k, tangerine):
  answer = 0

  # 서로 다른 종류의 수 최소화
  # 1. dict로 각 tangerine이 몇개씩 반복되는지 확인
  # 2. 각 tangerine의 개수만 뽑아 큰 값순서로 정렬
  # 3. k가 0이거나 0보다 작기 전까지 갯수 k에서 tangerine별 개수를 뺀다.

  fruit_dict = {}
  for item in tangerine:
    if item not in fruit_dict:
      fruit_dict[item] = 0

    fruit_dict[item] += 1

  fruit_items = sorted(fruit_dict.values(), reverse=True)

  for value in fruit_items:
    if k <= 0:
      break

    k -= value
    answer += 1

  return answer


from collections import Counter


def solution2(k, tangerine):
  count = 0
  counter_value_list = Counter(tangerine).values()

  for value in sorted(counter_value_list, reverse=True):
    if k <= 0:
      break

    k -= value
    count += 1

  return count
