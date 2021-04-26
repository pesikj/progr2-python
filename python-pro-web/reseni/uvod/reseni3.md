## První úkol

Soubor `views.py`, přidán pohled `VytvorKontakt` a `KontaktUlozen` a importy.

```python
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from . import models
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView

class VytvorKontakt(CreateView):
    model = models.Konakt
    template_name = "vytvor_kontakt.html"
    fields = ["jmeno", "prijimeni", "email", "datum_posledniho_kontaktu", "organizace"]
    success_url = reverse_lazy('kontakt_ulozen')

class KontaktUlozen(TemplateView):
    template_name = "kontakt_ulozen.html"

```

Šablona `base.html`, může tam být cokoli, není povinné.

```html
<h2>Správa kontaktů Czechitas</h2>
```


Šablona `vytvor_kontakt.html`. Není nutné používat Bootstrap.

```html
{% extends "base.html" %}
{% load bootstrap4 %}

{% block content %}
<form method="post">
    {% csrf_token %}
    {% bootstrap_form form %}
    {% buttons %}
        <input type="submit" value="Submit" class="btn btn-primary">
    {% endbuttons %}
</form>
{% endblock %}
```

Šablona `potvrzeni_kontaktu.html`.

```html
Kontakt byl uložen.
```

Soubor `urls.py`. Do seznamu je přidáno `vytvor-kontakt`.

```python
    path("vytvor-kontakt/", views.VytvorKontakt.as_view(), name="vytvor_kontakt"),
]

```

## Druhý úkol

Přidán nový pohled `VytvorKontaktKOrganizaciView`. Šablona zůstává stejná.

```python
class VytvorKontaktKOrganizaciView(CreateView):
    model = models.Konakt
    template_name = "vytvor_kontakt.html"
    fields = ["jmeno", "prijimeni", "email", "datum_posledniho_kontaktu"]
    success_url = reverse_lazy('kontakt_ulozen')

    def form_valid(self, form):
        id_organizace = self.kwargs['pk']
        organizace = models.Organizace.objects.get(pk=id_organizace)
        form.instance.organizace = organizace
        return super().form_valid(form)
```

Přidána nová URL adresa na nový pohled.

```python
path("organizace/<int:pk>/vytvor-kontakt", views.VytvorKontaktKOrganizaciView.as_view(), name="vytvor_kontakt_k_organizaci"),
```

Přidáno tlačítko s odkazem k detailu organizace.

```html
{% url 'vytvor_kontakt_k_organizaci' object.pk as target_url %}
{% bootstrap_button "Přidej kontakt" href=target_url button_type="link" button_class="btn-info" %}
```
