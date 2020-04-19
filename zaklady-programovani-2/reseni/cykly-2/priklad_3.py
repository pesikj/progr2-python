numberOfGuests = int(input("Zadej počet hostů: "))
guestList = []
for i in range(numberOfGuests):
  newGuest = input("Zadej jméno hosta nebo konec pro ukončení: ")
  if newGuest == "konec":
    break
  guestList.append(newGuest)
print(guestList)