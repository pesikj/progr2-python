## Vytvoření pohledu

`templates/contacts.html`

```html
<h2>Kontakty</h2>

<p>První kontakt</p>
<p>Druhý kontakt</p>
```

`templates/views.py`

```python
from django.shortcuts import render
from django.views.generic.base import TemplateView

class IndexView(TemplateView):
    template_name = "index.html"

class ContactsView(TemplateView):
    template_name = "contacts.html"
```


`templates/urls.py`

```python
from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path("contacts", views.ContactsView.as_view(), name="contacts")
]
```

## O nás

`about.html`

```html

<h2>O nás</h2>

<p>
  Informace o nás.
</p>
```

`templates/views.py`

```python
from django.shortcuts import render
from django.views.generic.base import TemplateView

class IndexView(TemplateView):
    template_name = "index.html"

class ContactsView(TemplateView):
    template_name = "contacts.html"
  
class AboutView(TemplateView):
    template_name = "about.html"
```

`templates/urls.py`

```python
from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path("contacts", views.ContactsView.as_view(), name="contacts"),
    path("about", views.AboutView.as_view(), name="about"),
]
```

## Pobočky

`templates/models.py`

```python

from django.db import models

class Kurz(models.Model):
  name = models.CharField(max_length=100)
  start = models.DateTimeField()
  end = models.DateTimeField()
  description = models.CharField(max_length=1000)
  price = models.IntegerField()

class Branch(models.Model):
  name = models.CharField(max_length=100)
  founded_on = models.DateField() # nebo DateTimeField
  email = models.CharField(max_length=50)
  head_count = models.IntegerField()
```

## Lidé

```python
from django.db import models

class Kurz(models.Model):
  name = models.CharField(max_length=100)
  start = models.DateTimeField()
  end = models.DateTimeField()
  description = models.CharField(max_length=1000)
  price = models.IntegerField()

class Branch(models.Model):
  name = models.CharField(max_length=100)
  founded_on = models.DateField() # nebo DateTimeField
  email = models.CharField(max_length=50)
  head_count = models.IntegerField()

class Person(models.Model):
  # Může být i jedno pole name
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  email = models.CharField(max_length=100)
  # příklad dalšího pole
  mobile_number = models.CharField(max_length=100)
```

