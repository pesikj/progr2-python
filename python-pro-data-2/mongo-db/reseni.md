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
