V předchozí lekci jsme si ukázali, jak se v Pandasu vytvoří DataFrame a jak z něj můžeme vybírat data pomocí různých způsobů dotazování. Nyní se posuneme o kus dále a ukážeme si, jak můžeme s DataFramy dělat složitější operace jako je filtrování chybějících hodnot, spojování a agregace.

## Maturita

Abychom měli nějaký praktický příklad k procvičování, použijeme fiktivní data z výsledků maturitních zkoušek během jednoho týdne na nějakém menším gymnáziu. Maturita se odehrává ve třech místnostech: U202, U203 a U302. Máme tedy tři tabulky dat, z každé místnosti jednu. Níže si můžete prohlédnout příklad tabulky z místnosti U202. Všechny tabulky jsou ke stažení zde: [u202.csv](assets/u202.csv), [u203.csv](assets/u203.csv), [u302.csv](assets/u302.csv).

| jméno             | předmět          | známka | den |
| ----------------- | ---------------- | ------ | --- |
| Jana Zbořilová    | Chemie           |        | pá  |
| Lukáš Jurčík      | Dějepis          | 3      | pá  |
| Pavel Horák       | Matematika       | 2      | út  |
| Lukáš Jurčík      | Společenské vědy | 2      | pá  |
| Pavel Kysilka     | Biologie         | 1      | pá  |
| Kateřina Novotná  | Dějepis          | 1      | po  |
| Marie Krejcárková | Fyzika           | 2      | čt  |
| Vasil Lácha       | Dějepis          | 4      | po  |
| Alexey Opatrný    | Matematika       | 2      | po  |
| Petr Valenta      | Dějepis          |        | pá  |
| Miroslav Bednář   | Chemie           | 2      | st  |
| Pavel Horák       | Chemie           | 5      | út  |
| Ivana Dvořáková   | Matematika       | 1      | st  |
| Lenka Jarošová    | Biologie         | 4      | st  |
| Miroslav Bednář   | Dějepis          | 5      | st  |

## Práce s chybějícími hodnotami

V praxi se poměrně často setkáme s tím, že v datovém setu některé hodnoty chybí. Můžeme si například všimnout, že v tabulce U202 dvěma studentům chybí známka. To může znamenat, že se doma hrůzou zhroutili a na maturitu ani nedorazili. Na takové případy je třeba být připraven.

V Pandasu, ale i obecně v datové analýze, je možné se s chybějícími daty vypořádat různými způsoby:

1. Nahradit je za jiné výchozí hodnoty.
1. Odstranit všechny řádky s chybějícími daty z datového setu.
1. Vyčlenit je do separátního datasetu a zpracovat je zvlášť.

Načtěme si naši první tabulku jako DataFrame.

```pycon
>>> import pandas
>>> u202 = pandas.read_csv('u202.csv', encoding='utf-8')
```

Pokud Pandas narazí na prázdnou buňku, vloží místo ní do tabulky speciální hodnotu `NaN` (z anglického <i>Not a Number</i> ). Jakmile tyto speciální hodnoty v našem DataFrame objevíme, můžeme použít několik různých metod.

Série obsahují metodu `isnull`, která vrátí pravdivostní sérii s hodnotou `True` všude tam, kde v původní sérii chybí hodnota. Metoda `notnull` pracuje přesně opačně. Vrátí pravdivostní sérii s hodnotami `True` všude tam, kde v původní sérii hodnota nechybí.

```pycon
>>> u202['známka'].isnull()
0      True
1     False
2     False
3     False
4     False
5     False
6     False
7     False
8     False
9      True
10    False
11    False
12    False
13    False
14    False
Name: známka, dtype: bool
```

Tyto metody můžeme využít například k tomu, abychom získali všechna data, kde chybí hodnota ve sloupečku <i>známka</i>.

```pycon
>>> u202[u202['známka'].isnull()]
            jméno  předmět  známka den
0  Jana Zbořilová   Chemie     NaN  pá
9    Petr Valenta  Dějepis     NaN  pá
```

Další užitečné metody na práci s chybějícími hodnotami najdeme na DataFrame.

1. `dropna()` \- vrátí datový set očištěn od chybějících dat
1. `dropna(ax`is=1) - odstraní všechny sloupce, které obsahují chybějící data
1. `fillna(x)` \- nahradí všechna chybějící data a hodnoty hodnotou x

## Spojení dat

Nyní bychom chtěli všechny tři naše tabulky spojit do jedné. Nejdříve si každou z nich načteme do samostatného DataFrame s tím, že vyhodíme studenty, kteří na maturitu nedorazili..

```pycon
>>> u202 = pandas.read_csv('u202.csv', encoding='utf-8').dropna()
>>> u203 = pandas.read_csv('u203.csv', encoding='utf-8').dropna()
>>> u302 = pandas.read_csv('u302.csv', encoding='utf-8').dropna()
```

Pokud chceme tyto tři DataFrame spojit do jednoho, můžeme použít funkci `concat`

```pycon
>>> maturita = pandas.concat([u202, u203, u302])
```

Pozor ale na to, že v takto vzniklém DataFrame se nám rozbije index, protože se prostě spojí za sebe indexy jednotlivých tabulek. Pokud chceme, aby Pandas při spojování index přepočítal, musíme napsat

```pycon
>>> maturita = pandas.concat([u202, u203, u302], ignore_index=True)
```

To už je lepší. Stále nám však zůstává jeden problém. Po spojení tabulek do jedné už nevíme, kdo maturoval v jaké místnosti. Tuto informaci si proto doplníme do původních tří tabulek jako nový sloupeček. Až poté tabulky spojíme do jedné.

```pycon
>>> u202['místnost'] = 'u202'
>>> u203['místnost'] = 'u203'
>>> u302['místnost'] = 'u302'
>>> maturita = pandas.concat([u202, u203, u302], ignore_index=True)
```

Takto už nám vznikla pěkná vyčištěná tabulka. Uložme si ji do CSV, ať ji nemusíme vyrábět pořád znova. Nebudeme ukládat index, protože ten si vždycky necháme vyrobit automaticky.

```pycon
>>> maturita.to_csv('maturita.csv', index=False)
```

Výslednou tabulku si můžete stáhnout jako soubor [maturita.csv](assets/maturita.csv).

## Joinování dat

Už jsme si ukázali, jak v Pandase spojovat tabulky za sebe, což v SQL odpovídá příkazu UNION. Pandas však umí DataFrame také mergovat, což odpovídá SQL příkazu JOIN. Abychom si tento postup mohli předvést, nečteme si tabulku, která uvádí, kdo v který den předsedal maturitní zkoušecí komisi.

| den | datum     | jméno            |
| --- | --------- | ---------------- |
| po  | 20.5.2019 | Marie Zuzaňáková |
| út  | 21.5.2019 | Marie Zuzaňáková |
| st  | 22.5.2019 | Petr Ortinský    |
| čt  | 23.5.2019 | Petr Ortinský    |
| pá  | 24.5.2019 | Alena Pniáčková  |

Data si můžete stáhnout jako soubor [predsedajici.csv](assets/predsedajici.csv). Načtěme si jej jako DataFrame.

```pycon
>>> preds = pandas.read_csv('predsedajici.csv', encoding='utf-8')
```

Join tabulek se v Pandase dělá pomocí funkce `merge`. Nejprve ji otestujme pouze na datech z prvni mistnosti.

```pycon
>>> test = pandas.merge(u202, preds)
```

Takto na poprvé se však s úspěchem nesetkáme, neboť výsledkem příkazu bude prázdný DataFrame. Důvod je ten, že metoda `merge` dělá ve výchozím nastavení INNER JOIN podle všech sloupečků, které mají stejná jména. Naše dvě tabulky se tedy spojí podle sloupečků <i>jméno</i> a <i>den</i>. Tyto dva sloupečky ale nemají pro žádný řádek v obou tabulkách stejnou hodnotu, takže nám ve výsledku žádný řádek nezbude.

Můžeme být neoblomná a zaexperimentovat s OUTER JOIN

```pycon
>>> test = pandas.merge(u202, preds, how='outer')
```

Takto nám ale ve výsledku vznikne ohromné množství nedefinovaných hodnot. Co doopravdy potřebujeme je joinovat pouze podle sloupečku <i>den</i> , což zařídíme takto

```pycon
>>> test = pandas.merge(u202, preds, on=['den'])
>>> test.head()
         jméno_x           předmět  známka den mistnost      datum           jméno_y
0   Lukáš Jurčík           Dějepis     3.0  pá     u202  24.5.2019   Alena Pniáčková
1   Lukáš Jurčík  Společenské vědy     2.0  pá     u202  24.5.2019   Alena Pniáčková
2  Pavel Kysilka          Biologie     1.0  pá     u202  24.5.2019   Alena Pniáčková
3    Pavel Horák        Matematika     2.0  út     u202  21.5.2019  Marie Zuzaňáková
4    Pavel Horák            Chemie     5.0  út     u202  21.5.2019  Marie Zuzaňáková
```

Potíž je v tom, že se teď oba sloupečky <i>jméno</i> automaticky přejmenovaly, aby neměly v tabulce stejný název. Zde můžeme použít metodu `rename`, abychom sloupečky přejmenovali na něco smysluplného.

```pycon
test = test.rename(columns={'jméno_x': 'jméno', 'jméno_y': 'předs'})
```

Nyní už tabulka vypadá hezky. Proveďme tedy totéž pro celý náš maturitní dataset a opět si jej uložme do souboru, ať jej máme vždy po ruce.

```pycon
>>> maturita2 = pandas.merge(maturita, preds, on=['den'])
>>> maturita2 = maturita2.rename(columns={'jméno_x': 'jméno', 'jméno_y': 'předs'})
>>> maturita2.to_csv('maturita2.csv', index=False)
```

Výslednou tabulku si opět můžete stáhnout jako soubor [maturita2.csv](assets/maturita2.csv).

## Grupování

Z databází známe kromě UNION a JOIN také operaci GROUP BY. V Pandase ji provedeme tak, že pomocí metody <i>groupby</i> vyrobíme z DataFrame speciální objekt `DataFrameGroupBy`. Dejme tomu, že chceme grupovat podle sloupečku <i>místnost</i>.

```pycon
>>> maturita2.groupby('místnost')
<pandas.core.groupby.generic.DataFrameGroupBy object at 0x7f96153a1cf8>
```

Na tomto speciálním objektu pak můžeme používat různé agregační funkce. Nejjednodušší je funkce `count`

```pycon
>>> maturita2.groupby('místnost').count()
          jméno  předmět  známka  den  datum  předs
místnost
u202         13       13      13   13     13     13
u203         13       13      13   13     13     13
u302         12       12      12   12     12     12
```

Další užitečné agregační funkce jsou například

- `sum` \- součet hodnot
- `max` \- maximální hodnota
- `min` \- minimální hodnota
- `first` \- první hodnota
- `last` \- poslední hodnota
- `mean` \- průměr z hodnot
- `median` \- medián z hodnot
- `var` \- rozptyl hodnot
- `std` \- standardní odchylka hodnot
- `all` \- `True`, pokud jsou všechny hodnoty `True`
- `any` \- `True`, pokud je alespoň jedna z hodnot `True`

Nemusíme samozřejmě grupovat přes všechny sloupečky. Vybereme si pouze ty, které nás zajímají. Zkusme například spočítat průměrnou známku z jednotlivých předmětů.

```pycon
>>> maturita2.groupby('předmět')['známka'].mean()
```

Všimněte si, že takto obdržíme sérii, nikoliv DataFrame. Pozornější z vás možná tuší, že abychom získali DataFrame, musíme psát

```pycon
>>> maturita2.groupby('předmět')[['známka']].mean()
```

```pycon
>>> nakupy.groupby("Jméno")["Částka v korunách"].sum()
Jméno
Libor    124
Míša     160
Ondra    500
Pavla     50
Petr     539
Zuzka     80
Name: Částka v korunách, dtype: int64
```
