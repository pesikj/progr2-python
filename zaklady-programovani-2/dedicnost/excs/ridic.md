---
title: Řidič
demand: 5
---

Pokračuj ve své práci pro zásilkovou společnost. Společnost nyní eviduje jednotlivé řidiče a eviduje balíky, které má každý řidič doručit.

- Vytvoř třídu `Driver`, která má dva atributy: `name` (jméno řidiče) a `packageList` (seznam balíků k doručení, na začátku je prázdný).
- Přidej třídě funkci `assignPackage`, která bude mít jeden parametr - `package` (balík k doručení, může se jednat i o cenný balík).
- Funkce nejprve zkontroluje, zda balík již nebyl doručen. Pokud ano, vypíše funkce text: `"Nelze přiřadit, balík již byl doručen."`
- Pokud balík ještě nebyl doručen, je přidán do seznamu balíků `packageList` (použij funkci `append`).
- U řidiče chceme sledovat, kolik by měl ještě doručit balíků. Napiš funkci `remainingPackages`, která vrátí počet balíků, které má řidič přiřazené a ještě je nedoručil.
