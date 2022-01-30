---
title: Lidé a kurzy
demand: 3
---

- Pokud jsi v rámci předchozího bonusu přidala model `Person`, pracuj s ním. Pokud ne, nejprve ho do aplikace přidej podle zadání z předchozí kapitoly.
- Na jednom kurzu se zpravidla podílí více lidí. Přidej modelu `Course` dvě pole: `lecturer` a `event_coordinator`. Obě pole budou cizími klíči modelu `Person`.
- Pokud máš dvě vazby mezi modely, musíš těmto vyzbám přiřadit různá jména, aby byly mezi sebou rozeznatelné. To nastavíš pomocí parametru `related_name` u pole `ForeignKey`. Hodnota by měla být řetězec, např. `course_event_coordinator`.
- Zkus nějakému kurzu nastavit nějaké osoby.
