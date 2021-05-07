---
title: Vídej do týmu!
demand: 3
---

Připrav rozhraní, pomocí kterého se mohou noví zájemci hlásit jako členové týmu.

- Uprav model `Person` tak, aby obsahovat pole `active`, které bude obsahovat informaci o tom, jestli je člen aktivní. Člen bude aktivní až poté, co jej jako aktivní označí někdo z Czechitas týmu. Vytvoř tedy pole typu `BooleanField` a jako parametr `default` nastav hodnotu `False`.
- Vytvoř pohled `PersonRegister`, která bude sloužit k registraci nového člena týmu. Pohledu vytvoř šablonu a nastav adresu.
- Vytvoř pohled a šabonu, na které bude uživatel přesměrován poté, co bude jeho přihláška zaregistrována. Zobraz např. informaci o tom, že přihláška byla zaregistrována a že zájemce v nejbližší době kontaktujeme.
- Otestuj formulář a zkontroluj, že se nová hodnota objeví v databázi.
