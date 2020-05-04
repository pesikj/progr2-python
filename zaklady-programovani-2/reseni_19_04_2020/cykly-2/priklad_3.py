"""
Vraťte se k příkladu se zadáváním seznamu hostu na párty a zkopírujte si kód k sobě do editoru. 
Upravte program tak, že pokud uživatel v průběhu zádávání jmen napíše “konec”, 
cyklus na zadávání jmen se ukončí.
"""

numberOfGuests = int(input("Zadej počet hostů: "))
guestList = []
for i in range(numberOfGuests):
  newGuest = input("Zadej jméno hosta nebo konec pro ukončení: ")
  if newGuest == "konec":
    break
  guestList.append(newGuest)
print(guestList)