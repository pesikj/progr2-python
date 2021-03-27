# Vakcíny

Stáhni si soubor [country_vaccinations.csv](country_vaccinations.csv) o průběhu očkování proti nemoci COVID-19. 

Stažení souboru pomocí `requests`:

```python
import requests

url = 'https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/country_vaccinations.csv'
r = requests.get(url, allow_redirects=True, verify=False)
open('country_vaccinations.csv', 'wb').write(r.content)
```

Dále napiš následující dotazy:

* Dotaz na počty očkovaných (sloupec `total_vaccinations`) v jednotlivých státech dne `2021-03-10` (s datem pracuj úplně stejně jako s řetězcem, tj. nevyužívej modeul `datetime`, ale vlož do dotazu přímo řetězec).
* Dotaz na řádky, kde `2021-03-10` bylo naočkováno více než 1 mil. obyvatel.
* Podíváme se na extrémní hodnoty. Napiš dotaz na řádky, kde za daný den naočkování více než 100 tisíc lidí nebo naopak méně než 100 lidí.
* Vypiš informace o očkování za dny `2021-03-10` a `2021-03-11` pro státy `United Kingdom`, `Finland` a `Italy`. Použij např. funkci `isin()`.
* Vypiš informace o očkování pro `Japan` mezi daty `2021-03-03` a `2021-03-09`. Data v tomto formátu můžeš porovnávat pomocí operátorů `>=` a `<=` jako řetězce, tj. opět nemusíš použít modul `datetime`.
