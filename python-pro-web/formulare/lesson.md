Pojďme se nyní podívat na to, jak vytvořit formuláře, pomocí kterých uživatelů komunikují s aplikací.

## Formuláře

Na začátku přidáme do aplikace model `Prihlaska`. Pokud se uživatel přihlásí do kurzu, ve skutečnosti vytvoří jeden záznam tohoto modelu a ten uloží do databáze.

```python
class Prihlaska(models.Model):
    email = models.CharField(max_length=100)
    jmeno = models.CharField(max_length=100)
    prijmeni = models.CharField(max_length=100)
    motivace = models.TextField()
    kurz = models.ForeignKey(Kurzy, on_delete=models.SET_NULL, null=True)
```

Abychom vytvořili nový záznam, můžeme vytvořit nový pohled na základě dalšího z generických pohledů, a to konkrétně `CreateView`. To patří do skupiny generických pohedů, které jsou určeny k úpravám záznamů. Dalšími takovými jsou `UpdateView`, `DeleteView` a obecný pohled `FormView`.

Po přidání modelu je potřeba provést migraci databáze a zaregistrovat model do administrátorského rozhraní.

### Přidání formuláře

Následně přidáme šablonu, kterou uložíme do souboru `prihlaska/prihlaska.html`. Šablona je poměrně jednoduchá, bude obsahovat tag `<from>`, do kterého vložíme `{{ form.as_p }}`. Tím říkáme, že chceme využít výchozí způsob frameworku Django na vykreslení formuláře, který si ještě vysvětlíme. Následně přidáme tag `<input>`, které vloží tlačítko pro uložení vstupu ve formuláři.

```html
<form method="post">{% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="Save">
</form>
```

Následně vytvoříme pohled `VytvorPrihlasku`, který bude dědit od třídy `CreateView`. Pohledu přidáme atributy `model`, `template_name` a `fields`. Atribut `fields` určuje, která pole se v našem formuláři zobrazí.

```python
from django.views.generic import ListView, DetailView, CreateView

class VytvorPrihlasku(CreateView):
    model = models.Prihlaska
    template_name = "prihlaska/prihlaska.html"
    fields = ["email", "jmeno", "prijmeni", "motivace", "kurz"]
```

Zobrazení formuláře bychom měli, je však třeba vyřešit, co se stane po jeho uložení. O uložení dat do databáze se postará Django, je však třeba vytvořit stránku, na kterou je uživatel přesměrován po vyplnění formuláře. Nejprve pro ni vytvoříme jednouduchou šablonu, kterou uložíme jako `prihlaska/potvrzeni.html`.

```html
<h2>Potvrzujeme přijetí přihlášky</h2>

V nejbližší době se ti ozveme s dalšími informacemi.
```

Protože půjde o stránku, která pouze zobrazí jednoduchou zprávu s poděkováním, můžeme vytvořit jednoduchý pohled, který bude dědit od třídy `TemplateView`. Pohled musí mít nastavený atribut `template_name`, který určuje cestu k naší šabloně.

```python
from django.views.generic.base import TemplateView

class PotvrzeniPrihlasky(TemplateView):
    template_name = "prihlaska/potvrzeni.html"
```

Pohledu následně přiřadíme adresu, abychom si jej mohli zobrazit v prohlížeči.

```python
urlpatterns = [
    path('', views.KurzyView.as_view(), name='index'),
    path('<int:pk>', views.DetailKurzView.as_view(), name='detail_kurzu'),
    path('prihlaska/', views.VytvorPrihlasku.as_view(), name='prihlaska'),
    path('prihlaska/potvrzeni/', views.PotvrzeniPrihlasky.as_view(), name='potvrzeni_prihlasky'),
]
```

A jako poslední krok nastavíme pohledu `VytvorPrihlasku` atribut `success_url`, kterému přiřadíme adresu `potvrzeni_prihlasky`. Aby došlo k překladu názvu adresy na adresu, použijeme funkci `reverse_lazy`.


```python
from django.urls import reverse_lazy

class VytvorPrihlasku(CreateView):
    model = models.Prihlaska
    template_name = "prihlaska/prihlaska.html"
    fields = ["email", "jmeno", "prijmeni", "motivace", "kurz"]
    success_url = reverse_lazy('potvrzeni_prihlasky')
```

### Upravení vzhledu formuláře

Formulář jsme sice vytvořili, ale vypadá poněkud nemoderně. Abychom dosáhli lepšího vzhledu, můžeme využít řadu existujících a zdarma dostupných nástrojů. Jedním z nich je framework [Boostrap](https://getbootstrap.com/), který vyvinula společnost Twitter. Boostrap lze poměrně snadno využít v naší aplikaci, a to s využitím modulu `django-bootstrap4`.

Ten je potřeba nejprve nainstalovat příkazem

```
pip install django-bootstrap4
```

Následně musíme přidat `'bootstrap4'` do seznamu aplikací `INSTALLED_APPS` v souboru `settings.py`.

Dále vytvoříme šablonu `base.html`, která bude jakýmsi základem naší aplikace a která bude určovat vzhled stránky. V šabloně musíme použít speciální tag `load`, abychom nahráli dodatečnou množinu tagů z frameworku bootstrap. Následně využijeme nově přidané tagy `bootstrap_css` a `bootstrap_javascript`.

```python
{% load bootstrap4 %}

{% bootstrap_css %}
{% bootstrap_javascript jquery='full' %}

{% block content %}

{% endblock %}
```

Dále upravíme šablonu `prihlaska/prihlaska.html` a k vytvoření formuláře použijeme tag `bootstrap_form`.

```python
{% extends "base.html" %}
{% load bootstrap4 %}

{% block content %}
<form method="post">{% csrf_token %}
    {% csrf_token %}
    {% bootstrap_form form %}
    {% buttons %}
        <input type="submit" value="Submit" class="btn btn-primary">
    {% endbuttons %}
</form>
{% endblock %}
```

### Úkoly

Vrať se ke své aplikaci `crm` pro správu kontaktů. 

- Přidej do aplikace formulář na přidání kontaktu. Vytvoř šablonu a pohled se všemi poli, které má model `Kontakt`. Následně pohledu přidej URL adresu.
- Pokud máš zájem, použij Bootstrap a vytvoř si šablonu `base.html`.
- Ověř, že vše funguje tím, že pro firmu vytvoříš nový kontakt.

### Přečtení kurzu z adresy

Náš formulář funguje, ale není uživatelsky přívětivý, protože obsahuje výběr konkrétního kurzu a těch mohou být i desítky. Lepší by bylo, kdyby mohl uživatel otevřít přihlášku ze stránky vybraného kurzu a informace o vybraném kurzu by se doplnila automaticky. Abychom toho dosáhli, musíme přidat metodu `form_valid()`, která je spuštěna při vyplnění formuláře a slouží k jeho validaci. My budeme uvažovat, že ID kurzu je v URL adrese, odkud ji načteme do proměnné `id_kurzu`. Přístup k této proměnné nám zajistí atribut `kwargs`, který v sobě agreguje různé informace z různých metod a můžeme si jej představit třeba jako domovní nástěnku, kam různí obyvatelé domu umisťují informace, které chtějí sdílet s ostatními. 

Následně informaci přiložíme k objektu `form.instance`. Nakonec využijeme funkci `super()`, protože jsme provedli jen malou úpravu a zbytek práce ponecháme na mateřské třídě.

```python
class VytvorPrihlasku(CreateView):
    model = models.Prihlaska
    template_name = "prihlaska/prihlaska.html"
    fields = ["email", "jmeno", "prijmeni", "motivace"]
    success_url = reverse_lazy('potvrzeni_prihlasky')

    def form_valid(self, form):
        id_kurzu = self.kwargs['pk']
        kurz = models.Kurzy.objects.get(pk=id_kurzu)
        form.instance.kurz = kurz
        return super().form_valid(form)
```

Následně musíme provést malou úpravu, aby aplikace počítala s výskytem klíče kurzu v URL adrese.

```python
urlpatterns = [
    path('', views.KurzyView.as_view(), name='index'),
    path('<int:pk>', views.DetailKurzView.as_view(), name='detail_kurzu'),
    path('prihlaska/<int:pk>/', views.VytvorPrihlasku.as_view(), name='prihlaska'),
    path('prihlaska/potvrzeni/', views.PotvrzeniPrihlasky.as_view(), name='potvrzeni_prihlasky'),
]
```

Nyní přidáme na stránku detailů kurzu tlačítko s odkazem na přihlášku. Využijeme tag `bootstrap_button`, aby náš odkaz vypadal jako tlačítko. Pro vygenerování adresy využijeme tag `url`, který již známe. Pouze je potřeba vytvořit adresu jako první krok a uložit ji do proměnné `target_url`, abychom se vyhnuli využití vnořených tagů.

```python
{% extends "base.html" %}
{% load bootstrap4 %}
{% block content %}
<h2>{{ object.nazev }}</h2>

<h3>Kdy</h3>
<p>{{ object.zacatek | date }} <br /> {{ object.zacatek | time }}-{{ object.konec | time }}</p>
<h3>Cena</h3>
<p>{{ object.cena }} Kč</p>

<p>{{ object.popis }}</p>

{% url 'prihlaska' object.pk as target_url %}
{% bootstrap_button "Přihlásit se" href=target_url button_type="link" button_class="btn-info" %}

{% endblock %}
```

Nyní se může uživatel snadno přihlásit, aniž by musel řešit výběr kurzu ze seznamu.

### Úkoly

- Vytvoř nový pohled pohled pro vytvoření kontaktu, který nebude mít pole `organizace`, ale bude organizaci číst z URL adresy.
- Nastav URL adresu pohledu, aby s ID firmy počítala.
- Na stránku firmy přidej tlačítko s odkazem "Přidej kontakt", které tě přesměruje na stránku s formulářem na přidání kontaktu.
- Ověř, že vše funguje tím, že pomocí nového formuláře vytvoříš kontakt.
