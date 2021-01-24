"""
Zkus pro našeho nakladatele vytvořit software s využitím tříd a objektů. 
Vytvoř tedy třídu Book, která reprezentuje knihu. Každá kniha bude mít atributy title, 
pages a price. Hodnoty nastav ve funkci __init__.

Přidej knize funkci getInfo, která vypíše informace o knize v nějakém pěkném formátu.
Občas se stane, že se kniha moc neprodává a knihkupec se snaží nalákat kupující slevou. 
Přidej funkci discount, která bude mít jeden parametr - velikost slevy v procentech. 
Funkce sníží cenu knihy o dané procento.
"""

class Book:
  def discount(self, discountInPercents):
    self.price *= (1 - discountInPercents/100)
  def getInfo(self):
    print(f"Název knihy: {self.title}. Počet stran: {self.pages}. Cena: {self.price}")
  def __init__(self, title, pages, price):
    self.title = title
    self.pages = pages
    self.price = price

kniha = Book("Noc, která mě zabila", 590, 499)
kniha.getInfo()
kniha.discount(10)
kniha.getInfo()
