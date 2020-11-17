V této části si zkusíme napas nějaké základní dotazy na naše data. `pandas` umožňují napsat dotazy podobně jako jazyk SQL, k práci ale jeho znalost vůbec ne potřebujeme.

Tentokrát si vyzkoušíme načíst data ze souboru ve formátu JSON. Konkrétně budeme pracovat s daty o státech světa, která jsou stažená ze služby [restcountries](https://restcountries.eu/). Data si můžeš [stáhnout zde](assets/staty.json). Opět platí, že si je musíš stáhnout do adresáře, kde máš právě otevřený terminál!

## Indexy

Pokud ještě nemáš otevřený Python terminál, otevři si ho. Soubor načteme pomocí funkce `read_json`, kde jako první parametr zadáme název souboru. Data jsou opět vrácena jako `DataFrame` a my si je uložíme do proměnné `staty`. U dat o státech světa však můžeme přidat jedno zlepšení. Víme, že každý stát na světě má svůj název a ten název je **unikátní** a **identifikuje ho**. Můžeme tedy tento název použít jako **index**. 

**K zamyšlení:** Jaký index bychom použili pro tabulku zaměstnanců ve firmě, tabulku obcí České republice a tabulku aut v autopůjčovně?

### Přidání indexu

To, jaký sloupec má být použit jako index, řeší funkce `set_index`. Ta nám vrátí upravený `DataFrame`, který si můžeme uložit do původní proměnné `staty`.

```pycon
>>> import pandas
>>> staty = pandas.read_json("staty.json")
>>> staty = staty.set_index("name")
```

Podívejme se nejprve, jaké informace jsou v naší tabulce obsažené.

```pycon
>>> staty.info()
<class 'pandas.core.frame.DataFrame'>
Index: 250 entries, Afghanistan to Zimbabwe
Data columns (total 6 columns):
 #   Column      Non-Null Count  Dtype
---  ------      --------------  -----
 0   capital     250 non-null    object
 1   region      250 non-null    object
 2   subregion   250 non-null    object
 3   population  250 non-null    int64
 4   area        240 non-null    float64
 5   gini        153 non-null    float64
dtypes: float64(2), int64(1), object(3)
memory usage: 13.7+ KB
```

### Výběr konkrétního a jedné hodnoty

Z názvů sloupců bychom mohli odvodit, jaké informace se v našem `DataFrame` nacházejí, ale možná se zorientujeme lépe, když se podíváme na nějaký konkrétní řádek.

K nalezení řádku pomocí indexu použijeme funkci `loc`, která funguje obdobně jako funkce `iloc`. Oproti ní však primárně používá námi zvolené indexy, zatímco funkce `iloc` pracuje s čísly řádků.

```pycon
>>> staty.loc["Czech Republic"] 
capital               Prague
region                Europe
subregion     Eastern Europe
population          10558524
area                   78865
gini                      26
Name: Czech Republic, dtype: object
```

Opět jsme vybrali jeden řádek, získáme tedy výsledek jako sérii. Můžeme však jít ještě dále a získat jednu konkrétní hodnotu. Funkci `loc` dodáme druhý parametr, který bude obsahovat jméno sloupce, ze kterého chceme hodnotu vybrat. Vyberme si třeba rozlohu, kterou uložíme do proměnné `rozloha`.

```pycon
rozloha = staty.loc["Czech Republic","area"]
```

Pokud by nás zajímaly informace o více řádcích, můžeme opět použít seznam. Index řádků, které nás zajímají, vložíme do seznamu a ten předáme jako první parametr funkci `loc`.

```pycon
>>> staty.loc[["Czech Republic","Slovakia"]] 
                   capital  region       subregion  population     area  gini
name
Czech Republic      Prague  Europe  Eastern Europe    10558524  78865.0  26.0
Slovakia        Bratislava  Europe  Eastern Europe     5426252  49037.0  26.0
```

Pomocí seznamu se můžeme zeptat i na informace z více sloupců. Zkusme si třeba porovnat rozlohu a počet obyvatel České republiky a všech jejích sousedních států.

```pycon
>>> staty.loc[["Slovakia","Poland","Germany","Austria"], ["area","population"]]                  
              area  population
name
Slovakia   49037.0     5426252
Poland    312679.0    38437239
Germany   357114.0    81770900
Austria    83871.0     8725931
```

## Dotazy

Nyní si vyzkoušíme jednu z hlavních prací datového analytika, a to je **psaní dotazů**. Logika psaní dotazů je v různých prostředích stejná, liší se pouze to, jak ji provádíme. Podívejme se na konkrétní příklady.

### Výběr sloupců

Již jsme si říkali, že ne vždy nás zajímají všechna data. Sloupce již umíme vybrat pomocí funkce `loc`. Funkce `loc` je praktická, pokud vybíráme konkrétní řádky a k nim nějaké konkrétní sloupce. Pokud ale chceme vybrat jen sloupec a zachovat všechny řádky, zpravidla použijeme výběr sloupců pomocí hranatých závorek. Zápis připomíná práci se seznamy - hranatou závorku napíšeme přímo za název proměnné, kde máme uložený `DataFrame`, a do ní vepíšeme název sloupce, který nás zajímá.

```pycon
>>> staty["population"]
```

Pokud nás zajímá více sloupců, můžeme opět použít seznam, do kterého sloupce vepíšeme.

```pycon
>>> staty[["population", "area"]] 
```

### Co vlastně umí série

Asi se teď říkáš, k čemu je to vlastně dobré. Zkusme si jednoduchý příklad: Chceme zjistit, kolik lidí žije ve všech státech světa. Bude nás tedy zajímat pouze sloupec `population`, kde máme sérii s počty obavytel jednotlivých států. Série sama o sobě umí zajímavé věci, například umí sama spočítat svůj součet a vrátit výsledek jako číslo. K tomu slouží funkce `sum`. K jejímu volání opět použijeme tečkovou notaci.

```pycon
>>> populace = staty["population"]      
>>> populace.sum()
7349137231
```

Oba kroky můžeme spojit do jednoho.

```pycon
>>> staty["population"].sum()
7349137231
```

Série umí spočítat řadu dalších věcí, jako třeba průměr (funkce `mean`), minimum a maximum (funkce `min` a `max`) nebo medián (funkce `median`). Přehled všech funkcí najdeš [v dokumentaci](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html).

### Podmínky (ano, už zase)

V datové analýze podmínkám rozhodně neutečeš. Podmínky jsou velmi užitečné, protože bez nich bychom museli pracovat se všemi daty, co jsme dostali, což není vždy žádoucí.

- Data často obsahují chyby, která vzniknou třeba špatným nastavením stroje nebo překlepem pracovníka, který je zadával. Pokud bychom chyby nechali v datech a dále s nimi pracovali, udělaly by nám tam pěknou paseku.
- Často cheme zpracovat jen část dat. Pokud máme například firmu s obchůdky v několika městech, můžeme chtít zpracovat jen data z jednoho města, pro nějaké konkrétní zboží nebo časové období.

V jazyce SQL píšeme podmínky za klíčové slovo `WHERE`, v Excelu můžeme použít funkce Filtr atd. V `pandas` používáme funkci `query`. Název této funkce si ale pamatovat nemusíš, protože namísto ní opět můžeme použít hranaté závorky.

 Začněme s tím, že se podíváme na nejmenší státy, které na světě jsou. Nechme si například vypsat státy, které mají méně než 1000 obyvatel. Postup si vysvětlíme ve dvou krocích.
 
 Nejprve potřebujeme formulovat podmínku. Ta bude vypadat takto `staty["population"] < 1000`. V podmínce máme sloupec, na který se ptáme, a porovnání s číselnou hodnotou. Používáme nám již známý operátor menší než (`<`). Zkusme si zadat samotnou podmínku do terminálu a podívejme se na výsledek.

```pycon
>>> staty["population"] < 1000     
name
Afghanistan          False
Åland Islands        False
Albania              False
Algeria              False
American Samoa       False
                     ...
Wallis and Futuna    False
Western Sahara       False
Yemen                False
Zambia               False
Zimbabwe             False
Name: population, Length: 250, dtype: bool
```

Pokud si vzpomeneš na hodnoty typu `bool`, víš, že ty mohly nabývat pouze dvou hodnot: `True` a `False`. Při použití operátorů pro porovnávání vždy získáme hodnotu typu `bool`. Pokud bychom například měli proměnnou `znamka` a napsali do terminálu `znamka < 3`, získáme jednu hodnotu `True` nebo `False`, a to podle toho, jakou hodnotu v proměnné `znamka` máme.

My v naší tabulce ale máme 250 států s různými počty obyvatel, proto nám náš dotaz vrací 250 hodnot, z nichž některé jsou `True` a některé `False`. Vytvořili jsme tedy jakýsi polotovar. My nyní chceme vidět jen ty řádku, kde máme hodnotu `True`, což nám dá státy s počtem obyvatel menší než 1000. K tomu využijeme poměrně zvláštní zápis - naši podmínku vložíme do hranatých závorek.

```pycon
>>> pidistaty = staty[staty["population"] < 1000]
>>> pidistaty[["population", "area"]]  
                                              population     area
name
Bouvet Island                                          0    49.00
United States Minor Outlying Islands                 300      NaN
Cocos (Keeling) Islands                              550    14.00
French Southern Territories                          140  7747.00
Heard Island and McDonald Islands                      0   412.00
Holy See                                             451     0.44
Pitcairn                                              56    47.00
South Georgia and the South Sandwich Islands          30      NaN
```

Tento podivný zápis má ve skutečnosti svoji logiku. My jsme v našem polotovaru získali sloupec, kde máme 250 hodnotu typu `bool`. `pandas` teď jednoduše udělají to, že vypíšou ty řádky řádky, kde má náš polotovar hodnotu `True` a ty, které mají hodnotu `False`, před námi skryjí.

V tabulce vidíme několik států a kromě Holy See (tj. Vatikánu) jsme o nich asi ani nikdy neslyšeli. V některých řádcích vidíme hodnotu `NaN`. To značí, že pro daný řádek hodnotu nemáme, pro některé státy tedy nemáme zadanou rozlohu. Měli bychom si tedy rozmyslet, zda s takovými státy v nějaké analýze vůbec pracovat.

### Spojení více podmínek

Často narazíme na případ, kdy chceme zkombinovat více podmínek, například chceme tržby v jedné prodejně a pro letošní rok. Při kombinaci se musíme rozhodnout, zda chceme, aby ke zobrazení řádku byly splněné obě, nebo zda stačí, aby byla splněna pouze jedna z nich (jde o princip používaný při [vícenásobných podminkách](http://nove.kodim.cz/czechitas/progr2-python/zaklady-programovani-2/podminky-2)).

Pokud chceme, aby musely být splněny obě podmínky, vložíme mezi ně symbol `&`. Uvažujme dvě podmínky:

- Stát musí mít alespoň 20 milionů obyvatel: `(staty["population"] > 20000000)`
- Stát se musí nacházev v Evropě: `staty["region"] == "Europe")`

Obě tyto podmínky napíšeme do závorek a vložíme mezi ně symbol `&`. Následně použijeme již známé hranaté závorky, které přidáme hned za proměnnou `staty`.

```pycon
>>> velkeEvropskeStaty = staty[(staty["population"] > 20000000) & (staty["region"] == "Europe")]
>>> velkeEvropskeStaty["population"]                                                            
name
France                                                   66710000
Germany                                                  81770900
Italy                                                    60665551
Poland                                                   38437239
Russian Federation                                      146599183
Spain                                                    46438422
Ukraine                                                  42692393
United Kingdom of Great Britain and Northern Ireland     65110000
Name: population, dtype: int64
```

Pokud chceme, aby stačilo splnění jedné podmínky, použijeme symbol `|`. Zde vypisujeme státy, které leží v západní nebo východní Evropě.

```pycon
>>> staty[(staty["subregion"] == "Western Europe") | (staty["subregion"] == "Eastern Europe")] 
                          capital  region       subregion  population         area  gini
name
Austria                    Vienna  Europe  Western Europe     8725931     83871.00  26.0
Belarus                     Minsk  Europe  Eastern Europe     9498700    207600.00  26.5
Belgium                  Brussels  Europe  Western Europe    11319511     30528.00  33.0
Bulgaria                    Sofia  Europe  Eastern Europe     7153784    110879.00  28.2
Czech Republic             Prague  Europe  Eastern Europe    10558524     78865.00  26.0
France                      Paris  Europe  Western Europe    66710000    640679.00  32.7
Germany                    Berlin  Europe  Western Europe    81770900    357114.00  28.3
Hungary                  Budapest  Europe  Eastern Europe     9823000     93028.00  31.2
Liechtenstein               Vaduz  Europe  Western Europe       37623       160.00   NaN
Luxembourg             Luxembourg  Europe  Western Europe      576200      2586.00  30.8
Moldova (Republic of)    Chișinău  Europe  Eastern Europe     3553100     33846.00  33.0
Monaco                     Monaco  Europe  Western Europe       38400         2.02   NaN
Netherlands             Amsterdam  Europe  Western Europe    17019800     41850.00  30.9
Poland                     Warsaw  Europe  Eastern Europe    38437239    312679.00  34.1
Republic of Kosovo       Pristina  Europe  Eastern Europe     1733842     10908.00   NaN
Romania                 Bucharest  Europe  Eastern Europe    19861408    238391.00  30.0
Russian Federation         Moscow  Europe  Eastern Europe   146599183  17124442.00  40.1
Slovakia               Bratislava  Europe  Eastern Europe     5426252     49037.00  26.0
Switzerland                  Bern  Europe  Western Europe     8341600     41284.00  33.7
Ukraine                      Kiev  Europe  Eastern Europe    42692393    603700.00  26.4
```

## Převody dat na DataFrame a zpět

`DataFrame` nejsou uzavřeným světem, ale umožňují snadný převod na seznamy, případně můžeme naopak převést seznam na `DataFrame`.

### Převod DataFrame na seznam

K takovému převodu na seznam nám poslouží kombinace funkcí `to_numpy` a `tolist`. Převod totiž neprovádíme přímo, ale jako mezikrok jej převedeme na pole modulu `numpy`.

```pycon
>>> statyList = staty.to_numpy().tolist() 
>>> statyList[0] 
['Kabul', 'Asia', 'Southern Asia', 27657145, 652230.0, 27.8]
```

Ve výsledných seznamech nám chybí názvy států. Potíž je v tom, že index se v Pandasu nebere jako součást dat. Pokud chceme index vrátit do původního stavu a mít ho jako automaticky generovaná čísla řádků, můžeme použít metodu `reset_index`. S její pomocí pak už dokážeme dostat z DataFramu čistá data takto

```pycon
>>> statyList = staty.reset_index().to_numpy().tolist() 
>>> statyList[0]
['Afghanistan', 'Kabul', 'Asia', 'Southern Asia', 27657145, 652230.0, 27.8]
```

### Vytvoření DataFrame ze seznamu

Zkusme si nyní opačný postup, převedeme si seznam seznamů (což je jiný zápis dvourozměrné tabulky) na `DataFrame`. Jistě si vzpomínáš na příklad se známkami z testu, kterým jsme měli na prvním workshopu.

```pycon
znamky = [
  ['Petr', 2],
  ['Roman', 1],
  ['Jitka', 3],
  ['Zuzana', 5],
  ['Ondřej', 2],
  ['Julie', 2],
  ['Karel', 4],
  ['Anna', 1],
  ['Eva', 1]
]
```

Naším úkolem bylo spočítat průměrnou známku. K tomu jsme použili cyklus.

```py
soucet = 0
for radek in znamky:
  soucet = soucet + radek[1]
prumer = soucet / len(znamky)
```

Průměrnou známku ale můžeme spočítat i pomocí `pandas`. Pomocí funkce `DataFrame` převedeme proměnnou `znamky` na `DataFrame`. Abychom měli v `DataFrame` správné názvy sloupců, definujeme je jako parametr `columns`.

Následně vybereme data ve sloupci `znamka`. Protože jsme vybrali jeden sloupec, získáme sérii. Průměrnou hodnotu v sérii pak spočítáme pomocí funkce `mean`.

```pycon
>>> znamky = pandas.DataFrame(znamky, columns=['student', 'znamka'])
>>> prumer = znamky["znamka"].mean()
```

### Čtení na doma: Vytvoření DataFrame ze seznamu slovníků

Pokud jsi absolvovala Úvod do programování v Pythonu 2, znáš již též slovníky. I pole složené ze slovníků můžeme převést na `DataFrame`.

```pycon
nakupy = [
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

Výhodou je, že nyní nemusíme přidávat názvy sloupců, protože ty už funkce `DataFrame` získá z klíčů slovníků.

```pycon
>>> nakupy = pandas.DataFrame(purchaseList)
>>> nakupy.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 11 entries, 0 to 10
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   person  11 non-null     object
 1   item    11 non-null     object
 2   value   11 non-null     int64
dtypes: int64(1), object(2)
memory usage: 392.0+ bytes
```
