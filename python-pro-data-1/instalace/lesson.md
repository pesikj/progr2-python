V rámci workshopu budeme používat modul pro práci s daty `pandas` a modul pro tvorbu grafů `matplotlib`. 

Pandas umožňuje pracovat s daty v ucelené struktuře podobné databázím. Díky mnoha zabudovaným funkcím umí rychle zpracovat velké množství dat, vyhodnocovat je a čistit, čímž šetří datovému analytikovi mnoho času.

## Instalace modulů

`pandas` a `matplotlib` je externí balíčky, který musíme nejdříve nainstalovat. Pro instalaci si otevřeme terminál a napíšeme na příkazovou řádku

```shell
$ py -m pip install pandas
$ py -m pip install matplotlib
```

Pokud používáme MacOS nebo Linux, napíšeme:

```shell
$ pip3 install pandas
$ pip3 install matplotlib
```

Pandas je relativně veliký balíček, který obsahuje mnoho modulů, takže instalace bude nějakou chvíli trvat. Terminál během instalace vypíše spoustu textu. Někde na konci bychom pak měli vidět text

```shell
Successfully installed numpy-1.19.4 pandas-1.1.4 python-dateutil-2.8.1 pytz-2020.4 six-1.15.0
```

Čísla verzí se mohou lišit, záleží na tom, jaká verze je právě aktuální. Instalaci si můžeš ověřit tím, že zkusíš moduly `pandas` a `matplotlib` importovat. Otevři Python terminál (příkaz `python` ve Windows a `python3` v Linuxu nebo MacOS) a napiš `import pandas`.

Pokud Python reaguje chybou `ModuleNotFoundError`, pak se instalace nepodařila.

```
>>> import pandas
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'pandas'
```

