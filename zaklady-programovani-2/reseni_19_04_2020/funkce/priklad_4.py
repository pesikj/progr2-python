"""
Napiš funkci divisor, která má dva parametry - čísla a a b. 
Úkolem funkce je najít největšího společného dělitele. 
K nalezení použij cyklus for a zbytek po celočíselném čelení - operátor %.
"""

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
