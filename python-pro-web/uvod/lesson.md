V této lekci si řekneme něco o tom, jak vlastně provádíme vývoj webu.

## O vývoji webu

Vývoj a provoz webu je disciplína, která v sobě zahrnuje několik složek.

Definice toho, jak by webová stránka měla vypadat, nazýváme kódování. Zpravidla prováděno v jazyce HTML s využitím kaskádových stylů (CSS). HTML a CSS vlastně poskytují informace pro webový prohlížeč, jaké informace má zobrazit a jak je naformátovat.

K vytvoření webové stránky mohou stačit pouze tyto jazyky. Jedná se především o weby, které zobrazují nějaké statické informace (např. osobní web, životopis atd.). Všechny informace, které stránka obsahuje, pak musí být vloženy do HTML souborů jako text a stránka nemůže obsahovat žádné prvky pro komunikaci mezi uživatelem a správcem webu (např. formuláře).

Většina dnešních webů by si pouze s HTML nevystačila. Chceme-li si například vytvořit zpravodajský server, chceme dát uživatelům možnost přihlášení (placené články, diskuse) a editorům webu chceme poskytnout příjemné prostředí, kam mohou vkládat své články. Takový web již musí být propojený s nějakým úložištěm dat, nejčastěji s databází. V databázi jsou uloženy články, informace o uživatelských článcích, diskusní příspěvky, kategorie článků, obrázky a spousta dalších informací. Takový web již musí být naprogramovaný, protože HTML si neumí načíst informace s databáze nebo zajistit přihlášení uživatele.

### Prostředí pro vývoj webu

K vývoji webu existuje nepřeberné množství technologií. Například [tento článek](https://www.appypie.com/top-web-development-frameworks) jich zmiňuje 51, v reálu jich ale bude mnohem víc. Často se používá pojem "framework", i když se nehodí na všechny používané technologie. Framework si můžeme zjednodušeně představit jako něco, co rozšiřuje možnosti nějakého programovacího jazyka, podobně jako moduly v Pythonu. 

Programovacích jazyků, které můžeme použít pro vývoj webu, je spousta. V souvislosti s webem je asi nejčastěji zmiňovaný JavaScript, který umožňuje stránce, aby byla "interaktivní", tj. aby mohla reagovat na akci uživatele (např. kliknutí), aniž by se musela celá znovu načíst. Není však jediný, podobné služby nám může zajistit Typescript, který se používá především pro větší projekty (např. Microsoft Teams) nebo CoffeeScript. Existuje i varianta Pythonu označovaná jako [Brython](https://brython.info/index.html), která umožňuje vývoj interaktivních webových stránek v Pythonu.

Další programovací jazyky, které používáme pro vývoj webu, jsou C#, Python, PHP, Ruby, Java a řada dalších.

V některých případech můžeme webový vývoj jasně rozdělit na front-end a back-end. Front-end je část aplikace, která "je vidět", a back-end ta část aplikace, která poskytuje data. Obě tyto části jsou pak spojené a komunikují spolu. Jasně oddělené jsou tyto části v architektuře označované jako microservices, která se skládá ze spousty malých API, ke kterým posílají jednotlivé části front-endu své zprávy a zobrazují odpovědi. U této architektury mohou být front-end a back-end zcela nezávislé projekty a každý může být vyvíjen jinou technologií, v jiném jazyce atd. 

Druhou možností je architektura označovaná jako model-view-controller, obvykle označované pod zkratkou MVC. Jednotlivé komponenty mají následující význam:

- Model reprezentuje datovou strukturu. Pomocí modelu říkáme, s jakými daty bude naše aplikace pracovat, jaká bude ukládat do databáze atd.
- View (pohled) převádí data do podoby vhodné k zobrazení uživateli.
- Controler (řadič) reaguje na události uživatele.

My budeme využívat framework Django, který je založený na obdobném přístupu, který je označovaný jako model-template-views. Modely zde mají stejnou funkci jako v MVC architektuře. Šablony určují, jak má stránka vypadat (obsahují i HTML kód) a view připravuje data k zobrazení uživateli a řídí zpracování uživatelských požadavků.

![Adult only](assets/django-mvt-based-control-flow.png)

## Django

Na začátku si v našem vývojovém prostředí vytvoříme nový projekt. Pokud používáme virtuální prostředí, nainstalujeme si do prostředí modul `django`.

### Vytvoření projektu

Máš-li modul dobře nainstalovaný, měl by ti fungovat následující příkaz na vytvoření nového projektu:

```
django-admin startproject czechitas
```

Django vytvoří řadu souborů, z nichž jsou pro nás důležité:

- `manage.py` je skript, který zajišťuje správu naší aplikace, např. díky ní můžeme aplikaci spustit.
- `czechitas/settings` obsahuje nastavení applikace (např. nastavení připojení k databázi).
- `czechitas/urls.py` obsahuje URL adresy, které jsou dostupné v naší aplikaci (ukážeme si později).

Příkaz ti vytvoří nový webový projekt. Tento projekt už si můžeš zkusit spustit pomocí příkazu

```
python manage.py runserver
```

Zkus si nyní otevřít [tento odkaz](http://127.0.0.1:8000/), ve kterém by měl běžet tvůj nový projekt. Adresa `127.0.0.1` je adresa tvého počítače, často označovaná jako `loopback`. Nepřipojuješ se tedy nikam do internetu, ale pracuješ na svém počítači.

### Vytvoření aplikace

Aplikace v `django` je složena do funkčních celků, které označujeme jako `app` (aplikace). Jednotlivé aplikace jsou mezi sebou relativně nezávislé a v jednom projektu jich samozřejmě můžeme mít více.

```
python manage.py startapp czechitas
```

Nová aplikace obsahuje následující soubory:

- `admin.py` obsahuje modely, které budou přístupné v administrátorském rozhraní.
- `migrations/` je adresář s tzv. migracemi, tj. úpravami struktury databáze.
- `models.py` obsahuje definici modelů.
- `tests.py` obsahuje definici automatických textů.
- `views.py` je soubor s definicí pohledů.

### Vytvoření pohledu

### Přidání URL adresy

### Vytvoření modelu

### Migrace databáze
