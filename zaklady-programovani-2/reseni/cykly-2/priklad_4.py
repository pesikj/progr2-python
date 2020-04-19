number = int(input("Zadej číslo: "))
prime = True
for i in range(2, number):
  if number % i == 0:
    prime = False
if prime:
  print("Číslo je prvočíslo!")
else:
  print("Číslo není prvočíslo!")
