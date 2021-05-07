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

