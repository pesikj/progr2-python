# Teplota ve městech

Stáhni si soubor [temperature.csv](temperature.csv), který obsahuje informace o průměrné teplotě v různých městech v **listopadu 2017**.

```python
import requests

url = "https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv"
r = requests.get(url, allow_redirects=True, verify=False)
open('temperature.csv', 'wb').write(r.content)
```

Vypiš si prvních několik řádků, ať si prohlédneš strukturu tabulky. 

Dále napiš následující dotazy:
* Dotaz na měření, která byla provedena v Praze. Je na datech něco zvláštního? Napadá tě, čím to může být? [Zde](https://cs.wikipedia.org/wiki/Stupe%C5%88_Fahrenheita) je nápověda.
* Dotaz na měření, ve kterých je teplota (sloupec `AvgTemperature`) vyšší než 80 stupňů.
* Dotaz na měření, ve kterých je teplota vyšší než 60 stupňů a současně bylo měření provedeno v regionu (sloupec `Region`) Evropa (Europe).
* Dotaz na extrémní hodnoty, tj. měření, ve kterých je teplota vyšší než 80 stupňů nebo menší než - 20 stupňů.

**Pokročilá varianta**

Nainstaluj si modul `pytemperature` a zkus si vytvořit nový sloupec, který bude obsahovat průměrnou templotu ve stupních Celsia. Ve svém programu nejprve proveď import modulu `pytemperature`. Nový sloupec pak přidáš do tabulky tak, že nalevo od `=` vložíš tabulku a název nového sloupce do hranatých závorek. Napravo pak můžeš provádět výpočty pomocí již existujících sloupců. Můžeš např. použít funkci `f2c` z modulu `pytemperature`, která převede teplotu ze stupňů Fahrenheita na stupně Celsia.

```python
import pytemperature
df["AvgTemperatureCelsia"] = pytemperature.f2c(df["AvgTemperature"])
```

Nyní můžeš zpracovat následující příklady:

* Dotaz na měření, ve kterých je teplota (sloupec `AvgTemperatureCelsia`) vyšší než 30 stupňů Celsia.
* Dotaz na měření, ve kterých je teplota vyšší než 15 stupňů Celsia a současně bylo měření provedeno v regionu (sloupec `Region`) Evropa (Europe).
* Dotaz na extrémní hodnoty, tj. měření, ve kterých je teplota vyšší než 30 stupňů Celsia nebo menší než -10 stupňů. Jsou některé hodnoty podezřelé?
