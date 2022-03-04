---
title: Práce s kódem
demand: 5
---

Chceš pomoci firmě, která vyvinula e-mailového klienta pro český trh. Níže je kousek kódu, který generuje popisky políček pro zadání adres příjemců, příjemců v kopii, příjemců ve skryté kopii a tlačítka pro odeslání nebo uložení. Nyní by firma ráda expandovala na německý trh. Bohužel vývojáři vkládali popisky do aplikace jako řetězce a ztratili přehled o řetězcích, které v aplikaci mají a které je potřeba je přeložit.

1. Zkopíruj si následující kód, uložený jako řetězec, do svého programu.
1. Vyhledej v programu všechny řádky, kde je ukládán řetězec do proměnné, např. řádek `sender_field_title = "Příjemce"`.
1. Pomocí dalšího regulárního výrazu vytáhni z každého řádku samotný řetězec (může být i s uvozovkami), např. `"Příjemce"`.

```
kod = """
sender_field_title = "Příjemce"
copy_field_title = "Kopie"
if blind_copy == True:
    blind_copy_title = "Skrytá kopie"
if action == "send":
    button_title = "Odeslat"
else:
    button_title = "Uložit koncept"
"""
```


