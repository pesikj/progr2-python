---
title: Krabicový graf
demand: 4
---

V souboru [data_with_ids.csv](https://raw.githubusercontent.com/pesikj/progr2-python/master/python-pro-data-1/power-bi/excs/krabicovy-graf/assets/data_with_ids.csv) jsou data o bankovních transakcích. Proveď import těchto dat do Power BI. Následně vytvoř dvojici krabicových grafů pro velikost příchozích plateb a velikost odchozích plateb. Pozor, jde o číselnou hodnotu, je třeba Power BI říct, aby neprováděl agregaci dat před vložením do naší vizualizace. Při vytváření grafu můžeš např. pomocí dotazu vytvořit dva samostatné `DataFrame`, jeden s příjmy a jeden s výdaji (data můžeš rozdělit pomocí dotazů). Po provedení dotazů proveď reset indexů u obou dotazů. Následně můžeš do nového `DataFrame` vložit sloupce `amount` vedle sebe (s vhodným pojmenováním) a zobrazit krabicový graf.
