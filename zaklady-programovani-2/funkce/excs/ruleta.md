---
title: Ruleta
demand: 5
---

Napiš funkci, která bude jednoduchou simulací rulety. Budeme uvažovat pouze možnost sázení na řady. Uživatel si může vybrat jednu ze tří řad:

- první řada (hodnoty 1, 4, 7 atd.),
- druhá řada (hodnoty 2, 5, 8 atd.),
- třetí řada (hodnoty 3, 6, 9 atd.).

- Zeptej se uživatele, na kterou ze tří řad sází a na výši sázky. 
- Vytvoř funkci `roulette`, která bude mít parametry číslo řady a výši sázky. Pomocí funkce `randint` z modulu `random` vygeneruj náhodné číslo v rozsahu od 0 (včetně) do 36.  Vyhodnoť, do které řady číslo náleží. Nezapomeň, že 0 nepatří do žádné z řad a pokud padne, uživatel vždy prohrává.
- Funkce `roulette` vrací hodnotu výhry. Pokud uživatel vsadil na správnou řadu, vyhrává dvojnásobek sázky, v opačném případě nevyhrává nic jeho sázka propadá.
