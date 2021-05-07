V této lekci si řekneme něco o tom, jak vlastně provádíme vývoj webu.

## O vývoji webu

Vývoj a provoz webu je disciplína, která v sobě zahrnuje několik složek.

Definice toho, jak by webová stránka měla vypadat, nazýváme **kódování**. Zpravidla prováděno v jazyce HTML s využitím kaskádových stylů (CSS). HTML a CSS vlastně poskytují informace pro webový prohlížeč, jaké informace má zobrazit a jak je naformátovat.

K vytvoření webové stránky mohou stačit pouze tyto jazyky. Jedná se především o weby, které zobrazují nějaké statické informace (např. osobní web, životopis atd.). Všechny informace, které stránka obsahuje, pak musí být vloženy do HTML souborů jako text a stránka nemůže obsahovat žádné prvky pro komunikaci mezi uživatelem a správcem webu (např. formuláře).

Většina dnešních webů by si pouze s HTML nevystačila. Chceme-li si například vytvořit zpravodajský server, chceme dát uživatelům možnost přihlášení (placené články, diskuse) a editorům webu chceme poskytnout příjemné prostředí, kam mohou vkládat své články. Takový web již musí být propojený s nějakým úložištěm dat, nejčastěji s databází. V databázi jsou uloženy články, informace o uživatelských článcích, diskusní příspěvky, kategorie článků, obrázky a spousta dalších informací. Takový web již musí být naprogramovaný, protože HTML si neumí načíst informace s databáze nebo zajistit přihlášení uživatele.

### Prostředí pro vývoj webu

K vývoji webu existuje nepřeberné množství technologií. Například [tento článek](https://www.appypie.com/top-web-development-frameworks) jich zmiňuje 51, v reálu jich ale bude mnohem víc. Často se používá pojem "framework", i když se nehodí na všechny používané technologie. Framework si můžeme zjednodušeně představit jako něco, co rozšiřuje možnosti nějakého programovacího jazyka, podobně jako moduly v Pythonu. 

Programovacích jazyků, které můžeme použít pro vývoj webu, je spousta. V souvislosti s webem je asi nejčastěji zmiňovaný JavaScript, který umožňuje stránce, aby byla "interaktivní", tj. aby mohla reagovat na akci uživatele (např. kliknutí), aniž by se musela celá znovu načíst. Není však jediný, podobné služby nám může zajistit Typescript, který se používá především pro větší projekty (např. Microsoft Teams) nebo CoffeeScript. Existuje i varianta Pythonu označovaná jako [Brython](https://brython.info/index.html), která umožňuje vývoj interaktivních webových stránek v Pythonu.

Další programovací jazyky, které používáme pro vývoj webu, jsou C#, Python, PHP, Ruby, Java a řada dalších.

V některých případech můžeme webový vývoj jasně rozdělit na **front-end** a **back-end**. Front-end je část aplikace, která "je vidět", a back-end ta část aplikace, která poskytuje data pro front-end. Obě tyto části jsou pak spojené a komunikují spolu. Jasně oddělené jsou tyto části v architektuře označované jako microservices, která se skládá ze spousty malých API, ke kterým posílají jednotlivé části front-endu své zprávy a zobrazují odpovědi. U této architektury mohou být front-end a back-end zcela nezávislé projekty a každý může být vyvíjen jinou technologií, v jiném jazyce atd. 

Druhou možností je architektura označovaná jako model-view-controller, obvykle označované pod zkratkou MVC. Jednotlivé komponenty mají následující význam:

- **Model** reprezentuje datovou strukturu. Pomocí modelu říkáme, s jakými daty bude naše aplikace pracovat, jaká bude ukládat do databáze atd.
- **View** (pohled) převádí data do podoby vhodné k zobrazení uživateli.
- **Controller** (řadič) reaguje na události uživatele.

My budeme využívat framework `Django`, který je založený na obdobném přístupu, který je označovaný jako model-template-views. Modely zde mají stejnou funkci jako v MVC architektuře. **Šablony** určují, jak má stránka vypadat (obsahují i HTML kód) a view připravuje data k zobrazení uživateli a řídí zpracování uživatelských požadavků.

![MVT](assets/django-mvt-based-control-flow.png)

## Django

Na začátku si v našem vývojovém prostředí vytvoříme nový projekt. 

### Vytvoření projektu

Máš-li modul `Django` dobře nainstalovaný, měl by ti fungovat následující příkaz na vytvoření nového projektu:

```
django-admin startproject czechitas
```

Django vytvoří řadu souborů, z nichž jsou pro nás důležité:

- `manage.py` je skript, který zajišťuje správu naší aplikace, např. díky ní můžeme aplikaci spustit.
- `czechitas/settings` obsahuje nastavení aplikace (např. nastavení připojení k databázi).
- `czechitas/urls.py` obsahuje URL adresy, které jsou dostupné v naší aplikaci (ukážeme si později).

Příkaz ti vytvoří nový webový projekt. Tento projekt už si můžeš zkusit spustit pomocí příkazu

```
cd czechitas
python manage.py runserver
```

Zkus si nyní otevřít [tento odkaz](http://127.0.0.1:8000/), ve kterém by měl běžet tvůj nový projekt. Adresa `127.0.0.1` je adresa tvého počítače, často se používá slovní název `locahost`. Nepřipojuješ se tedy nikam do internetu, ale pracuješ na svém počítači.

![MVT](assets/start-app.png)

### Vytvoření aplikace

Aplikace v `django` je složena do funkčních celků, které označujeme jako `app` (aplikace). Jednotlivé aplikace jsou mezi sebou relativně nezávislé a v jednom projektu jich samozřejmě můžeme mít více.

Pro Windows:

```
python manage.py startapp courses
```

Pro MacOS nebo Linux:

```
python3 manage.py startapp courses
```

Nová aplikace obsahuje následující soubory:

- `admin.py` obsahuje modely, které budou přístupné v administrátorském rozhraní.
- `migrations/` je adresář s tzv. migracemi. Migrace je úprava struktury databáze, ke které dochází, pokud měníme data, jaká aplikace ukládá.
- `models.py` obsahuje definici modelů.
- `tests.py` obsahuje definici automatických textů.
- `views.py` je soubor s definicí pohledů.

Po vytvoření prvního modelu již máme plnohodnotnou aplikaci a je ji nutné přidat do seznamu `INSTALLED_APPS`, který najdeme v souboru `settings.py`. Vidíme, že samotný seznam již obsahuje nějaké hodnoty. To jsou aplikace, které se starají o běh základních funkcí, jako je administrátorské rozhraní nebo přihlašování uživatelů.

```python
INSTALLED_APPS = [
  'courses.apps.CoursesConfig',
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',
]
```

### Vytvoření pohledu

Začneme s tím, že si vytvoříme pohled. Náš pohled bude velmi jednoduchý a zobrazí jen jednoduchý text "Vítej na webu Czechitas". Vyzkoušíme si na něm ale základní techniku vytvoření pohledu a přiřazení URL adresy.

Pohled vytvoř v souboru `views.py`. Django umožňuje vytvářet dva typy pohledů - pohledy založené na třídě (`class-based`) a pohledy založené na funkci (`function-based`). Doporučuji ti využívat pohledy založené na třídě, protože jsou přehlednější a využívají techniku, kterou již známe, a tou je dědičnost.

Nový pohled může dědit od celé řady tříd, tvůj první pohled bude dědit od třídy `TemplateView`. Tento pohled umí zobrazit nějakou šablonu.

```python
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"
```

Dále vytvoříme šablonu. V adresáři `courses` si vytvoříme nový adresář `templates`, do kterého přidáme soubor `index.html`. Obsah souboru pak může být libovolný, pro jednoduchost stačí třeba vloži nějaký nadpis.

```html
<h1>Vítejte na webu Czechitas!</h1>
```

### Přidání URL adresy

Nyní máš vytvořený pohled, ale zatím si jej nemůžeš otevřít, protože nemá přiřazenou žádnou adresu. Pojďme to napravit.

Je třeba provést dvě operace:
1. Upravit soubor `urls.py` v adresáři `czechitas` (adresář projektu), aby uměl uživatele přesměrovat do aplikace `courses`.
1. Upravit soubor `urls.py` v adresáři `courses` (adresář aplikace), aby tato aplikace uměla uživatele přesměrovat na náš pohled.

Začni s prvním krokem, tj. s úpravou souboru  `czechitas/urls.py`:

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("courses.urls")),
]
```

A následuje druhý krok, tj. vytvoření souboru `courses/urls.py`:

```python
from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]
```

Pokud si nyní otevřeme námi přidanou [url adresu](http://127.0.0.1:8000/), zobrazí se požadovaný text "Vítej na webu Czechitas!".

[[[ excs Cvičení
- pridani-pohledu
]]]

[[[ excs Bonusy
- o-nas
]]]


### Migrace databáze

Dalším důležitým pojmem je migrace. Migrace je vlastně soupis změn v databázi. Pokud totiž definujeme nový model, potřebujeme pro něj vytvořit tabulku v databázi, abychom záznamy tohoto modelu měli kam ukládat a odkud je načítat. Takový soupis změn označujeme jako migrace databáze. První migraci nám vytvoří `django` automaticky, protože potřebujeme vytvořil základní tabulky, jako třeba tabulku pro informace o uživatelích.

Poté zadáme příkaz pro provedení migrace.

Pro Windows:

```
python manage.py migrate
```

Pro MacOS nebo Linux:

```
python3 manage.py migrate
```

Už v základu v sobě má například aplikaci `auth`, která zajišťuje přihlášení uživatele pomocí hesla. Aplikace `admin` obsahuje administrátorské rozhraní, ve kterém můžete neomezeně prohlížet, upravovat, přidávat a mazat data v aplikaci.

### Čtení na doma: Nastavení databáze

Při práci s frameworkem Django můžeme použít jednoduchou databázi SQLite, která je v nastavena jako výchozí, nebo použít jinou databázi, nejčastěji PostgreSQL. Příklad nastavení PostgreSQL databáze je níže. Pro úspěšné nastavení potřebujeme následující:

- adresu serveru, kde databáze běží (pole `HOST`),
- uživatelské jméno a heslo pro připojení k databázi (pole `USER`, `PASSWORD`),
- jméno databáze (pole `NAME`),
- pole `ENGINE` pak určuje typ databáze, ke které se připojujeme.

```python
DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'moje_databáze',
    'USER': 'jirka',
    'PASSWORD': 'supertajne_heslo',
    'HOST': 'localhost',
    'PORT': '5432',
  }
}
```

### Vytvoření modelu

Nyní můžeme vytvořit náš první model. Náš první model bude reprezentovat kurzy, na které se budou moci uživatelé přihlašovat. Každý model charakterizuje řada datových polí a u každého pole nastavujeme jeho typ. Na to v Pythonu nejsme moc zvyklí, naše webová aplikace ale bude ukládat data do databáze a v takovém případě se hodí vědět, jaká data bude v sobě model mít.

Model je ve skutečnosti další třída, která dědí od základní třídy `Model`. Přidáme našemu kurzu celkem pět datových polí.

| Údaj | Datový typ |
|------|-------------|
| Jméno | text |
| Začátek | datum a čas |
| Konec | datum a čas |
| Popis | text |
| Cena | celé číslo |

Pro naše datové typy využijeme následující třídy:

| Datový typ | Třída |
|------|-------------|
| text | `CharField` |
| datum a čas | `DateTimeField` |
| celé číslo | `IntegerField` |

U textových polí je dobré nastavit maximální délku textu, kterou vložíme jako pojmenovaný parametr do závorek při vytváření třídy.

```python
class Kurz(models.Model):
  name = models.CharField(max_length=100)
  start = models.DateTimeField()
  end = models.DateTimeField()
  description = models.CharField(max_length=1000)
  price = models.IntegerField()
```

Nyní vytvoříme migraci, tj. připravíme skript, který obsahuje všechny informace o našem modelu:

Pro Windows:

```
python manage.py makemigrations
```

Pro MacOS nebo Linux:

```
python3 manage.py makemigrations
```

Terminál nám odpoví následující:

```
Migrations for 'courses':
  courses\migrations\0001_initial.py
    - Create model Kurz
```

Pokud si otevřeme adresář `migrations`, uvidíme v něm nový soubor `0001_initial.py`, který obsahuje popis našeho modelu. Nyní musíme migraci spustit, aby se připravené změny propsaly do databáze.

Pro Windows:

```
python manage.py migrate
```

Pro MacOS nebo Linux:

```
python3 manage.py migrate
```

### Vytvoření prvního uživatele

Nyní nastal čas podívat se do administrátorského rozhraní. Administrátorské rozhraní umožňuje vytvářet nové uživatele, pro přístup do něj se ale musíme přihlásit. Tento problém ve stylu Hlavy 22 vyřešíme pomocí příkazu do terminálu.

Pro Windows:

```
python manage.py createsuperuser
```

Pro MacOs nebo Linux:

```
python3 manage.py createsuperuser
```

Terminál se nás postupně zeptá na uživatelské jméno, e-mail a heslo. Postupně vyplníme všechny údaje a otevřeme si stránku [pro přihlášení](http://localhost:8000/admin/), kam naše uživatelské jméno a heslo zadáme.

Po přihlášení vidíme modely `Users` a `Groups`. Náš model `Kurz` tam ale není, ten musíme nejprve zaregistrovat.

### Registrace modelu

Registrace modelu je jednoduchá, stačí vložit následující kód do souboru `admin.py`.

```python
from django.contrib import admin
from . import models
admin.site.register(models.Kurz)
```

Po obnovení stránky již model vidíme. Zkus si nyní přidat nějaký záznam do našeho modelu pomocí tlačítka 'Add' v administraci projektu. Všimni si, že díky vhodně zvoleným datovým typům jednotlivých polí je jednoduché zadat data ve správném formátu.

[[[ excs Cvičení
- pobocky
]]]

[[[ excs Bonusy
- lide
]]]

