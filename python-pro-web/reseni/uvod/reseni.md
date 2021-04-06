```
python manage.py startapp crm
```

```python
#views.py

from django.http import HttpResponse
from django.views import View

class Index(View):
    def get(self, request):
        return HttpResponse('Vítej v CRM systému Czechitas!')
```

```python
# crm/urls.py

from django.urls import path

from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
]
```

```python
# czechitas/urls.py

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("kurzy.urls")),
    path('crm/', include("crm.urls"))
]
```

```python
# models.py

from django.db import models

class Kontakt(models.Model):
    jmeno = models.CharField(max_length=100)
    prijmeni = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    posledni_kontakt = models.DateTimeField()
```

```python
# settings.py - INSTALLED_APPS

INSTALLED_APPS = [
    'kurzy.apps.KurzyConfig',
    'crm.apps.CrmConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

```
python manage.py makemigrations
python manage.py migrate
```

```python
# admin.py

from django.contrib import admin
from . import models

admin.site.register(models.Kontakt)
```
