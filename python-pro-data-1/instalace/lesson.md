Pokud ještě nemáš nainstalovaný Python a Visual Studio Code na svém počítači, postupuj nejprve podle [tohoto návodu](http://kodim.cz/kurzy/uvod-do-progr/jazyky-nastroje/).

V rámci workshopu budeme používat modul pro práci s daty `pandas` a modul pro tvorbu grafů `matplotlib`. `pandas` a `matplotlib` je externí moduly, který musíme nejdříve nainstalovat. Pro instalaci si otevřeme terminál a napíšeme následující příkazy (pozor, znak dolaru `$` neopisuj):

```shell
$ py -m pip install numpy==1.19.3
$ py -m pip install pandas
$ py -m pip install matplotlib
```

`pandas` používá modul `numpy`, jehož současná verze si bohužel moc nerozumí s prostředím Visual Studio Code. Proto je v příkazech první řádek, kterým si nainstaluješ trochu starší, ale funkční verzi `numpy`. 

Pokud používáme MacOS nebo Linux, napíšeme:

```shell
$ pip3 install pandas
$ pip3 install matplotlib
```

Chyba modulu `numpy` se MacOS a Linuxu netýká, proto je v příkazech o jeden řádek méně.

`pandas` je relativně veliký modul, který obsahuje mnoho dalších modulů, takže instalace bude nějakou chvíli trvat. Terminál během instalace vypíše spoustu textu. Někde na konci bychom pak měli vidět text

```shell
Successfully installed pandas-1.1.4
```

Čísla verzí se mohou lišit, záleží na tom, jaká verze je právě aktuální. Instalaci si můžeš **ověřit** tím, že zkusíš moduly `pandas` a `matplotlib` importovat. Otevři Python terminál (příkaz `python` ve Windows a `python3` v Linuxu nebo MacOS), napiš `import pandas` a stiskni Enter. V ideálním případě Python nevypíše nic. To znamená, že modul importoval a můžeš ho začít používat.

Pokud Python reaguje chybou `ModuleNotFoundError` (viz níže), pak se instalace nepodařila.

```
>>> import pandas
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'pandas'
```

Následně pomocí `import matplotlib` vyzkoušej, zda jsi úspěšně nainstalovala i modul `matplotlib`.
