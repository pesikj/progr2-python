## Virtuální prostředí

Často v Pythonu používáme virtuální prostředí. To nám umožní pracovat na programech, které vyžadují různé verze určitých balíčků, aniž bychom je museli vždy při změně projektu přeinstalovat. Práce s virtuálním prostředím je popsaná [zde](https://docs.python.org/3/tutorial/venv.html).

```
python -m venv czechitas-env
```

Uživatelé **Linuxu a macOS** by měli použít příkaz

```
python3 -m venv czechitas-env
```


Uživatelé **Windows** se přepnou do nově vytvořeného virtuálního prostředí příkazem:

```
czechitas-env\Scripts\activate
```

Uživatelé **Linuxu a MacOS** se přepnou do nově vytvořeného virtuálního prostředí příkazem:

```
source czechitas-env/bin/activate
```

Od teď pracujeme ve virtuálním prostředí.
