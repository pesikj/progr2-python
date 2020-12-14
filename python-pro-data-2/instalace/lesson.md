Pokud ještě nemáš nainstalovaný Python a Visual Studio Code na svém počítači, postupuj nejprve podle [tohoto návodu](http://kodim.cz/kurzy/uvod-do-progr/jazyky-nastroje/).

V rámci workshopu budeme používat modul pro práci s databází MongoDB `pymongo`. `pymongo` je externí modul, který musíme nejdříve nainstalovat. Pro instalaci si otevřeme terminál a napíšeme následující příkazy (pozor, znak dolaru `$` neopisuj):

```shell
$ py -m pip install pymongo
```

Pokud používáme MacOS nebo Linux, napíšeme:

```shell
$ pip3 install pymongo
$ pip3 install matplotlib
```

```shell
Successfully installed pymongo-3.11.2
```

Číslo verze se může lišit, záleží na tom, jaká verze je právě aktuální. Instalaci si můžeš **ověřit** tím, že zkusíš modul `pymongo` importovat. Otevři Python terminál (příkaz `python` ve Windows a `python3` v Linuxu nebo MacOS), napiš `import pymongo` a stiskni Enter. V ideálním případě Python nevypíše nic. To znamená, že modul importoval a můžeš ho začít používat.

Pokud Python reaguje chybou `ModuleNotFoundError` (viz níže), pak se instalace nepodařila.

```
>>> import pandas
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'pandas'
```
