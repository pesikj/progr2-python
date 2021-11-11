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

Zkusíme si nyní vytvořit objekt, který bude reprezentovat manažera. U objektu vyzkoušíme, zda u ní funguje metoda `__str__()`. Tuto metodu jsme pro třídu `Manazer` neprogramovali, měla by být *zděděná* od třídy `Zamestnanec`.

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
- castecny-uvazek
- cenny-balik
]]]


## Kombinace seznamu a objektů

Pro personální systém firmy ale samotná informace o počtu podřízených zpravidla nebude dostatečná, je naopak potřeba podřízené a manažery přímo propojit. Jen tak bude jasné, za které zaměstnance manažer zodpovídá.

Upravme tedy třídu `Manazer` tím, že namísto atributu `pocet_podrizenych` vložíme seznam `podrizeni`, který bude na začátku prázdný. Dále přidáme metodu `pridej_podrizeneho()`, která vloží nového podřízeného do seznamu `podrizeni`.

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

# Další možnosti objektově orientovaného programování

Následující text popisuje další pokročilá témata, které většinou není možné během kurzu probrat, můžeš se však k nim kdykoli vrátit a prohloubit svoje znalosti.

## Abstraktní třída

Abstraktní třída má speciální význam v tom, že z ní rovnou **nevytváříme objekty**, je ale šablonou pro třídy, které od ní dědí.

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
    return 4 * self.a
  
  def vypocti_obsah(self):
    return self.a * self.a

  def __init__(self, a):
    self.a = a

class Obdelnik(Obrazec):
  def vypocti_obvod(self):
    return 2 * (self.a + self.b)
  
  def vypocti_obsah(self):
    return self.a * self.b

  def __init__(self, a, b):
    self.a = a
    self.b = b

maly_ctverec = Ctverec(10)
velky_obdelnik = Obdelnik(20, 25)
plocha_celkem = maly_ctverec.vypocti_obsah() + velky_obdelnik.vypocti_obsah()
print(f"Celková plocha obou obrazců je {plocha_celkem}.")
```

Pokud bys chtěl(a) vytvořit objekt se třídy `Obrazec`, Python vrátí chybu "`TypeError: Can't instantiate abstract class Obrazec with abstract methods vypocti_obsah, vypocti_obvod`". Slovo `instance` označuje pojem "instance objektové třídy", což je jen jiný výraz pro model.

### Funkce `isinstance()`

Abstraktní třída je výhodná v kombinaci s funkcí `isinstance()`. Ta vrací pravdivostní hodnotu (`bool`). Funkce ověří, zda je objekt založený na nějaké třídě. Založený může být i nepřímo. Například pokud vytvoříme objekt `neznamy_obrazec` ze třídy `Ctverec`, funkce `isinstance()` vrátí hodnotu `True`, pokud jako ověřovanou třídu vložíme `Ctverec`, ale i pokud vložíme třídu `Obrazec`.

Uvažujme nyní, že máme u nějakého objektu vypsat jeho obvod. Chceme to ale provést bezpečně, tj. chceme ověřit, že je přítomná metoda `vypocti_obsah()` a že daný objekt skutečně reprezentuje nějaký dvourozměrný odstavec. Využijeme tedy funkci `isinstance()`.

```python
neznamy_obrazec = Ctverec(10)
if isinstance(neznamy_obrazec, Obrazec):
  print(f"Obvod obrazce je {neznamy_obrazec.vypocti_obsah()}")
else:
  print("Objekt není dvourozměrný odstavec.")
```

## Vlastnosti objektu

U našich obrazců máme implementované metody metody `vypocti_obvod()` a `vypocti_obsah()`. Obvod a obsah jsou hodnoty, které jsou pro nějaký obrazec konkrétní velikosti konstantní. Bylo by tedy zajímavé upravit naše objekty tak, aby se obsah a obrazec tvářily jako atributy. Atribut objektu, pro jehož získání používáme funkci, je v Pythonu označován jako vlastnost (`property`). Vlastnosti označíme pomocí dekorátoru `@property`. U abstraktní třídy pak použijeme speciální dekorátor `@abstractproperty`.

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
    return 4 * self.a
  
  @property
  def obsah(self):
    return self.a * self.a

  def __init__(self, a):
    self.a = a

class Obdelnik(Obrazec):
  @property
  def obvod(self):
    return 2 (self.a + self.b)
  
  @property
  def obsah(self):
    return self.a * self.b

  def __init__(self, a, b):
    self.a = a
    self.b = b

maly_ctverec = Ctverec(10)
velky_obdelnik = Obdelnik(20, 25)
plocha_celkem = maly_ctverec.obsah + velky_obdelnik.obsah
print(f"Celková plocha obou obrazců je {plocha_celkem}.")
```

## Soukromé a veřejné metody
​
Soukromé metody jsou metody, které mohou být volány pouze jinými metodami dané třídy, nikoli však zvenku. Python, na rozdíl od jiných programovacích jazyků, skutečně soukromé metody nemá. Všechny metody a atributy tříd jsou veřejné a není žádný způsob jak je opravdu skrýt před vývojářem. 

Obecně platí, že atributy nebo metody začínající podtržítkem jsou soukromé a vývojář by je mimo danou třídu neměl číst, upravovat nebo volat. Takové metody nebo atributy se nezobrazí, pokud na třídu zavoláme funkci `help`. Zobrazí se až při bližším zkoumání, například pomocí funkce `dir`. Vývojář třídy tímto odhaluje všechny své karty a dává uživateli do rukou možnost tyto karty taktéž použít, pokud bude potřebovat. 

​
```python
class Zamestnanec:
    def __init__(self, krestni_jmeno, prijmeni):
        self.krestni_jmeno = krestni_jmeno
        self.prijmeni = prijmeni
    
    @property
    def _delka_jmena(self):
        return len(self.krestni_jmeno + self.prijmeni)
​
    @property
    def business_card_data(self):
        if self._delka_jmena < 20:
            return f"{self.krestni_jmeno} {self.prijmeni}"
        else:
            return f"{self.krestni_jmeno[0]}. {self.prijmeni}"
```
## Dvojité podtržítko — dunder funkce
​
`dunder` (double under) jsou funkce začínající a končící dvěma podtržítky. Dvěma z nich je již známé funkce `__init__` pro inizializaci třidy a `__str__` pro převod na řetězc. Mají svůj význam také mimo třídy, například `__file__` pro zjištění cesty, kde se soubor nachází. Jedná se o funkce či atributy, které jsou něčím výjimečné, v Pythonu mají předdefinováné chování a Python ví, jak s nimi pracovat. 

Několika dunder funkcemi můžeme upravit svou třídu tak, aby se chovala podobně a nebo stejně jako například `list`. Mimo dalších je touto dunder funkcí i  `__len__`, která vrací informaci o délce instance a je zavolána dosazením instance do funkce `len`. Délkou instance se rozumí to, co v daném kontextu dává smysl, pro firmu by mohlo jít o počet zaměstnanců a pro rok by šlo o měsíce.
​
```python
class Company:
    def __init__(self, Zamestnanecs):
        self.Zamestnanecs = Zamestnanecs
    
    def __len__(self):
        return len(self.Zamestnanecs)
​
    def __iter__(self):
        return iter(self.Zamestnanecs)
```
​
## Dědičnost a dvojíté podtržítko
​
Dvojité podtržení z jedné strany má také svůj význam. Jde o soukromé metody, které navíc zdědí jméno své třídy. Tím dává vývojář třídy najevo, že tato by opravdu za žádných okolností neměla být volána zvenku.

`__join_names` ze třidy `Zamestnanec` se po spuštění pro veřejnost přemění na `_Zamestnanec__join_names` a pro svou instanci zůstane jako `__join_names`. Díky tomuto nedojde v dědící třidě k přejmenování pomocných funkcí, které jsou zásádní pro fungování ostatních funkcí. I tyto funkce se nezobrazí po dosazení třídy nebo instance do napovídající funkce `help`. 
​
```python
class Zamestnanec:
    def __init__(self, krestni_jmeno, prijmeni):
        self.krestni_jmeno = krestni_jmeno
        self.prijmeni = prijmeni
    
    def __join_names(self):
        return (self.krestni_jmeno + self.prijmeni).lower()
​
    @property
    def email(self):
        return self.__join_names() + "@goodcompany.com"
​
class GoodCompanyZamestnanec(Zamestnanec):
    def __join_names(self):
        return self.prijmeni + self.krestni_jmeno
​
    @property
    def skype(self):
        return self.__join_names()
​
Zamestnanec = GoodCompanyZamestnanec("Alžběta", "Nováková")
​
print(Zamestnanec.skype)
print(Zamestnanec.email)
# print(Zamestnanec.__join_names()) # chyba
print(Zamestnanec._GoodCompanyZamestnanec__join_names()))
```
