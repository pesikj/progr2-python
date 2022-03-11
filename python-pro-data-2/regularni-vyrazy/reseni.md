# Cvičení: Regulární výrazy

## Předčíslí
```
\d{0,6}-?\d{6,10}/\d{4}
```
https://regex101.com/r/n7x9Wg/1

Není to dokonalé, ale jako řešení stačí
## Číslo účtu podruhé
```
[12][1-3]\d{6,8}/2100
```
https://regex101.com/r/VoUKri/3

## Registrační značka
```
\d[A-Z]\w \d{4}
```
https://regex101.com/r/wXlJDo/1
```
\d(A|B|C|E|H|J|K|L|M|P|S|T|U|Z)\w \d{4}
```
https://regex101.com/r/ZrPyTs/1
## Telefonní číslo
```
(\+420)? ?\d{3} ?\d{3} ?\d{3}
```
https://regex101.com/r/O50NSs/1
## Ministerstva
```
Ministerstvo[\w ]*
```
https://regex101.com/r/wrXVhD/1
## Nápravy
```
\w{1}\,\w{1} m
```
https://regex101.com/r/RydgSW/1
```
\w{2}\,\w{2} t
```
https://regex101.com/r/hbwv8Z/1
## Slavný soude
```
\d{2} [A-Z]{1,3} \d{1,4}/\d{4}
```
https://regex101.com/r/zy8n4X/1
## Ave, Caesar!
```
I?(V|X)?I{0,3}
(V|X|I)+
```
https://regex101.com/r/D31W3G/2

Není to dokonalé, ale jako řešení stačí

# Cvičení: Regulární výrazy v Pythonu

## Uživatelské jméno
```
import re
regularni_vyraz = re.compile(r"[a-z]{1,8}")
uzivatelske_jmeno = input("Zadej uživatelského jména: ")
vysledek = regularni_vyraz.fullmatch(uzivatelske_jmeno)
if vysledek:
    print("Uživatelské jméno je v pořádku.")
else:
    print("Uživatelské jméno nesplňuje požadavky")
```

## E-mail s tečkou

```
import re
regularni_vyraz = re.compile(r"\w+\.\w+@\w+\.cz")
email = "jiri.pesik@python.cz"
vysledek = regularni_vyraz.fullmatch(email)
if vysledek:
    print("E-mail jméno je v pořádku.")
```

## Záznamy

```
zaznamy = """
searchNumber: pavca.czechitas action: search phone number of user dita
user: pavca action: send sms to phone number +420728123456
user: jirka: action: send 2 sms to phone number +420734123456
"""
import re
regularniVyraz = re.compile(r"[+\d]{13}")
vysledky = regularniVyraz.findall(zaznamy)
for vysledek in vysledky:
    print(vysledek)
anonymni_zaznamy = regularniVyraz.sub("X" * 9, zaznamy)
print(anonymni_zaznamy)
```

## Adresy stránek

```
email_s_radami = """
Ahoj,
posílám ti pár tipů, kam se podívat. https://realpython.com nabízí spoustu článků i kurzů. http://docs.python.org nabízí tutoriál i rozsáhlou dokumentaci. http://www.learnpython.org nabízí hezky strukturovaný kurz pro začátečníky, rozebírá ale i nějaká pokročilejší témata. https://www.pluralsight.com je placený web, který ale kvalitou kurzů víceméně nemá konkurenci. Určitě ale sleduj i web https://www.czechitas.cz a přihlašuj se na naše kurzy!
"""
import re
regularni_vyraz = re.compile(r"https?://[\w\.]*")
vysledky = regularni_vyraz.findall(email_s_radami)
for vysledek in vysledky:
    print(vysledek)
```

## IP adresy

```
import re
regularni_vyraz = re.compile(r"[12]?\d{1,2}\.[12]?\d{1,2}\.[12]?\d{1,2}\.[12]?\d{1,2}")
uzivatelske_jmeno = input("Zadej adresu serveru: ")
vysledek = regularni_vyraz.fullmatch(uzivatelske_jmeno)
if vysledek:
    print("Odesílám zprávu.")
else:
    print("Adresa není platná.")
```

## Práce s kódem

```
kod = """
sender_field_title = "Příjemce"
copy_field_title = "Kopie"
if blind_copy:
    blind_copy_title = "Skrytá kopie"
if action == "send":
    button_title = "Odeslat"
else:
    button_title = "Uložit koncept"
"""

import re
regularni_vyraz = re.compile(r"[\w_]* \= \"[\w ]*\"")
vysledky = regularni_vyraz.findall(kod)
for vysledek in vysledky:
    regularni_vyraz_vnitrni = re.compile(r"\"[\w ]*\"")
    vysledky_vnitrni = regularni_vyraz_vnitrni.findall(vysledek)
    print(vysledky_vnitrni[0])

```
