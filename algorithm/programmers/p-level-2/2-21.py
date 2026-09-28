# 의상 [해시]


def solution(clothes):
  answer = 1
  hash_table = {}

  for value, category in clothes:
    if category not in hash_table:
      hash_table[category] = [value]
    else:
      hash_table[category] += [value]

  for temp in hash_table.values():
    n = len(temp) + 1
    answer *= n

  return answer - 1
