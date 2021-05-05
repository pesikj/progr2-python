Pokud ještě nemáš nainstalovaný Python a Visual Studio Code na svém počítači, postupuj nejprve podle [tohoto návodu](https://kodim.cz/czechitas/uvod-do-progr/priprava/jazyky-nastroje).

V rámci workshopu budeme používat modul pro práci `django`. `django` je externí modul, který musíme nejdříve nainstalovat. Pro instalaci si otevřeme terminál a napíšeme následující příkazy (pozor, znak dolaru `$` neopisuj):

```shell
$ py -m pip install django
```

Pokud používáme MacOS nebo Linux, napíšeme:

```shell
$ pip3 install django
```

Instalace bude trvat jen pár sekund. Terminál během instalace vypíše spoustu textu. Někde na konci bychom pak měli vidět text

```shell
Successfully installed asgiref-3.3.1 django-3.1.7 sqlparse-0.4.1
```

Číslo verze se může lišit, záleží na tom, jaká verze je právě aktuální. Instalaci si můžeš **ověřit** tím, že zkusíš modul `django` importovat. Otevři Python terminál (příkaz `python` ve Windows a `python3` v Linuxu nebo MacOS), napiš `import django` a stiskni Enter. V ideálním případě Python nevypíše nic. To znamená, že modul importoval a můžeš ho začít používat.

Pokud Python reaguje chybou `ModuleNotFoundError` (viz níže), pak se instalace nepodařila.

```
>>> import django
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'django'
```
