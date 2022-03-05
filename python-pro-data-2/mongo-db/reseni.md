# Čtení dat

## Hodnocení knih

Z předem připravené kolekce `goodreads`, která obsahuje knihy a jejich hodnocení na webu Goodreads.com, načti první dostupný dokument pomocí funkce `find_one()`.

```
kolekce = databaze["goodreads"]
vysledek = kolekce.find_one()
print(vysledek)
```

Najdi knihu, jejíž ISBN (`isbn`) je 038551641X.

```
kolekce = databaze["goodreads"]
dotaz = {"isbn": "038551641X"}
vysledek = kolekce.find_one(dotaz)
print(vysledek)
```

Napiš dotaz na knihy, jejichž autorem (`authors`) je spisovatel "Robert Graves". Načti všechny knihy dle daného dotazu a vypiš informace o nich na obrazovku.

```
dotaz = {"authors": "Robert Graves"}
vysledek = kolekce.find(dotaz)

for dokument in vysledek:
    print(dokument)
```

U knih, které napsal Robert Graves, vypiš pouze název a hodnocení (`average_rating`).

```
for dokument in vysledek:
    print(dokument["title"], dokument["average_rating"])
```

Vypiš informace o všech knihách, které získaly více než 2 milion hodnocení (`ratings_count`).

```
dotaz = {"ratings_count": {"$gt": 2_000_000}}
vysledek = kolekce.find(dotaz)

for dokument in vysledek:
    print(dokument)
```

Vypiš informace o všech knihách, které alespoň 40 000 textových hodnocení (`text_reviews_count`) a současně mají průměrné hodnocení (`average_rating`) větší než 4.

```
dotaz = {"text_reviews_count": {"$gt": 40_000}, "average_rating": {"$gt": 4}}
vysledek = kolekce.find(dotaz)

for dokument in vysledek:
    print(dokument)
```

Vypiš informace o všech knihách, jejímiž autory jsou Jared Diamond nebo Joseph A. Tainter (zde využij operátor `in`).

```
dotaz = {"authors": {"$in": ["Jared Diamond", "Joseph A. Tainter"]}}
vysledek = kolekce.find(dotaz)

for dokument in vysledek:
    print(dokument)
```

# Zápis dat

## Každý má svou pravdu

Uvažujme data o třech divadelních hrách, která jsou v následující tabulce.

| Představení          | Délka v minutách | Premiéra   | Derniéra   |
| -------------------- | ---------------: | ---------- | ---------- |
| Modrovous            |               70 | 2018-12-15 |            |
| Každý má svou pravdu |                  | 2020-02-08 |            |
| Expres na západ      |              120 |            | 2019-11-13 |

Splň následující úkoly.

- Přepiš tato data to tří slovníků. Pokud nějaký sloupec nemá hodnotu, vynech ho.
- Vlož jednotlivé slovníky postupně do své databáze do kolekce `hry`.
- Nech si na obrazovku vypsat ID alespoň jednoho vloženého dokumentu.

```
kolekce = databaze["hry"]
hra_1 = {
    "Představení": "Modrovous",
    "Délka v minutách": 70,
    "Premiéra": "2018-12-15"
}
hra_2 = {
    "Představení": "Každý má svou pravdu",
    "Premiéra": "2020-02-08"
}
id = kolekce.insert_one(hra_1)
print(id)
kolekce.insert_one(hra_2)
```

## Knihovna

Níže jsou informace o třech různých knihách.

První kniha:

- Název: Smrt bere jackpot
- Autor: Vincent McEveety
- Počet stran: 542

Druhá kniha:

- Název: Zaklínač I. - Poslední přání
- Autor: Andrzej Sapkowski
- Počet povídek: 8
- Počet stran: 274

Přepiš informace do slovníků a tyto slovníky vlož do jednoho seznamu. Tento seznam pak vlož najednou do kolekce `knihy` funkcí `insert_many()`.

```
kolekce = databaze["knihy"]

knihy = [
    {
        "Název": "Smrt bere jackpot",
        "Autor": "Vincent McEveety",
        "Počet stran": 542
    },
    {
        "Název": "Zaklínač I. - Poslední přání",
        "Autor": "Andrzej Sapkowski",
        "Počet povídek": 8,
        "Počet stran": 274,
    }
]
    
kolekce.insert_many(knihy)
```

## Expres na západ

* Načti z kolekce `hry` informace o hře Expres na západ, kterou jsi uložila v předchozím bloku cvičení.
* Doplň k této hře datum premiéry 2015-11-10.
* Ověř, že byla data správně uložena.

```
kolekce = databaze["hry"]

dotaz = { "Představení": "Expres na západ" }
noveHodnoty = { "$set": { "Premiéra": "2015-11-10" } }
kolekce.update_one(dotaz, noveHodnoty)

vysledek = kolekce.find_one(dotaz)
print(vysledek)
```

## Oprava chyby

U dat je často nutné kontrolovat jejich správnost. Například datum může být uvedeno v nesprávném formátu nebo může být zadaný den, který neexistuje. V kolekci je `goodreads` jedna kniha, která má jako datum vydání (`publication_date`) nastavenou podivnou hodnotu 6/31/1982, tedy 31. června 1986. Zjisti, o jakou knihu jde. Uprav hodnotu na "7/1/1982". Zkontroluj, že se hodnota správně uložila.

```
kolekce = databaze["goodreads"]

dotaz = { "publication_date": "6/31/1982" }
noveHodnoty = { "$set": { "publication_date": "7/1/1982" } }
kolekce.update_one(dotaz, noveHodnoty)

vysledek = kolekce.find_one(dotaz)
print(vysledek)

dotaz = { "publication_date":  "7/1/1982" }
vysledek = kolekce.find_one(dotaz)
print(vysledek)
```

## Změna názvu nakladatele

Uvažuj, že se nakladatel (`publisher`) "Ballantine Books" přejmenoval na "Johnnie Walker Books". Uprav hodnotu pole `publisher` u všech knih, které mají jako nakladatele "Ballantine Books".

```
dotaz = { "publisher": "Ballantine Books" }
noveHodnoty = { "$set": { "publisher": "Johnnie Walker Books" } }
kolekce.update_many(dotaz, noveHodnoty)

dotaz = { "publisher": "Johnnie Walker Books" }
vysledek = kolekce.find(dotaz)
for dokument in vysledek:
    print(dokument)
```
