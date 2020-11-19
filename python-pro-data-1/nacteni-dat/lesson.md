Než s daty začneme pracovat, musíme si je nejprve načíst.

## Základní práce s DataFrame

V Pandasu většinou pracujeme s datovou strukturou zvanou `DataFrame`. Je to tabulková datová struktura a funguje podobně jako tabulka v Exelu nebo v databázi. Můžeme jej považovat za další datový typ vedle slovníků a seznamů. `DataFrame` obsahuje data ve sloupcích, kde každý sloupec může mít různý datový typ, tedy například číslo, desetinné číslo, řetězec, pravdivostní hodnota a jiné.

**Poznámka:** Pokud znáš základy objektově orientovaného programování, pak věz, že `DataFrame` je ve skutečnosti třída a my na jejím základě budeme vytvářet objekty. 

Abychom si práci s DataFrame vyzkoušeli, vrátíme se k naší tabulce se seznamem nákupů.

| Jméno   | Datum      | Věc              |   Částka v korunách |
|:--------|:-----------|:-----------------|--------------------:|
| Petr    | 2020-02-05 | Prací prášek     |                 399 |
| Ondra   | 2020-02-08 | Savo             |                  80 |
| Petr    | 2020-02-24 | Toaletní papír   |                  65 |
| Libor   | 2020-03-05 | Pivo             |                 124 |
| Petr    | 2020-03-18 | Pytel na odpadky |                  75 |
| Míša    | 2020-03-30 | Utěrky na nádobí |                 130 |
| Ondra   | 2020-04-22 | Toaletní papír   |                 120 |
| Míša    | 2020-05-05 | Pečící papír     |                  30 |
| Zuzka   | 2020-06-05 | Savo             |                  80 |
| Pavla   | 2020-06-13 | Máslo            |                  50 |
| Ondra   | 2020-07-25 | Káva             |                 300 |

### Načítání dat

Tabulku výše si můžete stáhnout ve [formátu CSV](assets/nakupy.csv). Důležité je, že si soubor musíš uložit nebo zkopírovat do **stejného adresáře**, v jakém právě pracuješ ve Visual Studiu! To si ověříš pomocí příkazu `dir` ve Windows nebo `ls` v MacOS nebo Linuxu. Tento příkaz ti vypíše obsah aktuální adresáře. V přehledu souborů bys měla vidět soubor `nakupy.csv`.

Abychom tabulku načetli jako `DataFrame`, otevřeme si nejprve Python konzoli, importujeme modul `pandas` a načteme CSV soubor pomocí funkce `read_csv().`

```pycon
>>> import pandas
>>> nakupy = pandas.read_csv('nakupy.csv')
```

**Poznámka:** Modul `pandas` nabízí obrovské množství možností. Nemusíš si samozřejmě vše pamatovat, protože vše najdeš přehledně popsáno [v dokumentaci](https://pandas.pydata.org/docs/). Například funkce `read_csv` je [popsána zde](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html). Dokumentaci k samotnému DataFrame najdeš [zde](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html).

Funkce `read_csv` má spoustu nepovnných parametrů, o kterých si můžeme přečíst [v dokumentaci](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html). Například se tam dočteme, že `pandas` standardně nastavuje jako oddělovač sloupců čárku (parametr `sep`). Protože my většinou používáme středník, budeme muset tento parametr často nastavit. Náš soubor `nakupy.csv` ale používá čárku, takže nyní nic měnit nemusíš.

Celý DataFrame vypíšeme na obrazovku tak, že zobrazíme přímo proměnnou `nakupy`.

```pycon
>>> nakupy
    Jméno       Datum               Věc  Částka v korunách
0    Petr  2020-02-05      Prací prášek                399
1   Ondra  2020-02-08              Savo                 80
2    Petr  2020-02-24    Toaletní papír                 65
3   Libor  2020-03-05              Pivo                124
4    Petr  2020-03-18  Pytel na odpadky                 75
5    Míša  2020-03-30  Utěrky na nádobí                130
6   Ondra  2020-04-22    Toaletní papír                120
7    Míša  2020-05-05      Pečící papír                 30
8   Zuzka  2020-06-05              Savo                 80
9   Pavla  2020-06-13             Máslo                 50
10  Ondra  2020-07-25              Káva                300
```

Všimni si, že `pandas` nám přidal nový sloupec s číslem řádku. Jedná se o **index**, se kterým budeme později pracovat. Index je hodnota, která identifikuje řádek. V některých případech nemusíme jako index používat číslo řádku, ale můžeme jako index vybrat některý ze sloupců. Obdobnou funkci má v databázích **primární klíč**. Jako *best practice* se většinou uvádí, že index by měl být **unikátní**, i když to `pandas` (narozdíl od právě databází) nevyžadují. Mohli bychom si tedy jako index zvolit napříkad sloupec `Jmeno`, ale tím bychom si zadělávali na problém do budoucna (například v tom, že by práce s `DataFrame` byla [pomalejší](https://stackoverflow.com/q/16626058/4693904)).

Pandas nabízí kromě funkce `read_csv()` také funkci pro čtení formátu JSON `read_json()` nebo dokonce funkci pro čtení přímo Excelovových tabulek `read_excel()`.

### Základní informace o tabulce

Jakmile máme tabulku načtenou, budeme o ní chtít vědět nějaké úplně základní údaje. K tomu nám pomůže metoda `info()`, která vrací souhrnné informace o celé tabulce: názvy sloupců, datové typy, počet neprázdných hodnot atd.

```pycon
>>> nakupy.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 11 entries, 0 to 10
Data columns (total 4 columns):
 #   Column             Non-Null Count  Dtype 
---  ------             --------------  ----- 
 0   Jméno              11 non-null     object
 1   Datum              11 non-null     object
 2   Věc                11 non-null     object
 3   Částka v korunách  11 non-null     int64 
dtypes: int64(1), object(3)
memory usage: 480.0+ bytes
```

Počet řádků a sloupců můžeme získat z vlastnosti `shape`:

```pycon
>>> nakupy.shape
(11, 4)
```

**Poznámka:** Pokud znáš základy objektově orientovaného programování, pak věz, že `info` je ve skutečnosti funkce třídy `DataFrame`. 

`pandas` nám vrací výsledky v sekvenci, která se jmenuje `tuple`. Nás stačí vědět, že si z ní data můžeme načíst stejně jako ze seznamu. Na prvním místě je vždy počet řádků a na druhém počet sloupců. Pokud by nás třeba zajímal jen počet řádků, napíšeme: 

```pycon
>>> nakupy.shape[0]
11
```

Názvy všech sloupců pak z vlastnosti `columns`:

```pycon
>>> nakupy.columns
Index(['Jméno', 'Datum', 'Věc', 'Částka v korunách'], dtype='object')
```

## Index

Jak už víme, v `pandas` má každý řádek přiřazený index. Jako index můžeme zvolit některý ze sloupců. Pokud však tabulku načteme bez toho, abychom specifikovali index, `pandas` nám vytvoří **číselný index** automaticky. Je to něco podobného jako číslování řádků v Excelu.

K vybrání jednoho konkrétního řádku můžeme použít `iloc[]`. `iloc` nám umožní ptát se na konkrétní záznam podobně jako u sekvencí, jsou zde přítomné i hranaté závorky. `iloc` tedy ve skutečnosti není funkce, ale kromě jiného typu závorek s ní pracujeme jako s funkcí.

Zkusme si zobrazit třeba **čtvrtý** nákup. Číslujeme tradičně od nuly, jistě tě tedy nepřekvapí, že napíšeme `nakupy.iloc[3]`.

```
>>> nakupy.iloc[3] 
Jméno                     Libor
Datum                2020-03-05
Věc                        Pivo
Částka v korunách           124
Name: 3, dtype: object
```

Všimni si, že když jsme chtěli pouze jeden řádek, vypsal se nám výsledek jinak orientovaný, než když jsme chtěli řádků více. Je to proto, že pokud vybíráme pouze jeden řádek, vrátí nám takzvanou **sérii** (`Series`), což je jiný datový typ než DataFrame.

Metoda `iloc[]` umožňuje pro výběr řádků použít rozsah ve formátu `od:do`. K tomu používáme **dvojtečku**. Před dvojtečku píšeme první řádek, který chceme vypsat a za dvojtečku první řádek, který již vy výpisu nebude. Pokud tedy například napíšeme `nakupy.iloc[3:5]`, získáme třetí a čtvrtý řádek, ale už ne pátý.

```pycon
>>> nakupy.iloc[3:5] 
   Jméno       Datum               Věc  Částka v korunách
3  Libor  2020-03-05              Pivo                124
4   Petr  2020-03-18  Pytel na odpadky    
```

Pokud se chceme podívat třeba na první tři řádky, nemusíme před dvojtečku psát 0, stačí napsat `iloc[:3]`.

```pycon
>>> nakupy.iloc[:3] 
   Jméno       Datum             Věc  Částka v korunách
0   Petr  2020-02-05    Prací prášek                399
1  Ondra  2020-02-08            Savo                 80
2   Petr  2020-02-24  Toaletní papír                 65
```

Podobně si můžeme nechat vypsat poslední tři řádky. Pokud víme, že řádků je 10, chceme vypsat řádky od osmého dále. Nyní se nabízí napsat číslo před dvojtečku. Píšeme tam ale 8, protože řádek, jehož číslo je před dvojtečkou, je vždy součástí výpisu.

```pycon
>>> nakupy.iloc[8:] 
    Jméno       Datum    Věc  Částka v korunách
8   Zuzka  2020-06-05   Savo                 80
9   Pavla  2020-06-13  Máslo                 50
10  Ondra  2020-07-25   Káva                300
```

Nevýhodou postupu je, že si musíme předem zjistit, jak kolik řádků máme. U seznamů už ale existoval trik použití záporného čísla. Ten můžeš použít i v `pandas`. Pokud napíšeš `iloc[-3:]`, získáš též poslední tři řádky.

```pycon
>>> nakupy.iloc[-3:] 
    Jméno       Datum    Věc  Částka v korunách
8   Zuzka  2020-06-05   Savo                 80
9   Pavla  2020-06-13  Máslo                 50
10  Ondra  2020-07-25   Káva                300
```

**Tip:** Trik s dvojtečkou funguje i u sekvencí. Můžeme jej použít třeba na řetězce.

```pycon
>>> pozdrav = "Ahoj Jirko" 
>>> pozdrav[-5:] 
'Jirko'
```

### Začátek a konec jinak

Na prvních a posledních několik řádků se chceme podívat často, hlavně v případě, když moc dobře neznáme strukturu dat. Kromě funkce `iloc`, z níž se ti možná už začala točit hlava, k tomu ještě můžeme použít funkce `head` a `tail`.

```pycon
>>> nakupy.head()
   Jméno       Datum               Věc  Částka v korunách
0   Petr  2020-02-05      Prací prášek                399
1  Ondra  2020-02-08              Savo                 80
2   Petr  2020-02-24    Toaletní papír                 65
3  Libor  2020-03-05              Pivo                124
4   Petr  2020-03-18  Pytel na odpadky                 75
```

Často je užitečné podívat se spíše na konec souboru. Pokud jsou data seřazená podle času, uvidíme na konci souboru nejnovější data, která nás často (např. u kurzu měn nebo akcií) zajímají víc než dávná historie.

```pycon
>>> nakupy.tail()
    Jméno       Datum             Věc  Částka v korunách
6   Ondra  2020-04-22  Toaletní papír                120
7    Míša  2020-05-05    Pečící papír                 30
8   Zuzka  2020-06-05            Savo                 80
9   Pavla  2020-06-13           Máslo                 50
10  Ondra  2020-07-25            Káva                300
```

### Sloupce

Kromě řádků si často chceme vybrat jen některé sloupce, protože mnoho tabulek obsahuje spoustu různých informací a ne všechny nás musejí zajímat. Čísla sloupců zadáváme jako druhý parametr funkce `iloc`.

Pokud chceš například vypsat jména u prvních pět nákpů, jako první parametr napíš `:5` a jako druhý `0`.

```pycon
>>> nakupy.iloc[:5,0]
0     Petr
1    Ondra
2     Petr
3    Libor
4     Petr
Name: Jméno, dtype: object
```

U sloupců ale často narazíme na to, že jich chceme několik, ale ony nutně nemusí být vedle sebe. nás u nákupů asi bude nejvíce zajímat jméno a částka. Abychom dali dohromady dvě čísla, která neleží vedle sebe, můžeme použít seznam. Pro prvních pět nákupů tedy jako druhý parametr napíšeme `[0,3]`.

```pycon
>>> nakupy.iloc[:5,[0,3]] 
   Jméno  Částka v korunách
0   Petr                399
1  Ondra                 80
2   Petr                 65
3  Libor                124
4   Petr                 75
```

Pokud bys chtěla vidět všechny řádky, jako první parametr napiš pouze dvoutečku.

```pycon
>>> nakupy.iloc[:,[0,3]]  
    Jméno  Částka v korunách
0    Petr                399
1   Ondra                 80
2    Petr                 65
3   Libor                124
4    Petr                 75
5    Míša                130
6   Ondra                120
7    Míša                 30
8   Zuzka                 80
9   Pavla                 50
10  Ondra                300
```

@exercises ## Cvičení [

- nabidky
  ]@