[Power BI](https://powerbi.microsoft.com/en-au/) je nástroj vyvinutý společností [Microsoft](https://www.microsoft.com/cs-cz/), který slouží k tvorbě vizualizací a reportů. V Power BI si uživatel může tvořit interaktivní grafy a reporty podobně snadno, jako grafy v Excelu.

Power BI obvykle zvládne najít instalaci Pythonu. Před začátkem práce je ale dobré si nastavení zkontrolovat. Otevřeme si menu `File -> Options and Settings -> Options` a v dialogovém okně zvolíme `Python Scripting`. V menu `Detected Python home directories` je přehled instalací Pythonu, které byly Power BI detekovány.

![vyber_instalaci](assets/vyber_instalaci.png)

Pokud není požadovaná instalace na výběr, můžeme zvolit možnost `Other` a zadat adresář s požadovanou instalací ručně.

![vyber_instalaci_other](assets/vyber_instalaci_other.png)

## Zdroj dat

Power BI obsahuje samostatnou komponentu Power Query, která slouží pro zpracování dat. Prvním krokem je jejich načtení a získání. Power BI podporuje řadu různých zdrojů:

- soubory (např. ve formátu CSV, XML nebo JSON),
- databáze,
- služby Power Platform a cloudové služby Azure,
- on-line služby (např. Sharepoint, Dynamics 365, Google Analytics, GitHub, Twilio a řada dalších),
- ostatní (např. webové stránky či skripty v jazycích Python a R).

Python tedy můžeme využít jako zdroj dat a do Power BI můžeme například přenést již hotové skripty. Zkusme tedy nejprve přenést do Power BI výsledky maturity, se kterými jsme již pracovali. 

Ve skupině `Other` vybereme jako zdroj `Python script`. Budeme opět využívat modul `pandas`. Data načteme pomocí metody `read_csv`, do které vložíme URL jednotlivých datových souborů.

```
import pandas as pd

u202 = pd.read_csv("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/agregace-a-spojovani/assets/u202.csv")
u203 = pd.read_csv("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/agregace-a-spojovani/assets/u203.csv")
u302 = pd.read_csv("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/agregace-a-spojovani/assets/u302.csv")

```

Po stisknutí tlačítka OK se zobrazí dialogové okno, ve kterém vybereme, které datové zdroje chceme využít. Jednotlivé "zdroje" se v terminologii Power BI označují jako `query` (dotazy).

![vyber_zdroju](assets/vyber_zdroju.png)

Pokud vybereme všechny, uvidíme v levé části okna každý ze zdrojů jako samostatnou položku v menu, kterou si můžeme zobrazit.

![zobrazeni_zdroju](assets/zobrazeni_zdroju.png)

Nyní bychom mohli pomocí nástrojů Power Query mohli provést stejné transformace (propojení zdrojů, filtrování, případně agregace), abychom se dostali k obdobným výsledkům jako v předchozí části. Níže je například vidět dialog na pro spojení jednotlivých datových souborů.

![spojeni_dat](assets/spojeni_dat.png)

Efektivnější ale bude využít již připravený kód v jazyce Python a v Power BI pracovat až s připravenými výsledky. Smažme tedy všechny vytvořené dotazy a přidejme nový skript, ze kterého vybereme pouze dotaz `maturita`.

```
import pandas as pd

u202 = pd.read_csv("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/agregace-a-spojovani/assets/u202.csv")
u203 = pd.read_csv("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/agregace-a-spojovani/assets/u203.csv")
u302 = pd.read_csv("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/agregace-a-spojovani/assets/u302.csv")
u202['mistnost'] = 'u202'
u203['mistnost'] = 'u203'
u302['mistnost'] = 'u302'
maturita = pandas.concat([u202, u203, u302], ignore_index=True)
```

Po vyhodnocení výsledků maturity stačí, abychom tabulky propojili dohromady, 
agregace budou vypočteny automaticky při tvorbě vizualizací. Proto klikneme na tlačítko `Close & Apply`.

*Poznámka:* Pokud bychom se k editaci skriptu chtěli vrátit, klikneme na ikonku ozubeného kola v řádku `Source` v panelu napravo.

![editace_skriptu](assets/editace_skriptu.png)

## Vizualizace

Nyní můžeme vytvořit graf zobrazující průměrnou známku dle předmětu. K vytvoření grafu jsou potřeba následující kroky.

Pokud bychom chtěli názvy sloupců použít jako popisky os grafů, vyplatí se je přejmenovat pomocí volby `Rename`. 

![popisky](assets/popisky.png)

V menu vpravo vybereme typ vizualizace. Pro zobrazení průměru je vhodný například sloupcový graf (`stacked column chart` nebo `stacket bar chart`). Poté zaškrtneme pole Předmět a Známka vpravo. Power Bi automaticky použije textové pole Předmět jako popisek osy a číselné pole předmět pro výšku sloupců. Automaticky počítá součet, proto je nutné změnit typ agregace na průměr.

Dále je možné upravit titulek grafu a popisky os, aby byl graf co nejvíce srozumitelný. Nastavení vzhledu vizualizace provádíme pomocí menu `Format your visual` vpravo. V případě jednoduchého grafu je možné například vyplnit pouze titulek a popisky os vypnout.

Jako poslední možnost můžeme upravit řazení a seřadit předměty vzestupně podle průměru. Možnosti řazení jsou "schované" v menu vizualizace, které otevřeme pomocí ikonky tří teček vpravo nahoře.

![popisky](assets/razeni.png)

Tím je naše první vizualizace hotová.

![prumerna_znamka_graf](assets/prumerna_znamka_graf.png)

