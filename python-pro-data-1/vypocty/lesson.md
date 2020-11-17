## Transformace dat v Pandasu

Vytváření vlastních funkcí jsme si nevysvětlovali jen tak nazdařbůh. Naše nové schopnosti ihned využijeme při práci s daty. Často se nám totiž stane, že data nejsou v tak úplně dokonalém formátu, jak by se nám hodilo a musíme si je trošku pomasírovat, nebo-li odborně řečeno transformovat.

Uvažme jakéhosi Kristiána, jenž se snaží o zhubnutí do svého obleku, který má ještě z tanečních na střední škole. Náš Kristián se rozhodl po 14 dní zdravěji jíst a chodit pravidelně běhat. Své úsilí si poctivě zaznamenával do následující tabulky.

| den    | váha    | běh   | týden |
| ------ | ------- | ----- | ----- |
| pá 3.  | 75,6 kg | 3 km  | 1     |
| so 4.  | 75,3 kh | pauza | 1     |
| ne 5.  | 75,9kg  | pauza | 1     |
| po 6.  | 76,1 kg | 2 km  | 1     |
| út 7   | 75,4 kg | paza  | 1     |
| st 8.  | 75kg    | pauza | 1     |
| čt 9.  | 74,9 kg | 3     | 1     |
| pá 10. | 74,8 k  | pauza | 2     |
| so 11. | 74,3kg  | 3 km  | 2     |
| ne 12  | 75,2 kg | 4 km  | 2     |
| po 13. | 74,5 kg |       | 2     |
| út 14. | 74,2 kg | pauza | 2     |
| st 15. | 74,1 kg | 3 km  | 2     |
| čt 16  | 73,8 kg | 3km   | 2     |

Tabulku si můžete stáhnout jako soubor [vaha.txt](assets/vaha.txt). Bohužel Kristián není ten úplně nejvíc nejdůslednější člověk na planetě, takže hodnoty v druhém a třetím sloupečku nejsou vždy úplně konzistentní, hemží se to zde překlepy i občasnou chybějící hodnotou. Váha je řetězec, který nejen obsahuje i jednotky, ale navíc jsou desetinná čísla zapsána pomocí čárky. Navíc jsou hodnoty v tomto souboru jsou odděleny tabulátory, což svědčí o tom, že je Kristián asi vykopíroval přímo z Excelu nebo Google docs.

V dnešní lekci už nebudeme pracovat v příkazové řádce, ale napíšeme si regulérní program. Nejprve načteme naše data do DataFrame. Pozor na to, že oddělovače jsou tabulátory.

```py
import pandas
vaha = pandas.read_csv('vaha.txt', encoding='utf-8', sep='\t')
```

Můžeme si všimnout, že ani v prvních sloupečku, kde naštěstí žádné překlepy nemáme, nejsou data úplně v šikovném formátu. Datumy máme jako jméno a číslo dne. To je první věc, kterou se pokusíme napravit.

Ty nejužitečnější operace pro transformaci dat najdeme na sériích. Vezměme si první sloupeček naší tabulky jako sérii. Pomocí vlastnosti `.str` můžeme pracovat se sérií řetězců úplně stejně, jako pracujeme s jedním řetězcem. Můžeme se tak například zbavit zbytečných názvů dní.

```py
cisloDne = vaha['den'].str[3:]
print(cisloDne)
```

```pycon
0      3.
1      4.
2      5.
3      6.
4       7
5      8.
6      9.
7     10.
8     11.
9      12
10    13.
11    14.
12    15.
13     16
Name: den, dtype: object
```

Pokud chceme smazat otravné tečký na konci tak, rozsahy už nám nepomohou
protože na některých místech tečka chybí. Můžeme ale použít metody `replace` a
tečky nahradit prázdným řetězcem.

```py
cisloDne = vaha['den'].str[3:].str.replace('.', '')
print(cisloDne)
```

```pycon
0      3
1      4
2      5
3      6
4      7
5      8
6      9
7     10
8     11
9     12
10    13
11    14
12    15
13    16
Name: den, dtype: object
```

Všimněte si ale, že hodnoty v sérii `cisloDne` jsou pořád řetězce. Chceme-li je převést na čísla, musíme použít Pandas funkci `to_numeric`.

```pycon
cisloDne = vaha['den'].str[3:].str.replace('.', '')
cisloDne = pandas.to_numeric(cisloDne)
print(cisloDne)
```

```pycon
0      3
1      4
2      5
3      6
4      7
5      8
6      9
7     10
8     11
9     12
10    13
11    14
12    15
13    16
Name: den, dtype: int64
```

Takto máme sloupeček hezky vyčištěný. Zapojme ho jako nový sloupeček do naší tabulky. Zároveň ještě nahradíme sloupeček se dny pouze jejich názvy. Tím bude tabulka mnohem přehlednější.

```py
den = vaha['den'].str[:3]
vaha['číslo dne'] = cisloDne
vaha['den'] = den
print(vaha)
```

```pycon
    den     váha    běh  týden  číslo dne
0   pá   75,6 kg   3 km      1          3
1   so   75,3 kh  pauza      1          4
2   ne    75,9kg  pauza      1          5
3   po   76,1 kg   2 km      1          6
4   út   75,4 kg   paza      1          7
5   st      75kg  pauza      1          8
6   čt   74,9 kg      3      1          9
7   pá    74,8 k  pauza      2         10
8   so    74,3kg   3 km      2         11
9   ne   75,2 kg   4 km      2         12
10  po   74,5 kg    NaN      2         13
11  út   74,2 kg  pauza      2         14
12  st   74,1 kg   3 km      2         15
13  čt   73,8 kg    3km      2         16
```

## Chroustání sérií

První sloupeček naší tabulky byl ještě relativně snadný. S druhým to bude o dost těžší. Data nejsou moc konzistentní a dostat je do rozumné podoby znamená řešit různé speciální případy pomocí různých podmínek. S takovou situací se v praxi potkáme poměrně často. Data často přicházejí v různých podobách a na nás je umět je převést do takového formátu, se kterým zvládneme pracovat.

Pojďme nedjříve vyzkoumat, jakým nejjednodušším způsobem můžeme sloupeček s váhou transformovat. Po notné chvíli zírání do monitoru možná objevíme následující postup:

<i>Pokud se nám podaří rozdělit hodnotu podle mezery, můžeme první část převést na číslo. Pokud se to nepovede, můžeme dělit podle písmenka`'k'`.</i>

To už je relativně komplexní postup, který je výhodné zapsat jako funkci.

```py
def kilogramy(vstup):
  casti = vstup.split(' ')
  if len(casti) < 2:
    casti = vstup.split('k')

  return float(casti[0].replace(',', '.'))
```

Nyní jsme připravení tuto funkci vypustit na naše data. K tomu použijeme metodu na sériích s názvem `apply`. Tato metoda očekává jako vstup nějakou funkci. Tuto funkci pak spustí na každou jednotlivou položku série a ze získaných výsledků vyrobí novou sérii. Pokud vám tento postup připomíná chroustání seznamů, trefili jste do černého. Pojďme si tento postup vyzkoušet s naší novou funkcí.

```pycon
vaha['váha'] = vaha['váha'].apply(kilogramy)
print(vaha)
```

```pycon
    den  váha    běh  týden  číslo dne
0   pá   75.6   3 km      1          3
1   so   75.3  pauza      1          4
2   ne   75.9  pauza      1          5
3   po   76.1   2 km      1          6
4   út   75.4   paza      1          7
5   st   75.0  pauza      1          8
6   čt   74.9      3      1          9
7   pá   74.8  pauza      2         10
8   so   74.3   3 km      2         11
9   ne   75.2   4 km      2         12
10  po   74.5    NaN      2         13
11  út   74.2  pauza      2         14
12  st   74.1   3 km      2         15
13  čt   73.8    3km      2         16
```

Nádhera! Naše data jsou nyní mnohem učesanější a můžeme je začít vyhodnocovat na mnoho roztodivných způsobů. Sice nám ještě chybí vyčistit sloupeček obsahující uběhnuté kilometry, ale to jistě zvládnete jako cvičení.

## Vlastní agregační funkce

Naše dnešní povídání o Pandasu završíme tím, že si vytvoříme vlastní agregační funkci. Agregace pomocí vestavěných funkcí jako je součet, průměr, rozptyl apod. už jsme viděli. Takto bychom například mohli spočítat průměr váhy za každý týden zvlášť.

```py
print(vaha.groupby('týden')['váha'].mean())
```

```pycon
Name: den, dtype: object
týden
1    75.457143
2    74.414286
Name: váha, dtype: float64
```

V reálném světě tam venku se nám však snadno může stát, že budeme potřebovat agregovat data nějakým složitějším způsobem nebo prostě způsobem, který v sobě Pandas nemá přímo zabudovaný. Uvažme například situaci, kdy chceme spočítat takzvané rozpětí váhy za každý týden. Rozpětí je rozdíl mezi minimální a maximální hodnotou. Takovouto agregační funkci Pandas přímo nenabízí. Musíme si ji napsat sami.

Agregační funkce si píší tak, že na vstupu obdrží sérii a jejich výstupem je agregovaná hodnota. Naše funkce pro rozpětí tak bude vypadat celkem jednoduše.

```py
def spread(serie):
  return serie.max() - serie.min()
```

Nyní stačí tuto funci předat metodě `agg`. Tuto metodu můžeme volat na jednotlivých sériích. Zjistěme například rozpětí všech vah za celých 14 dní.

```py
print(vaha['váha'].agg(spread))
```

```pycon
2.299999999999997
```

Mnohem mocnější jsou však agregace při grupování. Naše funkce `spread` se tak zavolá na každou skupinu, která grupováním vznikne. Můžeme tedy rovnou spočítat rozpětí váhy v jednotlivých týdnech.

```py
print(vaha.groupby('týden')['váha'].agg(spread))
```

```pycon
týden
1    1.2
2    1.4
Name: váha, dtype: float64
```