Regulární výrazy jsou v podstatě malí "kouzelníci", kteří nám umožní vytáhnout z textu důležitá data. Často například dostaneme celou adresu jako jeden řetězec, například jako "Václavské nám. 837/11, 110 00 Nové Město" a my potřebujeme z adresy vytáhnout poštovní směrovací číslo, abychom zhruba věděli, kde se dané místo nachází.

O poštovním směrovacím čísle víme, že je složeno z pěti číslic a většinou (ale ne vždy) ho zapisujeme s mezerou mezi třetím a čtvrtém čísle. Potřebujeme tedy nějak obecně říct, že máme z textu vybrat pětici čísel, která může mít mezi třetím a čtvrtým číslem mezeru.

## Jak fungují regulární výrazy

Regulární výrazy umožňují používání symbolů, které mohou zastoupit nějaký znak (nebo více znaků). Fungují podobně jako třeba žolík v karetní hře nebo hvězdička ve vyhledávání souborů, umoňují ale přesněji specifikovat, co vlastně zastupují. Práci s regulárními výrazy si můžeme pohodlně trénovat například v aplikaci [Regular Expressions 101](https://regex101.com/). Do pole "Regular Expression" zadáváme reguálrní výraz a do pole "Text String" řetězec, se kterým pracujeme. Aplikace nám interaktivně podbarvuje části textu, které odpovídají našemu výrazu. Protože regulární výrazy se v různých programovacích jazycích mírně liší, měli bychom si vlevo v části "Flavor" přepnout na Python.

Oněm magickým znakům říkáme *metaznaky*. 

### Kvantifikátory

Zkusme si to na příkladu tečky `.`. Tečka zastupuje **právě jeden** libovolný znak. Ta skutečně odpovídá právě "žolíku". Pokud tedy budeme pracovat s řetězecem `"A23456789JQKA"` a zadáme regulární výraz `"78.JQK"`, podbarví se nám část řetězce od `7` do `J`.

Vyzkoušejme si nyní upravit program, který bude sledovat vývoj kurzu měn ve Směnárně Na Růžku, aby nám například poslal upozornění ve chvíli, kdy má nějaká měna výhodný kurz. Náš program zatím umí stáhnout informace do následující řetězce. 

```
Vítejte ve Směnárně Na Růžku!
Kurzy měn pro 19. 12. 2020 jsou:

1 €   = 26.35 Kč
1 $   = 21.76 Kč
1 £   = 28.78 Kč
1 DKK = 3.54 Kč

Neúčtujeme žádné poplatky.
```

Podívejme se nejprve na řádek, kde máme kurz Eura. Mohli bychom napsat pouze dolar, ale abychom označili i jedničku před znakem měny, napíšeme `1 €`.

### Skupiny znaků

Pokud chceme, aby náš metaznak zastupoval jeden ze skupiny znaků, vložíme tyto znaky do hranatých závorek `[ ]`. Například pokud chceme v kurzovním lístku vyhledat řádky, které mají v sobě znak dolaru nebo eura, napíšeme `1 [€$]`.

### Kvantifikátory

Další významnou skupinou metaznaků jsou kvantifikátory. Kvantifikátorů máme několik, začneme se složenými závorkami `{ }`. Ty nám říkají, kolikrát se znak před kvantifikátrem v řetězci může opakovat. Pokud vložíme do závorek jedno číslo `{n}`, znamená to opakování právě *n*-krát. Pokud dvě čísla `{m,n}`, znamená to opakování minimálně *m*-krát a maximálně *n*-krát a pokud `{n,}`, znamená to opakování minimálně *n*-krát a maximální počet opakování není omezený. Platí, že regulární výrazy jsou **žravé**, tedy zaberou vždy maximální možný počet znaků.

Pokud například chceme označit celou část našeho řádku s kurzem měn před symbolem `=`, napíšeme `1 [€$] {3}`. Mezera před složenými závorkami je důležitá, protože právě ona se má opakovat.

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

Morseova abeceda sloužila dřív k předávání zpráv. Každé písmeno mělo svoji reprezentaci pomocí krátkých a dlouhých signálů (např. telegrafem, rádiem nebo světlem baterky). Podívejme se na následující zprávu, zda v ní není skryto volání o pomoc. O pomoc voláme pomocí mezinárodní zkratky SOS, s kódujeme pomocí tří teček a O pomocí tří čárek.

```
.--- .- -.-. .... -.-. .. -.. --- -- ..- -.-.-- ... --- ... -.-.-- -. ..- -.. .. -- ... . -.-.--
```

K ověření, zda odesílatel volá o pomoc, napíšeme `\.{3} -{3} \.{3}`. Důležitá jsou **zpětná lomítka** před tečkami. Zpětná lomítka totiž říkají, že nechceme použít tečku jako takovou (která, jak už víme, ve světe regulárních výrazů zastupuje libovolný symbol), ale skutečnou tečku. Jak bychom našli písmeno J, které kódujeme jako tečku a tři čárky?

**Pozn.** Poznámku o zpětném lomítku si zapamatuj, protože to je často používaná technika v celém IT světě, nikoli pouze v Pythonu.

Kromě složených závorek existují i tři speciální kvantifikátory.

* `?` znamená výskyt minimálně 0-krát, maximálně 1-krát.
* `*` znamená výskyt minimálně 0-krát, maxiální počet není omezen.
* `+` znamená výskyt minimálně 1-krát, maxiální počet není omezen.

Pro náš případ s výběrem řádků můžeme použít např. `1 [€$] +`.

### Skupiny znaků

Ve většině případů potřebujeme pracovat nejen s konkrétním znakem nebo konkrétními znaky, ale skupinami znaků. Abychom si práci usnadnili a nemuseli používat příliš často hranaté závorky, existují předem definované skupiny znaků. Skupiny jsou celkem tři a ke každé z nich existuje i její "opak". Např. skupina `\d` označuje čísla a skupina `\D` označuje vše kromě čísel, tj. písmena, mezery, speciální znaky jako `€`, `$` atd. Přehled skunin najdeš zde:

* `\d` zahrnuje číslice 0-9.
* `\D` zahrnuje jakýkoliv znak kromě číslic 0-9
* `\w` zahrnuje alfanumerické znaky, tj. všechna čísla, malá i velká písmena a podtržítko.
* `\W` zahrnuje jakýkoliv znak kromě alfanumerických znaků.
* `\s` zahrnuje "bílé" znaky (mezera, tabulátor, znaky pro zalomení řádků).
* `\S` zahrnuje jakýkoliv znak kromě "bílých" znaků.

Níže máme různorodou skupinu textových dat, se kterými se často setkáváme. Vyzkoušejme si na nich, jak co vše zachytí skupiny znaků.

```
hadi_notace_ma_podtrzitka
9A55423
9A5 5423
+420 735 123 456
Václavské nám. 837/11, 110 00 Nové Město
19. prosince 2020
frantisek.novak@ocelove-mesto.cz
80-902734-1-6
```

### Několik příkladů

Zkusme nyní propojit naše znalosti dohromady.

Víme, že v britské angličtině používáme pro barvu výraz "colour" a v americké "color". Chceme-li spočítat, kolikrát je v textu zmíněna barva, použijeme `colou?r`.

Podobně můžeme využít regulární výraz k "license" "licence", napíšeme `licen[cs]e`.

Otazníky nám například pomůžou vypořádat se s nepovinnou mezerou, kterou píšeme například u data. U nás často používáme zápisy data 19. 12. 2020 nebo 19.12.2020. Pojďme sestavit regulární výraz:

* Na začátku je číslo dne. Uvažujme, že tam může být jedno nebo dvě čísla. Použujeme množinu `\d` a kvantifikátor `{1,2}`.
* Následuje tečka, kterou musíme zkrášlit zpětným lomítkem.
* Následuje nepovinná mezera. Zde využijeme kvantifikátor `?`.
* Pak už opakujeme tu samou myšlenku, abychom sestavili celý výraz: `\d{1,2}\. ?\d{1,2}\. ?\d{4}`.

Často chceme označit několik slov do jednoho bloku. Skuina `\w` nezahrnuje mezery, musíme ji tedy rozšířit na `[\w ]*`. Například adresu `Václavské náměstí 11, 110 00 Nové Město` tak rozdělíme na dva samostatné bloky.

Nyní už umíme sestavit výraz, kterým vybereme celý řádek s kurzem dolaru nebo eura: `1 [€$] += +\d+.\d+ Kč`.

Číslo bankovního účtu má v Česku tvar: 

* předčíslí (nepovinné, 0 až 6 číslic), zakončené je pomlčkou,
* číslo účtu (max. 10 číslic),
* lomítko,
* kód banky (právě 4 číslice).

Pokud bychom neuvažovali předčíslí, stačí nám regulární výraz `\d{6,10}\/\d{4}`, který by měl pasovat např. na číslo účtu 2300117015/2010. Nesmíme zapomenout na zpětné lomítko před lomítkem.

Uvažujme, že máme program, do kterého nějaký programátor vložil proměnnou `magickaKonstanta`. Víme, že proměnná je desetinné číslo, ale potřebujeme vědět, kde je zadána její hodnota. Napiš regulární výraz, který najde řádek, který 

```
polomer = input("Zadej poloměr koule: ")
polomer = int(polomer)
magickaKonstanta = 3.1415
objem = 4/3 * magickaKonstanta * polomer ** 3
povrch = 4 * magickaKonstanta * r ** 2
```

Zkus si program zkopírovat do Visual Studia a vyzkoušej si vyhledávání přepnout na regulární výrazy. Najde regulární výraz `magickaKonstanta = \d+\.\d*` správný řádek?

### Rozmezí

Kromě výpisu znaků a předdefinovanými skupiny můžeme ještě vybrat znaky pomocí rozmezí. K tomu použijeme pomlčku, kterou vepíšeme do hranatých závorek. Například čísla od 1 do 5 napíšeme jako `[1-5]`, malá písmena od `[a-e]` a všechna velká písmena jako `[A-Z]`.

Pokud například víme, že se na nějaké střední školy vyskytují třídy označené od A do M, regulární výraz pasující na všechna jména tříd je `[1-4][A-M]`.

Pokud potřebujeme zajistit, opakování určité sekvence znaků (ne jen znaku jednoho), můžeme sekvenci znaků uzavřít do kulatých závorek `( )` a za pravou závorku umístit kvantifikátor. Pokud máme variant více, můžeme k jejich oddělení použít znak `|`. Například pokud chceme vybrat oba víkendové dny, napíšme `(sobota|neděle)`.

### Další příklady

Podívejme se nyní na pár příkladů. Níže máme tabulku s kurzy Czechitas. 

* Chceme jít na kurz programování v Pythonu nebo v JavaScriptu. Kurz musí být pro začátečníky. Řádky, které nás zajímají, vyhledáme pomocí `Úvod do programování 1 - (JavaScript|Python)`. Co kdyby nám nevadil ani navazující kurz?
* Uvažujme, že nás zajímají pouze kurzy o víkendu. Vyzkoušíme si výraz `(sobota|neděle)`. Můžeme k povoleným dnům přidat ještě úterý?
* Protože se nám o víkendu nechce příliš brzy vstávat, chceme víkendové kurzy, které začínají nejdříve v 8:30. Napíšeme `(sobota|neděle) [89]:30`. Co kdybychom naopak chtěji kurzy, které začínají nejpozději v 8:30
* Napíšeme si regulární výraz, který označí všechna data ve formátu, jaký je v tabulce. Můžeme například použít výraz `\d{1,2}\. (led|úno). 2021`. Do závorky bychom pro rozvrh na celý rok potřebovali přidat zkratky všech měsíců.

```
9. led. 2021 sobota 9:30 - 16:30 Úvod do programování 1 - Java 
16. led. 2021 sobota 7:30 - 15:30 Úvod do programování 1 - JavaScript
16. led. 2021 sobota 8:30 - 17:30 Úvod do programování 2 - Python
18. led. 2021 úterý 9:30 - 17:30 Úvod do programování 1 - JavaScript
23. led. 2021 sobota 9:30 - 16:30 Úvod do programování 2 - Java
27. led. 2021 středa 9:30 - 17:30 Úvod do HTML a CSS
7. úno. 2021 neděle 8:30 - 17:30 Úvod do programování 1 - Python ONLINE
14. úno. 2021 neděle 8:30 - 17:30 Úvod do programování 1 - Python ONLINE
20. úno. 2021 sobota 9:30 - 17:30 Testuju Úvod do testování - manuální
```

* Poštovní směrovací číslo označíme výrazem `\d{3} ?\d{2}`.
* Regulární výraz, který rozpozná všechny paragrafy, které mají maximálně tři čísla, je `§\d{3}`.

## Cvičení

### Předčíslí u čísla účtu

Přidej k regulárnímu výrazu na číslo účtu možnost předčíslí, tj. na začátku může být 0 až 6 čísel a za nimi může (ale nemusí) být pomlčka.

### Číslo účtu podruhé

Nejmenovaná česká banka rozlišuje typy účtů podle číslic na začátku čísla. Například je-li první číslice 1, jedná se o investiční účet, je-li první číslice 2, jde o bankovní účet. Uvažujme, že naše tajemná banka má kód (poslední čtyři čísla) 2100.

* Uprav regulární výraz (nemusíš řešit předčíslí) tak, aby na prvním místě mohla být pouze 1 nebo 2.
* Uvažuj, že na druhém místě mohou být jen číslice 0, 1 nebo 2.

### Registrační značka

Standardní egistrační značky automobilů, vydané od roku 2004, mají následující formát:

* Na prvním místě je číslo.
* Na druhém místě písmeno, které označuje kraj.
* Na třetím místě je číslo nebo písmeno.
* Na čtvrtém místě je mezera a následuje čtveřice čísel.

Napiš regulární výraz, který bude kontrolovat formát registrační značky. Ověřit si ho můžeš na následujících značkách, které mají správný formát.

```
4A6 8244
6B2 6635
2AD 3824
7C1 5025
```

Značky níže mají špatný formát.

```
AC8 5484
924 1541
8A2 25C2
3P 4564
1A 25364
```

Zkus nyní regulární výraz ještě zdokonalit a povol na druhém místě pouze znak, který označuje nějaký konkrétní kraj. Platné znaky na druhém místě tedy budou tyto: `A, B, C, E, H, J, K, L, M, P, S, T, U, Z`.

### Telefonní číslo

V Česku máme standardně devítimístná telefonní čísla. Napiš regulární výraz, který sedí na "naše" telefonní čísla.

* Často se telefonní číslo rozděluje na trojice, které jsou odděleny mezerou. Uprav svůj výraz tak, aby odpovídal číslům s mezerou i bez mezery.
* Před telefonní číslo je výhodné přidat mezinárodní předvolbu (v našem případě +420), aby nám mohli volat i lidé ze zahraničí. Přidej to ke svému regulárnímu výrazu.

### Ministerstva

Napiš regulární výraz, který z následujícího řádku vybere celé názvy ministerstev.

```
Ministerstvo pro místní rozvoj, Celní správa České republiky, Ministerstvo životního prostředí, Ministerstvo práce a sociálních věcí, Český statistický úřad, Nejvyšší kontrolní úřad
```

### Slavný soude

Spisová značka, tj. označení spisu u soudu, má zpravidla následující formát:

* číslo soudního oddělení (např. 1 až 2 čísla),
* rejstříková značka (např. jedno až tři velká písmena),
* běžné číslo, podle toho kdy k soudu věc přišla (např. 1 až 4 čísla),
* za lomítkem daný ročník (4 čísla).

Může vypadat například takto: 63 C 397/2014. Napiš regulární výraz a na tomto příkladu jej vyzkoušej.

## Regulární výrazy v Pythonu

V Pythonu máme řadu funkcí, které můžeme použít pro práci s regulárními výrazy. Projdeme si ty základní. Funkce jsou v modulu `re`, který je součástí Pythonu a můžeš ho importovat pomocí příkazu `import re` na začátku programu.

### Ověření formátu

Často potřebujeme ověřit, jestli máme zadaná data ve správném formátu. Např. telefonní čísla, rodná čísla, ISBN u knih, poštovní směrovací čísla, e-maily nebo čísla bankovního účtu mají jasně definovaný formát. 

Zkusme si nejprve zadat rodné číslo. Víme, že rodné číslo se skládá ze 6 číslic, které kódují datum narození, a tří nebo čtyř číslic, které identifikují konkrétního člověka. Regulární výraz, který by číslo ověřil, je `\d{9,10}`.

Regulární výraz můžeme vytvořit pomocí funkce `compile()` z modulu `re`. Před řetězec s regulárními výrazy píšeme `r`, abychom Pythonu dali vědět, co je daný řetězec zač.

```py
import re
regularniVyraz = re.compile(r"\d{9,10}")

rezetec = "9511121234"
print(regularniVyraz.match(rezetec))
rezetec = "ahoj"
print(regularniVyraz.match(rezetec))
```

**Otázka:** Často je rodné číslo zapisováno ve formátu s podtržítkem, které odděluje datum narození od zbytku. Jak upravíme regulární výraz, aby akceptoval oba formáty, tj. formát s podtržítkem i bez potržítka?

Pokud funkce `match` došla k závěru, že se řetězec shoduje s regulárním výrazem, vrátí objekt  `Match`. S ním později budeme pracovat. Pokud by však funkce došla k závěru, že se řetězce s regulárním výrazem neshoduje, vrátí hodnotu označovanou jako `None`, tj. prázdnou hodnotu.

Funkce `match()` kontroluje řetězec od prvního znaku a pokud nenarazí na problém až do konce reguálního výrazu, vrátí objekt `Match`.

```py
import re
regularniVyraz = re.compile(r"\d{9,10}")

rezetec = "9511121234 je moje rodné číslo"
print(regularniVyraz.match(rezetec))
rezetec = "Moje rodné číslo je 9511121234"
print(regularniVyraz.match(rezetec))
```

### Přísnější ověření formátu

Pokud chceš ověřit, jestli řetězec odpovídá zadanému výrazu a není tam nic navíc, můžeš použít funkci `fullmatch`, která funguje stejně jako funkce `match()`.

```py
import re
regularniVyraz = re.compile(r"\d{9,10}")

rezetec = "9511121234"
print(regularniVyraz.match(rezetec))
rezetec = "9511121234$ je moje rodné číslo"
print(regularniVyraz.fullmatch(rezetec))
```

### Zapojení podmínky

Pojďme nyní zapojit do akce podmínku. Můžeme třeba uživateli vypsat, jestli jím zadaná hodnota je správná. Výsledek volání funkce `match()` můžeme vložit přímo do podmínky, protože podmínka, které nevložíme operátor na porovnávání (např. `==`) funguje takto:

* Pokud podmínce vložíme nějaký smysluplný výraz, vyhodnotí ho jako **pravda**.
* Pokud podmínce vložíme prázdnou hodnotu `None`, vyhodnotí ji jako **nepravda**.

```py
import re

regularniVyraz = re.compile(r"\d{9,10}")
vstup = input("Zadej rodné číslo: ")
hledani = regularniVyraz.fullmatch(vstup)
if hledani:
    print("Rodné číslo je v pořádku!")
else:
    print("Nesprávné rodné číslo!")
```

### E-maily

Pokud např. dostaneme e-mail `info@czechitas.cz`, víme, že je v pořádku. E-mail `info@czechitascz` by ale v pořádku nebyl, protože "koncovka" `"cz"` (v řeči počítačů doména prvního řádu) musí být oddělena tečkou.

```py
import re

regularniVyraz = re.compile(r"\w+@\w+\.cz")
email = input("Zadej e-mail: ")
hledani = regularniVyraz.fullmatch(email)
if hledani:
    print("Rodné číslo je v pořádku!")
else:
    print("Nesprávné rodné číslo!")
```

### Vyhledávání

Kromě ověřování správného formátu můžeme použít regulární výrazy i k vyhledávání. Například funkce `findall` vrátí ze zadaného řetězce všechny podřetězece, které odpovídají danému regulárnímu výrazu, jako seznam.

Následující program například z deníku lékaře vyhledá rodná čísla všech pacientů, které lékař zmínil.

```py
zapis = """
Zápisy o provedených vyšetřeních:
Pacient 6407156800 trpěl bolestí zad a byl poslán na vyšetření. 
Pacientka 8655057477 přišla na kontrolu po zranění kontníku.
Do ordinace telefonovala pacientka 7752126712, které byl elektronicky vydán recept na Paralen. 
"""
import re
regularniVyraz = re.compile(r"\d{9,10}")
vysledky = regularniVyraz.findall(zapis)
for vysledek in vysledky:
    print(vysledek)
```

### Nahrazování

Uvažujme, že máme nějakém textu provést anonymizaci, tj. vymazat všechny osobní údaje. K tomu můžeme využít funkci `sub()`, která nahradí všechny podřetězce, které odpovídají regulárnímu výrazu, námi zadanou hodnotou.

```py
zapis = """
Zápisy o provedených vyšetřeních:
Pacient 6407156800 trpěl bolestí zad a byl poslán na vyšetření. 
Pacientka 8655057477 přišla na kontrolu po zranění kontníku.
Do ordinace telefonovala pacientka 7752126712, které byl elektronicky vydán recept na Paralen. 
"""
import re
regularniVyraz = re.compile(r"\d{9,10}")
anonymniZapis = regularniVyraz.sub("X" * 9, zapis)
print(anonymniZapis)
```

## Cvičení

### Uživatelské jméno

Náš systém vyžaduje od uživatele zadání uživatelského jména. Uživatelské jméno smí obsahovat pouze malá písmena a smí být maximálně 8 znaků dlouhé. Požádej uživatele o zadání uživatelského jména a pomocí regulárního výrazu vyhodnoť, zda je zadané správné.

### E-mail s tečkou

Uprav program na ověření e-mailu tak, aby akceptoval i e-maily, které mají v první části tečku, např jiri.pesik@python.cz.

### Záznamy

Uvažujme aplikaci, která si ukládá informace o činnosti uživatelů do textového souboru. Příklad souboru je níže.

```py
zaznamy = """
searchNumber: 
searchNumber: pavca.czechitas action: search phone number of user dita
user: pavca action: send sms to phone number +420728123456
user: jirka: action: send 2 sms to phone number +420734123456
"""
```

* Napiš program, který vypíše všechna telefonní čísla, která jsou v textovém souboru zmíněna.
* Nahraď tato telefonní čísla nějakým řetězcem (např. "XXX"), aby nebyla v záznamech dostupná.

