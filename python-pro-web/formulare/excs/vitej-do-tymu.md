---
title: Vídej do týmu!
demand: 3
---

Připrav rozhraní, pomocí kterého se mohou noví zájemci hlásit jako členové týmu. Pokud zatím nemáš vytvořený model `Person`, zkopíruj si ho z kódu níže a proveď migraci databáze.

```python
class Person(models.Model):
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  email = models.CharField(max_length=100)
```

- Uprav model `Person` tak, aby obsahovat pole `active`, které bude obsahovat informaci o tom, jestli je člen aktivní. Člen bude aktivní až poté, co jej jako aktivní označí někdo z Czechitas týmu. Vytvoř tedy pole typu `BooleanField` a jako parametr `default` nastav hodnotu `False`, tj. vlož do modelu `Person` následující řádek:

```python
active = models.BooleanField(default=False)
```

- Vytvoř pohled `PersonRegister`, která bude sloužit k registraci nového člena týmu. Pohledu vytvoř šablonu a nastav adresu.
- Vytvoř pohled a šabonu, na které bude uživatel přesměrován poté, co bude jeho přihláška zaregistrována. Chceš-li si ušetřit práci, můžeš uživatele přesměrovat na již existující pohled `ApplicationConfirmation`, protože tento obecný text se hodí pro oba případy.
- Otestuj formulář a zkontroluj, že se nová hodnota objeví v databázi.
