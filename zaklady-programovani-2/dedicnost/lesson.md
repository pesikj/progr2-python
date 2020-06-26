## Dědičnost

Třídy mají jednu zajímavou vlastnost - mohou od sebe **dědit**. Uvažujme třeba, že bychom chtěli vytvořit novou třídu `Manager`, která reprezentuje zaměstnance, který má nějaké podřízené. U manažera bychom rádi měli seznam jeho podřízených. Jinak se samozřejmě manažer od ostatních nijak neliší - má jméno, název pozice i nárok na dovolenou. 

Ideální by tedy bylo mít kopii třídy `Employee`, která bude mít nový atribut `subordinates` (seznam jeho podřízených). Samozřejmě bychom mohli kód třídy `Employee` zkopírovat a upravit, ale díky dědičnosti to můžeme udělat i lépe. Můžeme novou třídu `Manager` postavit na základě třídy `Employee`. Třída `Manager` tak zdědí od třídy `Employee` všechny atributy a funkce, a my jen přidáme nebo upravíme, co potřebujeme.

Napíšeme tedy novou funkci `__init__`, protože potřebujeme vytvořit atribut `subordinates` jako prázdný list. Poté přidáme funkci `addSubordinate`, která k listu připojí jednoho podřízeného.

```py
class Manager(Employee):
  def addSubordinate(self, newSubordinate):
    self.subordinates.append(newSubordinate)

  def __init__(self, name, position):
    self.name = name
    self.position = position
    self.remainingHolidayDays = 25
    self.subordinates = []
```

Zkusíme si nyní vytvořit objekt, který bude reprezentovat manažera. U objektu vyzkoušíme, zda u ní funguje metoda `getInfo`. Tuto metodu jsme pro třídu `Manager` neprogramovali, měla by být zděděná od třídy `Employee`.

```py
boss = Manager("Marian Přísný", "vedoucí konstrukčního oddělení")
print(boss.getInfo())
```

Zatím vše funguje, přesto můžeme náš kód ještě vylepšit. Ve funkci `__init__` musíme poněkud nešikovně opisovat tři řádky, které nastavují hodnoty atributů. Přitom ty stejné řádky už jsou v třídě `Employee`. Mohli bychom nějak existující kód z třídy `Employee` upravit? 

Ve skutečnosti ano. Využijeme k tomu speciální funkci `super`, kterou se odvoláme na **mateřskou třídu aktuální třídy**. Následně můžeme použít tečku a zavolat funkci `__init__`. Tím tedy voláme funkci `__init()__` mateřské třídy `Employee`.

```py
class Manager(Employee):
  def addSubordinate(self, newSubordinate):
    self.subordinates.append(newSubordinate)

  def __init__(self, name, position):
    super().__init__(name, position)
    self.subordinates = []
```

Třída `Manager` se tak o něco zkrátila a zpřehlednila.

Náš kód už bychom mohli spustit, ale nemohli bychom pořádně otestovat, že přidávání podřízených funguje. My je totiž ukládáme, ale zatím nemáme funkci pro jejich vypsání. Přidáme tedy funkci `getSubordinates`, která vrátí informaci o podřízených manažera.

```py
class Manager(Employee):
  def addSubordinate(self, newSubordinate):
    self.subordinates.append(newSubordinate)

  def getSubordinates(self):
    subordinates = f"{self.name} má tyto podřízené: "
    for item in self.subordinates:
      subordinates += item.name + ", "
    return subordinates
  
  def __init__(self, name, position):
    super().__init__(name, position)
    self.subordinates = []
```

Nyní můžeme vše vyzkoušet. Vedoucímu, který je uložený v proměnné `boss`, přiřadíme dva podřízené. Následně si zkusíme proměnné vypsat.

```py
frantisek = Employee("František Novák", "konstruktér")
klara = Employee("Klára Nová", "konstruktérka")

boss = Manager("Marian Přísný", "vedoucí konstrukčního oddělení")
boss.addSubordinate(frantisek)
boss.addSubordinate(klara)
print(boss.getSubordinates())
```

Náš program tedy vytvoří tři objekty - dva zaměstnance a jednoho manažera. Manažerovi jsme přiřadili zaměstnance jako podřízené. A vidíme, že naše akce proběhla správně, protože tito dva zaměstnanci se objevili ve výpisu podřízených.

@exercises ## Příklady na dědičnost [

- cenny-balik
- castecny-uvazek ]@

@exercises bonuses [
  
- ridic ]@