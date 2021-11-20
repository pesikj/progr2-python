Dalším konceptem, se kterým se v tomto kurzu seznámíme, jsou objekty (`objects`). Na objektech je založeno **objektově orientované programování** (Object-oriented programming - OOP), tedy princip psaní programů, ve kterém jsou bloky kódu poskládané do **tříd** a **objektů**. 

Objekty mají často reprezentovat nějaké entity v realitě. Pokud bychom například vyvíjeli administrativní software pro firmy, vytvoříme tam objekty reprezentující zaměstnance, pracoviště, firemní automobily atd. U zásilkové společnosti bychom vytvářeli objekty, které reprezentují balíky, řidiče atd.

## Objekty a třídy

Na začátku si musíme vytvořit **třídu** (`class`). Vztah mezi třídou a objekty si můžeme představit na příkladu formulářů. Třída je prázdný formulář - obsahuje kolonky, které by měly být vyplněny. Objekt je pak vyplněný formulář, který už má v sobě nějaká konkrétní data. Podobně jako formulářů můžeme vyplnit více, může na základě jedné třídy vzniknout několik objektů. Objekty jsou vzájemně **nezávislé**, takže práce s jedním objektem neovlivňuje ostatní. Analogicky, pokud upravujeme jeden formulář, nijak tím neměníme ostatní.

Třídy mají dvě důležité charakteristiky - mají **atributy** (v nich uchováváme hodnoty) a **metody** (vykonávají nějaké příkazy). Atributy jsou vlastně proměnné, pouze jsou navázané na konkrétní objekt. Funkce jsme poznali v předchozí kapitole, metody jsou pak funkce navázané na konkrétní objekt a pracují s jeho atributy.

Popišme si konkrétně náš příklad software pro firmy. V něm můžeme mít například třídu `Zamestnanec`, který reprezentuje zaměstnance. Třída může mít jméno, pracovní pozici, oddělení, plat, zbývající dny dovolené atd. Zaměstnanec může mít i metody - například metodu na vybrání dovolené, vytištění výplatní pásky, výpočet věku atd. Název třídy bychom měli začínat vždy **velkým písmenem**.

Před vytvářením objektů je třeba mít připravenou třídu, na základě které objekt vznikne. K tomu použijeme klíčové slovo `class`. Za něj přijde **název třídy** a opět **dvojtečka**. Pro začátek si vytvořme třídu jen s jednou metodou `vypis_informace`, která vypíše informace o zaměstnanci.

Všimni si parametru `self` u metody. Pomocí `self` se **odkazujeme na atributy objektu**. Pokud chceme získat hodnotu atributu, napíšeme klíčové slovo `self`, **tečku** a **název atributu**. Tečky při práci s objekty používáme velmi často a jsou jakousi analogií k hranatým závorkám u sekvencí.

```py
class Zamestnanec:
  def vypis_informace(self):
    return f"{self.jmeno} pracuje na pozici {self.pozice}."
```

Protože pracujeme s metodou, můžeme (ale nemusíme) použít klíčové slovo `return` a vrátit nějakou hodnotu.

Zkusme si nyní vytvořit objekt, který reprezentuje zaměstnance Františka. Objekt vytvoříme podobně, jako bychom volali funkci - použijeme **název třídy** a **kulaté závorky**. Objekt uložíme do proměnné `frantisek`. Dále přiřadíme proměnné `frantisek` hodnoty atributů `jmeno` a `pozice` a vyzkoušíme metodu `vypis_informace`. 

```py
frantisek = Zamestnanec()
frantisek.jmeno = "František Novák"
frantisek.pozice = "konstruktér"
print(frantisek.vypis_informace())
```

Zkusíme přidat ještě jednu zaměstnankyni.

```py
klara = Zamestnanec()
klara.jmeno = "Klára Nová"
klara.pozice = "konstruktérka"
```

Nyní vyzkoušíme vypsat informace obou zaměstnanců.

```py
print(frantisek.vypis_informace())
print(klara.vypis_informace())
```

## Metoda `__init__`

Z výpis vidíme, že se informace zaměstnanců nijak nepomíchaly a každý zaměstnanec má uložené své vlastní údaje.

Tento postup ale působí lehce chaoticky. V naší analogii s formuláři to vypadá, že si každý může do formuláře vyplnit, co chce. Abychom měli objekt více pod kontrolou, můžeme využít metodu `__init__` (název zapisujeme včetně podtržítek). Tato metoda je speciální v tom, že je **zavolána při vytvoření objektu**. Můžeme jí (jako jakékoli jiné metodě) přiřadit parametry a zajistit, aby hodnoty parametrů uložila jako atributy objektu.

```py
class Zamestnanec:
  def vypis_informace(self):
    return f"{self.jmeno} pracuje na pozici {self.pozice}."
  def __init__(self, jmeno, pozice):
    self.jmeno = jmeno
    self.pozice = pozice
```

Tento styl je standardní - parametry jsou pojmenované stejně jako atributy objektu, kam se jejich hodnoty ukládají. Mezi `self.jmeno` a `jmeno` je důležitý rozdíl:

- `jmeno` je parametr metody `__init__` a jeho hodnota **není přístupná** pro ostatní funkce objektu.
- `self.jmeno` je atribut objektu, který v objektu **zůstane** a můžou s ním pracovat ostatní metody. 

Díky metodě `__init__` máme zjednodušené vytváření objektu, protože hodnoty parametrů nyní vepíšeme přímo do závorek při vytváření objektu.

```py
frantisek = Zamestnanec("František Novák", "konstruktér")
klara = Zamestnanec("Klára Nová", "svářeč")

print(frantisek.vypis_informace())
print(klara.vypis_informace())
```

Nyní již víme, že každý objekt třídy `Zamestnanec` má vyplněné jméno a pozici. Zkusme nyní naši třídu obohatit o novou metodu - čerpání dovolené. Na začátku bude mít každý zaměstnanec nárok na dovolenou, kterou může v průběhu roku čerpat. Čerpání zajistíme pomocí metody `cerpani_dovolene`. Budeme hlídat i to, aby zaměstnanec nárok na dovolenou nepřečerpal.

```py
class Zamestnanec:
  def cerpani_dovolene(self, days):
    if self.pocet_dni_dovolene >= days:
      self.pocet_dni_dovolene -= days
      return f"Užij si to."
    else:
      return f"Bohužel už máš nárok jen na {self.pocet_dni_dovolene} dní."
  
  def vypis_informace(self):
    return f"{self.jmeno} pracuje na pozici {self.pozice}."
    
  def __init__(self, jmeno, pozice):
    self.jmeno = jmeno
    self.pozice = pozice
    self.pocet_dni_dovolene = 25
```

Nyní se podívejme, jak budou vyřizovány Františkovy žádosti o dovolenou.

```py
frantisek = Zamestnanec("František Novák", "konstruktér")

print(frantisek.cerpani_dovolene(5))
print(frantisek.cerpani_dovolene(15))
print(frantisek.cerpani_dovolene(10))
```

### Metoda `__str__`

Pojďme ještě použití naší třídy trochu zjednodušit. Naše třída umí přehledně vypsat informace díky metodě `cerpani_dovolene()`. Třídu ale může používat i jiný programátor a ten o této metodě nemusí vědět a tak intuitivně vyzkouší funkci `print()`, které vloží nějaký objekt třídy `Zamestnanec`.

```python
print(frantisek)
```

Odpovědí bude poněkud záhadný text ve stylu

```python
<__main__.Zamestnanec object at 0x00000126F0084850>
```

Funke `print()` se totiž pokusí převést objekt na typ řetězec. Protože naše třída nemá tuto funkci naprogramovanou, použije se standardní formát, který nám říká, že jde o objekt třídy `Zamestnanec` a kde je uložený v paměti. Bylo by však dobré místo toho získat nějaký srozumitelný výpis, třeba takový, který poskytuje metoda `vypis_informace()`.

Převod na řetězec zařídíme tím, že třídě přidáme metodu `__str__`. Dvě lomítka opět značný zvláštní význam. Ten spočívá v tom, že Python využije tuto metodu vždy, když jej požádáme o převod objektu na řetězec. Můžeme tedy přejmenovat metodu `vypis_informace()` na `__str__`. Výstupem našeho programu pak bude text o tom, jak se zaměstnanec jmenuje a kde pracuje.

```python
class Zamestnanec:
  def __str__(self):
    return f"{self.jmeno} pracuje na pozici {self.pozice}."
  def __init__(self, jmeno, pozice):
    self.jmeno = jmeno
    self.pozice = pozice

frantisek = Zamestnanec("František Novák", "konstruktér")
print(str(frantisek))
```

Tím jsme si ukázali, jak vytvořit třídu, objekty a jak s nimi pracovat.


[[[ excs Cvičení: Slovníky
- balik
- zkusebka
]]]

## Čtení na doma - datové třídy

Obsah metody `__init__()` je příklad `boilerplate code`. Název se odkazuje na kovové štítky, které jsou umístěny na bojlerech. V programování to znamená kód, který se často opakuje bez nějakých velkých změn.

V Pythonu ve verzi 3.7 přibyly datové třídy (`dataclass`), které si obsah metody vytvoří samy. Do datové třídy pouze napíšeme seznam jejích atributů spolu s jejich typy hodnot. Můžeme přidat i výchozí hodnotu, jak je vidět u atributu `pocet_dni_dovolene`

```py
from dataclasses import dataclass

@dataclass
class Zamestnanec:
  jmeno: str
  pozice: str
  pocet_dni_dovolene: int = 25

  def cerpani_dovolene(self, days):
    if self.pocet_dni_dovolene >= days:
      self.pocet_dni_dovolene -= days
      return f"Užij si to."
    else:
      return f"Bohužel už máš nárok jen na {self.pocet_dni_dovolene} dní."

  def vypis_informace(self):
    return f"{self.jmeno} pracuje na pozici {self.pozice}."
    
frantisek = Zamestnanec("František Novák", "konstruktér")
print(frantisek.cerpani_dovolene(5))
print(frantisek.cerpani_dovolene(15))
print(frantisek.cerpani_dovolene(10))
```

Více o datových třídách najdeš v [v dokumentaci](https://docs.python.org/3/library/dataclasses.html).
