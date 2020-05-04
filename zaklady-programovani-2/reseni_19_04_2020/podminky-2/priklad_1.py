"""
Požádejme uživatele, ať zadá celé číslo. Vypište, zda je číslo dělitelné 3 i 4 současně.

Tip: nezapomeňte si zadané číslo převést na int.
"""

number = int(input("Zadej číslo: "))
if number % 3 == 0 and number % 4 == 0:
  print("Číslo je dělitelné 3 i 4 zároveň.")
else:
  print("Číslo není dělitelné 3 i 4 zároveň.")