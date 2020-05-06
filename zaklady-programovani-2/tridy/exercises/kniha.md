---
title: Kniha
demand: 4
---

Nyní píšeme software pro knihkupce. Vytvoř tedy třídu `Book`, která reprezentuje knihu. Každá kniha bude mít atributy `authors` (typ `str`), `title` (typ `str`) a `price` (typ `float`). Hodnoty nastav ve funkci `__init__`. 

- Přidej knize funkci `getInfo`, která vypíše informace o knize v nějakém pěkném formátu.
- Občas se stane, že se kniha moc neprodává a knihkupec se snaží nalákat kupující slevou. Přidej funkci `discount`, která bude mít jeden parametr - velikost slevy v procentech. Funkce sníží cenu knihy o dané procento.