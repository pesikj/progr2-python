Seznamy jsou velmi užitečná datová struktura, protože umožňují ukládat spoustu dat do jedné proměnné. Pokud do nich ale ukládáme informace různého typu, může brzy vzniknout chaos. Podívejme se třeba seznam, kde se nachází informace o námi vybraném dárku.

```py
["Čajová konvička s hrnky", 899, True]
```

Pokud by program editoval někdo jiný, těžko asi odhadne, co znamená polední hodnota `True`. Bylo by možné jednotlivé položky nějak popsat? Ve skutečnosti ano, přesně toto řeší datový typ slovník (`dict`).

## O slovnících

Princip slovníků skutečně vychází z papírových slovníků, kde je každý záznam identifikován pomocí nějakého slova a k tomuto slovu jsou přiřazená nějaká data (nejčastěji textový popis). Na podobném principu fungují třeba i muzea, kde exponáty mají štítky s popisky.

Na rozdíl od seznamů nemají slovníky indexy, ale **klíče** (`key`). Jako klíče mohou sloužit všechny datové typy, které známe, s výjimkou seznamů (tj. `int`, `float`, `bool` `string`). Nejčastěji se přirozeně používají řetězce. Všechny mohou být i hodnotami. Jako hodnotu můžeme použít i seznam.

Vezměme nyní náš seznam s informacemi o dárku a převeďme ho na slovník.

```py
gift = {"title": "Čajová konvička s hrnky", "price": 899, "inStock": True}
```

Takový zápis je jistě mnohem srozumitelnější.

Jednotlivou položku slovníků získáme opět pomocí hranatých závorek, do nichž zapíšeme hodnotu klíče.

```py
print(f"Náš dárek {gift['title']} stál {gift['price']} Kč.")
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

Vraťme se nyní k našemu úplně prvnímu příkladu - finančnímu vyrovnání spolubydlících. Slovníky by nám zde mohla pomoci, protože nám pomůžou při tvorbě tabulky s celkovou útratou za jednotlivé spolubydlící. Samotné nákupy již náme též uložené jako slovníky.

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

Musíme si ještě vysvětlit, jak ověřit, jestli nějaká hodnota už ve slovníku je. K tomu použijeme operátor `in`, jako tomu bylo v případě seznamu. Pouze namísto indexu vkládáme klíč.

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

Zkusme si ještě z našeho slovníku vypočítat celkovou útratu. K tomu můžeme využít cyklus `for`. Zde je pouze jeden malý rozdíl. Každá položka slovníku se skládá z klíče a samotné hodnoty. V cyklu můžeme použít oboje (a často i používáme). Využijeme tedy **dvě proměnné**, které oddělíme čárkou. Do první proměnné je uložený klíč a do druhé hodnota.

```py
totalValue = 0
for person, value in sumPerPerson.items():
  totalValue += value
  print(f"{person} untratil(a) za společné nákupy {value} Kč.")
```

Jako poslední krok zbývá určení průměrné hodnoty na osobu. Zde opět využijeme funkci `len`, která umí pracovat i se slovníky.

```py
averageValue = totalValue / len(sumPerPerson)
print(f"Průměrná hodnota na osobu je {round(averageValue)} Kč.")
```

@exercises ## Další možnosti podmínek [

- vecirek
- ctenar
- vysvedceni
- spz ]@

@exercises bonuses [

- spolubydlici ]@