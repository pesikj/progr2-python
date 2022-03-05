---
title: Hodnocení knih
demand: 2
---

* Z předem připravené kolekce `goodreads`, která obsahuje knihy a jejich hodnocení na webu Goodreads.com, načti první dostupný dokument pomocí funkce `find_one()`. 
* Najdi knihu, jejíž ISBN (`isbn`) je 038551641X.
* Napiš dotaz na knihy, jejichž autorem (`authors`) je spisovatel "Robert Graves". Načti všechny knihy dle daného dotazu a vypiš informace o nich na obrazovku.
* Vypiš informace o všech knihách, které získaly více než 2 milion hodnocení (`ratings_count`).
* Vypiš informace o všech knihách, které alespoň 1000 stran.
* Vypiš informace o všech knihách, jejímiž autory jsou Jared Diamond nebo Joseph A. Tainter (zde využij operátor `in`).

Všimni si, v jakém formátu je zadané datum vydání (`publication_date`). Jde o americký formát, který má ze záhadných důvodů na prvním místě měsíc a na druhém den.
