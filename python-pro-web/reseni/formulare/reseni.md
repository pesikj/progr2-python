## Vídej do týmu!

`views.py`

```python
from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.views.generic.base import TemplateView
from . import models
from django.urls import reverse_lazy

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

class ApplicationCreateView(CreateView):
    model = models.Application
    template_name = "application_create.html"
    fields = ["email", "first_name", "last_name", "motivation", "course"]
    success_url = reverse_lazy("application_confirmation")

class ApplicationConfirmation(TemplateView):
    template_name = "application_confirmation.html"

class PersonRegisterView(CreateView):
    model = models.Person
    fields = ["first_name", "last_name", "email"]
    template_name = "person_register.html"
    success_url = reverse_lazy("application_confirmation")
```

```html
<form method="post">{% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="Odeslat">
</form>
```

`courses/urls.py`

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
    path('prihlaska/<int:pk>/', views.ApplicationCreateView.as_view(), name='application_create'),
    path('prihlaska/potvrzeni/', views.ApplicationConfirmation.as_view(), name='application_confirmation'),
    path('prihlaska-clena-tymu/', views.PersonRegisterView.as_view(), name='person_register'),
]
```
