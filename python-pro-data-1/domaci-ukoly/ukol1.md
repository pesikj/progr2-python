# Twilio

Stáhni si soubor [twlo.csv](twlo.csv), který obsahuje informace o vývoji ceny akcie firmy [Twilio](https://www.twilio.com/) od začátku roku 2020. Soubor obsahuje informace o otevírací, minimální, maximální a uzavírací ceně za každý den.

Stažení souboru pomocí `requests`:

```python
import requests

url = 'https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/twlo.csv'
r = requests.get(url, allow_redirects=True, verify=False)
open('twlo.csv', 'wb').write(r.content)
```

* Zjisti, kolik má soubor řádek a kolik sloupců.
* Podívej se na 5 řádků s cenami na začátku souboru, využij k tomu *funkci* `iloc` i funkci `head()`.
* U akcií nás zajímají především nejnovější ceny. Podívej se na poslední řádek souboru. Tentokrát využij způsob dle vlastního výběru :-)
* Počet řádků ulož do proměnné `pocet_radku` jako číslo.
* Pokud *funkci* `iloc` zadáš číslo řádku i číslo sloupce, odkazuješ se na jednu konkrétní hodnotu. Pandas ti tuto hodnotu vrací jako číslo. Načti si tedy první hodnotu zavírací ceny (sloupec `Close`) v souboru a poslední hodnotu zavírací ceny v souboru. Vypočítej, o kolik procent se zvýšila hodnota akcie.
* Vyber si sloupec s maximální cenou akcie (sloupec `High`) za jednotlivé dny pomocí `loc` nebo `iloc` jako sérii. Na sloupec použij funkci `.max()`, abys zjistila maximální zaznamenanou cenu akcie za celé období. Obdobným způsobem použij funkci `.min()` na sloupec `Low`. Z těchto hodnot zjistíš maximální rozsah obchodní ceny akcie, což je základ jednoho z akciových ukazatelů (*price range*).
