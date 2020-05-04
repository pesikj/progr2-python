"""
Pokračuj ve své práci pro zásilkovou společnost. Společnost nově doručuje i cenné balíky, které mají zadanou určitou hodnotu.

Vytvoř třídu ValuablePackage, která dědí od třídy Package. ValuablePackage má navíc atribut value, ostatní atributy dědí od třídy Package.
Atribut value nastav pomocí funkce __init__. Ostatní parametry předej funkci __init__ třídy Package.
Vytvoř si alespoň jeden objekt a zkus volání jeho funkcí.
"""


class Package:
  def deliver(self):
    self.delivered = True
  def getInfo(self):
    if self.delivered:
      deliveredText = "Balík byl doručen"
    else:
      deliveredText = "Balík zatím nebyl doručen."
    print(f"Balík je na adresu {self.address} a váží {self.weightInKilos}. {deliveredText}")
  def __init__(self, address, weightInKilos):
    self.address = address
    self.weightInKilos = weightInKilos
    self.delivered = False

class ValuablePackage(Package):
  def __init__(self, address, weightInKilos, value):
    super().__init__(address, weightInKilos)
    self.value = value

valuablePackage = ValuablePackage("Plzeňská 123, Praha", 2, 10000)
valuablePackage.getInfo()
valuablePackage.deliver()
valuablePackage.getInfo()