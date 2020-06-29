""" 
Napiš funkci totalPrice, která vypočte cenu noci v hotelu. 
Funkce bude mít dva parametry - persons (typ int) a breakfast (typ bool). 
Cena za noc za osobu je 850 Kč a cena za snídani za osobu je 125 Kč. 
Funkce vrátí výslednou cenu. Parametr breakfast je nepovinný a výchozí hodnota je False.

Funkci vyzkoušej se zadáním dvou i jedné hodnoty, např. totalPrice(3), totalPrice(2, True).
"""

def totalPrice(persons, breakfast=False):
  pricePerPerson = 850
  if breakfast:
    pricePerPerson += 125
  return pricePerPerson * persons

print(totalPrice(3))
print(totalPrice(3, True))
