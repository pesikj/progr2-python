class Package:
  def getInfo(self):
    print(self.address)
    print(self.weightInKilos)
    if self.delivered:
      print("Již byl doručen.")
    else:
      print("Ještě nebyl doručen.")
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
  def printPackages(self):
    # Tato funkce je navíc, není v zadání.
    for package in self.packageList:
      package.getInfo()
  def __init__(self, name):
    self.name = name
    self.packageList = []
valuablePackage = ValuablePackage("Liberec 123", 4.0, 2000)
pavel = Driver("Pavel")
pavel.assignPackage(valuablePackage)
pavel.printPackages()
