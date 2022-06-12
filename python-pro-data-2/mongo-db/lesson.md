Databáze je systém, který slouží k ukládání dat. Standardní relační databáze ukládají data do předem definovaných tabulek, které jsou provázány vztahy (odtud pojem "relační"). Nejznámější zdarma dostupné databáze jsou PostgreSQL, MySQL a SQLite, z placených poté Microsoft SQL Server nebo Oracle Database. Pro práci s databázemi používáme jazyk SQL (Structured Query Language).

Hlavní motivace, proč používat databáze, jsou:

- umožňují efektivně uložit velké množství dat,
- poskytují způsob, jak snadno a rychle najít požadovanou informaci,
- snadno můžeme přidávat, upravovat, řadit a mazat záznamy,
- umožňují propojení s aplikacemi (např. weby),
- řeší přístup více uživatelů najednou,
- zajišťují zabezpečení dat.

## Čtení dat

NoSQL databáze jsou poměrně široký pojem a zahrnuje různé typy databází, které používají jiný způsob ukládání dat než tabulky provázané relacemi. Konkrétně existuje několik typů NoSQL databází.

- Key-value databáze ukládají data do dvojic, kde jeden prvek (klíč) identifikuje hodnotu (value). Na stejném principu fungují například slovníky v Pythonu.
- Grafové databáze vycházejí z teorie grafů. To je součást matematiky, která se zabývá strukturami složenými z bodů (vrcholů) a spojnic mezi nimi (hranami). Pomocí teorie grafů lze řešit například dopravní úlohy. V grafu pak vrcholy symbolizují města a hrany vzdálenosti mezi nimi. Můžeme pak např. spočítat nejkratší trasu pro návštěvu několika měst. (Speciální případ, kdy navštěvujeme všechna města, se na nazývá *problém obchodního cestujícího*.)
- Dokumentové databáze slouží k ukládání dokumentů, nejčastěji ve formátu JSON, XML nebo YAML.

My se budeme zabývat databází MongoDB, což je dokumentová databáze využívající formát JSON.

Kromě NoSQL databází se v poslední době objevil blockchain, což je způsob ukládání dat, kdy již vložené záznamy nelze nijak upravit.

### Formát JSON

Pojďme se nyní vrátit k našemu příkladu se spolubydlícími. Uvažujeme, že si chtějí svoje výdaje evidovat v databázi. Protože jsou ale poněkud neukáznění, ke každému nákupu si zapisuje různé věci. Např. někdo zapisuje datum nákupu, jiný poznámku, značku výrobku, jestli byl produkt v akci atd. Kvůli jejich kreativitě se rozhodli, že využijí NoSQL databázi, která jim dá větší volnost než klasická databáze. Domluvili se ale, že je nutné vždy uvést jméno kupujícího a cenu. Jednotlivé nákupy pak máme zapsané ve formátu JSON a naším úkolem je uložit je do databáze.

Níže jsou informace o nákupu, jak je zaprotokoloval Petr.

- jméno: Petr,
- věc: Prací prášek,
- částka v korunách: 399,
- datum: 2020-03-04,
- značka: Persil,
- hmotnost: 7.8.

Formát JSON taktéž připomíná slovníky v Pythonu. Data jsou uspořádána do dvojic - klíče a hodnoty. Níže vidíš, jak vypadají data zapsaná ve formátu JSON.

```
nakup = {
    "Jméno": "Petr",
    "Cena": 399,
    "Věc": "Prací prášek",
    "Datum": "2020-03-04",
    "Značka": "Persil",
    "Hmotnost": 7.8
}
```

Ve světě relačních databází používáme ke čtení příkaz `SELECT`. Většinou nechceme načíst všechna data v tabulce (kolekci), ale pouze jejich část. Nyní si ukážeme, jak nastavit, jaká data chceme získat.

### Test načtení dat

K načtení jednoho záznamu použijeme funkci `find_one()`. Pokud funkci nedáme žádný parametr, vrátí nám první záznam z kolekce.

```py
vysledek = kolekce.find_one()
print(vysledek)
```

Funkce vrátí první vložený záznam, který obsahuje námi zadané hodnoty a vygenerované ID.

### Sestavení dotazu

Na MongoDB a modulu `pymongo` je sympatické, že pro dotazy používáme slovník. Dotazy tedy píšeme stejně, jako když připravujeme data pro vložení. Zkusme třeba napsat dotaz na nákupy, které provedl Libor. Dotaz ve formě slovníku předáme funkce `find_one()`.

```py
dotaz = {"Jméno": "Libor"}
vysledek = kolekce.find_one(dotaz)
print(vysledek)
```

Většinou chceme vrátit všechny řádky, které odpovídají našemu dotazu. K tomu slouží funkce `find()`. Ta nám vrátí všechny dokumenty, které odpovídají našemu dotazu, jako seznam. Seznam poté můžeme projít pomocí cyklu.

```py
dotaz = {"Jméno": "Petr"}
vysledek = kolekce.find(dotaz)
for dokument in vysledek:
    print(dokument)
```

Pokud chceme požadovaný dokument vybrat na základě více klíčů, jednoduše z těchto klíčů sestavíme slovník.

```py
dotaz = {"Jméno": "Petr", "Věc": "Toaletní papír"}
vysledek = kolekce.find(dotaz)
for dokument in vysledek:
    print(dokument)
```

Pokud bychom chtěli vypsat jenom nějakou konkrétní informaci (např. cenu), vložíme požadovaný klíč do hranatých závorek za proměnnou `dokument`. Je to podobné, jako kdybychom četli nějakou hodnotu ze seznamu, pouze nepoužíváme číselný index. Pokud znáš slovníky, je ti zápis určitě povedomý.

```py
vysledek = kolekce.find(dotaz)
for dokument in vysledek:
    print(dokument["Částka v korunách"])
```

Určitým nebezpečím je, že tento zápis skončí chybou, pokud by v některém dokumentu nebyl přítomen daný klíč. Pokud máme obavu, že nějaká informace může chybět, můžeme využít metodu `get()`, které můžeme vložit výchozí hodnotu, kterou vrátí, nenalezne-li požadovaný klíč.

Další věc, na kterou si musíme dát pozor, je, že na rozdíl od seznamu nebo slovníku nemůžeme výsledek dotazu automaticky projít cyklem dvakrát. Pokud bychom chtěli s výsledkem stejného dotazu pracovat opakovaně, musíme použít metodu `rewind()` nebo položit dotaz znovu. Proměnná `vysledek` je totiž ve skutečnosti jakási forma záložky (kurzor) v knize. Pokud knihu dočteme, zůstane záložka na konci. Chceme-li knihu přečíst znovu, musíme nejprve záložku přesunout na začátek.

```py
vysledek.rewind()
for dokument in vysledek:
    print(dokument.get("Datum", "Datum není zadáno"))
```

### Větší než, menší než...

U číselných hodnot a dat chceme často formulovat dotaz obsahující nerovnost. Mohli bychom například chtít vypsat všechny nákupy v hodnotě větší než 100 Kč. MongoDB nepoužívá symboly `>` a `<`, ale jejich anglické zkratky. Například porovnání **větší než** zapisujeme jako `$gt`, což vychází z anglického "greater than". Dolar přidáváme, aby si MongoDB zkratku nespletlo s názvem sloupce. Kompletní přehled operátorů najdeš v tabulce níže.

| Význam           | Zápis v Pythonu | Zápis v MongoDB |
| ---------------- | :-------------: | :-------------: |
| Větší než        |       `>`       |      `$gt`      |
| Menší než        |       `<`       |      `$lt`      |
| Větší nebo rovno |      `>=`       |     `$gte`      |
| Menší nebo rovno |      `<=`       |     `$lte`      |

Operátor a hodnotu, se kterou chceme porovnávat, píšeme jako slovník, kde operátor je klíč `{"$gt": 100}`. To pak vložíme do dalšího slovníku, kterým určíme, pro jaký sloupec naše podmínka platí `{"Částka v korunách": {"$gt": 100}}`. Celý zápis tedy vypadá takto:

```py
dotaz = {"Částka v korunách": {"$gt": 100}}
vysledek = kolekce.find(dotaz)
for dokument in vysledek:
    print(dokument)
```

### Výběr hodnoty ze seznamu

Někdy potřebujeme do jednoho dotazu vložit více možných hodnot pro jeden klíč. V MongoDB používáme operátor `in`. Operátor `in` známe i z Pythonu a jeho funkce je zde obdobná: ptáme se, jestli je hodnota klíče pro daný řádek přítomna v námi zadaném seznamu. Syntaxi najdeš na příkladu níže.

```py
dotaz = {"Jméno": {"$in": ["Libor", "Míša"]}}
vysledek = kolekce.find(dotaz)
for dokument in vysledek:
    print(dokument)
```

### Počet hodnot

Pokud by nás zajímal počet dokumentů, které vyhovují našemu dotazu, můžeme použít metodu `count_documents()`, která pro danou kolekci vrátí počet dokumentů, které vyhovují danému dotazu.

```py
dotaz = {"Jméno": {"$in": ["Libor", "Míša"]}}
vysledek = kolekce.find(dotaz)
print(kolekce.count_documents(dotaz))
```

### Dotaz typu "nebo"

Uvažujme nyní, že bychom chtěli vyhledat nákupy, které provedl Petr *nebo* šlo o nákupy toaletního papíru. V tomto případě nemůžeme vložit oba klíče a hodnoty vedle sebe, protože bychom získali nákupy, které provedl Petr *a současně* šlo o nákupy toaletního papíru. K získání dokumentů, které vyhovují alespoň jedné z podmínek, můžeme použít operátor `$or`. Klíče a hodnoty, které hledáme, pak vložíme do seznamu.

```py
dotaz = {"$or": [{"Jméno": "Petr"}, {"Věc": "Pečící papír"}]}
vysledek = kolekce.find(dotaz)
for dokument in vysledek:
    print(dokument)
```

### Použití regulárních výrazů

V MongoDB můžeme k vyhledávání používat i regulární výrazy. Pokud si například nejsme jisti, jak jsou v kolekci zapsané pytle na odpadky (můžou být v jednotném i množném čísle), můžeme použít žolíky na poslední dvě písmena, která se pro jednotné a množné číslo liší. Při použití regulárních výrazů používáme operátor `$regex`.

```py
dotaz = {"Věc": {"$regex": "Pyt.. na odpadky"}}
vysledek = kolekce.find(dotaz)
for polozka in vysledek:
    print(polozka)
```

Pro lepší kontrolu můžeme použít i skupiny.

```py
dotaz = {"Věc": {"$regex": "Pyt(le|el) na odpadky"}}
vysledek = kolekce.find(dotaz)
for polozka in vysledek:
    print(polozka)
```

### Čtení na doma: Velikost písmen

Pokud bychom chtěli u **hodnot** provádět vyhledávání bez ohledu na velikost písmen, můžeme k tomu využít metodu `collation`. Té jako parametr zadáme dvojici hodnot - `locale` a `strength`. Locale je označení jazyka, podle kterého se má velikost písmen posuzovat, v našem případě zvolíme `cs` (češtinu), pro angličtinu bychom například zadali `en`. Druhý parametr označuje, zda má být velikost písmen ignorována. Pokud zadáme `2`, je při vyhledávání ignorována, pokud `1`, musí být velikost písmen u hodnoty dokumentu stejná jako v našem dotazu.

Pozor, toto nastavení ovlivní pouze hodnoty, velikost písmen u klíče musí být stejná v našem dotazu i dokumentu.

```py
dotaz = {"Věc": "pytel na odpadky"}
vysledek = kolekce.find(dotaz).collation({"locale": "cs", "strength": 2})
for polozka in vysledek:
    print(polozka)
```

Alternativně můžeme použít regulární výrazy, kde nastavíme operátoru `$options` hodnotu `i`, což znamená, že je u regulárních výrazů ignorována velikost písmen (další možnosti, které je možné nastavit, jsou k dispozici v [dokumentaci](https://www.mongodb.com/docs/manual/reference/operator/query/regex/)).

```py
dotaz = {"Věc": {"$regex": "pyt(le|el) na odpadky", "$options": 'i'}}
vysledek = kolekce.find(dotaz)
for polozka in vysledek:
    print(polozka)
```

[[[ excs Úkoly
- hodnoceni-knih
]]]


## Ukládání dat

### Vložení jednoho záznamu

Pojďme tento nákup zapsat do naší databáze. V jazyce SQL obvykle používáme příkaz `INSERT`. Názvem příkazu je inspirován i název funkce, kterou budeme používat my.

Ještě malá poznámka ke struktuře. Každá databázový server může obsahovat několik **databází** (např. máme různé databáze pro různé zákazníky, programy, oddělení atd.). V MongoDB se každá databáze skládá z **kolekcí** (v relačních databázích se skládá z tabulek) a každá kolekce se skládá z **dokumentů** (v relačních databázích se tabulka skládá z řádků). Chceme-li něco ukládat, musíme nejprve vytvořit nebo zvolit databázi a kolekci, aby MongoDB vědělo, kam dokument vložit.

K připojení k databázi použijeme modul `pymongo`, který je potřeba importovat příkazem `import`. Následně musíme zadat adresu serveru, uživatelské jméno a heslo. Tyto informace zjistíš během kurzu. Po přihlášení vytvoříme klienta, který bude prostředníkem mezi námi a MongoDB serverem. Následně vybereme konkrétní databázi a kolekci.

```py
import pymongo
nakup = {
    "Jméno": "Petr",
    "Věc": "Prací prášek",
    "Částka v korunách": 399,
    "Datum": "2020-03-04",
    "Značka": "Persil",
    "Hmotnost": 7.8
}

kolekce = databaze["nakupy"]
id = kolekce.insert_one(nakup)
print(id.inserted_id)
```

Ke vložení dokumentu do kolekce použijeme funkce `insert_one()`, která slouží ke vložení jednoho dokumentu. Funkce vrací hodnotu `id`, což je jednoznačný identifikátor našeho záznamu. Samotné ID nám toho moc neřekne, jeho hodnota je například `5fda6f16e6aeccec0ef40b87`.

### Vložení více záznamů

Nyní zkusme vložit více záznamů najednou. Zbývající nákupy máme v proměnné, která se jmenuje `zbyvajici_nakupy`. Tato proměnná obsahuje seznam, což poznáme podle hranatých závorek na začátku a na konci. Seznam se skládá ze slovníků, které mají různé klíče podle toho, co kdo považoval za důležité.

```py
zbyvajici_nakupy = [
    {
        "Jméno": "Petr",
        "Věc": "Toaletní papír",
        "Částka v korunách": 35,
        "Počet rolí": 3
    },
    {
        "Jméno": "Libor",
        "Věc": "Jahodová marmeláda",
        "Částka v korunách": 50,
        "Datum": "2020-03-15"
    },
    {
        "Jméno": "Petr",
        "Věc": "Pytel na odpadky",
        "Částka v korunách": 90,
        "Objem pytle": 15
    },
    {
        "Jméno": "Míša",
        "Věc": "Fólie na potraviny",
        "Částka v korunách": 30,
        "Datum": "2020-03-25"
    },
    {
        "Jméno": "Míša",
        "Věc": "Paralen",
        "Částka v korunách": 130
    },
    {
        "Jméno": "Gumové rukavice",
        "Věc": "Savo",
        "Částka v korunách": 200,
    }
]

kolekce.insert_many(zbyvajici_nakupy)
```

Více záznamů vložíme pomocí funkce `insert_many()`, které předáme náš seznam.

## Mazání dat

Často se nám stane, že potřebujeme nějaký záznam smazat, například když omylem vložíme stejnou informaci do kolekce dvakrát. K mazání záznamů můžeme používat funkce `delete_one()` a `delete_many()`. Při volání funkcí vždy použijeme dotaz, který určí, který záznam (nebo které záznamy) chceme smazat.

Funkce `delete_one()` smaže jeden záznam, i kdyby konkrétnímu dotazu vyhovovalo záznamů více. Pokud žádný vyhovující záznam nenajde, neprovede žádnou operaci. Následující kód tedy způsobí, že Petr bude mít v kolekci o jeden nákup méně.

```py
dotaz = {"Jméno": "Petr"}
kolekce.delete_one(dotaz)
```

Následující kód je radikálnější a smaže všechny Petrovy nákupy.

```py
dotaz = {"Jméno": "Petr"}
kolekce.delete_many(dotaz)
```

Pokud chceme smazat jeden konkrétní záznam, často to provádíme na základě jeho jednoznačného identifikátoru `_id`, které každému záznamu přiřadí databáze automaticky. Známe-li `_id`, můžeme ho vložit do dotazu stejně jako jakýkoli jiný klíč a použít ke smazání záznamu. Protože každý dokument má své unikátní `_id`, je logické využít funkci `delete_one()`.

```py
dotaz = {"_id": "62248970d034741099592733"}
kolekce.delete_one(dotaz)
```

[[[ excs Cvičení
- pravda
]]]

[[[ excs Bonusové cvičení
- knihovna
]]]


## Úprava dat

Často potřebujeme upravit již existující záznam. V jazyce SQL k tomu existuje příkaz `UPDATE`, MongoDB můžeme využít funkce `update_one()` nebo `update_many()`.

### Úprava jednoho záznamu

Při úpravách záznamů musíme vždy specifikovat, který záznam chceme upravit. Záznam, který chceme upravit, opět vybereme pomocí dotazu. Jednomu dotazu může vyhovovat více dokumentů. funkce `update_one()` však upraví pouze první vyhovující záznam, na který narazí. Úpravu hodnot specifikujeme jako slovník, do něhož vložíme dvojice klíče-hodnota stejně, jako když jsme vytvářeli nový záznam, např. takto: `{ "Poznámka": "Odečtena vrácená záloha za lahve." }`. Podobně jako u dotazů pak použijeme operátor, který bude tvořit nadřazený slovník. Tentokrát použijeme operátor `$set`. Výsledný slovník pro úpravu dokumentu tedy vypadá takto: `{ "$set": { "Poznámka": "Odečtena vrácená záloha za lahve." } }`.

Níže vidíš sestavení obou slovníků a volání funkce `update_one()`.

```py
dotaz = { "Věc": "Pivo" }
noveHodnoty = { "$set": { "Poznámka": "Odečtena vrácená záloha za lahve." } }
kolekce.update_one(dotaz, noveHodnoty)
```

### Úprava více záznamů

Pokud našemu dotazu vyhovuje více dotazů a my chceme upravit všechny, použijeme funkci `update_many()`. Zadání pro ni připravíme stejně, tj. vytvoříme jeden slovník pro dotaz a další slovník jako popis toho, co má funkce upravit. Například víme, že Petr notoricky zapomíná na dodání účtenky, tak k jeho nákupům přidáme připomenutí.

```py
dotaz = { "Jméno": "Petr" }
noveHodnoty = { "$set": { "Poznámka": "Chybí účtenka." } }
kolekce.update_many(dotaz, noveHodnoty)
```

[[[ excs Úkoly
- expres
- oprava-chyby
]]]

[[[ excs Bonusy
- nakladatel
]]]

## Čtení na doma: Agregace

Zkusme si nyní vytvořit nějaké složitější dotazy. Důležitou operací, kterou s daty často provádíme, je řazení. Pro řazení potřebujeme zařídit dvě věci.

První z nich je **index**. Index si můžeme představit jako datovou strukturu, která usnadňuje vyhledávání a další práci s hodnotami. Index vytvoříme poměrně jednoduše, a to s využitím metody `create_index()`. U indexu musíme specifikovat, pro který klíč má být vytvořen. Pokud například chceme seřadit nákupy podle klíče `"Částka v korunách"`, vytvoříme index následujícím způsobem.

```py
kolekce = databaze["nakupy"]
kolekce.create_index("Částka v korunách")
```

U větších kolekcí může vytvoření indexu trvat delší dobu. Vytváření indexu může pokračovat i chvíli poté, co skript skončí, v takovém případě je potřeba počkat na vytvoření kompletního indexu.

Dále potřebujeme vytvořit **pipeline**. To je seznam (přeneseně i doslova) kroků, které chceme provést. My do seznamu vložíme pouze jeden krok, a to řazení. Každý krok zadáváme jako slovník. Vytvoříme slovník, který má jako klíč operátor `"$sort"` (operátor pro řazení). Hodnotou klíče je opět slovník, kam vložíme klíč, podle kterého chceme řadit, a hodnotou je `pymongo.ASCENDING` nebo `pymongo.DESCENDING` podle toho, zda chceme řadit vzestupně či sestupně.

Pro větší přehlednost si krok uložíme do samostatné proměnné `krokRazeni`. Po vytvoření pipeline zavoláme metodu `aggregate`, která provede všechny kroky (v našem případě jeden) a výsledek tradičně uložíme do proměnné `vysledek`.

```py
krokRazeni = {
    "$sort": {
        "Částka v korunách": pymongo.DESCENDING
    }
}

pipeline = [
    krokRazeni
]
vysledek = kolekce.aggregate(pipeline)
for dokument in vysledek:
    print(dokument)
```

Nyní vytvoříme spojení do skupiny (`group`). U spojení více řádků do skupin potřebujeme říci, podle jakého klíče vytvoříme skupiny. Pokud bychom chtěli zjistit, kolik každý ze spolubydlících utratil za nákupy, vytvoříme skupiny podle sloupce `Jméno`. Dále vytvoříme nový klíč `Celkem utraceno`, jehož hodnota bude součet všech nákupů v rámci dané skupiny. Samotné spuštění pipeline je již stejné.

```py
kolekce = databaze["nakupy"]

krokSoucetNakladu = {
   "$group": {
         "_id": "$Jméno",
         "Celkem utraceno": { "$sum": "$Částka v korunách" }, 
   }
}

pipeline = [
   krokSoucetNakladu,
]

vysledek = kolekce.aggregate(pipeline)
for dokument in vysledek:
    print(dokument)
```

Nyní si zkusíme vytvořit pipeline se dvěma kroky. Prvním krokem je součet hodnot nákupů jednotlivých spolubydlících. V druhém kroku seřadíme spolubydlící dle celkové útraty od nejvíce po nejméně utrácejícího.

```py
kolekce = databaze["nakupy"]
krokSoucetNakladu = {
    "$group": {
        "_id": "$Jméno",
        "Celkem utraceno": {"$sum": "$Částka v korunách"},
    }
}
krokRazeni = {
    "$sort": {
        "Celkem utraceno": pymongo.DESCENDING
    }
}

pipeline = [
    krokSoucetNakladu,
    krokRazeni
]

vysledek = kolekce.aggregate(pipeline)
for dokument in vysledek:
    print(dokument)
```
