Během workshpou Úvod do programování 2 - Python se ponoříme o něco hlouběji do tajů programování a podíváme se, jaké další možnosti nabízí jazyk Python. Na začátku bychom si ale měli zopakovat věci, které jsme již probírali na kurzu Úvod do programování 1, případně je známe odjinud.

Na této stránce najdeš několik příkladů. Nejlepší způsob, jak si svoje znalosti procvičit, je zkopírovat si kódy příkladů do Visual Studia Code nebo jiného editoru a zkusit si, co dělají. Neboj se ani příklady modifikovat a změnit jejich funkci, v textu najdeš spoustu námětů. Nemůžeš při tom nic rozbít, maximálně si kód ze stránky zkopíruješ znovu. 

## Proměnné

Proměnné jsou způsob, jak v našem programu uložit nějaké hodnoty. Jak jejich název napovídá, hodnotu uloženou v proměnné můžeme kdykoli změnit. Proměnné můžeme použít například jako vstup pro nějaké výpočty, předat je funkci ke zpracování nebo vypsat uživateli.

Do proměnných jsme ukládali například vstupy od uživatelů nebo výsledky našich výpočtů. Hodnoty proměnných jsme též často vypisovali na obrazovnku.

## Datové typy

Každá proměnná má nějaký datový typ. Datových typů jsme poznali celkem pět.

| Datový typ | Označení v Pythonu | Příklad hodnoty |
|------------|--------------------|-----------------|
| celé číslo |  `int` | `10`, `- 100` |
| desetinné číslo | `float`  | `5.0`, `-8.6`, `130.4582`
| řetězec | `string` | `"Kolik třešní, tolik višní"`
| pravdivostní hodnota | `bool` | `True`, `False`
| seznam | `list` | `[1, True, "Test", 3.3]`, `[1, 4, 8, 13]`

S různými datovými typy můžeme provádět různé operace. Například můžeme sečíst dvě celá čísla (výsledkem je běžný součet) nebo dva řetězce (výsledkem je spojení obou řetězců dohromady). 

Některé operace naopak dělat nemůžeme - například není možné sečíst číslo a řetězec. Naštěstí můžeme změnit datový typ proměnné pomocí funkcí `str()`, `int()` a `float()`. Ty jsou pojmenované vždy podle cílového datového typu.

#### Na co si dát pozor

Často zapomínáme, že funkce `input()` nám vrací vždy řetězec, bez ohledu na to, jestli uživatel zadal text nebo číslo. Vyzkoušejte si následující příklad:

```py
numberOfTickets = input("Kolik si přejete lístků? ")
pricePerTicket = 345
totalPrice = numberOfTickets * pricePerTicket
print(totalPrice)
```

Python bere náš vstup jako řetězec a pokud jej násobíme číslem, udělá standardní operaci při násobení čísla a řetězce - 345krát zopakuje daný text. Následující progrma už bude fungovat tak, jak čekáme.

```py
numberOfTickets = input("Kolik si přejete lístků? ")
pricePerTicket = 345
numberOfTickets = int(numberOfTickets)
totalPrice = numberOfTickets * pricePerTicket
print(totalPrice)
```

**Námět:** Zkus spojit funkce `input` a `int` do jedné, tj. spojte obě funkce do jednoho řádku. Tím program zkrátíš a zpřehledníš.

#### Tip

Pokud má náš program dát uživateli nějaký výstup, často v něm musíme kombinovat čísla a texty, spojovat je a převádět. Uvažujme například jednoduchou větu: "Cena 2 lístků na hru Každý má svou pravdu je celkem 690 Kč." V ní máme jako proměnné název hry, počet lístků a cenu. I takto jednoduchá věta vyústí v relativně nepřehledný zápis.


```py
play = "Každý má svou pravdu"
numberOfTickets = int(input("Kolik si přejete lístků? "))
pricePerTicket = 345
totalPrice = pricePerTicket * numberOfTickets

print("Cena " + str(numberOfTickets) + " lístků na hru " + play + " je celkem " + str(totalPrice) + " Kč.")
```

Relativně novou vlastnístí Pythonu je možnost využívání f-stringů. Důležité je před uvozovky vložit písmeno `f`. Poté můžeme vkládat do složených závorek přímo názvy proměnných, nemusíme tedy používat znaménka `+`. Navíc za nás Python automaticky obstará i převod čísel na `string`, není tedy třeba používat funkci `str()`.

```py
print(f"Cena {numberOfTickets} lístků na hru {play} je celkem {totalPrice} Kč.")
```

## Podmínky

Naše programy se často musejí *rozhodovat* a některé bloky kódu se spouštěstí pouze za předpokladu splnění nějaké podmínky. Podmínku začínáme klíčovým slovem `if`. Blok, který se spouští při splnění podmínky, je vždy odsazený (standardně se používají 2 nebo 4 mezery).

Uvažujme například kino, které dává slevu 10 % při nákupu lístků za celkovou cenu více než 500 Kč. Pokud tedy zákazník zakoupí větší množství lístků, dostaneme informaci o získané slevě. Každý zákazník pak získá informaci o celkvé ceně, protože tento blok již není odsazený.

```py
numberOfTickets = int(input("Kolik si přejete lístků? "))
pricePerTicket = 190
totalPrice = numberOfTickets * pricePerTicket
if totalPrice >= 500:
  discount = 0.1
  totalPrice = totalPrice * (1 - discount)
  print(f"Získáváte slevu {discount * 100} %")
print(f"Celková cena nákupu je {totalPrice} Kč.")
```

**Námět:** Zkus přidat zaokrouhlení ceny na celé koruny.

#### Na co si dát pozor

Na konci řádku s podmínkou musíme zapsat dvojtečku (`:`). Poté Visual Studio Code provádí odsazení automatiky. Každá podmínka musí obsahovat alespoň jeden řádek, tj. minimálně jeden řádek po podmínce musí být odsazený.

#### Komplexnější podmínky

Pokud si přejeme spustit nějaký blok kódu v případě, že podmínka není splněná, použijeme klíčové slovo `else`.

```py
itemsInStock = 5
numberOfItems = int(input("Kolik si přejete koupit kusů zboží? "))

if numberOfItems <= itemsInStock:
  print("Položky byly vloženy do košiků.")
else:
  print(f"Bohužel máme na skladě posledních {itemsInStock} kusů.")
```

Podmínek můžeme mít i několik za sebou.

```py
points = int(input("Kolik bodů získal student v testu? "))
if points <= 60:
  mark = 5
elif points <= 70:
  mark = 4
elif points <= 80:
  mark = 3
elif points <= 90:
  mark = 2
else:
  mark = 1
print(f"Známka z testu je {mark}.")
```

 Všiměte si, že Python "skočí" do prvního bloku, kde je podmínka splněná. Pokud tedy student například získá 55 bodů, byla by splněná i podmínka `points <= 75`, `points <= 90`. Díky první podmínce se ale do proměnné `mark` uloží známka 5 a program dále skočí na konec bloku s výpisem podmínek.

 **Námět**: Bylo by možné namísto operátoru `<=` použít operátor `>=`? Stačí pouze nahradit znaménka? Nebo je potřeba jinak seřadit podmínky?

Poslední možností jsou vnořené podmínky, tj. podmínky uvnitř podmínek. Uvažujme například mládeži nepřístupný film. Není-li zájemce o film plnoletý, je mu vypsát text o nepřístupnosti. Pouze plnoletý zákazník je tázán na počet lístků a při nákupu většího množství lístků může opět získat slevu. Tentokrát máme dvě možné slevy - 10 % při nákupu nad 500 Kč a 25 % při nákupu nad 1000 Kč.

```py
pricePerTicket = 190
age = int(input("Jaký je váš věk? "))
if age >= 18:
  numberOfTickets = int(input("Kolik si přejete lístků? "))
  totalPrice = numberOfTickets * pricePerTicket
  if totalPrice >= 1000:
    discount = 0.25
    print(f"Získáváte slevu {discount * 100} %")
  elif totalPrice >= 500:
    discount = 0.1
    print(f"Získáváte slevu {discount * 100} %")
  else:
    discount = 0
  totalPrice *=  (1 - discount)
  print(f"Celková cena nákupu je {round(totalPrice)} Kč.")
else:
  print("Tento film bohužel není mládeži přístupný.")
```

Všimněte si, že klíčová slova `else` a `elif` jsou vždy zarovnaná stejně jako začátek podmínky, ke které se vztahují.

**Námět:** Zkus program upravit tak, že nedává slevy v procentech, ale například při nákupu nad 500 Kč má zákazník 1 lístek zdarma a při nákupu nad 1000 Kč 3 lístky zdarma.

## Sekvence

Sekvence jsou hodnoty, které v sobě obsahují jiné hodnoty. Zatím jsme poznali základní dva typy sekvencí - řetězec (`string`) a seznam (`list`).

### Řetězce jeko sekvence

Řetězce jsou vlastně sekvence skládající se z jednotlivých písmen. K jednotlivým prvkům sekvence přistupujeme pomocí hranatých závorek, které píšeme za název řetězce. Písmena jsou číslovaná (indexovaná) od 0.

Ukážeme si například, jak z rodného čísla zjistit datum narození.

```py
birthNumber = input("Zadejte rodné číslo: ")
yearOfBirth = birthNumber[0] + birthNumber[1]
yearOfBirth = int(yearOfBirth)
if yearOfBirth > 20:
  yearOfBirth = 1900 + yearOfBirth
else:
  yearOfBirth = 2000 + yearOfBirth
print(f"Uživatel(ka) se narodil(a) v roce {yearOfBirth}.")
```

**Námět:** Doplň do programu určení rodného čísla na základě pohlaví a vypište ho. Zkus určit měsíc narození obecně pro obě pohlaví pomocí zbytku po celočíselném dělení.

### Seznamy

Seznamy zapisujeme do hranatých závorek. Do seznamu můžeme vložit libovolný datový typ, jaký už známe. Začněme například s řetězci.

```py
guestList = ["Jirka", "Klára", "Natálie"]
```

Chceme-li přidat jednu položku do seznamu, použijeme funkce `append`.

```py
newGuest = input("Zadej jméno dalšího hosta: ")
guestList.append(newGuest)
print(guestList)
```

**Námět:** Vypiš uživateli informaci o počtu hostů v seznamu.

Chceme-li si ověřit, zda je nějaká hodnota v seznamu, můžeme použít operátor in.

```py
incomingPerson = input("Zadej jméno příchozího hosta: ")
if incomingPerson in guestList:
  print("Buď vítán(a)!")
else:
  print("Bohužel nejsi na seznamu.")
```

Sekvence v sobě mohou obsahovat i jiné sekvence. Je to podobné, jako polička na knihy. Ta obsahuje několik knih, každá kniha má několik kapitol, každá kapitola se skládá ze spousty slov a písmen. Níže máš příklad seznamu uvnitř seznamu, který obsahuje známky studentů v nějakém předmětu.

```py
schoolMarks = [
  ["Jiří", 1, 4, 3, 2],
  ["Natálie", 2, 3, 4],
  ["Klára", 3, 2, 4, 1, 3]
]

print(f"První student(ka) v seznamu je {schoolMarks[0][0]}.")
print(f"Její/jeho poslední známka je {schoolMarks[0][-1]}.")
```

**Námět:** Vypiš počet známek nějakého studenta/studentky. Pozor, ať do počtu nezapočítáváš jméno osoby.

## Cykly

Poslední kapitolou, kterou si zopakujeme, jsou cykly. Cykly jsou způsob, jak programu říct, aby opakoval nějakou činnost.

Ideální je využití cyklů spolu s kolekcemi. Pro každý prvek kolekce provedeme nějakou činnost. Uvažujme například vysvědčení studenta základní školy.

```py
schoolReport = [
  ["Český jazyk", 1], 
  ["Anglický jazyk", 1], 
  ["Matematika", 1], 
  ["Přírodopis", 2],
  ["Dějepis", 1],
  ["Fyzika", 2],
  ["Hudební výchova", 4],
  ["Výtvarná výchova", 2],
  ["Tělešná výchova", 3],
  ["Chemie", 4],
]
```

Nejprve si zkusme vypočítat průměrnou známku studenta na vysvědčení. 

```py
sumOfMarks = 0
for mark in schoolReport:
  sumOfMarks += mark[1]
average = round(sumOfMarks/len(schoolReport), 2)
print(f"Průměrná známka studenta je {average}.")
```

Dále můžeme například vypsat všechny předměty, které jsou pro studenta problematické, tj. ty, ze kterých má známku horší než trojku.

```py
problematicSubjects = []
print("Pro studenta jsou problematické tyto předměty:")
for mark in schoolReport:
  if mark[1] > 3:
    print(mark[0])
```

**Námět:** Pro přijetí na střední školu jsou často důležité známky jen z některých předmětů. Vypočtěte tedy průměr známek z obou jazyků, matematiky a fyziky. Tip: uložte si tyto předměty do seznamu a použijte podmínku s operátorem `in`.
