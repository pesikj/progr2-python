## Pobočky

`views.py`

```python

from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from . import models

class IndexView(TemplateView):
    template_name = "index.html"

class ContactsView(TemplateView):
    template_name = "contacts.html"
  
class AboutView(TemplateView):
    template_name = "about.html"

class CourseListView(ListView):
    model = models.Course
    template_name = "course_list.html"

class BranchListView(ListView):
    model = models.Branch
    template_name = "branch_list.html"

```

`branch_list.html`

```html

{% block content %}
<h2>Seznam poboček</h2>

<ul>
    {% for item in object_list %}
    <li>{{ item.name }}</li>
    {% endfor %}
</ul>
{% endblock %}
```

`urls.py`

```python
from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path("contacts", views.ContactsView.as_view(), name="contacts"),
    path("about", views.AboutView.as_view(), name="about"),
    path('kurzy/', views.CourseListView.as_view(), name='course_list'),
    path('pobocky/', views.BranchListView.as_view(), name='branch_list'),
]
```

## Kurzy a pobočky

`models.py`

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
  branch = models.ForeignKey("Branch", on_delete=models.PROTECT, null=True)

class Course(models.Model):
  name = models.CharField(max_length=100)
  start = models.DateTimeField()
  end = models.DateTimeField()
  description = models.CharField(max_length=1000)
  price = models.IntegerField()
  category = models.ForeignKey("Category", on_delete=models.PROTECT, null=True)
```

## Lidé a kurzy

`models.py`

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
  branch = models.ForeignKey("Branch", on_delete=models.PROTECT, null=True)

class Course(models.Model):
  name = models.CharField(max_length=100)
  start = models.DateTimeField()
  end = models.DateTimeField()
  description = models.CharField(max_length=1000)
  price = models.IntegerField()
  category = models.ForeignKey("Category", on_delete=models.PROTECT, null=True)
  lecturer = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, related_name="course_lecturer")
  event_coordinator = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True,related_name="course_event_coordinator")
```

## Vytvoření pohledu

`person_list.html`

```html
{% block content %}
<h2>Tým Czechitas</h2>

<ul>
    {% for item in object_list %}
    <li>{{ item.first_name }} {{ item.last_name }}</li>
    {% endfor %}
</ul>
{% endblock %}
```

`views.py`

```python
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from . import models

class IndexView(TemplateView):
    template_name = "index.html"

class ContactsView(TemplateView):
    template_name = "contacts.html"
  
class AboutView(TemplateView):
    template_name = "about.html"

class CourseListView(ListView):
    model = models.Course
    template_name = "course_list.html"

class BranchListView(ListView):
    model = models.Branch
    template_name = "branch_list.html"

class PersonListView(ListView):
    model = models.Person
    template_name = "person_list.html"
```

`urls.py`

```python
from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path("contacts", views.ContactsView.as_view(), name="contacts"),
    path("about", views.AboutView.as_view(), name="about"),
    path('kurzy/', views.CourseListView.as_view(), name='course_list'),
    path('pobocky/', views.BranchListView.as_view(), name='branch_list'),
    path('tym/', views.PersonListView.as_view(), name='branch_list'),
]
```

## Detail pobočky

`templates/branch_detail.html`

```html
<h2>Pobočka {{ object.name }}</h2>

<p>V pobočce pracuje {{ object.head_count }} lidí. </p>
```

`views.py`

```python
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from . import models

class IndexView(TemplateView):
    template_name = "index.html"

class ContactsView(TemplateView):
    template_name = "contacts.html"
  
class AboutView(TemplateView):
    template_name = "about.html"

class CourseListView(ListView):
    model = models.Course
    template_name = "course_list.html"

class BranchListView(ListView):
    model = models.Branch
    template_name = "branch_list.html"

class PersonListView(ListView):
    model = models.Person
    template_name = "person_list.html"

class CourseDetailView(DetailView):
    model = models.Course
    template_name = "course_detail.html"

class BranchDetailView(DetailView):
    model = models.Branch
    template_name = "branch_detail.html"
```

`urls.py`

```python
from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path("contacts", views.ContactsView.as_view(), name="contacts"),
    path("about", views.AboutView.as_view(), name="about"),
    path('kurzy/', views.CourseListView.as_view(), name='course_list'),
    path('pobocky/', views.BranchListView.as_view(), name='branch_list'),
    path('tym/', views.PersonListView.as_view(), name='branch_list'),
    path('kurz/<int:pk>', views.CourseDetailView.as_view(), name='course_detail'),
    path('pobocka/<int:pk>', views.BranchDetailView.as_view(), name='course_detail'),
]
```

## Navigační panel

```html
<ul>
    <li><a href="{% url 'contacts' %}">Kontaky</a></li>
    <li><a href="{% url 'course_list' %}">Kurzy</a></li>
</ul>
```
