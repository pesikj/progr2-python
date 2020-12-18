Databáze je systém, který slouží k ukládání dat. Standardní relační databáze ukládají data do předem definovaých tabulek, které jsou provázány vztahy (odtud pojem "relační"). Nejznámější zdarma dostupné databáze jsou PostreSQL, MySQL a SQLite, z placených poté Microsoft SQL Server nebo Oracle Database. Pro práci s databázemi používáme jazyk SQL (Structured Query Language).

Hlavní motivace, proč používat databáze, jsou:

- umožňují efektivně uložit velké množství dat,
- poskytují způsob, jak snadno a rychle najít požadovatnou informaci,
- snadno můžeme přidávat, upravovat, řadit a mazat záznamy,
- umožňují propojení s aplikacemi (např. weby),
- řeší přístup více uživatelů najednou,
- zajišťují zabezpečení dat.

## Ukládání dat

NoSQL databáze jsou poměrně široký pojem a zahrnuje různé typy databází, které používají jiný způsob ukládání dat než tabulky provázané relacemi. Konkrétně existuje několik typů NoSQL databází.

- Key-value databáze ukládají data do dvojic, kde jeden prvek (klíč) identifikuje hodnotu (value). Na stejném principuje fungují například slovníky v Pythonu.
- Grafové databáze vycházejí z teorie grafů. To je součást matematiky, která se zabývá strukturami složenými z bodů (vrcholů) a spojnic mezi nimi (hranami). Pomocí teorie grafů lze řešit například dopravní úlohy. V grafu pak vrcholy symbolizují města a hrany vzdálenosti mezi nimi. Můžeme pak např. spočítat nejkratší trasu pro návštěvu několika měst. (Speciální případ, kdy navštěvujeme všechna města, se na nazývá problém obchodního cestujícího.)
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

### Vložení jednoho záznamu

Pojďme tento nákup zapsat do naší databáze. V jazyce SQL obvykle používáme příkaz `INSERT`. Názvem příkazu je inspirován i název funkce, kterou budeme používat my.

Ještě malá poznámka ke struktuře. Každá databázový server může obsahovat několik databází (např. máme různé databáze pro různé zákazníky, programy, oddělení atd.). V MongoDB se každá databáze skládá z kolekcí (v relačních databázích se skládá z tabulek) a každá kolekce se skládá z dokumentů (v relačních databázích se tabulka skládá z řádků). Chceme-li něco ukládat, musíme nejprve vytvořit nebo zvolit databázi a kolekci, aby MongoDB vědělo, kam dokument vložit.

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

userName = ""
password = ""
address = ""
myclient = pymongo.MongoClient(f"mongodb://{userName}:{password}@{address}:27017/?")
databaze = klient[""]
kolekce = databaze[""]
id = kolekce.insert_one(nakup)
print(id)
```

Ke vložení dokumentu do kolekce použijeme funkce `insert_one()`, která slouží ke vložení jednoho dokumentu. Funkce vrací hodnotu `id`, což je jednoznačný identifikátor našeho záznamu. Samotné ID nám toho moc neřekne, jeho hodnota je například `5fda6f16e6aeccec0ef40b87`.

### Vložení více záznamů

Nyní zkusme vložit více záznamů najednou. Zbývající nákupy máme v proměnné, která se jmenuje `zbyvajici_nakupy`. Tato proměnná obsahuje seznam, což poznáme podle hranatých závorek na začátku a na konci. Seznam se skládá ze slovníků, které mají různé klíče podle toho, co kdo považoval za důležité.

```py
zbyvajici_nakupy = [
    {
        "Jméno": "Petr",
        "Věc": "Toaletní papír",
        "Částka v korunách": 65,
        "Počet rolí": 6,
    },
    {
        "Jméno": "Libor",
        "Věc": "Pivo na kolaudačku",
        "Částka v korunách": 124,
        "Vratná záloha": 20,
        "Datum": "2020-03-01",
        "Poznámka": "Vrátit otevírák sousedům",
    },
    {
        "Jméno": "Petr",
        "Věc": "Pytel na odpadky",
        "Částka v korunách": 75,
        "Objem pytle": 10,
        "Upozornění": "Příště koupit větší!!!",
    },
    {
        "Jméno": "Míša",
        "Věc": "Utěrky na nádobí",
        "Částka v korunách": 130,
        "Barva": "modrá",
        "Počet kusů v balení": 10,
    },
    {
        "Jméno": "Ondra",
        "Věc": "Toaletní papír",
        "Částka v korunách": 120,
        "Počet rolí": 15,
        "Běžná cena": 150,
    },
    {
        "Jméno": "Míša",
        "Věc": "Pečící papír",
        "Částka v korunách": 30,
        "Místo nákupu": "Albert",
        "Délka v metrech": 30,
        "Poznámka": "Peče celá země",
    },
    {
        "Jméno": "Zuzka",
        "Věc": "Savo",
        "Částka v korunách": 80,
        "Poznámka": "Dokoupit rukavice",
    },
    {
        "Jméno": "Pavla",
        "Věc": "Máslo",
        "Částka v korunách": 50,
        "Datum trvanlivosti": "2020-05-01",
    },
    {
        "Jméno": "Ondra",
        "Věc": "Káva",
        "Částka v korunách": 300,
        "Počet kusů": 2,
        "Značka": "Davidoff",
        "Poznámka": "Nejvíc vypila Míša",
    },
]

kolekce.insert_many(zbyvajici_nakupy)
```

Více záznamů vložíme pomocí funkce `insert_many()`, které předáme náš seznam.

## Cvičení

### Každý má svou pravdu

Uvažujme data o třech divadelních hrách, která jsou v následující tabulce.

| Představení          | Délka v minutách | Premiéra   | Derníéra   |
| -------------------- | ---------------: | ---------- | ---------- |
| Modrovous            |               70 | 2018-12-15 |            |
| Každý má svou pravdu |                  | 2020-02-08 |            |
| Expres na záped      |              120 |            | 2019-11-13 |

Splň následující úkoly.

- Přepiš tato data to tří slovníků. Pokud nějaký sloupec nemá hodnotu, vynech ho.
- Vlož jednotlivé slovníky postupně do své databáze do kolekce `hry`.
- Nechci si na obrazovku vypsat ID alespoň jednoho vloženého dokumentu.

### Knihovna

Níže jsou informace o třech různých knihách.

První kniha:

- Název: Smrt bere jackpot
- Žánr: Detektivní příběh
- Počet stran: 542
- Oběť: Freddy Brower
- Vrah: Leon Lamarr
- Motiv: Výhra v loterii

Druhá kniha:

- Název: Zaklínač I. - Poslední přání
- Autor: Andrzej Sapkowski
- Žánr: Fantasy
- Počet povídek: 8
- Počet stran: 274

Třetí kniha:

- Název: Matyáš Sandorf
- Podtitul: Nový hrabě Monte Christo
- Autor: Jules Verne
- Počet stran: 442
- První vydání: 1885

Přepiš informace do slovníků a tyto slovníky vlož do jednoho seznamu. Tento seznam pak vlož najednou do kolekce `knihy` funkcí `insert_many()`.

## Čtení dat

Zatím jsme data pouze vkládali, nyní je zkusíme přečíst. Ve světě relačních databází používáme ke čtení příkaz `SELECT`. Většinou nechceme načíst všechna data v tabulce (kolekci), ale pouze jejich část. Nyní si ukážeme, jak nastavit, jaká data chceme získat.

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

### Čtení na doma: Výběr hodnoty ze seznamu

Někdy potřebujeme do jednoho dotazu vložit více možných hodnot pro jeden klíč. V MongoDB používáme operátor `in`. Operátor `in` známe i z Pythonu a jeho funkce je zde obdobná: ptáme se, jestli je hodnota klíče pro daný řádek přítomna v námi zadaném seznamu. Syntaxi najdeš na příkladu níže.

```py
dotaz = {"Jméno": {"$in": ["Libor", "Míša"]}}
vysledek = kolekce.find(dotaz)
for dokument in vysledek:
    print(dokument)
```

## Úprava dat

Často potřebujeme upravit již existující záznam. V jazyce SQL k tomu existuje příkaz `UPDATE`, MongoDB můžeme využít funkce `update_one()` nebo `update_many()`.

### Úprava jednoho záznamu

Při úpravách záznamů musíme vždy specifikovat, který záznam chceme upravit. Záznam, který chceme upravit, opět vybereme pomocí dotazu. Jednomu dotazu může vyhovovat více dokumentů. funkce `update_one()` však upraví pouze první vyhovující záznam, na který narazí. Úpravu hodnot specifikujeme jako slovník, do něhož vložíme dvojice klíče-hodnota stejně, jako když jsme vytvářeli nový záznam, např. takto: `{ "Poznámka": "Otevírák jsme vrátili. " }`. Podobně jako u dotazů pak použijeme operátor, který bude tvořit nadřazený slovník. Tentokrát použijeme operátor `$set`. Výsledný slovník pro úpravu dokumentu tedy vypadá takto: `{ "$set": { "Poznámka": "Otevírák jsme vrátili. " } }`.

Níže vidíš sestavení obou slovníků a volání funkce `update_one()`.

```py
dotaz = { "Věc": "Pivo" }
noveHodnoty = { "$set": { "Poznámka": "Otevírák jsme vrátili. " } }
kolekce.update_one(dotaz, noveHodnoty)
```

### Úprava více záznamů

Pokud našemu dotazu vyhovuje více dotazů a my chceme upravit všechny, použijeme funkci `update_many()`. Zadání pro ni připravíme stejně, tj. vytvoříme jeden slovník pro dotaz a další slovník jako popis toho, co má funkce upravit. Například víme, že Petr notoricky zapomíná na dodání účtenky, tak k jeho nákupům přidáme připomenutí.

```py
dotaz = { "Jméno": "Petr" }
noveHodnoty = { "$set": { "Poznámka": "Chybí účtenka." } }
kolekce.update(dotaz, noveHodnoty)
```

## Úkoly

