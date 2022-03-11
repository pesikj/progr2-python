Funkce nám umožňují program strukturovat do bloků a využívat stejný kód na více místech, aniž bychom ho museli kopírovat. Funkcí již jsme poznali několik (např. `round`, `int`, `len`, `print`, `input`), zatím jsme ale žádnou vlastní funkci nevytvořili. Vytváření funkcí se naučíme v této části.

## Definice funkce

K definici funkce používáme klíčové slovo `def`. Dále následuje **název funkce** a její **parametry** (`parameter`) v kulatých závorkách. Pojem parametr funkce už také známe, pomocí parametrů předáváme funkci hodnoty ke zpracování. Například funkci `print` předáváme řetězec, která má vypsat na obrazovku.

Po názvu funkce následuje **dvojtečka** `:`, která napovídá, že kód pod dvojtečkou bude **odsazený**. Kód funkce končí tam, kde již kód není odsazený.

**Poznámka:** Je zde též trochu zrádná terminologie. Při definici funkce definujeme její parametry, ale při volání funkce zapisujeme do závorek argumenty (`arguments`).

Začněme s jednoduchou funkcí, která pouze vypíše text na obrazovku.

```py
def greet_user():
  print("Ahoj!")
```

Pokud tento kód zkopírujeme do programu, zdánlivě se nic nestane. Funkce je sice vytvořena, ale nevoláme ji. 

```py
def greet_user():
  print("Ahoj!")
greet_user()
```

Nyní již program náš pozdrav vypíše.

Všimni si ještě dvou dvou věcí:

- Volání funkce je až **pod její definicí**. Pokud bychom pořadí obrátili, Python vrátí chybu, protože by v čase volání funkci ještě neznal.
- Za **voláním** funkce musíme vždy uvést **kulaté závorky**. Pokud nepředáváme žádnou hodnotu, zůstanou závorky prázdné.

Upravme naši funkci tak, aby vypsala oslovení, které jí zadáme:

```py
def greet_user(name):
  print(f"Ahoj {name}!")
greet_user("Jirko")
```

Naše funkce zatím provedly nějakou akci, ale nevrátily nám žádný **výstup**. Často nám funkce vracejí nějakou hodnotu. Hodnotu, kterou má funkce vrátit, označíme klíčovým slovem `return`. Zkusme si tedy vytvořit funkci, která vrací součet dvou čísel.

```py
def sum_two_numbers(a, b):
  return a + b
```

Výstup funkce můžeme uložit do proměnné.

```py
returned_value = sum_two_numbers(5, 3)
print(returned_value)
```

V proměnné `returned_value` tedy budeme mít uložený výsledek našeho součtu a s ním můžeme dále pracovat.

**Poznámka:** Jakmile program narazí na slovo `return`, běh funkce se ukončí. Například funkce níže žádný výpis neprovede.

```py
def sum_two_numbers(a, b):
  return a + b
  print(sum)
```

### Čtení na doma - čistá funkce

Níže definovaná funkce je bez tzv. *vedlejších efektů* (`side effect`), tj. používá pouze své parametry a nepoužívá žádné proměnné definované mimo ni (např. vstup od uživatele). Stejně tak mimo návratové hodnoty nijak neovlivňuje běh programu. Funkci bez vedlejších efektů se říká čistá funkce (`pure function`). Její výhodou je, že pro stejný vstup vždy vrací stejný výstup, což například usnadňuje testování nebo hledání chyby.

```py
def sum_two_numbers(a, b):
  return a + b
```

Níže uvedená funkce není čistá, protože čte proměnnou "zvenku". Může tedy v různých situacích vracet různé výsledky.

```py
exchange_rate = 26
def convert_to_euro(crown):
  return crown * exchange_rate
```

Takto uvedená funkce je již čistou funkcí.

```py
def convert_to_euro(crown, exchange_rate):
  return crown * exchange_rate
```

### Funkce bez kódu

Pokud si při návrhu programu uvědomíte, že je nějaká funkce potřeba, ale zatím nemáte čas naprogramovat ji, můžete funkci deklarovat a do jejího těla napsat klíčové slovo `pass`. Tento příkaz nic nevykoná, ale díky ní máte splněnou podmínku, že funkce musí mít alespoň jeden řádek.

```py
def code_me_later(par1, par2):
  pass
```
## Pár příkladů využití funkcí

Vraťme se k našemu příkladu z opakovací lekce, kde jsme měli určit známku z testu na základě počtu bodů. Uvažujme nyní, že student, který získá z testu známku 5, má možnost test jedenkrát opakovat. Podmínku, kterou jsme měli v prvním cvičení, tedy budeme potřebovat dvakrát - pro první a případný druhý pokus. Proto je ideální tuto podmínku umístit do funkce.

```py
def get_mark(points):
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
mark = get_mark(points)
if mark == 5:
  points = int(input("Zadej počet bodů v opravném pokusu: "))
  mark = get_mark(points)
print(f"Výsledná známka je {mark}.")
```

## Nepovinné parametry

Na příkladu funkce `round` jsme viděli, že u některých funkcí není třeba vyplňovat všechny parametry. Vraťme se k funkci `get_mark()`. Uvažujme nyní, že studenti mají možnost získat bonusové body (např. za odevzdání úkolů), které se pak připočítávají k bodům z testu. 

```py
def get_mark(points, bonus=0):
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
mark = get_mark(points, bonus)
if mark == 5:
  points = int(input("Zadej počet bodů v opravném pokusu: "))
  mark = get_mark(points, bonus)
print(f"Výsledná známka je {mark}.")
```


[[[ excs Cvičení: Funkce
- nasobeni
- hotel
]]]

[[[ excs Bonusy
- narozeni
- ruleta
]]]

### Čtení na doma - typování funkcí

Python patří mezi *dynamicky typové jazyky*, což znamená, že při vytvoření proměnné neříkáme, jaký typ hodnoty do ní budeme ukládat. Od verze 3.5 ale podporuje `typing`. Můžeme tedy říct, jaký typ hodnoty by *měla obsahovat* nějaká proměnná, Python to však nekontroluje a neukončí program s chybou, pokud do proměnné vložíme hodnotu jiného typu. Typování ale funguje jako nápověda pro programátory a především vývojová prostředí, která pak umějí vývojářům lépe napovídat při psaní programů a případně je upozornit, pokud plánují do proměnné vložit něco, co tam nepatří.

Níže je příklad funkce `get_mark()` s typováním. Typovat můžeme jednotlivé parametry i návratovou hodnotu, jejíž typ je za "šipkou" `->`.

```py
def get_mark(points: int, bonus: int=0) -> int:
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

print(get_mark(50, 30))
```
