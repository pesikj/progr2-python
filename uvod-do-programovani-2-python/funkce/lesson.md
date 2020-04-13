Funkcí již jsme poznali několik (např. `round`, `int`, `float`, `print`, `input`), zatím jsme ale žádnou vlastní funkci nenapsali. Funkce nám umožňují program strukturovat do bloků a využívat stejný kód na více místech, aniž bychom ho museli kopírovat.

## Definice funkce

K definici funkce používáme klíčové slovo `def`. Dále následuje název funkce a její parametry v kulatých závorkách. Pojem "parametr funkce" už také známe, jsou to hodnoty, které předáváme funkci ke zpracování. Například funkci `print` předáváme řetězec, která má vypsat na obrazovku. Poté následuje dvojtečka `:`, která napovídá, že kód pod dvojtečkou bude odsazený. Kód funkce končí tam, kde již kód není odsazený.

Začněme s jednoduchou funkcí, která pouze vypíše text na obrazovku.

```py
def greetUser():
  print("Ahoj!")
```

Pokud tento kód nakoírujeme do programu, zdánlivě se nic nestane. Funkce je sice vytvořena, ale protože ji nevoláme, nespustí se a program skončí. 

```py
def greetUser():
  print("Ahoj!")
greetUser()
```

Všimni si dvou věcí:

- Volání funkce je až pod její definicí. Pokud bychom pořadí obrátili, Python vrátí chybu, protože by v čase volání funkci ještě neznal.
- Za voláním funkce musíme vždy uvést kulaté závorky. Pokud nepředáváme žádný parametr, zůstanou závorky prázdné.

```py
def greetUser(address):
  print(f"Ahoj {address}!")
greetUser("Jirko")
```

Naše funkce zatím provedly nějakou akci, ale nevrátily nám žádný výstup.  Často nám funkce vracejí nějakou hodnotu. Hodnotu, kterou má funkce vrátit, označíme klíčovým slovem `return`. Zkusme si tedy vytvořit funkci, která vrací součet dvou čísel.

```py
def sumTwoNumbers(a, b):
  return a + b
```

Výstup funkce můžeme uložit do proměnné a dál s ním pracovat.

```py
def sumTwoNumbers(a, b):
  return a + b

returnedValue = sumTwoNumbers(5, 3)
print(returnedValue)
```

V proměnné `returnedValue` tedy budeme mít uložený výsledek našeho součtu a s ním můžeme dále pracovat.

**Poznámka:** Jakmile program narazí na slovo `return`, běh funkce se ukončí. Následující příkazy se tedy již nespustí.

```py
def sumTwoNumbers(a, b):
  return a + b
  print(sum)
```

**Tip:** Pokud si při návrhu programu uvědomíte, že je nějaká funkce potřeba, ale zatím nemáte čas naprogramovat ji, můžete funkci deklarovat a do jejího těla napsat klíčové slovo `pass`. Tento příkaz nic nevykoná, ale díky ní máte splněnou podmínku, že funkce musí mít alespoň jeden řádek.

```py
def codeMeLater(par1, par2):
  pass
```
## Pár příkladů využití funkcí

Vraťme se k našemu příkladu z opakovací lekce, kde jsme měli určit známku z testu na základě počtu bodů. Uvažujme nyní, že student, který získá z testu známku 5, má možnost test jedenkrát opakovat. Podmínku, kterou jsme měli v prvním cvičení, tedy budeme potřebovat dvakrát - pro první a případný druhý pokus. Proto je ideální tuto podmínku umístit do funkce.

```py
def getMark(points):
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
  return mark
```

Nyní můžeme tuto funkci volat z různých míst programu:

```py
points = int(input("Zadej počet bodů v testu: "))
mark = getMark(points)
if mark == 5:
  points = int(input("Zadej počet bodů v opravném pokusu: "))
  mark = getMark(points)
print(f"Výsledná známka je {mark}.")
```

## Nepovinné parametry

Na příkladu funkce `round` jsme viděli, že u některých funkcí není třeba vyplňovat všechny parametry. Zkusme si takovou funkci napsat sami. Napišme si funkci, která projde seznam položek a vybere ty, které jsou skladem a současně je jejich hodnota v dané cenové relaci. 

```py
listOfItems = [
  {"title": "Modrá kravata", "price": 239, "inStock": True},
  {"title": "Luxusní psací pero", "price": 1599, "inStock": True},
  {"title": "Parfém", "price": 559, "inStock": False},
  {"title": "Čajová konvička s hrnky", "price": 899, "inStock": True},
  {"title": "Sklenice na víno", "price": 799, "inStock": True},
  {"title": "Finess náramek", "price": 2399, "inStock": False},
  {"title": "Degustační balíček kávy", "price": 599, "inStock": True},
]
```

Uvažujeme, že parametry `minPrice` a `maxPrice` není třeba zadávat a pokud je uživatel nezadá, pak jako `minPrice` budeme uvažovat 0 a jako `maxPrice` 5000. Naše funkce projde seznam a vrátí ty položky, které vyhovují našim požadavkům.

```py
def filterItems(listOfItems, minPrice=0, maxPrice=5000):
  suitableItems = []
  for item in listOfItems:
    if minPrice <= item["price"] <= maxPrice and item["inStock"]:
      suitableItems.append(item)
  return suitableItems
```

Nyní funkce vrátí všechny položky, které mají cenu mezi 0 a 5000 Kč.

```py
suitableItems = filterItems(listOfItems)
print(f"Na seznamu je {len(suitableItems)} možných dárků.")
```

Pokud zadáme jako první parametr 500, odpadne Modrá kravata s cenou 239.

```py
suitableItems = filterItems(listOfItems, 500)
print(f"Na seznamu je {len(suitableItems)} možných dárků.")
```

A pokud vyplníme i druhý parametr, zůstanou ve výběru 3 dárky.

```py
suitableItems = filterItems(listOfItems, 500, 1000)
print(f"Na seznamu je {len(suitableItems)} možných dárků.")
```


@exercises ## Funkce [

- nasobeni
- bonusy
- narozeni ]@

@exercises bonuses [

- delitel ]@