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

@exercises ## Cykly 2 [

- tombola
- delitelnost
- hoste ]@

@exercises bonuses [

- prvocislo ]@