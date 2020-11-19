---
title: Studenti
demand: 3
---

Stáhněte si datové sety, se kterými budeme pracovat v tomto cvičení: [jmena.csv](assets/jmena.csv), [studenti1.csv](assets/studenti1.csv), [studenti2.csv](assets/studenti2.csv). První set už známe z minulé lekce. Druhé dva sety obsahují seznam studentů na nějaké menší IT fakultě. Proveďte následující úkoly a zodpovězte předložené otázky.

1. Načtěte dva datové sety studentů do oddělených pandas DataFrame a pomocí funkce `concat` je spojte do jednoho setu.
1. Pokud studentovi chybí ročník, znamená to, že již nestuduje. Pokud mu chybí číslo skupiny, znamená to, že jde o dálkového studenta. Kolik studentů v datovém setu již nestuduje a kolik jsou dálkoví studenti?
1. Vyčistěte data od studentů, kteří nestudují nebo studují jen dálkově. Nadále budeme pracovat pouze s prezenčními studenty.
1. Zjistěte, kolik prezenčních studentů je v každém z oborů.
1. Zjistěte průměrný prospěch studentů v každém oboru.
1. Načtěte datový set s křestními jmény. Proveďte join s tabulkou studentů tak, abychom věděli pohlaví jednotlivých studentů.
1. Zjistěte, zda na naší fakultě studují IT spíše ženy nebo spíše muži.