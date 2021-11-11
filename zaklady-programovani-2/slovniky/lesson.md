Seznamy jsou velmi užitečná datová struktura, protože umožňují ukládat spoustu dat do jedné proměnné. Pokud do nich ale ukládáme informace různého typu, může brzy vzniknout chaos. Podívejme se třeba seznam, který obsahuje informace o položce v e-shopu.

```py
["Čajová konvička s hrnky", 899, True]
```

Dokázali bychom asi odhadnout, že první prvek je název a druhý cena. Co však znamená `True`? To za seznamu na první pohled patrné není. Samozřejmě by bylo možné tu informaci někam poznamenat, ale možná by stálo za to mít tu informaci přímo v sekvenci.

A přesně toto řeší datový typ slovník (`dict`).

## O slovnících

Princip slovníků skutečně vychází z papírových slovníků, kde je každý záznam identifikován pomocí nějakého slova a k tomuto slovu jsou přiřazená nějaká data (nejčastěji textový popis). Na podobném principu fungují třeba i muzea, kde exponáty mají štítky s popisky.

Na rozdíl od seznamů nemají slovníky indexy, ale **klíče** (`key`). Jako klíče mohou sloužit datové typy `int`, `float`, `bool` `string` (a další, které zatím neznáme). Nejčastěji se přirozeně používají řetězce. Každý klíč má přiřazenou **hodnotu**. Hodnotou může být libovolný datový typ.

Vezměme nyní náš seznam s informacemi o položce v e-shopu a převeďme ho na slovník.

```py
item = {"title": "Čajová konvička s hrnky", "price": 899, "in_stock": True}
```

Takový zápis je jistě mnohem srozumitelnější. Nyní vidíme, že poslední hodnota označuje, zda je položka skladem. Všimni si, že slovníky zapisujeme do **složených závorek**, mezi klíčem a hodnotou je **dvojtečka** a jednotlivé dvojice jsou odděleny **čárkami**.

Ze slovníku můžeme snadno získat jednu jeho hodnotu. K tomu použijeme **hranaté závorky**, do kterých zapíšeme klíč.

```py
title = item['title']
```

Zkusme si třeba vypsat informace o položce.

```py
print(f"Vybraný předmět je", item["title"], "a stojí", item["price"], "Kč.")
```

Je možné též použít formátované řetězce (f-stringy).

```py
print(f"Vybraný předmět je {item['title']} a stojí {item['price']} Kč.")
```

**Pozor:** Při použití f-stringů je nutné uvnitř hranatých závorek použít jiný typ označení řetězců. Začínáte-li text pomocí uvozovek, pro klíče slovníku použijte apostrofy.

Funkci `print()` můžeme použít i na celý slovník. Python pak použije standardní výpis, který vypadá stejně, jako když slovník zapisujeme. Hodí se to, když potřebujeme zkontrolovat, co vlastně ve slovníku je.

```py
{'title': 'Čajová konvička s hrnky', 'price': 899, 'in_stock': True}
```

K ověření, jestli nějaký klíč už ve slovníku je, použijeme operátor `in`, jako tomu bylo v případě seznamu. Pouze namísto indexu vkládáme klíč.

```py
item = {"title": "Čajová konvička s hrnky", "price": 899, "in_stock": True}
if "weight" in item:
  print(f"Hmotnost předmětu je", item["weight"], "kg.")
else:
  print("Hmotnost není zadána.")
```

Snadno můžeme nějakou existující hodnotu upravit nebo přidat novou.

```py
item['price'] = 929
item['weight'] = 0.4
```

Jako klíče slovníku používat i proměnné.

```py
key = 'price'
item[key] = 929
```

Prázdný slovník vytvoříme pomocí prázdných složených závorek, tedy například:

```py
item = {}
```

Zkusme si ještě jeden motivační příklad. Uvažujme například, že chystáme firemní výlet a chceme nakoupit špekáčky pro kolegy. Abychom věděli, kolik jich máme celkem koupit, vytvoříme si slovník a pro každého z kolegů a kolegyň si budeme evidovat, kolik špekáčků plánují během výletu sníst.

```py
sausages = {"Jirka": 2, "Naty": 1, "Adam": 4, "Lucka": 2, "Pavča": 2}
```

Počet kolegů, kteří jdou na párty, zjistíme pomocí nám již známé funkce funkce `len`.

```py
print(len(sausages))
```

Uvažujme například, že se Naty na poslední chvíli omluví. Upravíme tedy hodnotu s klíčem `Naty` na 0.

```py
sausages["Naty"] = 0
print(len(sausages))
```

Drobnou nevýhodou je, že funkce `len` bude stále vracet hodnotu 5, protože klíč `Naty` je ve slovníku stále přítomen. Alternativně můžeme klíč ze slovníku úplně vyřadit. K tomu slouží funkce `pop`.

```py
sausages.pop("Naty")
```

Nyní funkce `len` vrátí 4.

[[[ excs Cvičení: Slovníky
- vysvedceni
- detektivky
- tombola
]]]

[[[ excs Bonusy
- vecirek
]]]
