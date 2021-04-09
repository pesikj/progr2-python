## Cyklus pomocí číselné řady

V první kapitole jsme si vyzkoušeli (nebo spíše zopakovali) cyklus spuštěný nad námi vytvořeným seznamem. Použití cyklů je ale širší. Například si můžeme číselně zvolit, kolikrát by se nějaký cyklus měl opakovat. K tomu využijeme funkci `range`. Tato funkce vytvoří posloupnost (`sequence`) čísel a cyklus je spuštěn pro každý prvek této posloupnosti. 

Funkci `range` můžeme zadat parametry `start` (začátek posloupnosti) a `stop` (konec posloupnosti, tato hodnota již v posloupnosti není !). Můžeme však zadat pouze parametr `stop` a pak jako `start` použita 0.

Samotný zápis cyklu se téměř neliší, používáme klíčová slova `for`, `in` a dvojtečku. Mezi `for` a `in` vkládáme název proměnné, která se stane dočasným nositelem čísla, se kterým cyklus právě pracuje. Pro tuto dočasnou číselnou proměnnou se v programování velice často používá jednoduchý název `i`.

Zkusíme si nejprve vypsat všechna čísla od 0 do nějaké hodnoty.

```py
stop = int(input("Zadej konec: "))
for i in range(stop):
  print(i)
```

Takto například vypadá průběh programu:

```
Zadej nejvyšší číslo: 5
0
1
2
3
4
```

Všimni si, že zadáme-li jako vstup `5`, výpis končí číslem `4`, hodnota zadaná jako `end` tam již skutečně není.

Zkusme nyní využít i parametr `start`. Zkusíme si třeba vypsat čísla nikoli od 0, ale od nějaké konkrétní hodnoty.

```py
start = int(input("Zadej začátek: "))
stop = int(input("Zadej konec: "))
for i in range(start, stop):
  print(i)
```

Opět platí, že dovnitř cyklu můžeme vložit podmínku. Zkusme si například vypsat pouze ta čísla z daného rozsahu, která jsou dělitelná třemi.

```py
start = int(input("Zadej začátek: "))
stop = int(input("Zadej konec: "))
for i in range(start, stop):
  if i % 3 == 0:
    print(i)
```

Pevný počet opakování ale zdaleka nevyužíváme jen v kombinaci s čísly. Vraťme se třeba k našemu příkladu na seznam hostů z opakovací lekce. Seznam hostů nemusíme zapisovat přímo do programu, ale můžeme požádat uživatele, aby nám jména hostů postupně zadával. Jména pak připojujeme k seznamu stávajícímu hostů pomocí funkce `append`.

```py
numberOfGuests = int(input("Zadej počet hostů: "))
guestList = []
for i in range(numberOfGuests):
  newGuest = input("Zadej jméno hosta: ")
  guestList.append(newGuest)
print(guestList)
```

#### Tip

Všiměte si, že prázdný seznam jsme vytvořili jednoduše pomocí prázdných hranatých závorek `[]`.

## Přerušení cyklu

Často se ocitneme v situaci, že cyklus chceme ukončit v jeho průběhu. Je to podobné, jako když něco hledáme a procházíme při tom všechny místnosti v domě. Jakmile danou věc nalezneme, hledání ukončíme.

K ukončení běhu cyklu používáme klíčové slovo `break`. Jakmile program narazí na slovo `break`, cyklus ukončí a pokračuje dál v kódu, který je pod cyklem. Příkaz `break` používáme v drtivé většině případů v kombinaci s podmínkou `if`.

Uvažujme třeba prekérní situaci, kdy na poslední chvíli potřebujeme objednat dárek na oslavu narozenin. Máme seznam zboží v e-shopu a u každého zboží máme jeho název, cenu a počet kusů skladem. Vzhledem k situaci potřebujeme, aby bylo zboží skladem a současně chceme dárek s cenou od 500 do 1000 Kč. Protože nemáme čas, spokojíme se s prvním nalezeným dárkem.

```py
listOfItems = [
  {"title": "Modrá kravata", "price": 239, "inStock": True},
  {"title": "Luxusní psací pero", "price": 1599, "inStock": True},
  {"title": "Degustační balíček kávy", "price": 599, "inStock": True},
  {"title": "Parfém", "price": 559, "inStock": False},
  {"title": "Čajová konvička s hrnky", "price": 899, "inStock": True},
  {"title": "Sklenice na víno", "price": 799, "inStock": True},
  {"title": "Finess náramek", "price": 2399, "inStock": False},
]

for item in listOfItems:
  if 500 <= item["price"] <= 1000 and item["inStock"]:
    print(f"Vybraný dárek je {item['title']}")
    break
```

Pokud bychom příkaz `break` odebrali, program by pokračoval v hledání a vypsal ještě 2 další dárky, která vyhovují podmínkám.

#### Tip

Všimni si, že podmínku, zda určité číslo leží mezi dvěma jinými čísly, můžeme zapsat ve stylu `dolniHranice <= cislo <= horniHranice`. To je zjednodušení zápisu `dolniHranice <= cislo and cislo <= horniHranice`.

[[[ excs Cvičení: Další příklady cyklů
- tombola
- delitelnost
- hoste
]]]

[[[ excs Bonusy
- prvocislo
]]]

## Dobrovolné čtení na doma: cyklus `while` a příkaz `continue`

Aby byl tento text co nejkompletnější, je třeba zmínit i cyklus `while` a příkaz `continue`.

### Cyklus `while`
Nejdříve si pro zopakování probereme, že cyklus `for` slouží k procházení složených datových typů. Při procházení seznamů získáváme přístup ke každému prvku seznamu. Při procházení řetězců se jedná o každé písmeno. Cyklus `for` využíváme i při procházení slovníků a pro velmi mnoho dalších případů (např. procházení otevřených souborů po řádcích).

Naproti tomu, cyklus `while` je obecný cyklus a svou konstrukcí má blíže k podmínce `if`. U podmínky `if` platí, že odsazený blok po podmínce `if` se provede, pokud se samotná podmínka, tj. výraz mezi `if` a dvojtečkou vyhodnotí jako `True`.

U cyklu `while` platí, že se jeho blok kódu provádí **opakovaně dokud** jeho podmínka platí. U následujícího příkladu je uživatel tázán na heslo stále dokola dokud heslo 123456 nezadá správně.

```py
spravneHeslo = "123456"
zadaneHeslo = input("Zadej heslo: ")

while zadaneHeslo != spravneHeslo:
  zadaneHeslo = input("Zadej heslo: ")

print("Heslo zadano")
```

Pokud používáme cyklus `while` je třeba mít na paměti, že v těle cyklu musí existovat šance na to, že se podmínka cyklu změní a cyklus se tím ukončí. Při programování se však velmi často stane, že uděláme chybu, která neumožní ukončení cyklu a nám vznikne _nekonečný_ cyklus. Naštěstí existuje klávesová zkratka Ctrl+C, která v terminálu program vykonávaný Python interpretem nemilosrdně ukončí i uprostřed nekonečného cyklu.

O pojmu _nekonečný cyklus_ si povíme něco více. Protože již z předchozí části známe příkaz `break`, který nám ukončí cyklus (to platí i pro cyklus `while`), můžeme si dovolit vytvořit nekonečný cyklus záměrně. Předchozí příklad je možné přepsat do následující podoby a například obohatit o výpis o nevyhovujícím heslu.

```py
spravneHeslo = "123456"

while True:
  if input("Zadej heslo: ") == spravneHeslo:
    break
  print("Špatné heslo")

print("Heslo zadano")
```

Podmínka cyklu `while` se bude vyhodnocovat vždy jako pravdivá (jedná se o hodnotu _True_) a pouze na nás je, abychom ve vhodném místě cyklus `while` ukončili pomocí příkazu `break`.

[[[ excs Cvičení: Cyklus while
- hadani
]]]

### Příkaz `continue`
Příkaz `continue` je podobný příkazu `break`, ale s tím rozdílem, že neukončí celý cyklus, ale pouze přeskočí zbytek těla cyklu a pokračuje další iterací. Pokud je použit v cyklu `for`, řídící proměnná cyklu `for` nabude nové hodnoty (tzn. zpracuje se další prvek seznamu nebo další číslo z rozsahu `range()`). U cyklu `while` dojde opět k vyhodnocování jeho podmínky.

Následující příkaz vytiskne pouze ta čísla z číselné řady, která jsou dělitelná 10. Zbytek přeskočí pomocí příkazu `continue`.

```py
stop = int(input("Zadej konec: "))

for i in range(stop):
  if i % 10 != 0:
    continue

  print(i)
```

Příkazy `break` a `continue` je možné v rámci jednoho cyklu zkombinovat, např.

```py
soucet = 0

while True:
  vstup = input("Zadej číslo: ")

  if not vstup:
    break

  if not vstup.isdigit():
    print("Nezadal jsi číslo")
    continue

  print(f"Zadáno číslo {vstup}")
  soucet += int(vstup)

print(f"Součet je {soucet}")
```

Nekonečný cyklus se ukončí příkazem `break` pokud `vstup` neobsahuje žádné znaky (jedná se o prázdný řetězec). Pokud by dále řetězec `vstup` nebyl složen pouze z cifer, zadaná hodnota se přeskočí.


### Část `else` u cyklů
Může se vám stát, že při čtení cizího kódu narazíte na `else`, před kterým se ale nenachází žádný blok `if`. Klíčové slovo `else` totiž může být použito ve více různých konstrukcích a jednou z nich je použití u cyklů. Jedná se o specifikum Pythonu, které obecně není moc běžné. Větev `else` patřící k cyklu `for` nebo k cyklu `while` se vykoná pokud cyklus **nebyl** ukončen příkazem `break`. Toto není příliš intuitivní je potřeba si to zapamatovat. Je to ovšem pokročilá věc, kterou vás nikdo nenutí používat je zde zmíněna pouze pro kompletnost.

