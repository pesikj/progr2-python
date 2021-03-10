Dalším konceptem, se kterým se v tomto kurzu seznámíme, jsou objekty (`objects`). Na objektech je založeno **objektově orientované programování** (Object-oriented programming - OOP), tedy princip psaní programů, ve kterém jsou bloky kódu poskládané do **tříd** a **objektů**. 

Objekty mají často reprezentovat nějaké entity v realitě. Pokud bychom například vyvíjeli administrativní software pro firmy, vytvoříme tam objekty reprezentující zaměstnance, pracoviště, firemní automobily atd. U zásilkové společnosti bychom vytvářeli objekty, které reprezentují balíky, řidiče atd.

## Objekty a třídy

Na začátku si musíme vytvořit **třídu** (`class`). Vztah mezi třídou a objekty si můžeme představit na příkladu formulářů. Třída je prázdný formulář - obsahuje kolonky, které by měly být vyplněny. Objekt je pak vyplněný formulář, který už má v sobě nějaká konkrétní data. Podobně jako formulářů můžeme vyplnit více, může na základě jedné třídy vzniknout několik objektů. Objekty jsou vzájemně nezávislé, takže práce s jedním objektem neovlivňuje ostatní. Analogicky, pokud upravujeme jeden formulář, nijak tím neměníme ostatní.

Třídy mají dvě důležité charakteristiky - mají **atributy** (v nich uchováváme hodnoty) a **funkce** (vykonávají nějaké příkazy). Atributy jsou vlastně proměnné, pouze jsou navázané na konkrétní objekt. Funkce jsme poznali v předchozí kapitole, jsou ale též navázané na konkrétní objekt a pracují s jeho atributy.

Popišme si konkrétně náš příklad software pro firmy. V něm můžeme mít například třídu `Employee`, který reprezentuje zaměstnance. Třída může mít jméno, pracovní pozici, oddělení, plat, zbývající dny dovolené atd. Zaměstnanec může mít i funkce - například funkci na vybrání dovolené, vytištění výplatní pásky, výpočet věku atd.

Před vytvářením objektů je třeba mít připravenou třídu, na základě které objekt vznikne. K tomu použijeme klíčové slovo `class`. Za něj přijde **název třídy** a opět **dvojtečka**. Pro začátek si vytvořme třídu jen s jednou funkcí `getInfo`, která vypíše informace o zaměstnanci.

Všimni si parametru `self` u funkce. Pomocí `self` se **odkazujeme na atributy objektu**. Pokud chceme získat hodnotu atributu, napíšeme klíčové slovo `self`, **tečku** a **název atributu**. Tečky při práci s objekty používáme velmi často a jsou jakousi analogií k hranatým závorkám u sekvencí.

```py
class Employee:
  def getInfo(self):
    return f"{self.name} pracuje na pozici {self.position}."
```

Protože pracujeme s funkcí, můžeme (ale nemusíme) použít klíčové slovo `return` a vrátit nějakou hodnotu.

Zkusme si nyní vytvořit objekt, který reprezentuje zaměstnance Františka. Objekt vytvoříme podobně, jako bychom volali funkci - použijeme **název třídy** a **kulaté závorky**. Objekt uložíme do proměnné `frantisek`. Dále přiřadíme proměnné `frantisek` hodnoty atributů `name` a `position` a vyzkoušíme funkci `getInfo`. 

```py
frantisek = Employee()
frantisek.name = "František Novák"
frantisek.position = "konstruktér"
print(frantisek.getInfo())
```

Zkusíme přidat ještě jednu zaměstnankyni.

```py
klara = Employee()
klara.name = "Klára Nová"
klara.position = "konstruktérka"
```

Nyní vyzkoušíme vypsat informace obou zaměstnanců.

```py
print(frantisek.getInfo())
print(klara.getInfo())
```

## Funkce `__init__`

Z výpis vidíme, že se informace zaměstnanců nijak nepomíchaly a každý zaměstnanec má uložené své vlastní údaje.

Tento postup ale působí lehce chaoticky. V naší analogii s formuláři to vypadá, že si každý může do formuláře vyplnit, co chce. Abychom měli objekt více pod kontrolou, můžeme využít funkce `__init__` (název zapisujeme včetně podtržítek). Tato funkce je speciální v tom, že je **zavolána při vytvoření objektu**. Můžeme jí (jako jakékoli jiné funkci) přiřadit parametry a zajistit, aby hodnoty parametrů uložila jako atributy objektu.

```py
class Employee:
  def getInfo(self):
    return f"{self.name} pracuje na pozici {self.position}."
  def __init__(self, name, position):
    self.name = name
    self.position = position
```

Tento styl je standardní - parametry jsou pojmenované stejně jako atributy objektu, kam se jejich hodnoty ukládají. Mezi `self.name` a `name` je důležitý rozdíl:

- `name` je parametr funkce `__init__` a jeho hodnota **není přístupná** pro ostatní funkce objektu.
- `self.name` je atribut objektu, který v objektu **zůstane** a můžou s ním pracovat ostatní funkce. 

Díky funkci `__init__` máme zjednodušené vytváření objektu, protože hodnoty parametrů nyní vepíšeme přímo do závorek při vytváření objektu.

```py
frantisek = Employee("František Novák", "konstruktér")
klara = Employee("Klára Nová", "svářeč")

print(frantisek.getInfo())
print(klara.getInfo())
```

Nyní již víme, že každý objekt třídy `Employee` má vyplněné jméno a pozici. Zkusme nyní naši třídu obohatit o novou funkci - čerpání dovolené. Na začátku bude mít každý zaměstnanec nárok na dovolenou, kterou může v průběhu roku čerpat. Čerpání zajistíme pomocí funkce `takeHoliday`. Budeme hlídat i to, aby zaměstnanec nárok na dovolenou nepřečerpal.

```py
class Employee:
  def takeHoliday(self, days):
    if self.remainingHolidayDays >= days:
      self.remainingHolidayDays -= days
      return f"Užij si to."
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
frantisek = Employee("František Novák", "konstruktér")

print(frantisek.takeHoliday(5))
print(frantisek.takeHoliday(15))
print(frantisek.takeHoliday(10))
```

Tím jsme si ukázali, jak vytvořit třídu, objekty a jak s nimi pracovat.


[[[ excs Objekty a třídy [
- kniha
- balik
]]]

[[[ excs Bonusy
- zkusebka
]]]
