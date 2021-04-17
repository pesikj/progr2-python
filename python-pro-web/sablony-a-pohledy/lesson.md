Nyní si ukážeme, jak naše modely a naše data zobrazit uživatelům.

## Vytvoření seznamu kurzů

Víme, že webové stránky jsou vytovřené v jazyce HTML. Pojďme si tedy vytvořit HTML stránku, která bude obsahovat seznam našich kurzů. V rámci Djanga vytváříme tzv. šablony, což jsou HTML soubory, které jsou ale obohacené o speciální tagy. Přehled tagů, které jsou v Djangu k dispozici, najdeš [zde](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/). Šablony v Djangu ukládáme do adresáře `templates`. Pro přehlednost je lepší, když šablonu pro nějaký konkrétní model uložíme do podadresáře, který má jméno daného modelu. 

Naše první šablona bude mít za úkol zobrazit kurzy, které jsou aktuálně v nabídce. Pro takový typ šablony je vhodné vložit do názvu `list`. Vytvoříme tedy šablonu `templates/kurzy/kurzy_list.html`.

### Vytvoření pohledu

Začneme s tím, že vytvoříme pohled. Tentokrát náš pohled založíme na třídě `ListView`. Tato třída patří mezi [generické pohledy](https://docs.djangoproject.com/en/3.2/topics/class-based-views/generic-display/), které mají zabudovanou určitou funkcionalitu a jsou svázány s nějakým modelem. Třída `ListView` má za úkol zobrazit uživateli seznam záznamů nějakého modelu. Nový pohled musí mít nastavené dvě klíčové informace:

- model, jehož záznamy má zobrazit (atribut `model`),
- šablonu, kterou má použít k vytvoření webové stránky (atribut `template_name`).

Vytvoříme tedy třídu `KurzyView` a nastavíme jí potřebné atributy.

```python
from django.shortcuts import render

from django.views.generic import ListView
from . import models

class KurzyView(ListView):
    model = models.Kurz
    template_name = "kurzy/kurzy_list.html"
```

Našemu pohledu už můžeme přidat i URL adresu. Nemusíme přidávat novou adresu, ale můžeme nahradit model `MujPrvniPohled`, který už nepotřebujeme.

```python
from django.urls import path

from . import views

urlpatterns = [
    path('', views.KurzyView.as_view(), name='index'),
]
```

### Vytvoření šablony

Pojďme dát šabloně nějaký obsah. Jako první vytvoříme seznam všech kurzů. K tomu využijeme speciální tag `for`. Ten slouží k vytvoření cyklu v rámci naší šablony. Tento speciální tag zapisujeme do páru značek `{% %}`, abychom ho odlišili od zbytku HTML kódu. Současně musíme přidat i ukončovací tag `endfor`, protože v jazyce HTML by nám nefungoval tradiční přístup Pythonu založený na mezerách.

Náš cyklus projde všechny kurzy v naší aplikaci a vypíše je. Všechny kurzy máme umístěné v proměnné `object_list`, což zařídí pohled `KurzyView`, resp. jeho mateřská třída `ListView`. Jako pomocnou proměnnou v cyklu využijeme proměnnou `kurz`, do které cyklus postupně vloží všechny naše kurzy.

Máme-li proměnnou `kurz`, můžeme nyní do naší webové stránky vypsat libovolnou informaci o našem kurzu. Začneme s polem `nazev`. Abychom vypsání názvu kurzu odlišili od odstatních proměnných, zapíšeme ho do dvojice značek `{{ }}`.

Níže je výsledný kód naší šablony.

```python
{% block content %}
<ol>
    {% for kurz in object_list %}
    <li>{{ kurz.nazev }}</li>
    {% endfor %}
</ol>
{% endblock %}
```

## Vazby mezi modely

Modely jsou často mezi sebou provázané. Například víme, že Czechitas organizují kurzy do témat, např. Programuju, Tvořím web atd. Pojďme si vytvořit model, který bude tyto kategorie reprezentovat.

```python
class Kategorie(models.Model):
  nazev = models.CharField(max_length=100)
```

Jako druhý krok upravíme model `Kurz`, kterému přidáme nové pole `pobocka`, které je typu `ForeignKey` (tj. cizí klíč). Poli nastavíme parametr `null` jako `True`, což znamená, že toto pole nemusí mít vyplněnou hodnotu.

```python
class Kurz(models.Model):
  nazev = models.CharField(max_length=100)
  zacatek = models.DateTimeField()
  konec = models.DateTimeField()
  popis = models.CharField(max_length=1000)
  cena = models.IntegerField()
  kategorie = models.ForeignKey(Kategorie, on_delete=models.SET_NULL, null=True)
```

Následně opět provedeme migraci, abychom model přidali do databáze.

```
python manage.py makemigrations kurzy
python manage.py migrate
```

Abychom model `Kategorie` viděli v databázi, musíme jej ještě zaregistrovat.

```python
from django.contrib import admin
from . import models
admin.site.register(models.Kurz)
admin.site.register(models.Kategorie)
```

## Pohled pohledu na detail kurzu

### Vytvoření pohledu

### Vytvoření šablony

### Vytvoření odkazu
