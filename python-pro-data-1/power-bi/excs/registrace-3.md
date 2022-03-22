---
title: Registrace po týdnech
demand: 4
---

Pro delší časovou řadu by bylo zajímavé zobrazit si počty registrací uživatelů po týdnech. Týdny v hierarchii data nejsou (a ani být nemohou, protože řada týdnů spadá do dvou různých měsíců). Lze ale využít funkci [weeknum](https://docs.microsoft.com/en-us/dax/weeknum-function-dax) a přidat nový sloupec s číslem týdne. Dále zkus přidat Quick Measure, která bude určovat relativní změnu v počtu registrací oproti předchozímu týdnu. Výslek zobraz jako sloupcový graf.
