Nyní si ukážeme, jak naše modely a naše data zobrazit uživatelům.

### Vytvoření šablony a pohledu

Víme, že webové stránky jsou vytovřené v jazyce HTML. Pojďme si tedy vytvořit HTML stránku, která bude obsahovat seznam našich kurzů. V rámci Djanga vytváříme tzv. šablony, což jsou HTML soubory, které jsou ale obohacené o speciální tagy.

První tag, který využijeme, je tag `for`. Ten slouží k vytvoření cyklu v rámci naší šablony. My potřebujeme cyklus, který projde všechny kurzy v naší aplikaci a vypíše je. Všechny kurzy máme umístěné v proměnné `object_list`.

`templates/kurzy/kurzy_list.html`
```python
{% block content %}
<ol>
    {% for kurz in object_list %}
    <li>{{ kurz.nazev }}</li>
    {% endfor %}
</ol>
{% endblock %}
```

```python
from django.shortcuts import render

from django.views.generic import ListView
from . import models

class KurzyView(ListView):
    model = models.Kurz
    template_name = "kurzy/kurzy_list.html"
```

```python
from django.urls import path

from . import views

urlpatterns = [
    path('', views.KurzyView.as_view(), name='index'),
]
```