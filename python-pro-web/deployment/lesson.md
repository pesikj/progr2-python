
```
pip install gunicorn django-heroku python-decouple
```

```
pip freeze > requirements.txt  
```


Vytvořte soubor `Procfile`

```
web: gunicorn (Your app).wsgi
```

```python
import os
import django_heroku
import dj_database_url
from decouple import config
```

```python
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

```python
django_heroku.settings(locals())
```

```
heroku config:set DISABLE_COLLECTSTATIC=1
python manage.py collectstatic
```


https://dev.to/developerroad/tutorial-deploying-a-django-app-on-heroku-4k6o