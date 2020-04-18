---
title: Balík
demand: 4
---

Pokračuj ve své práci pro zásilkovou společnost. Společnost nyní eviduje jednotlivé řidiče a eviduje balíky, které má každý řidič doručit.

- Vytvoř třídu `Driver`, která má dva atributy: `name` (jméno řidiče) a `packageList` (seznam balíků k doručení, na začátku je prázdný).
- Přidej třídě funkci `assignPackage`, která bude mít jeden parametr - `package` (balík k doručení).
- Funkce nejprve zkontroluje, zda balík již nebyl doručen. Pokud ano, vypíše funkce text: "Nelze přiřadit, balík již byl doručen."
- Pokud balík ještě nebyl doručen, je přidán do seznamu balíků `packageList` (použij funkci `assign`).
