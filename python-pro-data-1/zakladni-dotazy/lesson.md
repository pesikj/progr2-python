## Základní práce s DataFrame

V Pandasu většinou pracujeme s datovou strukturou zvanou `DataFrame`. Je to tabulková datová struktura a funguje podobně jako tabulka v Exelu. Můžeme jej považovat za další datový typ vedle slovníků a seznamů. DataFrame obsahuje data ve sloupcích, kde každý sloupec může mít různý datový typ, tedy například číslo, desetinné číslo, řetězec, pravdivostní hodnota a jiné.

Abychom si práci s DataFrame vyzkoušeli, vrátíme se k naší tabulce se seznamem nákupů. Abychom si mohli vyzkoušet i práci s daty, máme v tabulce navíc sloupec `Datum`.

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

Tabulku výše si můžete stáhnout ve [formátu CSV](assets/nakupy.csv). Důležité je, že si soubor musíš uložit nebo zkopírovat do **stejného adresáře**, v jakém právě pracuješ ve Visual Studiu! Abychom si ji mohli prohlédnout jako DataFrame, otevřeme si nejprve Python konzoli, importujeme modul `pandas` a načteme CSV soubor pomocí funkce `read_csv().`

```pycon
>>> import pandas
>>> nakupy = pandas.read_csv('nakupy.csv')
```

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

Všimni si, že `pandas` nám přidal nový sloupec s číslem řádku. Jedná se o **index**, se kterým budeme později pracovat.

Pandas nabízí kromě funkce `read_csv()` také funkci pro čtení formátu JSON `read_json()` nebo dokonce funkci pro čtení přímo Excelovových tabulek `read_excel()`.

### Základní informace o tabulce

V realitě máme většinou větší objemy dat a stačí nám prohlédnout si začátek tabulky, abychom měli představu o jejím obsahu. K tomu slouží funkce `head`. Ta standardně vypíše 5 řádků.

```
>>> nakupy.head()
   Jméno       Datum               Věc  Částka v korunách
0   Petr  2020-02-05      Prací prášek                399
1  Ondra  2020-02-08              Savo                 80
2   Petr  2020-02-24    Toaletní papír                 65
3  Libor  2020-03-05              Pivo                124
4   Petr  2020-03-18  Pytel na odpadky                 75
```

Často je užitečné podívat se spíše na konec souboru. Pokud jsou data seřazená podle času, uvidíme na konci souboru nejnovější data, která nás často (např. u kurzu měn nebo akcií) zajímají víc než dávná historie.

```
>>> nakupy.tail()
    Jméno       Datum             Věc  Částka v korunách
6   Ondra  2020-04-22  Toaletní papír                120
7    Míša  2020-05-05    Pečící papír                 30
8   Zuzka  2020-06-05            Savo                 80
9   Pavla  2020-06-13           Máslo                 50
10  Ondra  2020-07-25            Káva                300
```

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

Názvy všech sloupců pak z vlastnosti `columns`:

```pycon
>>> nakupy.columns
Index(['Jméno', 'Datum', 'Věc', 'Částka v korunách'], dtype='object')
```

## Index

V `pandas` má každý řádek přiřazený index. Jako index můžeme zvolit některý ze sloupců. Pokud však tabulku načteme bez toho, abychom specifikovali index, `pandas` nám vytvoří číselný index automaticky. Je to něco podobného jako číslování řádků v Excelu.

K vybrání jednoho konkrétního řádku můžeme použít funkce `loc[]` a `iloc[]`.

Všimněte si nového prvního sloupečku, který obsahuje index vytvořený Pandas. Vzhledem k tomu, že index je nyní číselný, může být trochu matoucí rozdíl mezi použitím metod `loc[]` a `iloc[]`. Metoda `loc[]` vždycky vždycky vždycky používá pro výběr dat **jména** řádků (tedy index). V předchozích příkladech byla jména řádků názvy měst, nyní jsou jména řádků obyčejná čísla. Index je v tedy v tomto případě stejný, jako pozice řádků. Dejme tomu, že chceme získat všechna města od začátku tabulky po město Most. V předchozím příkladu, kde indexem byly názvy měst, bychom psali

```pycon
>>> nakupy.loc[3]  
Jméno                Libor
Věc                   Pivo
Částka v korunách      124
Name: 3, dtype: object
```

Nyní, když máme index číselný píšeme

```pycon
>>> nakupy.loc[2:4] 
   Jméno               Věc  Částka v korunách
2   Petr    Toaletní papír                 65
3  Libor              Pivo                124
4   Petr  Pytel na odpadky                 75
```

```pycon
>>> nakupy.loc[:2]  
   Jméno             Věc  Částka v korunách
0   Petr    Prací prášek                399
1  Ondra            Savo                 80
2   Petr  Toaletní papír                 65
```

V tomto případě tedy volání `loc[]` vypadá stejně jako `iloc[]`. Rodíl je však v tom, že rozsahy v indexu vždy počítají horní mez **včetně** , kdežto rozsahy v pozicích počítají horní mez **vyjma**. Kdybychom tedy chtěli stejná data pomocí metody `iloc[]`, psali bychom

```pycon
>>> mesta.iloc[:4]
```

## Základní selekce

Abychom dokázali s naší tabulkou manipulovat, potřebujeme dobře rozumět tomu, jak vlastně Pandas DataFrame funguje. Pomůže nám k tomu následující obrázek, který ukazuje, jak náš DataFrame vypadá poté, co jsme jej načetli z CSV.

![Pandas DataFrame](assets/dataframe.svg){.fig .fig-100}

Do začátku je nejdůležitější si uvědomit, že Pandas pracuje nejen se jmény sloupců, ale také se **jmény řádků**. Jménům řádků se v Pandasu říká _index_. Již při načtení našeho DataFrame z CSV jsme zvolili, že řádky se budou jmenovat podle názvů měst (použili jsme parametr `index_col`). Zvolili jsme tedy sloupec `mesto` jako náš index. Díky tomu máme jednoznačné názvy sloupců i řádků a můžeme tak vytvářet různé dotazy na data z tabulky.

### Výběr podle jmen řádků a sloupců

K výběru dat pomocí jmen řádků a sloupců slouží metoda `loc[]`. Je to trochu zvláštní metoda, neboť se volá pomocí hranatých závorek namísto kulatých. Jakmile tuto divnou věc s větším či menším vzdorem přijmeme, můžeme pomocí ní zkusit vybrat z tabulky jeden řádek tak, že napíšeme do těchto hranatých závorek přímo jeho název.

```pycon
>>> mesta.loc['brno']
kraj            JHM
obyvatel    379 527
linky            22
vymera       230.22
Name: brno, dtype: object
```

Chceme-li řádků více, stačí jejich jména napsat jako seznam.

```pycon
>>> mesta.loc[['brno', 'praha', 'ostrava']]
        kraj   obyvatel  linky  vymera
mesto
brno     JHM    379 527     22  230.22
praha    PHA  1 294 513     24  496.00
ostrava  MSK    290 450     15  214.23
```

Všimněte si, že když jsme chtěli pouze jeden řádek, vypsal se nám výsledek jinak orientovaný, než když jsme chtěli řádků více. Je to proto, že pokud dáme metodě `loc[]` jméno řádku přímo, vrátí nám takzvanou _sérii_ , což je jiný datový typ než DataFrame. Pokud chceme DataFrame i v případě jednoho řádku, musíme dotaz zadat jako jednoprvkový seznam.

```pycon
>>> mesta.loc[['brno']]
      kraj obyvatel  linky  vymera
mesto
brno   JHM  379 527     22  230.22
```

Metoda `loc[]` dokonce umožňuje pro výběr řádků použít rozsah od:do.

```pycon
>>> mesta.loc['most':'plzen']
        kraj obyvatel  linky  vymera
mesto
most     ULK   66 644      5   86.94
olomouc  OLK  100 494      7  103.36
ostrava  MSK  290 450     15  214.23
plzen    PLK  170 936      3  137.65
```

S rozsahy uvnitř `loc[]` můžeme pracovat podobně jako jsme byli zvyklí u číselných rozsahů při výběru hodnot z obyčejných seznamů. Můžeme tak například vybrat všechny řádky od města most až do konce tabulky

```pycon
>>> mesta.loc['most':]
```

nebo všechna města od začátku až po Plzeň

```pycon
>>> mesta.loc[:'plzen']
```

Metodu `loc[]` můžeme také použít k výběru podle jmen sloupců. Stačí dotaz na sloupce zadat jako druhý parametr metody. Vypišme například počty obyvatel všech měst mezi Mostem a Plzní

```pycon
>>> mesta.loc['most':'plzen', 'obyvatel']
mesto
most        66 644
olomouc    100 494
ostrava    290 450
plzen      170 936
```

Při výběru sloupců podle jmen můžeme použít úplně stejných triků jako při výběru řádků. Vyzkoušejte si následující následující dotazy:

Vyber počty obyvatel a počty linek pro všechna města až po Plzeň.

```pycon
>>> mesta.loc[:'plzen', ['obyvatel', 'linky']]
```

Vyber všechny sloupce až po linky pro všechna města počínaje Mostem.

```pycon
>>> mesta.loc['most':, :'linky']
```

Vyber všechny řádky pro sloupce od linek dál.

```pycon
>>> mesta.loc[:, 'linky':]
```

### Výběr podle pozic řádků a sloupců

Při práci s většími tabulkami se nám může snadno stát, že nechceme vybírat sloupce nebo řádky podle jejich jmen, nýbrž podle jejich pozic. K tomu slouží metoda `iloc[]`. Tato metoda se používá velmi podobně jako metoda `loc[]` s tím rozdílem, že pro výběr použivá právě pozice, nikoliv jména. Pandas čísluje pozice řádků a sloupců uvnitř DataFramu stejně, jak jsme zvyklí, tedy vždy od nuly. Můžeme proto rovnou vyzkoušet několik dotazů.

Řádek na pozici 3 jako série.

```pycon
>>> mesta.iloc[3]
kraj           ULK
obyvatel    66 644
linky            5
vymera       86.94
Name: most, dtype: object
```

Řádek na pozici 3 jako DataFrame:

```pycon
>>> mesta.iloc[[3]]
      kraj obyvatel  linky  vymera
mesto
most   ULK   66 644      5   86.94
```

Řádky na pozicích 1, 3 a 5:

```pycon
>>> mesta.iloc[[1, 3, 5]]
        kraj obyvatel  linky  vymera
mesto
liberec  LBK  103 979      6  106.09
most     ULK   66 644      5   86.94
ostrava  MSK  290 450     15  214.23
```

Řádky 1 až 4, sloupce od 2 nahoru:

```pycon
>>> mesta.iloc[1:4, 2:]
          linky  vymera
mesto
liberec       6  106.09
litvinov      5   40.70
most          5   86.94
```

Metoda `iloc[]` je tedy velmi podobá metodě `loc[]`. Je zde však jeden významný rozdíl. Pokud používáme uvnitř `iloc[]` rozsahy (například `2:5`), horní hranice je **vždy vyjma** , tedy řádek 5 nebude do výberu zahrnut. Pokud však použjeme rozsah v metodě `loc[]`, bude horní mez **vždy včetně**. Takže rozsah `'liberec':'most'` bude obsahovat i řádek se jménem most.

## Ukládání dat

Podobně jako jsme měli funkce `read_csv`, `read_json` a `read_excel` pro čtení dat, máme také metody pro zápis dat. Pomocí metod `to_csv` a `to_json` můžeme celý DataFrame zapsat do CSV nebo JSONu. Stačí zadat název souboru

```pycon
>>> mesta.to_csv('data.csv')
```

Užitečná je také metoda `to_html`, která zapíše DataFrame jako webovou stránku. Zkuste napsat

```pycon
>>> mesta.to_html('data.html')
```

a otevřít soubor `data.html` v prohlížeči. Takto si můžete tabulku prohlédnout hezky naformátovanou.

@exercises ## Cvičení [

- ceska-jmena
  ]@

## Dotazy jako v SQL

Kromě metod `loc[]` a `iloc[]` umožňuje Python DataFrame psát dotazy nad tabulkami podobným způsobem, jako se píší dotazy v jazyce SQL. Stačí použít obyčejné hranaté závorky jako je známe z práce se seznamy.

Aby následující příklady byly co nejvíc srozumitelné, budeme uvádět i jejich ekvivalent v SQL. Můžeme si představovat, že máme tabulku měst uloženou nejen jako DataFrame v Pythonu ale také jako tabulku v SQL databázi.

### Výběr sloupečků

**Dotaz:**

Sloupečky `linky` a `obyvatel`.

SQL:

```sql
SELECT linky, obyvatel FROM mesta;
```

Pandas:

```py
mesta[['linky', 'obyvatel']]
```

Výsledek:

```pycon
          linky   obyvatel
mesto
brno         22    379 527
liberec       6    103 979
litvinov      5     24 143
most          5     66 644
olomouc       7    100 494
ostrava      15    290 450
plzen         3    170 936
praha        24  1 294 513
```

### Podmínky

**Dotaz:**

Všechny sloupečky pro města s více než deseti linkami.

SQL:

```sql
SELECT * FROM mesta WHERE linky > 10;
```

Pandas:

```py
mesta[mesta['linky'] > 10]
```

Výsledek:

```pycon
        kraj   obyvatel  linky  vymera
mesto
brno     JHM    379 527     22  230.22
ostrava  MSK    290 450     15  214.23
praha    PHA  1 294 513     24  496.00
```

**Dotaz:**

Sloupečky 'kraj' a 'vymera' pro města s rozlohou mezi 100 a 200 km2.

SQL:

```sql
SELECT kraj, vymera FROM mesta WHERE vymera >= 100 and vymera <= 200;
```

Pandas:

```py
mesta[(mesta['vymera'] >= 100) & (mesta['vymera'] <= 200)][['kraj', 'vymera']]
```

Výsledek:

```pycon
        kraj  vymera
mesto
liberec  LBK  106.09
olomouc  OLK  103.36
plzen    PLK  137.65
```

V posledním dotazu už je taková přehršel hranatých a kulatých závorek, že by z toho znejistěl i kovaný Pythonista. Můžeme si situaci malinko ulehčit tím, že si obsah hranatých závorek nejdříve uložíme do proměnné a až pak dotaz vyhodnotíme

```pycon
>>> radky = (mesta['vymera'] >= 100) & (mesta['vymera'] <= 200)
>>> sloupce = ['kraj', 'vymera']
>>> vyber = mesta[radky][sloupce]
```

Všimněte si, že výsledkem každého dotazu je opět DataFrame, který jsme si takto uložili do proměnné vyber. Nad touto proměnnou pak můžeme vesele spouštět jakékoliv další dotazy.

### Logické operátory v podmínkách

Před chvílí jsme viděli použití operátoru `&`, který v dotazech slouží jako logická spojka AND. Můžeme však také použít operátor `|`, který představuje logické OR. Chtějme například počty linek všech měst z Jihomomoravského nebo Olomouckéko kraje

```pycon
>>> mesta[(mesta['kraj'] == 'JHM') | (mesta['kraj'] == 'OLK')][['linky']]
         linky
mesto
brno        22
olomouc      7
```

Snadno se však může stát, že budeme chtít krajů více, například Jihomoravský, Olomoucký a Ústecký. Takový zápis by byl pomocí operátoru OR nepraktický. Zde můžeme použít metodu `isin()`, která vrací `True`, pokud se hodnota nachází v zadaném seznamu.

```pycon
>>> mesta[mesta['kraj'].isin(['JHM', 'ULK', 'OLK'])][['linky']]
          linky
mesto
brno         22
litvinov      5
most          5
olomouc       7
```

Poslední operátor, který můžeme v podmínkách dotazů použít vypadá takto `~` a představuje negaci. Můžeme tak vypsat linky všech měst, které se nenacházeji v jednom ze zadaných krajů:

```pycon
>>> mesta[~mesta['kraj'].isin(['JHM', 'ULK', 'OLK'])][['linky']]
         linky
mesto
liberec      6
ostrava     15
plzen        3
praha       24
```

Kombinací výše uvedených operátorů můžeme snadno vytvořit velmi komplikované dotazy. Vzhledem k tomu, že výsledky všech dotazů jsou opět DataFramy, můžeme si výsledky dotazů ukládat do proměnných a pouštět na nich další dotazy až se dostaneme ke kýženému výsledku.

## Převod mezi DataFrame a seznamy

Python DataFrame je obsáhlý a komplikovaný objekt. Pokud s ním chceme pracovat, musíme znát spoustu triků a metod, které nám Pandas poskytuje. Občas se nám tak může hodit převést DataFrame na prachobyčejný Pythonovský seznam seznamů, což je teritorium, ve kterém jsme si po mnoha lekcích Pythonu zatím mnohem jistější než v Pandasu. K takovému převodu nám poslouží jednoduchý příkaz.

```pycon
>>> data = mesta.values.tolist()
>>> data
[['JHM', '379 527', 22, 230.22], ['LBK', '103 979', 6, 106.09], ['ULK', '24 143', 5, 40.7], ['ULK', '66 644', 5, 86.94], ['OLK', '100 494', 7, 103.36], ['MSK', '290 450', 15, 214.23], ['PLK', '170 936', 3, 137.65], ['PHA', '1 294 513', 24, 496.0]]
```

Ve výsledných seznamech nám ovšem chybí názvy měst. Potíž je v tom, že index se v Pandasu nebere jako součást dat. Pokud chceme index vrátit do původního stavu a mít ho jako automaticky generovaná čísla řádků, můžeme použít metodu `reset_index()`. S její pomocí pak už dokážeme dostat z DataFramu čistá data takto

```pycon
>>> data = mesta.reset_index().values.tolist()
```

Můžeme však postupovat i obráceně a vyrobit DataFrame ze seznamu seznamů. Pokud však nechceme názvy sloupců jako čísla, je třeba názvy dodat.

```pycon
>>> mesta2 = pandas.DataFrame(data, columns=['mesto', 'kraj', 'obyvatel', 'linky', 'vymera'])
```

@exercises ## Cvičení [

- ceska-jmena-podruhe
- puvod-jmen
  ]@

## Čtení na doma

Na konci této lekce už nejspíš máte základní intuici o tom, co to Pandas je a k čemu asi tak slouží. Abychom mohli pokročit dále, je potřeba si některé detaily fungování Pandasu objasnit více do hloubky, čímž předejdeme pozdějšímu zmatení.

### Série

DataFrame není jediná datová struktura, se kterou Pandas pracuje. Už během lekce jsem malinko narazili na takzvané série (anglicky _Series_ ). Sérii si můžeme představit jako seznam hodnot s indexem. Vyrobit sérii není nic těžkého. Mějme například obyčejný seznam značek aut

```pycon
>>> brands = ['subaru', 'toyota', 'honda', 'ford', 'mazda', 'tesla']
```

Z tohoto seznamu velmi snadno vyrobíme sérii

```pycon
>>> sbrands = pandas.Series(brands)
>>> sbrands
0    subaru
1    toyota
2     honda
3      ford
4     mazda
5     tesla
dtype: object
```

Všimněte si, že nám Pandas automaticky vyrobil index. To je jedna z hlavních věcí, které odlišují Série od klasických seznamů. Série má vždy index. Lze si ji tak představit jako jeden sloupeček nějaké tabulky.

Pokud by se nám při výrobě série nelíbil automaticky generovaný index, můžeme si specifikovat index vlastní. Dejme tomu, že bychom chtěli číslovat od jedničky místo od nuly.

```pycon
>>> sbrands = pandas.Series(brands, [1, 2, 3, 4, 5, 6])
>>> sbrands
1    subaru
2    toyota
3     honda
4      ford
5     mazda
6     tesla
dtype: object
```

Můžeme samozřejmě specifikovat i jiný index než číselný.

```pycon
>>> sbrands = pandas.Series(brands, ['a', 'b', 'c', 'd', 'e', 'f'])
>>> sbrands
a    subaru
b    toyota
c     honda
d      ford
e     mazda
f     tesla
dtype: object
```

Dokonce můžeme sérii vyrobit přímo ze slovníku.

```pycon
>>> sbrands = pandas.Series({
...   'a': 'subaru',
...   'b': 'toyota',
...   'c': 'honda',
...   'd': 'ford',
...   'e': 'mazda',
...   'f': 'tesla'
... })
```

K přístupu k prvkům série můžeme použít notaci, kterou jsem zvyklí používat na seznamech.

```pycon
>>> sbrands[1]
'toyota'
```

U sérií však také funguje přístup skrze index.

```pycon
>>> sbrands['b']
'toyota'
```

### Série v DataFrame

Série však nemusíme vyrábět přímo od píky tak jako výše. Častěji získáme sérii tak, že si vytáhneme sloupeček z nějakého DataFrame. Vezměme například naši tabulku s údaji o českých městech. Schválně ji načteme do DataFrame tak, aby indexem byly názvy měst.

```pycon
>>> mesta = pandas.read_csv('mesta.csv', index_col='mesto')
```

Každý sloupeček této tabulky pak můžeme získat jako sérii. Zkusme to například se sloupečkem `linky`.

```pycon
>>> mesta['linky']
mesto
brno        22
liberec      6
litvinov     5
most         5
olomouc      7
ostrava     15
plzen        3
praha       24
Name: linky, dtype: int64
```

Stejně jako u DataFrame, indexem v naší sérii jsou názvy měst.

### Aritmetika se sériemi

Jak už nejspíš tušíte, série jsou mnohem mocnější než obyčejné Python seznamy a můžeme nad nimi podnikat spoustu šikovných operací, které u seznamů nefungují.

Série můžeme sčítat, odčítat, násobit, dělit úplně stejně, jako by to byla čísla.

```pycon
>>> mesta['linky'] + mesta['linky']
mesto
brno        44
liberec     12
litvinov    10
most        10
olomouc     14
ostrava     30
plzen        6
praha       48
Name: linky, dtype: int64
```

Sami si můžete vyzkoušet ostatní operátory. Operace fungují také mezi sérií a číslem.

```pycon
>>> mesta['linky'] * 3
mesto
brno        66
liberec     18
litvinov    15
most        15
olomouc     21
ostrava     45
plzen        9
praha       72
Name: linky, dtype: int64
```

### Porovnávání sérií

Série můžeme také provnávat. Zkusme například takovýto výraz

```pycon
>>> mesta['linky'] > 10
mesto
brno         True
liberec     False
litvinov    False
most        False
olomouc     False
ostrava      True
plzen       False
praha        True
Name: linky, dtype: bool
```

Všimněte si, že výsledkem porovnání série s číslem je nová série, která obsahuje pravdivostní hodnoty. Ty jsou `True` právě tam, kde je porovnání splněno.

Pravdivostní série jsou velmi zajimavá zvířátka. Můžeme je kombinovat pomocí operátorů `&` (a zároveň), `|` (nebo), `~` (negace). Můžeme tedy napsat něco podobného, co jsme již v této lekci viděli.

```pycon
>>> (mesta['linky'] > 10) & (mesta['linky'] < 20)
mesto
brno        False
liberec     False
litvinov    False
most        False
olomouc     False
ostrava      True
plzen       False
praha       False
Name: linky, dtype: bool
```

Ten nejpřekvapivější trik je, že pomocí pravdivostních sérií můžeme také vyhledávat v DataFramech. Nejdříve si uložme výsledek našeho výpočtu do proměnné

```pycon
>>> query = (mesta['linky'] > 10) & (mesta['linky'] < 20)
```

Tato proměnná nyní obsahuje pravdivostní sérii. Můžeme tedy dále psát

```pycon
>>> mesta[query]
        kraj obyvatel  linky  vymera
mesto
ostrava  MSK  290 450     15  214.23
```

Tento příklad vnáší jasnější porozumění do toho, proč fungují vyhledávací výrazy jako tento:

```pycon
>>> mesta[(mesta['linky'] > 10) & (mesta['linky'] < 20)]
```

### Metody na sériích

Série mají opravdu úctyhodné množství metod. Najdeme zde mimo jiné nám už známé metody `loc` a `iloc`, které fungují stejně jako na DataFrame. Další užitečná metoda je například metoda `mean`, která spočítá průměr z hodnot v sérii.

```pycon
>>> mesta['linky'].mean()
10.875
```

Další šikovné metody mohou být například `min` a `max`, které najdou nejmenší a největší hodnotu. Ty se pak dají s výhodou použít k různým dotazům. Zkusme například zjistit, které město má nejvíce tramvajových linek.

```pycon
>>> mesta[mesta['linky'] == mesta['linky'].max()]
      kraj   obyvatel  linky  vymera
mesto
praha  PHA  1 294 513     24   496.0
```

Tímto výčet metod na sériích rozhodně nekončí. Pokud vás zajímá, jaké všechny metody lze na sériích použít, můžete nahlédnout do [oficiální dokumentace pandasu](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html).
