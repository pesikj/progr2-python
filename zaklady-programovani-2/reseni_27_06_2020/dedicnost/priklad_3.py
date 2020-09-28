"""
Pokračuj ve své práci pro zásilkovou společnost. Společnost nyní eviduje jednotlivé řidiče a eviduje balíky, které má každý řidič doručit.

Vytvoř třídu Driver, která má dva atributy: name (jméno řidiče) a packageList (seznam balíků k doručení, na začátku je prázdný).

Přidej třídě funkci assignPackage, která bude mít jeden parametr - package (balík k doručení).

Funkce nejprve zkontroluje, zda balík již nebyl doručen. Pokud ano, vypíše funkce text: “Nelze přiřadit, balík již byl doručen.”

Pokud balík ještě nebyl doručen, je přidán do seznamu balíků packageList (použij funkci assign).

U řidiče chceme sledovat, kolik by měl ještě doručit balíků. Napiš funkci remainingPackages, která vrátí počet balíků, které má řidič přiřazené a ještě je nedoručil.
"""

class Package:
  def getInfo(self):
    text = f"Adresa: {self.address}. Hmotnost: {self.weightInKilos} kg. "
    if self.delivered:
      text += "Již byl doručen."
    else:
      text += "Ještě nebyl doručen."
    print(text)
  def deliver(self):
    self.delivered = True
  def __init__(self, address, weightInKilos):
    self.address = address
    self.weightInKilos = weightInKilos
    self.delivered = False
package1 = Package("Praha 5, 123", 3.0)
package2 = Package("Plzeň", 2.5)

class ValuablePackage(Package):
  def __init__(self, address, weightInKilos, value):
    super().__init__(address, weightInKilos)
    self.value = value

class Driver():
  def assignPackage(self, package):
    if package.delivered:
      print("Balík nelze přiřadit. Balík již byl doručen.")
    else:
      self.packageList.append(package)
  def remainingPackages(self):
    count = 0
    for package in self.packageList:
      if package.delivered == False:
        count += 1
    return count
  def printPackages(self):
    # Tato funkce je navíc, není v zadání.
    for package in self.packageList:
      package.getInfo()
  def __init__(self, name):
    self.name = name
    self.packageList = []
package = Package("Praha 6", 2.7)
valuablePackage = ValuablePackage("Liberec 123", 4.0, 2000)
pavel = Driver("Pavel")
pavel.assignPackage(valuablePackage)
pavel.assignPackage(package)
print(pavel.remainingPackages())
package.deliver()
print(pavel.remainingPackages())
