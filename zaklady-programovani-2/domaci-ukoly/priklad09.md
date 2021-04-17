# Maturita

```python
vysledky = [
  {"Jméno": "Mirek Dušín", "Český jazyk": 1, "Anglický jazyk": 2, "Matematika": 1, "Biologie": 1, "Zeměpis": 1},
  {"Jméno": "Jarka Metelka", "Český jazyk": 3, "Anglický jazyk": 1, "Matematika": 3, "Dějepis": 2, "Ekonomika": 5},
  {"Jméno": "Jindra Hojer", "Český jazyk": 2, "Anglický jazyk": 2, "Matematika": 1, "Biologie": 3, "Chemie": 3},
  {"Jméno": "Červenáček", "Český jazyk": 1, "Anglický jazyk": 1, "Matematika": 1, "Fyzika": 2, "Informatika": 4},
  {"Jméno": "Rychlonožka", "Český jazyk": 4, "Anglický jazyk": 3, "Matematika": 2, "Chemie": 1, "Biologie": 4},
]
```

Uvažuj program, který bude pracovat s výsledky z maturitní zkoušky. Každý student
může mít jeden z následujících výsledků:
- "Prospěl s vyznamenáním", pokud je průměr jeho známek maximálně 1.5 a nemá žádnou trojku.
- "Neprospěl", pokud má alespoň jednu pětku.
- "Prospěl", pokud nemá vyznamenání a současně nedostal žádnou pětku.

Přidej funkci `ohodnot_studenta()`, která bude mít jeden parametr, kterým
je slovník se známkami studenta. Funkce rozhodne, zda student prospěl, prospěl s
vyznamenáním nebo neprospěl podle výše popsaných kritérií.

Dále napiš cyklus, který projde seznam `vysledky` a pomocí funkce
`ohodnot_studenta()` zjistí prospěch studenta. Následně pro každého studenta vypíše jeho
jméno a informaci o tom, zda prospěl, neprospěl či prospěl s vyznamenáním.

Výstup tvého programu by mohl vypadat např. takto:

```
Mirek Dušín: Prospěl s vyznamenáním
Jarka Metelka: Neprospěl
Jindra Hojer: Prospěl
Červenáček: Prospěl s vyznamenáním
Rychlonožka: Prospěl
```