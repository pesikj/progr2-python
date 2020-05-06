Seznamy jsou velmi užitečná datová struktura, protože umožňují ukládat spoustu dat do jedné proměnné. Pokud do nich ale ukládáme informace různého typu, může brzy vzniknout chaos. Podívejme se třeba seznam, který obsahuje informace o předmětu v obchodě.

```py
["Čajová konvička s hrnky", 899, True]
```

Dokázali bychom asi odhadnout, že první prvek je název a druhý cena. Co však znamená `True`? To za seznamu na první pohled patrné není. Samozřejmě by bylo možné tu informaci někam poznamenat, ale možná by stálo za to mít tu informaci přímo v sekvenci.

A přesně toto řeší datový typ slovník (`dict`).

## O slovnících

Princip slovníků skutečně vychází z papírových slovníků, kde je každý záznam identifikován pomocí nějakého slova a k tomuto slovu jsou přiřazená nějaká data (nejčastěji textový popis). Na podobném principu fungují třeba i muzea, kde exponáty mají štítky s popisky.

Na rozdíl od seznamů nemají slovníky indexy, ale **klíče** (`key`). Jako klíče mohou sloužit všechny datové typy, které známe, s výjimkou seznamů (tj. `int`, `float`, `bool` `string`). Nejčastěji se přirozeně používají řetězce. Každý klíč má přiřazenou **hodnotu**. Hodnotou může být libovolný datový typ.

Vezměme nyní náš seznam s informacemi o předmětu a převeďme ho na slovník.

```py
item = {"title": "Čajová konvička s hrnky", "price": 899, "inStock": True}
```

Takový zápis je jistě mnohem srozumitelnější. Nyní vidíme, že poslední hodnota označuje, zda je položka skladem.

Všimni si, že slovníky zapisujeme do **složených závorek**, mezi klíčem a hodnotou je **dvojtečka** a jednotlivé dvojice jsou odděleny **čárkami**.

Ze slovníku můžeme snadno získat jednu jeho hodnotu. K tomu použijeme hranaté závorky, do kterých zapíšeme klíč.

```py
title = item['title']
```

Zkusme si třeba vypsat informace o položce.

```py
print(f"Vybraný předmět je {gift['title']} a stojí {gift['price']} Kč.")
```

**Pozor:** Při použití f-stringů je nutné uvnitř hranatých závorek použít jiný typ označení řetězců. Začínáte-li text pomocí uvozovek, pro klíče slovníku použijte apostrofy.

Podobně snadno můžeme nějakou existující hodnotu upravit nebo přidat novou.

```py
gift['price'] = 929
gift['weightInKilos'] = 0.4
```

Dále je možné jako slovníky používat i proměnné.

```py
key = 'price'
gift[key] = 929
```

Prádný slovník vytvoříme pomocí prázdných složených závorek, tedy například:

```py
gift = {}
```

### Slovníky a cykly

V úvodním workshopu jsme si ukázali, že pro práci se sekvencemi jsou ideální cykly. Vyzkoušíme si nyní, jak se slovníky pracovat pomocí cyklů.

Vraťme se nyní k našemu úplně prvnímu příkladu - finančnímu vyrovnání spolubydlících. Slovníky by nám zde mohla pomoci, protože nám pomůžou při tvorbě tabulky s celkovou útratou za jednotlivé spolubydlící. 

Samotné nákupy již náme též uložené jako slovníky.

```py
purchaseList = [
  {"person": "Petr", "item": "Prací prášek", "value": 399},
  {"person": "Ondra", "item": "Savo", "value": 80},
  {"person": "Petr", "item": "Toaletní papír", "value": 65},
  {"person": "Libor", "item": "Pivo", "value": 124},
  {"person": "Petr", "item": "Pytel na odpadky", "value": 75},
  {"person": "Míša", "item": "Utěrky na nádobí", "value": 130},
  {"person": "Ondra", "item": "Toaletní papír", "value": 120},
  {"person": "Míša", "item": "Pečící papír", "value": 30},
  {"person": "Zuzka", "item": "Savo", "value": 80},
  {"person": "Pavla", "item": "Máslo", "value": 50},
  {"person": "Ondra", "item": "Káva", "value": 300}
]
```

Útraty jednotlivých spolubydlících si budeme ukládat do nového slovníku. Musíme si tedy nejprve vysvětlit, jak ověřit, jestli nějaká hodnota už ve slovníku je. Pokud spolubydlící v našem novém slovníku ještě částku nemá, vložíme tam hodnotu aktuálního nákupu. Pokud tam nějakou částku už má, přičteme k této částce hodnotu aktuálního nákupu.

K ověření, jestli nějaký klíč už ve slovníku je, použijeme operátor `in`, jako tomu bylo v případě seznamu. Pouze namísto indexu vkládáme klíč.

```py
sumPerPerson = {}
for purchase in purchaseList:
  person = purchase["person"]
  value = purchase["value"]
  if person in sumPerPerson:
    sumPerPerson[person] += value
  else:
    sumPerPerson[person] = value
```

Vypíšeme si nyní útraty jednotlivých spolubydlících a spočteme celkovou útratu. K tomu můžeme využít cyklus `for`. Zde je pouze jeden malý rozdíl. Každá položka slovníku se skládá z klíče a samotné hodnoty. V cyklu můžeme použít oboje (a často i používáme). Využijeme tedy **dvě proměnné**, které oddělíme čárkou. Do první proměnné je uložený klíč a do druhé hodnota. Všimněte si též, že za slovník vkládáme `.items()`.

```py
totalValue = 0
for person, value in sumPerPerson.items():
  totalValue += value
  print(f"{person} utratil(a) za společné nákupy {value} Kč.")
```

Jako poslední krok zbývá určení průměrné hodnoty na osobu. Zde opět využijeme funkci `len`, která umí pracovat i se slovníky.

```py
averageValue = totalValue / len(sumPerPerson)
print(f"Průměrná hodnota na osobu je {round(averageValue)} Kč.")
```

@exercises ## Další možnosti podmínek [

- vecirek
- ctenar ]@

@exercises bonuses [
- vysvedceni
- spolubydlici ]@