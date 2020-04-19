start = int(input("Zadej začátek: "))
stop = int(input("Zadej konec: "))

print("Čísla dělitelná 3 i 4 současně:")
for i in range(start, stop):
  if i % 3 == 0 and i % 4 == 0:
    print(i)

print("Čísla dělitelná 5 nebo 6:")
for i in range(start, stop):
  if i % 5 == 0 or i % 6 == 0:
    print(i)