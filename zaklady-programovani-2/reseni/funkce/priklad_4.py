def divisor(a, b):
  biggestDivisor = 1
  if a < b:
    stop = a
  else:
    stop = b
  for i in range(2, stop+1):
    if a % i == 0 and b % i == 0:
      biggestDivisor = i
  return biggestDivisor
