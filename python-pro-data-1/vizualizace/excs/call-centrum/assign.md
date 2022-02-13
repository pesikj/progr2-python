---
title: Call centrum
demand: 2
---


V souboru [callcentrum.txt](assets/callcentrum.csv) najdete několik tisíc záznamů pro call centrum, které udávají časy mezi jednotlivými příchozími hovory v minutách a vteřinách. Načtěte tato data do série v Pythonu. Časy převeďte na vteřiny a zobrazte jejich histogram a boxplot. Co lze z těchto dvou grafů vyčíst?

K převodu na vteřiny můžeš použít metodu `str.split()`. Pomocí ní rozdělíš hodnoty minut a vteřit do samostatných sloupců. Pomocí metody `astype(int)` převedeš hodnoty na čísla. Poté pomocí počítaných sloupců můžeš spočítat celkový počet vteřin.

```pycon
import requests

r = requests.get("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/vizualizace/excs/call-centrum/assets/callcentrum.csv")
open("callcentrum.csv", "wb").write(r.content)

callcentrum = pandas.read_csv("callcentrum.csv")
callcentrum = callcentrum["hodnota"].str.split(':', expand=True).astype(int)
```
