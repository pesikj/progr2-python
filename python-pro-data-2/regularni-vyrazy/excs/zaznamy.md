---
title: Záznamy
demand: 2
---

Uvažujme aplikaci, která si ukládá informace o činnosti uživatelů do textového souboru. Příklad souboru je níže.

```py
zaznamy = """
searchNumber: pavca.czechitas action: search phone number of user dita
user: pavca action: send sms to phone number +420728123456
user: jirka: action: send 2 sms to phone number +420734123456
"""
```

* Napiš program, který vypíše všechna telefonní čísla, která jsou v textovém souboru zmíněna.
* Nahraď tato telefonní čísla nějakým řetězcem (např. "XXX"), aby nebyla v záznamech dostupná.

