---
title: Řidič
demand: 4
---

Pokračuj ve své práci pro zásilkovou společnost. Společnost nyní eviduje jednotlivé řidiče a eviduje balíky, které má každý řidič doručit.

- Vytvoř třídu `Ridic`, která má dva atributy: `jmeno` (jméno řidiče) a `seznam_baliku` (seznam balíků k doručení, na začátku je prázdný).
- Přidej třídě metodu `prirad_balik`, která bude mít jeden parametr - `balik` (balík k doručení, může se jednat i o cenný balík). Funkce nejprve zkontroluje, zda balík již nebyl doručen. Pokud ano, vypíše funkce text: `"Nelze přiřadit, balík již byl doručen."` Pokud balík ještě nebyl doručen, je přidán do seznamu balíků `seznam_baliku` (použij funkci `append`).
- U řidiče chceme sledovat, kolik by měl ještě doručit balíků. Napiš funkci `zbyva_baliku`, která vrátí počet balíků, které má řidič přiřazené a ještě je nedoručil.
