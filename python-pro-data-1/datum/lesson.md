Data patří k základním datovým typům a provázejí nás celý život. Každý máme své datum narození, daum, kdy jsme šli poprvé do školy atd. Data jsou však záludná v tom, že je můžeeme zapsat v různých fomátech. Pojďme se podívat, jak data v různých formátech zpracovat a jak je naopak vypsat.

## Vytvoření data

K práci s daty potřebujeme modul `datetime`, který je základní součástí Pythonu, takže jej nemusíme instalovat. Stačí jej importovat.

```pycon
>>> from datetime import datetime, timedelta
```

Občas je matoucí, že modul `datetime` se dále člení. Obsahuje typ pro uložení samotného data (bez času) `date`, typ pro uložení samotného času (bez data) `time`, typ pro uložení data i času `datetime`, typ pro práci s intervaly `timedelta` a typ pro práci s časovými zónami `tzinfo`. Proto jsme napsali poněkud legrační zápis, ve kterém je dvakrát `datetime`.

První datum, které nás napadne, je aktuální.

```pycon
>>> datetime.now()
datetime.datetime(2020, 11, 21, 20, 26, 26, 472567)
```

Nejjednodušší způsob, jak datum vytvořit, je pomocí funkce `datetime`. Té zadáváme hodnoty postupně: nejprve rok, poté měsíc, den, hodiny, minuty, sekundy a mikrosekundy. Pouze první tři parametry jsou povinné, další vypisovat nemusíme a Python si za ně případně dosadí nuly.

Zkusme si vytvořit proměnnou, která bude reprezentovat start Apolla 11.

```pycon
>>> apolloStart = datetime(1969, 7, 16, 14, 32)
>>> print(apolloStart)
```

Pokud by nás zajímalo, jaký den v týdnu Apollo startovalo, můžeme použít funkci `weekday()` nebo `isoweekday()`. Pozor, je mezi nimi rozdíl. Obě číslují od pondělí, funkce `weekday()` však čísluje od 0 a funkce `isoweekday()` od 1.

```pycon
>>> apolloStart.weekday()
2
>>> apolloStart.isoweekday() 
3
```

### Formátování

Hodnotu aktuální proměnné můžeme vypsat na obrazovku pomocí funkce `print()`. Ta vypíše datum v tzv. ISO formátu (jako oddělovač data a času je použita mezera).

```pycon
>>> print(apolloStart)
1969-07-16 14:32:00
```

Standardně je jako oddělovač použit symbol `T`. Stoprocentně autentický zápis v ISO formátu získáme pomocí funkce `isoformat()`.

```pycon
>>> apolloStart.isoformat()
'1969-07-16T14:32:00'
```

Často ale chceme data vypsat v jiném formátu. Ve střední Evropě jsme zvyklí psát na začátek číslo dne, pak měsíc atd. a jako oddělovač používáme tečku. Pokud chceme výpis v tomto formátu, musíme to Pythonu říct. 

Pokud chceme datum vypsat ve vlastním formátu, použijeme funkci `strftime()`. Ta používá tzv. direktivy, což jsou vlastně značky, které reprezentují nějaý konkrétní časový údaj. Tyto značky poskládáme do řetězce a ten pak tvoří instrukce pro Python, jak má zpracovat datum. Základní direktivy jsou v tabulce níže.

| Direktiva  | Význam |
|:---| :---|
| `%d`  | den  |
| `%m`  | měsíc |
| `%Y`  | rok (nezkrácený) |
| `%H`  | hodina (rozsah 0-23) |
| `%M`  | minuta |
| `%S`  | sekunda |

 Kompletní tabulku s direktivami najdeš [zde](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes). 

 Zkusme si třeba vypsat datum startu Apolla 11 v našem středoevropském formátu.

```pycon
>>> apolloStart.strftime("%d. %m. %Y, %H:%M")            
'16. 07. 1969, 14:32'
```

### Čtení data z výstupu

Bohužel data často získáváme jako řetězce (např. z CSV souborů, ze vstupů od uživatele atd.). Abychom s ním mohli pracovat, musíme si ho převést na typ `datetime`. 

Pokud jsou data v ISO formátu, máme vyhráno. Je možné použít funkci `fromisoformat()`, které stačí zadat řetězec a ona se již o vše postará.

```pycon
>>> apolloPristani = datetime.fromisoformat("1969-07-21T18:54:00")
```

Takové štěstí ale často nemáme, protože řada programů ukládá datum ve formátu, který má nastavený aktuální uživatel. K načtení pak použijeme funkci `strptime()`, které zadáme formát data a času, se kterým máme tu čest.

```pycon
>>> apolloPristani = datetime.strptime("21. 7. 1969, 18:54", "%d. %m. %Y, %H:%M")
```

### Počítání s daty

Často s daty potřebujeme počítat. Pokud například víme, kdy závodník proběhl startem a cílem, můžeme spočítat, kolik času strávil na trati. Dvě data od sebe můžeme jednoduše odečíst. Zkusme si spočítat, jak dlouho trvala mise Apollo.

```pycon
>>> delkaMise = apolloPristani - apolloStart
>>> print(delkaMise)
5 days, 4:22:00
```

Výsledek je hodnota typu `timedelta`.

## Cvičení

### Převod času

V proměnné `apolloStart` máme uložený datum a čas startu Apolla 11. Vypiš datum na obrazovku ve formátu, na který jsou zvyklí Američané, tj. na první místo napiš měsíc, dále den a nakonec rok, jako oddělovače použij lomítka. Čas vypisovat nemusíš.

### Čas od startu

Satelit Solar Orbiter, který má za cíl pozorování Slunce, odstartoval 10. února 2020 v 5:03. Ulož si hodnotu startu do proměnné.

- Který den v týdnu Solar Orbiter odstartoval?
- Spočítej, kolik času od jeho startu uplynulo.

### Doprava večeře

Zákazník si objednal večeři na webu dovážkové služby 13. listopadu 2020 v 19:47. Víme, že převzetí objednávky restaurací v průměru trvá 8 minut a 35 sekund, příprava jídla trvá 30 minut a doprava jídla k zákazníkovi 25 minut a 30 sekund. Kdy očekáváme, že jídlo dorazí zákazníkovi?
