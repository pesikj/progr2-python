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
