# 연속 부분 수열 합의 개수 [연습문제] ⭐️ 시간복잡도 개선 필요
def solution(elements):
  n = len(elements)
  new_set = set()

  # 길이가 index인 연속 부분 수열을 만들기 위한 setting
  for index in range(1, n + 1):
    # 길이가 length인 연속 부분 수열
    for _ in range(n):
      check = sum(elements[:index])
      if check not in new_set:
        new_set.add(check)

      # 가장 첫 번째 요소를 element 가장 뒤에 추가
      elements.append(elements.pop(0))

  return len(new_set)
