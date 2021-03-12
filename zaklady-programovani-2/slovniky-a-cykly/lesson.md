V úvodním workshopu jsme si ukázali, že pro práci se sekvencemi jsou ideální cykly. Vyzkoušíme si nyní, jak se slovníky pracovat pomocí cyklů.

## Slovníky a cykly

Abychom si ukázali průchod slovníkem pomocí cyklu, použijeme slovník s údaji o prodejích knih z cvičení z minulé kapitoly. Ve slovníku tedy máme následující data:

```py
sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}
```

Zkusme si nejprve vypsat názvy všech knih ve slovníku (bez počtu prodaných kusů). K tomu použijeme cyklus `for`, který již známe. Pomocnou proměnnou si pojmenujeme `key`. Tato proměnná funkce podobně jako u seznamu - postupně se do ní vloží hodnoty jednotlivých klíčů slovníku.

```py
for key in sales:
  print(key)
```

Zkusme nyní informaci o každém prodeji vypsat pomocí věty, do které vložíme název knihy a počet prodaných kusů. Oproti předchozímu příkladu je tu změna. **Každá položka** slovníku se skládá z **klíče a samotné hodnoty**. V cyklu můžeme přečíst oboje (a často i používáme). Využijeme tedy **dvě proměnné**, které oddělíme čárkou. Do první proměnné je uložený klíč a do druhé hodnota. 

Všimněte si též, že za slovník vkládáme `.items()`.


```py
for key, value in sales.items():
  print(f"Knihy {key} bylo prodáno {value} výtisků.")
```

Zkusme si nyní spočítat celkový počet prodaných kusů. Vytvoříme si tedy proměnnou `totalSales` a pro každou knihu do ní přičteme počet prodaných kusů.

```py
totalSales = 0
for key, value in sales.items():
  print(f"Knihy {key} bylo prodáno {value} výtisků.")
  totalSales += value
print(f"Celkem bylo prodáno {totalSales} výtisků.")
```


## Dvourozměrné tabulky v Pythonu

O knihách můžeme evidovat mnohem více informací. Uvažujme nyní, že chceme mít uložen nejen počet prodaných kusů, ale i cenu knihy. Použijeme opět slovník, pro jednu knihu by zápis vypadal takto:

```py
book = {"title": "Zkus mě chytit", "sold": 4165, "price": 347}
```

My ale máme další dvě knihy. Jak vložíme všechny knihy do jedné proměnné? Použijeme k tomu seznamy, které již známe! Seznam se všemi slovníky může vypadat takto:

```py
books = [
  {"title": "Zkus mě chytit", "sold": 4165, "price": 347, "year": 2018},
  {"title": "Vrah zavolá v deset", "sold": 5681, "price": 299, "year": 2019},
  {"title": "Zločinný steh", "sold": 2565, "price": 369, "year": 2019},
]
```
Je to v podstatě běžná dvourozměrná tabulka, jakou můžeme vytvořit například v Excelu.

Upravme nyní náš výpočet celkového počtu prodaných knih. Nyní pomocí cyklu `for` procházíme seznam, vrátíme se tedy zpět k jedné proměnné, kterou si pojmenujeme `item`. Do té cyklus nyní nebude ukládat číslo, ale slovník. Protože my chceme vědět počet prodaných kusů, z každého slovníku si načteme hodnotu uloženou pod klíčem `sold`.

```py
sales = 0
for item in books:
  sales += item["sold"]
print(f"Celkem bylo prodáno {sales} knih.")
```

Zkusme si ještě spočítat tržby nejen v prodaných kusech, ale i v penězích. Vždy tedy počet prodaných knih (hodnota s klíčem `sold`) vynásobíme cenou jedné knihy (hodnota s klíčem `price`).

```py
sales = 0
for item in books:
  sales += item["sold"] * item["price"]
print(f"Celkové tržby jsou {sales} Kč.")
```

A zkusme ještě jednu úpravu. Nakladatele zajímá, jaké jsou peněžní tržby za knihy vydané v roce 2019. U každé knihy tedy musíme zkontrolovat, zda vyšla v roce 2019, a pouze pokud je tato podmínka splněná, přičteme tržbu za knihu k proměnné `sales`.

```py
sales = 0
for item in books:
  if item["year"] == 2019:
    sales += item["sold"] * item["price"]
print(f"Celkové tržby za knihy prodané v roce 2019 jsou {sales} Kč.")
```

[[[ excs Cvičení: Slovníky a cykly
- ctenar
- vysvedceni
]]]

[[[ excs Bonusy
- spz
]]]

## Čtení na doma

Vraťme se nyní k našemu úplně prvnímu příkladu - finančnímu vyrovnání spolubydlících. Slovníky by nám zde mohla pomoci, protože nám pomůžou při tvorbě tabulky s celkovou útratou za jednotlivé spolubydlící.

Jeden nákup zapsaný do slovníku vypadá například takto:

```py
{"person": "Petr", "item": "Prací prášek", "value": 399}
```

Protože nákupů bylo více, jeden slovník by nám nestačil. Proto vytvoříme více slovníků a ty uložíme do seznamu.

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

```py
sumPerPerson = {}
for item in purchaseList:
  person = item["person"]
  value = item["value"]
  if person in sumPerPerson:
    sumPerPerson[person] += value
  else:
    sumPerPerson[person] = value
```

Vypíšeme si nyní útraty jednotlivých spolubydlících a spočteme celkovou útratu. K tomu můžeme využít cyklus `for`. Zde je pouze jeden malý rozdíl.

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

[[[ excs Cvičení na doma
- spolubydlici
]]]
