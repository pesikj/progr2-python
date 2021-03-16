---
title: Registrační značka
demand: 3
---

Standardní registrační značky automobilů, vydané od roku 2004, mají následující formát:

* Na prvním místě je číslo.
* Na druhém místě písmeno, které označuje kraj.
* Na třetím místě je číslo nebo písmeno.
* Na čtvrtém místě je mezera a následuje čtveřice čísel.

Napiš regulární výraz, který bude kontrolovat formát registrační značky. Ověřit si ho můžeš na následujících značkách, které mají správný formát.

```
4A6 8244
6B2 6635
2AD 3824
7C1 5025
```

Značky níže mají špatný formát.

```
AC8 5484
924 1541
8A2 25C2
3P 4564
1A 25364
```

Zkus nyní regulární výraz ještě zdokonalit a povol na druhém místě pouze znak, který označuje nějaký konkrétní kraj. Platné znaky na druhém místě tedy budou tyto: `A, B, C, E, H, J, K, L, M, P, S, T, U, Z`.
