Regulární výrazy jsou v podstatě malí "kouzelníci", kteří nám umožní vytáhnout z textu důležitá data. Často například dostaneme celou adresu jako jeden řetězec, například jako "Václavské nám. 837/11, 110 00 Nové Město" a my potřebujeme z adresy vytáhnout poštovní směrovací číslo, abychom zhruba věděli, kde se dané místo nachází.

O poštovním směrovacím čísle víme, že je složeno z pěti číslic a většinou (ale ne vždy) ho zapisujeme s mezerou mezi třetím a čtvrtém čísle. Potřebujeme tedy nějak obecně říct, že máme z textu vybrat pětici čísel, která může mít mezi třetím a čtvrtým číslem mezeru.

## Jak fungují regulární výrazy

Regulární výrazy umožňují používání symbolů, které mohou zastoupit nějaký znak (nebo více znaků). Fungují podobně jako třeba žolík v karetní hře nebo hvězdička ve vyhledávání souborů, umoňují ale přesněji specifikovat, co vlastně zastupují. Práci s regulárními výrazy si můžeme pohodlně trénovat například v aplikaci [Regular Expressions 101](https://regex101.com/). Do pole "Regular Expression" zadáváme reguálrní výraz a do pole "Text String" řetězec, se kterým pracujeme. Aplikace nám interaktivně podbarvuje části textu, které odpovídají našemu výrazu. Protože regulární výrazy se v různých programovacích jazycích mírně liší, měli bychom si vlevo v části "Flavor" přepnout na Python.

Oněm magickým znakům říkáme *metaznaky*. 

Zkusme si to na příkladu tečky `.`. Tečka zastupuje **právě jeden** libovolný znak. Ta skutečně odpovídá právě "žolíku". Pokud tedy budeme pracovat s řetězecem `"A23456789JQKA"` a zadáme regulární výraz `"78.JQK"`, podbarví se nám část řetězce od `7` do `J`.

Vyzkoušejme si nyní upravit program, který bude sledovat vývoj kurzu měn ve Směnárně Na Růžku, aby nám například poslal upozornění ve chvíli, kdy má nějaká měna výhodný kurz. Náš program zatím umí stáhnout informace do následující řetězce.

Pokud chceme, aby náš metaznak zastupoval jeden ze skupiny znaků, vložíme tyto znaky do hranatých závorek `[ ]`. Například pokud chceme v kurzovním lístku vyhledat řádky, které mají v sobě znak dolaru nebo eura, napíšeme `1 [€$]`.

```
Vítejte ve Směnárně Na Růžku!
Kurzy měn pro 19. 12. 2020 jsou:

1 €   = 26.35 Kč
1 $   = 21.76 Kč
1 £   = 28.78 Kč
1 DKK = 3.54 Kč

Neúčtujeme žádné poplatky.
```

Další významnou skupinou metaznaků jsou kvantifikátory. Kvantifikátorů máme několik, začneme se složenými závorkami `{ }`. Ty nám říkají, kolikrát se znak před kvantifikátrem v řetězci může opakovat. Pokud vložíme do závorek jedno číslo `{n}`, znamená to opakování právě *n*-krát. Pokud dvě čísla `{m,n}`, znamená to opakování minimálně *m*-krát a maximálně *n*-krát a pokud `{n,}`, znamená to opakování minimálně *n*-krát a maximální počet opakování není omezený. Platí, že regulární výrazy jsou **žravé**, tedy zaberou vždy maximální možný počet znaků.

Pokud například chceme označit celou část našeho řádku s kurzem měn před symbolem `=`, napíšeme `1 [€$] {3}`.

Někdy se ale náš kurzovní lístek může "nafouknout", proto můžeme využít i výraz `1 [€$] {3,}`.

```
Vítejte ve Směnárně Na Růžku!
Kurzy měn pro 19. 12. 2020 jsou:

1 €     = 26.35 Kč
1 $     = 21.76 Kč
1 £     = 28.78 Kč
1 DKK   =  3.54 Kč
100 INR = 29.43 Kč

Neúčtujeme žádné poplatky.
```

Kromě složených závorek existují i tři speciální kvantifikátory.

* `?` znamená výskyt minimálně 0-krát, maximálně 1-krát.
* `*` znamená výskyt minimálně 0-krát, maxiální počet není omezen.
* `+` znamená výskyt minimálně 0-krát, maxiální počet není omezen.

Pro náš případ s výběrem řádků můžeme použít např. `1 [€$] +`.

Ve většině případů potřebujeme pracovat nejen s konkrétním znakem nebo konkrétními znaky, ale skupinami znaků. Abychom si práci usnadnili a nemuseli používat příliš často hranaté závorky, existují předem definované skupiny znaků. Skupiny jsou celkem tři a ke každé z nich existuje i její "opak". Např. skupina `\d` označuje čísla a skupina `\D` označuje vše kromě čísel, tj. písmena, mezery, speciální znaky jako `€`, `$` atd. Přehled skunin najdeš zde:

* `\d` zahrnuje číslice 0-9.
* `\D` zahrnuje jakýkoliv znak kromě číslic 0-9
* `\w` zahrnuje alfanumerické znaky, tj. všechna čísla, malá i velká písmena a podtržítko.
* `\W` zahrnuje jakýkoliv znak kromě alfanumerických znaků.
* `\s` zahrnuje "bílé" znaky (mezera, tabulátor, znaky pro zalomení řádků).
* `\S` zahrnuje jakýkoliv znak kromě "bílých" znaků.

`1 [€$] += +\d+.\d+ Kč`

Pokud chceme definovat skupinu znaků, které následují v abecedě (resp. přesněji v tabulce znaků) za sebou, můžeme je zapsat jako interval, například [1-5], [a-e] nebo třeba [A-Z]
Pokud potřebujeme zajistit, opakování určité sekvence znaků (ne jen znaku jednoho), můžeme sekvenci znaků uzavřít do závorek (( a )) a pokud za pravou kulatou závorku doplníme kvantifikátor, bude se počet opakování vztahovat na celou sekvenci znaků uzavřenou do závorek.
Pokud chceme dát na výběr několik variant textu (třeba Petr nebo Pavel), jako oddělovač variant použijeme metaznak | (výraz bude tedy Petr|Pavel)
Pokud chceme přikázat, že hledaný textový řetězec se musí nacházet na začátku nebo konci prohledávaného textu, použijeme metaznaky, které nazýváme hranice (boundaries) nebo ukotvení (anchors) – na různé typy hranic se podíváme níže.