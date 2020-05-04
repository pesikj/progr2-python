"""
Požádej uživatele o zadání celého čísla. Následně urči, zda je toto číslo prvočíslo.

Prvočíslo je číslo, které je dělitelné beze zbytku pouze 2 čísly - 1 a sebou samotným.

Například 5 je prvočíslo, protože je dělitelná pouze 1 a 5.
Naoapk 4 není prvočíslo, protože je dělitelná 1, 2 a 4.
"""

number = int(input("Zadej číslo: "))
prime = True
for i in range(2, number):
  if number % i == 0:
    prime = False
    break
if prime:
  print("Číslo je prvočíslo!")
else:
  print("Číslo není prvočíslo!")
