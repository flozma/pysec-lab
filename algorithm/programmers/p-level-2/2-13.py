def solution(n):
  MOD = 1234567

  # fibonacci f(n) = f(n-2) + f(n-1)
  # 1 1
  # 2 2
  # 3 3
  # 4 5

  if n == 1:
    return 1
  if n == 2:
    return 2

  a, b = 1, 2

  for i in range(3, n + 1):
    a, b = b, (a + b) % MOD

  return b
