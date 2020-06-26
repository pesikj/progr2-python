Funkce nám umožňují program strukturovat do bloků a využívat stejný kód na více místech, aniž bychom ho museli kopírovat. Funkcí již jsme poznali několik (např. `round`, `int`, `len`, `print`, `input`), zatím jsme ale žádnou vlastní funkci nevytvořili. Vytváření funkcí se naučíme v této části.

## Definice funkce

K definici funkce používáme klíčové slovo `def`. Dále následuje **název funkce** a její **parametry** (`parameter`) v kulatých závorkách. Pojem parametr funkce už také známe, pomocí parametrů předáváme funkci hodnoty ke zpracování. Například funkci `print` předáváme řetězec, která má vypsat na obrazovku. Po názvu funkce následuje **dvojtečka** `:`, která napovídá, že kód pod dvojtečkou bude **odsazený**. Kód funkce končí tam, kde již kód není odsazený.

**Poznámka:** Je zde též trochu zrádná terminologie. Při definici funkce definujeme její parametry, ale při volání funkce zapisujeme do závorek hodnoty (`arguments`).

Začněme s jednoduchou funkcí, která pouze vypíše text na obrazovku.

```py
def greetUser():
  print("Ahoj!")
```

Pokud tento kód zkopírujeme do programu, zdánlivě se nic nestane. Funkce je sice vytvořena, ale nevoláme ji. 

```py
def greetUser():
  print("Ahoj!")
greetUser()
```

Nyní již program náš pozdrav vypíše.

Všimni si ještě dvou dvou věcí:

- Volání funkce je až **pod její definicí**. Pokud bychom pořadí obrátili, Python vrátí chybu, protože by v čase volání funkci ještě neznal.
- Za **voláním** funkce musíme vždy uvést **kulaté závorky**. Pokud nepředáváme žádnou hodnotu, zůstanou závorky prázdné.

Upravme naši funkci tak, aby vypsala oslovení, které jí zadáme:

```py
def greetUser(name):
  print(f"Ahoj {name}!")
greetUser("Jirko")
```

Naše funkce zatím provedly nějakou akci, ale nevrátily nám žádný **výstup**. Často nám funkce vracejí nějakou hodnotu. Hodnotu, kterou má funkce vrátit, označíme klíčovým slovem `return`. Zkusme si tedy vytvořit funkci, která vrací součet dvou čísel.

```py
def sumTwoNumbers(a, b):
  return a + b
```

Výstup funkce můžeme uložit do proměnné.

```py
returnedValue = sumTwoNumbers(5, 3)
print(returnedValue)
```

V proměnné `returnedValue` tedy budeme mít uložený výsledek našeho součtu a s ním můžeme dále pracovat.

**Poznámka:** Jakmile program narazí na slovo `return`, běh funkce se ukončí. Například funkce níže žádný výpis neprovede.

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

Funkci můžeme volat z různých míst programu:

```py
points = int(input("Zadej počet bodů v testu: "))
mark = getMark(points)
if mark == 5:
  points = int(input("Zadej počet bodů v opravném pokusu: "))
  mark = getMark(points)
print(f"Výsledná známka je {mark}.")
```

## Nepovinné parametry

Na příkladu funkce `round` jsme viděli, že u některých funkcí není třeba vyplňovat všechny parametry. Vraťme se k funkci `getMark`. Uvažujme nyní, že studenti mají možnost získat bonusové body (např. za odevzdání úkolů), které se pak připočítávají k bodům z testu. 

```py
def getMark(points, bonus=0):
  if points + bonus <= 60:
    mark = 5
  elif points + bonus <= 70:
    mark = 4
  elif points + bonus <= 80:
    mark = 3
  elif points + bonus <= 90:
    mark = 2
  else:
    mark = 1
  return mark
```

Nyní opět zavoláme funkci. Uvažujeme stále možnost jednoho opravného pokusu, počet bonusových bodů zůstává.

```py
points = int(input("Zadej počet bodů v testu: "))
bonus = int(input("Zadej počet bonusových bodů: "))
mark = getMark(points, bonus)
if mark == 5:
  points = int(input("Zadej počet bodů v opravném pokusu: "))
  mark = getMark(points, bonus)
print(f"Výsledná známka je {mark}.")
```


@exercises ## Funkce [

- nasobeni
- hotel ]@

@exercises bonuses [

- narozeni
- ruleta ]@