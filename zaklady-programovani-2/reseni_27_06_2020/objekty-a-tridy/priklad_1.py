"""
Uvažuj, že navrhuješ software pro zásilkovou společnost.

Vytvoř třídu Package, která bude mít tři atributy - address, weightInKilos a delivered. 
První dva atributy nastav pomocí parametrů funkce __init__. Parametr delivered nastav na začátku jako False.

Připoj ke třídě funkci deliver, která změní hodnotu parametru delivered na True.

Přidej funkci getInfo, která vypíše adresu, hmotnost a informaci o tom, zda byl balík již doručen.

Zkus si vytvořit nějaké objekty ze třídy Package a ověř, že vše funguje.
"""


class Package:
  def deliver(self):
    self.delivered = True
  def __str__(self):
    if self.delivered:
      deliveredText = "Balík byl doručen"
    else:
      deliveredText = "Balík zatím nebyl doručen."
    return "Balík je na adresu {self.address} a váží {self.weightInKilos}. {deliveredText}"
  def __init__(self, address, weightInKilos):
    self.address = address
    self.weightInKilos = weightInKilos
    self.delivered = False

