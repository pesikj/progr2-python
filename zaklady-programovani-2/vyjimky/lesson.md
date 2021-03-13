Tato bonusová kapitola není nezbytně nutná pro základní programování v Pythonu. V mnoha případech se obejdete bez znalosti práce s výjimkami. Pokud to ale s Pythonem myslíte vážně, tato část se vám bude rozhodně hodit.

## Chyby v programu
Mnohokrát jsme se již setkali s tím, že náš program neudělal co jsme si mysleli a Python skončil s chybovou hláškou. V tuto chvíli je nejdůležitější nepanikařit a v klidu si přečíst co nám Python interpret říká. Drtivá většina základních chyb nejsou žádné záludnosti a Python interpret nám často přímo radí, jak chybu opravit. Důležité je nemít z těchto chyb špatný pocit. Programování je často neustálé zkoušení různých pokusů dokud to nebude dělat to, co chceme.

Chybové hlášky jsou taky ta lepší varianta chyby. Pokud nám ji Python vypíše a skončí, tak jistě víme, že je něco špatně. Mnohem hůř se hledají chyby v programu, který Python interpret vyhodnotí jako syntakticky a sémanticky správný, ale ve skutečnosti vůbec nedělá to co si myslíme, že má dělat.

### Chyby, které musíme opravit
Nyní si ukážeme pár typických chyb, které se vám jistě často dějí:
```pycon
>>> promenna = 10
>>> print(promenna)
10
>>> print(promena)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'promena' is not defined
```

_NameError_ nastává v momentě, kdy Python narazí na slovo, které nezná. Vzhledem k tomu, že klíčová slova, jako `if`, `else`, `def` nebo `import` všechna Python musí znát, zbývají jako další možnosti názvy našich proměnných, funkcí nebo tříd. Pokud v názvu uděláme překlep, nebo použijeme něco, co jsme si vůbec nedefinovali, Python zahlásí _NameError_ a my musíme tuto chybu v programu opravit.

```pycon
>>> if 1 > 0
  File "<stdin>", line 1
    if 1 > 0
           ^
SyntaxError: invalid syntax
```
Další častý problém je chyba v syntaxi. V předcházejícím případě chybí na konci řádku dvojtečka `:`.


```pycon
>>> if 1 > 0:
... print()
  File "<stdin>", line 2
    print()
    ^
IndentationError: expected an indented block
```
_Indentation_ je anglický výraz pro odsazení. Vše co je shodně odsazeno patří do jednoho bloku, který končí prvním řádkem, který je odsazen o jedno méně. V tomto případě je problém, že volání funkce `print()` není v bloku odsazeno vůbec. Dbejte na správné nastavení editoru a nemíchejte odsazování různým počtem mezer nebo tabulátorů. Pozor na kód, který kopírujete z internetu!


### Chyby, které můžeme zkusit ošetřit
Dostáváme se k části chyb, které někdy mohou být naše neúmyslné chyby, ale někdy se může jednat o chybu vzniklou vstupem programu (např. od uživatele funkcí `input()` nebo v seznamu parametrů příkazové řádky `sys.argv`. Dokončený program nesmí na žádný vstup od uživatele zhavarovat s chybovou hláškou od Python interpretu (jako vidíme ve všech těchto případech).

```pycon
>>> l = [0, 1, 2]
>>> l[3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
```
Častá chyba je hledání indexu, který už v seznamu není.

```pycon
>>> zvirata = {'dog': 'pes', 'cat': 'kocka'}
>>> zvirata['cat']
'kocka'
>>> zvirata['rat']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'rat'
```
Obdobně můžeme narazit na neexistující klíč slovníku.

Poslední příklad, který si ukážeme je chyba, která může nastat např. při pokusu o přetypování.
```pycon
>>> int(input("Zadej cislo: "))
Zadej cislo: 0
0
```
Funkce `intput()` nám zastaví běh, programu a vyčkává na uživatele, než něco napíše a zmáčkne _Enter_. Můžeme se setkat s _"hodným"_ uživatelem, který na výzvu k zadání čísla skutečně zadá číslo. My si ho přetypujeme pomocí funkce `int()` a můžeme s ním dále počítat.

Co když ale uživatel zadá řetězec, který není složen pouze z cifer desítkové číselné soustavy 0 až 9, a tím pádem ho není možné přetypovat na datový typ `int`?
```pycon
>>> int(input("Zadej cislo: "))
Zadej cislo: cislo
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'cislo'
```

## Různé přístupy k ošetřování vstupů
Ještě než se pustíme do samotného ošetřování výjimek povíme si něco o ošetřování vstupů programu. Pokud totiž program nemá žádné uživatelské vstupy, nejedná se o moc užitečný program. Takový program by se choval vždy stejně a vypsal by jen to, co jsme mu zadrátovali uvnitř (např. text _"Hello wordl!"_).

Důležité je si pod pojmem vstup programu představit mnoho různých věcí, např.:
* Návratovou hodnotu funkce `input()` - vstup textu z klávesnice
* Parametry programu na příkazové řádce (`sys.argv`)
* Data z načítaného souboru
* Data stažená přes internet z API nebo webové stránky
* Formuláře na webové stránce (viz [xkcd komix](https://xkcd.com/327/))
* Posloupnost klikání na tlačítka a jiné prvky u GUI aplikací

Všechny tyto vstupy mohou způsobit v našem programu chyby, kterým se vždy musíme snažit předejít. K tomu se používají dva hlavní přístupy.

### Nejprve otestuj a pak proveď
Pokud bychom neznali nic jiného a chtěli např. ošetřit, že program je vždy spuštěn alespoň s jedním parametrem na příkazové řádce, uděláme to nějak takto:

```py
import sys

if len(sys.argv) > 1:
    print(f"Zadán parametr: {sys.argv[1]}")
else:
    print("Zadej parametr na příkazovou řádku!")
```

```shell
$ python program.py
Zadej parametr na příkazovou řádku!
```

```shell
$ python program.py PARAMETR
Zadán parametr: PARAMETR
```

Teď přichází druhý problém, a to, že chceme, aby parametr byl číslo, protože s ním chceme počítat (např. vypsat číslo o jedničku vyšší). Dá se to provést složenou podmínku, kde budeme zároveň kontrolovat, jestli se parametr skládá z cifer. Použijeme k tomu metodu řetězců [isdigit()](https://docs.python.org/3/library/stdtypes.html#str.isdigit)

```py
import sys

if len(sys.argv) > 1 and sys.argv[1].isdigit():
    cislo = int(sys.argv[1])
    print(f"Zadán parametr: {cislo}")
    print(f"O jedničku vyšší je: {cislo+1}")
else:
    print("Zadej číslo jako parametr na příkazovou řádku!")
```

```shell
$ python program.py PARAMETR
Zadej číslo jako parametr na příkazovou řádku!
```

```shell
$ python program.py 100
Zadán parametr: 100
O jedničku vyšší je: 101
```

Už se nám to testování před provedením operace trochu komplikuje a to řešíme zatím jen dvě podmínky. V reálném světě je to ještě složitější.

### Proveď a řeš až problémy
Proto byl v mnoha programovacích jazycích vytvořen mechanismus výjimek a jejich obsluhy. Kromě Pythonu jsou to např. jazyky C++, Java nebo C#.

Slouží nám k tomu nová klíčová slova `try` a `except`. Kus kódu, ve kterém může dojít k výjimce obalíme blokem `try`. Za tím to blokem _odchytíme_ příslušnou výjimku v bloku `except`.

Předchozí příklad přepíšeme následujícím způsobem:

```python
import sys

try:
    print(f"Zadán parametr: {sys.argv[1]}")
except IndexError:
    print("Zadej parametr na příkazovou řádku!")
```

Toto řešení nám odchytává _IndexError_ na seznamu `sys.argv`, tzn. nenapsali jsme na příkazovou řádku potřebný parametr.

Pro odchycení výjimky při chybném přetypování řetězce na číslo pomocí funkce `int()` zařadíme další blok `except`, kde odchytneme jinou výjimku:

```python
import sys

try:
    print(f"Zadán parametr: {sys.argv[1]}")
    print(f"O jedničku vyšší je: {int(sys.argv[1])+1}")
except IndexError:
    print("Zadej parametr na příkazovou řádku!")
except ValueError:
    print("Zadej číslo jako parametr na příkazovou řádku!")
```

[[[ excs Cvičení: Výjimky
- deleni
]]]

## Dobrovolné čtení na doma: Pokročilá práce s výjimkami v Pythonu
Pro úplnost doplním, že je možné odchytávat více výjimek v jednom bloku `except`. Tyto výjimky oddělený čárkou **musí** být v závorkách, aby tvořily _n-tici_ (_tuple_). N-tice jsou možná trochu pokročilejší koncept v Pythonu. Pokud netušíte o co se jedná, tak si s tím zatím nelamte hlavu. Rozšířením bloku `except` o klíčové slov `as` si můžeme text výjimky uložit do proměnné. V Pythonu je možný i mechanismus odchytávání všech možných výjimek v jednom bloku `except`, ale to patří k zavrženíhodným programátorským technikám, a proto si to ani nebudeme ukazovat.

```python
import sys

try:
    print(f"Zadán parametr: {sys.argv[1]}")
    print(f"O jedničku vyšší je: {int(sys.argv[1])+1}")
except (IndexError, ValueError) as e:
    print(f"Výjimka: {e}")
    print("Zadej číslo jako parametr na příkazovou řádku!")
```

Pokud stále pokračujete ve čtení této dobrovolné části, vězte, že kromě bloku `try` a `except` je možné zařadit i bloky `else` (toto `else` se nekamarádí s `if`, ale patří k obsluze výjimek. Je to pouze znovu využité klíčové slovo). Tento blok `else` se vykoná, pokud výjimka v bloku `try` nenastala.

Poslední parťák mezi klíčovými slovy k obsluze výjimek je `finally`. Uvozuje blok kódu, který se vykoná za všech okolností (i kdyby výjimka nastala či nenastala). Důležité je zachovat pořadí těchto bloků:

* `try`
* `except`
* (`except`) - více možných bloků `except` pod sebou
* `else`
* `finally`

Jedná už o pokročilé téma, proto zde nebudu uvádět žádné příklady a odkážu vás na oficiální dokumentaci [oficiální tutoriál](https://docs.python.org/3/tutorial/errors.html).

### Vyvolání výjimky
Až budete tvořit složité programy v Pythonu a budete dobře rozumět obsluze výjimek, může vám přijít na mysl otázka, jestli můžeme výjimku sami vyvolat.

Uvažujme předchozí příklad s přetypováním čísla na příkazové řádce a zvolme si další podmínku, např. musí se jednat o kladné číslo. Tuto podmínku musíme otestovat pomocí `if`:

```python
import sys

try:
    print(f"Zadán parametr: {sys.argv[1]}")
    cislo = int(sys.argv[1])
    if cislo < 1:
        raise RuntimeError

    print(f"O jedničku vyšší je: {cislo+1}")
except IndexError:
    print("Zadej parametr na příkazovou řádku!")
except ValueError:
    print("Zadej číslo jako parametr na příkazovou řádku!")
except RuntimeError:
    print("Zadej KLADNÉ číslo jako parametr na příkazovou řádku!")
```

Pomocí klíčového slova `raise` jsme zde vyvolali obecnou výjimku chyby v běhu programu, kterou poté v příslušném bloku `except` odchytíme. _RuntimeError_ jsem vybral ze seznamu vestavěných výjimek v Pythonu a nejlépe vystihuje chybu, která nastala. _ValueError_ by byl také dobrou volbou, ale už se používá pro jinou chybu. Pokud bych potřeboval, mohu si vytvořit i výjimku s vlastním názvem, ale to už si zájemci přečtou v [oficiální dokumentaci](https://docs.python.org/3/tutorial/errors.html).
