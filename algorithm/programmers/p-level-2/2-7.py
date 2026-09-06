# 짝지어 제거하기 [2017 팁스타운]


def solution(s):
  stack = []

  for index in range(0, len(s)):
    if len(stack) != 0 and stack[len(stack) - 1] == s[index]:
      stack.pop()
    else:
      stack.append(s[index])

  return 1 if len(stack) == 0 else 0


def solution2(s):
  stack = []

  for char in s:
    if len(stack) == 0:
      stack.append(char)
    elif stack[-1] == char:
      stack.pop()
    else:
      stack.append(char)

  return 1 if len(stack) == 0 else 0
