# 괄호 회전하기 [월칸 코드 챌린지 시즌 2]

# Stack
def check(s):
  stack = []

  for char in s:
    if len(stack) == 0:
      stack.append(char)
    else:
      # 뒤이어 짝이 맞는다는 이야기
      if char == ")" and stack[-1] == "(":
        stack.pop()
      elif char == "]" and stack[-1] == "[":
        stack.pop()
      elif char == "}" and stack[-1] == "{":
        stack.pop()
      else:
        stack.append(char)
  return 1 if len(stack) == 0 else 0


def solution(s):
  answer = 0

  for index in range(len(s)):
    if check(s):
      answer += 1

    s = s[1:] + s[:1]

  return answer
