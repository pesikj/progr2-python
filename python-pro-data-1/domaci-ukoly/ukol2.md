# Hra o trůny

Stáhni si soubor [character-deaths.csv](character-deaths.csv), který obsahuje informace o smrti některých postav z prvních pěti knih románové série Píseň ohně a ledu (A Song of Fire and Ice).

Stažení souboru pomocí `requests`:

```python
import requests

url = 'https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/character-deaths.csv'
r = requests.get(url, allow_redirects=True, verify=False)
open('character-deaths.csv', 'wb').write(r.content)
```

*Pozn. Úkoly se týkají zcela nevýznamných postav, proto je riziko spoileru minimální :-)*

* Načti soubor do tabulky (DataFrame) a nastav sloupec `Name` jako index.
* Zobraz si sloupce, které tabulka má. Posledních pět sloupců tvoří zkratky názvů knih a informace o tom, jestli se v knize postava vyskytuje.
* Použij *funkci* `loc` ke zjištění informací o smrti postavy jménem "Hali".
* Použij *funkci* `loc` k zobrazení řádků mezi "Gevin Harlaw" a "Gillam".
* Použij *funkci* `loc` k zobrazení řádků mezi "Gevin Harlaw" a "Gillam" a sloupce `Death Year`.
* Použij *funkci* `loc` k zobrazení řádků mezi "Gevin Harlaw" a "Gillam" a informace o tom, v jakých knihách se postava vyskytuje, tj. vypiš všechny sloupce mezi `GoT` a `DwD`.
