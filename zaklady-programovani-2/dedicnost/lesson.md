## Dědičnost

Třídy mají jednu zajímavou vlastnost - mohou od sebe **dědit**. Uvažujme třeba, že bychom chtěli vytvořit novou třídu `Manazer`, která reprezentuje zaměstnance, který má nějaké podřízené. U manažera bychom rádi evidovali počet jeho podřízených. Jinak se samozřejmě manažer od ostatních nijak neliší - má jméno, název pozice i nárok na dovolenou. 

Ideální by tedy bylo mít kopii třídy `Zamestnanec`, která bude mít nový atribut `pocet_podrizenych` (seznam jeho podřízených). Samozřejmě bychom mohli kód třídy `Zamestnanec` zkopírovat a upravit, ale díky dědičnosti to můžeme udělat i lépe. Můžeme novou třídu `Manazer` postavit na základě třídy `Zamestnanec`. Třída `Manazer` tak zdědí od třídy `Zamestnanec` všechny atributy a metody, a my jen přidáme nebo upravíme, co potřebujeme.

Napíšeme tedy novou funkci `__init__`, protože potřebujeme vytvořit atribut `pocet_podrizenych`.

```py
class Manazer(Zamestnanec):
  def __init__(self, jmeno, pozice, pocet_podrizenych):
    self.jmeno = jmeno
    self.pozice = pozice
    self.pocet_podrizenych = pocet_podrizenych
    self.pocet_dni_dovolene = 25
```

Zkusíme si nyní vytvořit objekt, který bude reprezentovat manažera. U objektu vyzkoušíme, zda u ní funguje metoda `__str__`. Tuto metodu jsme pro třídu `Manazer` neprogramovali, měla by být zděděná od třídy `Zamestnanec`.

```py
boss = Manazer("Marian Přísný", "vedoucí konstrukčního oddělení")
print(boss)
```

Zatím vše funguje, přesto můžeme náš kód ještě vylepšit. Ve funkci `__init__` musíme poněkud nešikovně opisovat tři řádky, které nastavují hodnoty atributů. Přitom ty stejné řádky už jsou v třídě `Zamestnanec`. Mohli bychom nějak existující kód z třídy `Zamestnanec` upravit? 

Ve skutečnosti ano. Využijeme k tomu speciální funkci `super()`, kterou se odvoláme na **mateřskou třídu aktuální třídy**. Následně můžeme použít tečku a zavolat funkci `__init__`. Tím tedy voláme funkci `__init()__` mateřské třídy `Zamestnanec`.

```py
class Manazer(Zamestnanec):
  def __init__(self, jmeno, pozice, pocet_podrizenych):
    super().__init__(jmeno, pozice)
    self.pocet_podrizenych = pocet_podrizenych
```

Pojďme ještě upravit výpis informace pomocí metody `__str__()`. U třídy `Manazer` budeme chtít do výpisu přidat informaci o tom, kolik má manažer podřízených. Opět můžeme pomocí funkce `super()` zavolat metodu `__str__()` z mateřské třídy `Zamestnanec` a připojit k ní větu o počtu podřízených.

```py
class Manazer(Zamestnanec):
  def __str__(self):
    return super().__str__() + f" Má {self.pocet_podrizenych} podřízených."
  def __init__(self, jmeno, pozice, pocet_podrizenych):
    super().__init__(jmeno, pozice)
    self.pocet_podrizenych = pocet_podrizenych
```

Vyzkoušíme znovu dvojici příkazů, kterou jsme zkoušeli předtím.

```python
boss = Manazer("Marian Přísný", "vedoucí konstrukčního oddělení", 5)
print(boss)
```

Výsledkem je text:

```
Marian Přísný pracuje na pozici vedoucí konstrukčního oddělení. Má 5 podřízených.
```

[[[ excs Cvičení: Dědičnost
- cenny-balik
- castecny-uvazek
]]]


## Kombinace seznamu a objektů

Pro personální systém firmy ale samotná informace o počtu podřízených zpravidla nebude dostatečná, je naopak potřeba podřízené a manažery přímo propojit. Jen tak bude jasné, za které zaměstnance manažer zodpovídá.

Upravme tedy třídu `Manazer` tím, že namísto atributu `pocet_podrizenych` vložíme seznam `podrizeni`, který bude na začátku prázdný. Dále přidáme metodu `pridej_podrizeneho()`, která vlozi nového podrizeneho do seznamu `podrizeni`.

```py
class Manazer(Zamestnanec):
  def pridej_podrizeneho(self, podrizeny):
    self.podrizeni.append(podrizeny)

  def __init__(self, jmeno, pozice):
    self.jmeno = jmeno
    self.pozice = pozice
    self.pocet_dni_dovolene = 25
    self.podrizeni = []
```

Náš kód už bychom mohli spustit, ale nemohli bychom pořádně otestovat, že přidávání podřízených funguje. My je totiž ukládáme, ale zatím nemáme funkci pro jejich vypsání. Přidáme tedy funkci `vypis_podrizene`, která vrátí informaci o podřízených manažera.

```py
class Manazer(Zamestnanec):
  def pridej_podrizeneho(self, newSubordinate):
    self.podrizeni.append(newSubordinate)

  def vypis_podrizene(self):
    podrizeni = ""
    for item in self.podrizeni:
      podrizeni += item.jmeno + ", "
    return podrizeni
  
  def __init__(self, jmeno, pozice):
    super().__init__(jmeno, pozice)
    self.podrizeni = []
```

Nyní můžeme vše vyzkoušet. Vedoucímu, který je uložený v proměnné `boss`, přiřadíme dva podřízené. Následně si zkusíme proměnné vypsat.

```py
frantisek = Zamestnanec("František Novák", "konstruktér")
klara = Zamestnanec("Klára Nová", "konstruktérka")

boss = Manazer("Marian Přísný", "vedoucí konstrukčního oddělení")
boss.pridej_podrizeneho(frantisek)
boss.pridej_podrizeneho(klara)
print(boss.vypis_podrizene())
```

Náš program tedy vytvoří tři objekty - dva zaměstnance a jednoho manažera. Manažerovi jsme přiřadili zaměstnance jako podřízené. A vidíme, že naše akce proběhla správně, protože tito dva zaměstnanci se objevili ve výpisu podřízených.

Jako poslední můžeme vrátit metodu `__str__()`, která zjistí počet podřízených z délky seznamu `podrizeni`.

```py
class Manazer(Zamestnanec):
  def __str__(self):
    return super().__str__() + f" Má {len(self.podrizeni)} podřízených."

  def pridej_podrizeneho(self, newSubordinate):
    self.podrizeni.append(newSubordinate)

  def vypis_podrizene(self):
    podrizeni = ""
    for item in self.podrizeni:
      podrizeni += item.jmeno + ", "
    return podrizeni
  
  def __init__(self, jmeno, pozice):
    super().__init__(jmeno, pozice)
    self.podrizeni = []
```

[[[ excs Kombinace seznamu a objektů
- ridic
]]]

## Abstraktní třída

Abstraktní třída je dalším konceptem ve světě objektově orientovaného programování. Abstraktní třída má speciální význam v tom, že z ní rovnou nevytváříme objekty, je ale šablonou pro třídy, které od ní dědí.

Např. uvažujme program, který počítá obvody a obsahy geometrických obrazců. Začneme vytvořením mateřské třídy `Obrazec`, která bude mít metody `vypocti_obvod()` a `vypocti_obsah()`. U neznámého obrazce ale nemá smysl do těchto tříd implementovat výpočet, protože nevíme, jaký vzorec bychom měli použít. Proto vytvoříme třídu `Obrazec` jako abstraktní třídu. To v Pythonu uděláme tak, že jí nastavíme jako mateřskou třídu třídu `ABC` z modulu `abc`. Její metody poté budou též abstraktní. To zařídíme tak, že nad ně vložíme značku `@abstractmethod`. Tato prozvláštní značka se v jazyce Pythonu označuje jako **dekorátor** (`decorator`).

```python
from abc import ABC, abstractmethod

class Obrazec(ABC):
  @abstractmethod
  def vypocti_obvod():
    pass

  @abstractmethod
  def vypocti_obsah():
    pass
```

Dále přidáme třídy `Ctverec` a `Obdelnik`, které budou dědit od třídy `Obrazec`. Těmto třídám už můžeme implementovat metody `vypocti_obvod()` a `vypocti_obsah()`, založit na jejich základě objekty a pracovat s nimi.

```python
class Ctverec(Obrazec):
  def vypocti_obvod(self):
    return self.a * self.a
  
  def vypocti_obsah(self):
    return 4 * self.a

  def __init__(self, a):
    self.a = a

class Obdelnik(Obrazec):
  def vypocti_obvod(self):
    return self.a * self.b
  
  def vypocti_obsah(self):
    return 4 * self.b

  def __init__(self, a, b):
    self.a = a
    self.b = b

maly_ctverec = Ctverec(10)
velky_obdelnik = Obdelnik(20, 25)
plocha_celkem = maly_ctverec.vypocti_obsah() + velky_obdelnik.vypocti_obsah()
print(f"Celková plocha obou obrazců je {plocha_celkem}.")
```

### Funkce `isinstance()`

Abstraktní třída je výhodná v kombinaci s funkcí `isinstance()`. Ta vrací pravdivostní hodnotu (`bool`). Funkce ověří, zda je objekt založený na nějaké třídě. Založený může být i nepřímo. Například pokud vytvoříme objekt `neznamy_obrazec` ne třídy `Ctverec`, funkce `isinstance()` vrátí hodnotu `True`, pokud jako ověřovanou třídu vložíme `Ctverec`, ale i pokud vložíme třídu `Obrazec`.

Uvažujme nyní, že máme u nějakého objektu vypsat jeho obvod. Chceme to ale provést bezpečně, tj. chceme ověřit, že je přítomná metoda `vypocti_obsah()` a že daný objekt skutečně reprezentuje nějaký dvourozměrný odstavec. Využijeme tedy funkci `isinstance()`.

```python
neznamy_obrazec = Ctverec(10)
if isinstance(neznamy_obrazec, Obrazec):
  print(f"Obvod obrazce je {neznamy_obrazec.vypocti_obsah()}")
else:
  print("Objekt není dvourozměrný odstavec.")
```

## Vlastnosti objektu

U našich obrazců máme implementované metody metody `vypocti_obvod()` a `vypocti_obsah()`. Obvod a obsah jsou ale hodnoty, které jsou pro nějaký obrazec konkrétní velikosti konstantní.  Bylo by tedy zajímavé upravit naše objekty tak, aby se obsah a obrazec tvářily jako atributy. Atribut objektu, pro jehož získání používáme funkci, je v Pythonu označován jako vlastnost (`property`). Vlastnosti označíme pomocí dekorátoru `@property`. U abstraktní třídy pak použijeme speciální dekorátor `@abstractproperty`.

Vlastnosti poté čteme jako atributy, tj. nepoužíváme kulaté závorky jako při volání funkce.

```python
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
```
