Nyní si ukážeme, jak naše modely a naše data zobrazit uživatelům.

## Vytvoření seznamu kurzů

Víme, že webové stránky jsou vytovřené v jazyce HTML. Pojďme si tedy vytvořit HTML stránku, která bude obsahovat seznam našich kurzů. V rámci Djanga vytváříme tzv. šablony, což jsou HTML soubory, které jsou ale obohacené o speciální tagy. Přehled tagů, které jsou v Djangu k dispozici, najdeš [zde](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/). Šablony v Djangu ukládáme do adresáře `templates`.

Naše první šablona bude mít za úkol zobrazit kurzy, které jsou aktuálně v nabídce. Pro takový typ šablony je vhodné vložit do názvu `list`. Vytvoříme tedy šablonu `templates/course_list.html`.

### Vytvoření pohledu

Začneme s tím, že vytvoříme pohled. Tentokrát náš pohled založíme na třídě `ListView`. Tato třída patří mezi [generické pohledy](https://docs.djangoproject.com/en/3.2/topics/class-based-views/generic-display/), které mají zabudovanou určitou funkcionalitu a jsou svázány s nějakým modelem. Třída `ListView` má za úkol zobrazit uživateli seznam záznamů nějakého modelu. Nový pohled musí mít nastavené dvě klíčové informace:

- model, jehož záznamy má zobrazit (atribut `model`),
- šablonu, kterou má použít k vytvoření webové stránky (atribut `template_name`).

Vytvoříme tedy třídu `CourseListView` a nastavíme jí potřebné atributy.

```python
from django.views.generic import ListView

class CourseListView(ListView):
    model = models.Course
    template_name = "course_list.html"
```

Našemu pohledu už můžeme přidat i URL adresu.

```python
    path('kurzy/', views.CourseListView.as_view(), name='course_list'),
```

### Vytvoření šablony

Pojďme dát šabloně nějaký obsah. Jako první vytvoříme seznam všech kurzů. K tomu využijeme speciální tag `for`. Ten slouží k vytvoření cyklu v rámci naší šablony. Tento speciální tag zapisujeme do páru značek `{% %}`, abychom ho odlišili od zbytku HTML kódu. Současně musíme přidat i ukončovací tag `endfor`, protože v jazyce HTML by nám nefungoval tradiční přístup Pythonu založený na mezerách.

Náš cyklus projde všechny kurzy v naší aplikaci a vypíše je. Všechny kurzy máme umístěné v proměnné `object_list`, což zařídí pohled `CourseListView`, resp. jeho mateřská třída `ListView`. Jako pomocnou proměnnou v cyklu využijeme proměnnou `item`, do které cyklus postupně vloží všechny naše kurzy.

Máme-li proměnnou `item`, můžeme nyní do naší webové stránky vypsat libovolnou informaci o našem kurzu. Začneme s polem `name`. Abychom vypsání názvu kurzu odlišili od odstatních proměnných, zapíšeme ho do dvojice značek `{{ }}`.

Níže je výsledný kód naší šablony.

```html
{% block content %}
<ul>
    {% for item in object_list %}
    <li>{{ item.name }}</li>
    {% endfor %}
</ul>
{% endblock %}
```

[[[ excs Cvičení
- pobocky
]]]

[[[ excs Bonus
- lide
]]]


## Vazby mezi modely

Modely jsou často mezi sebou provázané. Například víme, že Czechitas organizují kurzy do témat, např. Programuju, Tvořím web atd. Pojďme si vytvořit model, který bude tyto kategorie reprezentovat a umožní uživatelům si např. filtrovat kurzy podle jejich zájmu.

```python
class Category(models.Model):
  name = models.CharField(max_length=100)
```

Jako druhý krok upravíme model `Course`, kterému přidáme nové pole `category`, které je typu `ForeignKey` (tj. cizí klíč). Poli nastavíme parametr `null` jako `True`, což znamená, že toto pole nemusí mít vyplněnou hodnotu. Cizí klíč je ve skutečnosti vazba na jiný model. Tato konkrétní vazba je typu 1:N, což znamená, že jeden kurz má přiřazenou jednu kategorii, ale jedna kategorie může mít více kurzů.

```python
class Kurz(models.Model):
  name = models.CharField(max_length=100)
  start = models.DateTimeField()
  end = models.DateTimeField()
  description = models.CharField(max_length=1000)
  price = models.IntegerField()
  category = models.ForeignKey(Kategorie, on_delete=models.SET_NULL, null=True)
```

Pokud bychom uvažovali složitější případ N:N (např. jako tagy u článků na blogu), pak můžeme využít pole `ManyToManyField`. Naopak pokud má být vazba 1:1, použijeme pole `OneToOneField`. V takovém případě bychom ale teoreticky mohli oba modely spojit do jednoho.

Následně opět provedeme migraci, abychom model přidali do databáze.

```
python manage.py makemigrations kurzy
python manage.py migrate
```

Abychom model `Category` viděli v administrátorském rozhraní, musíme jej ještě zaregistrovat v souboru `admin.py`.

```python
admin.site.register(models.Category)
```

[[[ excs Cvičení
- kurzy-a-pobocky
]]]

[[[ excs Bonus
- lide-a-kurzy
]]]


## Pohled na detail kurzu

Stránka se seznamem zpravidla neobsahuje všechny dostupné informace, protože by to bylo nepřehledné. Namísto toho jsou do stránky vložené odkazy na stránku s detaily konkrétního záznamu, v našem případě vybraného kurzu.

### Vytvoření pohledu

Před vytvořením pohledu bychom si měli připravit prázdný soubor, do kterého později vložíme šablonu. Náš soubor opět uložíme do adresáře `teplates` a pojmenujeme ho `course_detail.html`.

K vytvoření pohledu na jeden konkrétní záznam vytvoříme nový pohled na základě dalšího z generických pohledů, a to `DetailView`. Jak už název napovídá, jedná se o pohled na jeden vybraný záznam. Vytvoříme tedy nový pohled `CourseDetailView` a opět mu nastavíme atributy `model` a `template_name.`

```python
class CourseDetailView(DetailView):
    model = models.Course
    template_name = "course_detail.html"
```

### Vytvoření šablony

Pojďme nyní vložit náš kód do šablony. Ke konkrétnímu záznamu budeme přistupovat pomocí proměnné `object`, což je opět umožněno díky mateřské třídě `DetailView`.

Vyzkoušejme si ještě další důležitou součást frameworku Djagno -- šablonové filtry (`template filters`). Ty nám umožňují upravit nějakou informaci předtím, než ji zobrazíme uživatelům. Uvažujme třeba, že budeme chtít zobrazit zvlášť datum workshopu a zvlášť čas začátku a konce. Abychom z pole `zacatek` získali pouze datum, využijeme filtr `date`. Filtry píšeme do dvojice složených závorek a za znak `|`. Dále využijeme filtr `time` pro získání času začátku a konce kurzu.

Seznam všech dostupných kurzů najdeš [v dokumentaci](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/).

```html
<h2>{{ object.name }}</h2>

<h3>Kdy</h3>
<p>{{ object.start | date }} <br /> {{ object.start | time }}-{{ object.end | time }}</p>
<h3>Cena</h3>
<p>{{ object.price }} Kč</p>

<p>{{ object.description }}</p>
```

### Vytvoření odkazů

Pohled a šablonu máme připravené, ale zatím nemají uživatelé možnost se k nim dostat. Musíme opět pohledu přiřadit nějakou adresu. Adresa tentokrát musí obsahovat jeden důležitý prvek, a to je označení kurzu, který má stránka zobrazit. Toto označení vložíme do adresy jako číslo, které bude svázané s **primárním klíčem** nějakého záznamu. Primární klíč vytváří `django` u všech modelů automaticky a je posloupností celý čísel jdoucí od 1.

Pokud chceme nějaký parametr vložit do adresy, vkládáme ho do dvojice špičatých závorek. Zapisujeme tam typ hodnoty (jde o celé číslo, takže píšeme `int`) a název pole. Jako název pole napíšeme `pk`. Mezi typ a název hodnoty vložíme dvojtečku.

```python
    path('kurz/<int:pk>', views.CourseDetailView.as_view(), name='course_detail'),
```

Následně upravíme šablonu `course_list.html`, aby k názvům kurzů vkládala i odkazy na detaily jednotlivých kurzů. K tomu využijeme tag `url`. Protože jde o tag, zapíšeme ho do dvojice `{% %}`. Následně přidáme název URL adresy `course_detail` a hodnotu, která bude vložena jako parametr do adresy, tedy primární klíč `kurz.pk`.

```html
<h2>Seznam kurzů</h2>
<p>Zde vidíte aktuální nabídku kurzů</p>
<ul>
    {% for item in object_list %}
    <li><a href="{% url 'course_detail' item.pk %}">{{ item.nazev }}</a></li>
    {% endfor %}
</ul>
```

Nyní se uživatel může prokliknout ze seznamu kurzů na detail vybraného kurzu.

[[[ excs Cvičení
- detail-pobocky
]]]
