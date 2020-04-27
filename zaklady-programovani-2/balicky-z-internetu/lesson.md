Internet nabízí obrovské množství frameworků, balíčků a knihoven, které si můžeme přidat do našeho programu. Řadu z nich můžeme jednoduše nainstalovat pomocí aplikace `pip`.

V úvodním kurzu jsme vytvářeli program pro směnárnu. Nevýhodou ale bylo, že jsme museli zadávat kurz ručně. Vyzkoušíme, jestli by bylo možné získat kurz přímo z internetu automaticky. Program by si pak vždy stáhl nový kurz z internetu a odpadly by nám starosti s aktualizací.

Podívejme se, jestli existuje něco, co by nám mohlo pomoci. Zadejme do Google (či jiného vyhledávače) výraz `python exchange rate`.

První odkazy vedou na balíček `forex-python`, která čerpá kurzy z kurzu s měnami Forex. 

Balíček je možné najít na webu GitHub [zde](https://github.com/MicroPyramid/forex-python). S GitHubem už jsme se setkali. Je to vlastně takový katalog programů, které si můžeme stáhnout. Pokud je chceme použít v našem programu, musíme si však dát pozor na licenci.

Stránka balíčku přímo pro `pip` jde [zde](https://pypi.org/project/forex-python/). Tento web poskytuje seznam programů, které si můžete stáhnout pomocí aplikace `pip`.

Dále si můžeme otevřít i dokumentaci programu, která je [zde](https://forex-python.readthedocs.io/en/latest/usage.html). Je trochu podrobnější než text na GitHubu.


## Instalace knihovny

Nyní můžeme nainstalovat knihovnu `forex-python`.

Většina knihoven má nějaký manuál nebo tutoriál, kde autor popisuje, jak program nainstalovat a jak jej používat. Podívejme se tedy přímo na [GitHub](https://github.com/MicroPyramid/forex-python).

V návodu vidíme příkaz k instalaci:

```
pip install forex-python
```

Pokud následující postup nefunguje, můžeme knihovnu stáhnout a spustit instalaci ručně.

```
python setup.py install
```

Zkusme si nyní otevřít terminál a vyzkoušet základní příkazy, které balíček umí.

```py
python
from forex_python.converter import CurrencyRates
c = CurrencyRates()
```

Zkusme si vypsat kurzy české koruny.

```py
>>> c.get_rates('CZK') 
{'GBP': 0.0324795265, 'HKD': 0.3163155152, 'IDR': 641.344922573, 'ILS': 0.1462179869, 'DKK': 0.277780673, 'INR': 3.1080256105, 'CHF': 0.0392458309, 'MXN': 0.9621984812, 'CZK': 1.0, 'SGD': 0.0577762061, 'THB': 1.3348719476, 'HRK': 0.283390411, 'EUR': 0.0372245384, 'MYR': 0.1768463371, 'NOK': 0.4210765337, 'CNY': 0.2879913639, 'BGN': 0.0728037522, 'PHP': 2.0642123288, 'PLN': 0.1692711435, 'ZAR': 0.745439994, 
'CAD': 0.0567934783, 'ISK': 5.803305539, 'BRL': 0.2106350506, 'RON': 0.1799545861, 'NZD': 0.0670339488, 'TRY': 0.2772185825, 'JPY': 4.37983919, 'RUB': 2.9925662597, 'KRW': 49.6028141751, 'USD': 0.0408092615, 'AUD': 0.0637991364, 'HUF': 13.0546456224, 'SEK': 0.4063356164}
```

Formát výstupu nám napovídá, že kurzy jsou uložené ve slovníku, klíčem je zkratka měny a hodnotou je kurz. Hodnoty se vám asi zdají divné. Je to totiž tzv. přímý zápis, tj. zápis, který nám ukazuje, kolik jednotek cizí měny si lze pořídit za 1 Kč. Konkrétně, za 1 Kč si lze pořídit 0.0325 GBP ( britských liber). Touto informací bychom ale naše zákazníky poměrně zmátli.

My jsme zvyklí na nepřímý zápis, tj. na zápis, který říká, kolik korun potřebujeme na jednu jednotku cizí měny. Zkusme náš přímý zápis převést. Jestliže platí 1 CZK = 0.0325 GBP, pak platí 1 / 0.0325 CZK = 1 GBP. Napíšeme tedy program, který vypíše tabulku s měnami, jaká bývá ve směnárně.

```py
from forex_python.converter import CurrencyRates
c = CurrencyRates()
rates = c.get_rates('CZK')
for key, value in rates.items():
  rate = 1 / value
  print(f"1 {key} = {round(rate, 2)}")
```

Se seznamem si můžeme dále hrát. Můžeme si například vypsat jen měny, se kterými naše malá směnárna obchoduje.

```py
currencyList = ["GBP", "EUR", "USD"]
for key, value in rates.items():
  if key in currencyList:
    rate = 1 / value
    print(f"1 {key} = {round(rate, 2)}")
```

Toto by šlo napsat i jinak - v Pythonu máme stále co objevovat!

