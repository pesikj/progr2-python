---
title: Zkušební doba
demand: 3
---

U zaměstnanců budeme nově evidovat, jestli jsou ve zkušební době. 

- Rozšiřte funkci `__init__` třídy `Employee` o parametr `probation`, který bude typu `bool`. Tuto hodnotu uložte jako atribut třídy `Employee`.
- Upravte funkci `__init__` třídy `Manager`. Hodnotu parametru `probation` předejte funkci `__init__` třídy `Employee`.
- Upravte funkci `getInfo`. Pokud je zaměstnanec ve zkušební době, přidát k jeho/jejímu výpisu text `Je ve zkušební době.`