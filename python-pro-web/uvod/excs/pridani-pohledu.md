---
title: Vytvoření pohledu
demand: 3
---

Na webu Czechitas je nejen úvodní stránka, ale řada dalších stránek. Jednou z ní je stránka s kontakty.

Vytvoř pohled `ContactsView` a k němu šablonu `contacts.html`, která bude obsahovat nějaké kontaktní informace.

Do souboru `kurzy/urls.py` přidej adresu stránky s kontakty. V seznamu `urlpatterns` přibude nová hodnota:

```python
path("contacts", views.ContactsView.as_view(), name="kontakty")
```

Celý soubor tedy bude vypadat takto:

```python
from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path("contacts", views.ContactsView.as_view(), name="kontakty")
]
```


Otevři si odkaz [http://127.0.0.1:8000/contacts/](http://127.0.0.1:8000/contacts/) a ověř, že se zobrazí stránka s kontakty.
