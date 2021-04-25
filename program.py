from abc import ABC, abstractproperty

class Obrazec(ABC):
  @abstractproperty
  def obvod():
    pass

  @abstractproperty
  def obsah():
    pass

class Ctverec(Obrazec):
  @property
  def obvod(self):
    return self.a * self.a
  
  @property
  def obsah(self):
    return 4 * self.a

  def __init__(self, a):
    self.a = a

class Obdelnik(Obrazec):
  @property
  def obvod(self):
    return self.a * self.b
  
  @property
  def obsah(self):
    return 4 * self.b

  def __init__(self, a, b):
    self.a = a
    self.b = b

maly_ctverec = Ctverec(10)
velky_obdelnik = Obdelnik(20, 25)
plocha_celkem = maly_ctverec.obsah + velky_obdelnik.obsah
print(f"Celková plocha obou obrazců je {plocha_celkem}.")
