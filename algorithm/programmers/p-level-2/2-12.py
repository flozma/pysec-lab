# 구명보트 [탐욕법(Greedy)]

# greedy + two-pointer
# Greedy 알고리즘은 매 단계에서 당장 가장 유리하다고 판단되는 선택을 하면서 답을 구하는 방법


def solution(people, limit):
  answer = 0
  people.sort(reverse=True)

  left = 0  # 제일 큰 몸무게의 사람 index
  right = len(people) - 1  # 제일 낮은 몸무게의 사람 index

  while left < right:
    sum = people[left] + people[right]

    if sum > limit:
      # 가장 무거운 사람이 가장 가벼운 사람과도 탈 수 없는 경우
      # -> 다른 누구와도 탈 수 없음 (무거운 사람 혼자 보내기 위해 answer += 1)
      left += 1
    else:
      # 함께 탈 수 있다면 두 사람을 같은 보트로 보내기
      # -> answer += 1
      left += 1
      right -= 1

    answer += 1

  if left == right:  # 1명 남아 있는 경우, 보트 1개 추가
    answer += 1

  return answer
