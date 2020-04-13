Posledním konceptem, se kterým se v tomto kurzu seznámíme, jsou objekty (`objects`). Na objektech je založeno objektově orientované programování, tedy princip psaní programů, ve kterém jsou bloky kódu poskládané do objektů. 

Objekty mají často reprezentovat nějaké objekty v realitě. Pokud bychom například vyvíjeli administrativní software pro firmy, vytvoříme tam objekty reprezentující zaměstnance, pracoviště, firemní automobily atd.

### Objekty a třídy

Před vytvořením nějakého objektu musíme vytvořit **třídu** (`class`). Vztah mezi třídou a objekty si můžeme představit na příkladu formulářů. Třída je prázdný formulář - obsahuje kolonky, které by měly být vyplněny. Objekt je pak vyplněný formulář, který už má v sobě nějaká konkrétní data. Podobně jako formulářů můžeme vyplnit více, může na základě jedné třídy vzniknout několik objektů. Objekty jsou vzájemně nezávislé, takže práce s jedním objektem neovlivňuje ostatní. Analogicky, pokud upravujeme jeden formulář, nijak tím neupravujeme ostatní.

Třídy mají dvě důležité charakteristiky - mají atributy (v nich uchováváme hodnoty) a funkce (vykonávají nějaké příkazy). Atributy jsou vlastně proměnné, pouze jsou navázané na konkrétní objekt. Funkce jsme poznali v předchozí kapitole, jsou ale též navázané na konkrétní objekt a pracují s jeho atributy.

Popišme si konkrétně náš příklad software pro firmy. V něm můžeme mít například třídu `Employee`, který reprezentuje zaměstnance. Třída může mít jméno, pracovní pozici, oddělení, plat, zbývající dny dovolené atd. Zaměstnanec může mít i funkce - například funkci na vybrání dovolené, vytištění výplatní pásky atd.

Před vytvářením objektů je třeba mít připravenou třídu, na základě které objekt vznikne. K tomu použijeme klíčové slovo `class`. Za něj přijde název třídy a opět dvojtečka. Pro začátek si vytvořme třídu jen s jednou funkcí `getInfo`, která vypíše informace o zaměstnanci.

Všimni si parametru `self` u funkce. Tím se odkazujeme na konkrétní objekt. Pomocí `self` se odkazujeme na atributy objektu. Pokud chceme získat hodnotu atributu, napíšeme klíčové slovo `self`, tečku a název atributu. Tečky při práci s objekty používáme velmi často a jsou jakousi analogií k hranatým závorkám u sekvencí.

```py
class Employee:
  def getInfo(self):
    return f"{self.name} pracuje na pozici {self.position}."
```

Protože pracujeme s funkcí, můžeme (ale nemusíme) použít klíčové slovo `return` a vrátit nějakou hodnotu.

Zkusme si nyní vytvořit objekt, který reprezentuje zaměstnance Františka. Objekt vytvoříme podobně, jako bychom volali funkci - použijeme název třídy a kulaté závorky. Objekt uložíme do proměnné `franta`. Dále přiřadíme proměnné `franta` hodnoty atributů `name` a `position` a vyzkoušíme funkci `getInfo`. 

```py
franta = Employee()
franta.name = "František Novák"
franta.position = "konstruktér"
print(franta.getInfo())
```

Zkusíme přidat ještě jednoho zaměstnance.

```py
vasek = Employee()
vasek.name = "Václav Dvořák"
vasek.position = "svářeč"
```

Nyní vyzkoušíme vypsat informace obou zaměstnanců.

```py
print(franta.getInfo())
print(vasek.getInfo())
```

### Funkce `__init__`

Z výpis vidíme, že se informace zaměstnanců nijak nepomíchaly a každý zaměstnanec má uložené své vlastní údaje.

Tento postup ale působí lehce chaoticky. V naší analogii s formuláři to vypadá, že si každý může do formuláře vyplnit, co chce. Abychom měli objekt více pod kontrolou, můžeme využít funkce `__init__` (název zapisujeme včetně podtržítek). Tato funkce je speciální v tom, že je zavolána při vytvoření objektu. Můžeme jí (jako jakékoli jiné funkci) přiřadit parametry a zajistit, aby hodnoty parametrů uložila jako atributy objektu.

```py
class Employee:
  def getInfo(self):
    return f"{self.name} pracuje na pozici {self.position}."
  def __init__(self, name, position):
    self.name = name
    self.position = position
```

Tento styl je standardní - parametry jsou pojmenované stejně jako atributy objektu, kam se jejich hodnoty ukládají. Mezi `self.name` a `name` je tedy tento rozdíl:

- `name` je parametr funkce `__init__` a jeho hodnota není přístupná pro ostatní funkce objektu.
- `self.name` je atribut objektu, který v objektu zůstane a můžou s ním pracovat ostatní funkce. 

Díky funkci `__init__` máme zjednodušené i vytváření objektu, protože hodnoty parametrů nyní vepíšeme přímo do závorek při vytváření objektu.

```py
franta = Employee("František Novák", "konstruktér")
vasek = Employee("Václav Dvořák", "svářeč")

print(franta.getInfo())
print(vasek.getInfo())
```

Nyní již víme, že každý objekt třídy `Employee` má vyplněné jméno a pozici. Zkusme nyní naši třídu obohatit o novou funkci - čerpání dovolené. Na začátku bude mít každý zaměstnanec nárok na dovolenou, kterou může v průběhu roku čerpat. Čerpání zajistíme pomocí funkce `takeHoliday`. Budeme hlídat i to, aby zaměstnanec nárok na dovolenou nepřečerpal.

```py
class Employee:
  def takeHoliday(self, days):
    if self.remainingHolidayDays >= days:
      self.remainingHolidayDays -= days
      return f"Užij si to. Poté zbývá {self.remainingHolidayDays} dní."
    else:
      return f"Bohužel už máš nárok jen na {self.remainingHolidayDays} dní."
  def getInfo(self):
    return f"{self.name} pracuje na pozici {self.position}."
  def __init__(self, name, position):
    self.name = name
    self.position = position
    self.remainingHolidayDays = 25
```

Nyní se podívejme, jak budou vyřizovány Františkovy žádosti o dovolenou.

```py
franta = Employee("František Novák", "konstruktér")

print(franta.takeHoliday(5))
print(franta.takeHoliday(15))
print(franta.takeHoliday(10))
```

Tím jsme si ukázali, jak vytvořit třídu, objekty a jak s nimi pracovat.

## Dědičnost

Třídy mají ještě jednu zajímavou vlastnost - mohou od sebe dědit. Uvažujme třeba, že bychom chtěli vytvořit novou třídu `Manager`, která reprezentuje zaměstnance, který má nějaké podřízené. U manažera bychom rádi měli seznam jeho podřízených. Jinak se samozřejmě manažer od ostatních nijak neliší - má jméno, název pozice i nárok na dovolenou. 

Ideální by tedy bylo mít kopii třídy `Employee`, která bude mít nový atribut `subordinateList` (seznam jeho podřízených). Samozřejmě bychom mohli kód třídy `Employee` zkopírovat a upravit, ale díky dědičnosti to můžeme udělat i lépe.

Můžeme novou třídu `Manager` postavit na základě třídy `Employee`. Třída `Manager` tak zdědí od třídy `Employee` všechny atributy a funkce, a my jen přidáme nebo upravíme, co potřebujeme.

Napíšeme tedy novou funkci `__init__`, protože potřebujeme vytvořit atribut `subordinateList` jako prázdný list. Poté přidáme funkci `addSubordinate`, která k listu připojí jednoho podřízeného.

```py
class Manager(Employee):
  def addSubordinate(self, newSubordinate):
    self.subordinateList.append(newSubordinate)
  
  def __init__(self, name, position):
    self.name = name
    self.position = position
    self.remainingHolidayDays = 25
    self.subordinateList = []
```

Zkusíme si nyní vytvořit objekt, který bude reprezentovat manažera. U objektu vyzkoušíme, zda u ní funguje metody `getInfo`. Tuto metodu jsme pro třídu `Manager` neprogramovali, měla by být zděděná od třídy `Employee`.

```py
boss = Manager("Marian Přísný", "vedoucí konstrukčního oddělení")
print(boss.getInfo())
```

Zatím vše funguje, přesto můžeme náš kód ještě vylepšit. Ve funkci `__init__` musíme poněkud nešikovně opisovat tři řádky, které nastavují hodnoty atributů. Přitom ty stejné řádky už jsou v třídě `Employee`. Mohli bychom nějak existující kód z třídy `Employee` upravit? 

Ve skutečnosti ano. Využijeme k tomu speicální funkci `super`, kterou se odvoláme na mateřskou třídu aktuální třídy. Následně můžeme použít tečku a zavolat funkci `__init__`. Tím voláme funkci `__init()__` mateřské třídy `Employee`.

```py
class Manager(Employee):
  def addSubordinate(self, newSubordinate):
    self.subordinateList.append(newSubordinate)
  
  def __init__(self, name, position):
    super().__init__(name, position)
    self.subordinateList = []
```

Třída `Manager` se tak o něco zkrátila a zpřehlednila.

Náš kód už bychom mohli spustit, ale nemohli bychom pořádně otestovat, že přidávání podřízených funguje. My je totiž ukládáme, ale zatím nemáme funkci pro jejich vypsání. Přidáme tedy funkci `getSubordinates`, která vrátí informaci o podřízených manažera.

```py
class Manager(Employee):
  def addSubordinate(self, newSubordinate):
    self.subordinateList.append(newSubordinate)

  def getSubordinates(self):
    subordinates = f"{self.name} má tyto podřízené: "
    for subordinate in self.subordinateList:
      subordinates += subordinate.name + ", "
    return subordinates
  
  def __init__(self, name, position):
    super().__init__(name, position)
    self.subordinateList = []
```

Nyní můžeme vše vyzkoušet. Vedoucímu, který je uložený v proměnné `boss`, přiřadíme dva podřízené. Následně si zkusíme proměnné vypsat.

```py
franta = Employee("František Novák", "konstruktér")
vasek = Employee("Václav Dvořák", "svářeč")

boss = Manager("Marian Přísný", "vedoucí konstrukčního oddělení")
boss.addSubordinate(franta)
boss.addSubordinate(vasek)
print(boss.getSubordinates())
```

Náš program tedy vytvoří tři objekty - dva zaměstnance a jednoho manažera. Manažerovi jsme přiřadili zaměstnance jako podřízené. A vidíme, že naše akce proběhla správně, protože tito dva zaměstnanci se objevili ve výpisu podřízených.

@exercises ## Další možnosti podmínek [

- balik
- cenny-balik
- zkusebka ]@

@exercises bonuses [

- ridic ]@