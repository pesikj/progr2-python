Podívejme se krátce na to, co je datová analýza (data analytics). Definicí je spousta. Můžeme například říct, že datová analýza mění _data_ ve _znalosti_. Data si můžeme představit jako dlouhé a rozsáhlé tabulky s tisíci či miliony řádků, v nichž bychom se bez pomoci neměli šanci vyznat. Znalostí je něco, co je pro člověka mentálně uchopitelné a může to být například použito jako podklad pro rozhodnutí.

U výrobní firmy máme například obrovské tabulky tržeb a nákladů, které nám samy o sobě nic neřeknou. Znalostí pak může být třeba to, který produkt je nejvíce ziskový, zda by některý z produktů potřeboval větší propagaci nebo zda jej neprodáváme příliš draho.

Do datové analýzy můžeme započítat velké množství činnost. Typickými příklady jsou:

- čištění dat (kontrola chyb, hledání duplicitních záznamů atd.),
- transformace dat,
- vizualizace dat,
- návrh datové architektury.

Součástí zpracování je i strojové učení (machine learning), což si můžeme představit jako používání různých algoritmů k hledání společných trendů a závislostí mezi daty a vytváření predikcí. Často je to označování jako datová věda (mechine learning).

## Proč se datovou analýzou zabýváme

V současné době zažívá datová analýza a strojové učení velký rozmach. To má několik předpokladů:

- obrovské množství dat,
- dostatečná výpočetní kapacita,
- algoritmy a software ke zpracování dat.

V případě firmy je motivací k datové analýze především zlepšení podnikání (snížení nákladů, zvýšení tržeb, vyšší spokojenost zákazníka atd.). Datovou analýzu ale můžeme prové sami, když si např. budeme sledovat svoje výdaje a zjišťovat, kolik za co utrácíme (a kde by mělo smysl ušetřit).

Kromě Pythonu se pro zpracování dat používá jazyk R. Výhodou Pythonu je, že jde o obecný jazyk, se kterým můžeme provádět spoustu dalších věcí, R je jazyk zaměřený pouze na zpracování dat.

## Odkud data bereme

Data se nejčastěji nachází v databázích nebo v souborech.

Data můžeme v základu rozdělit na textová data (včetně dat, která můžeme na texty převést), videa, obrázky a zvuky.

### Zápisy textových dat

Podívejme se nyní na základní formáty, jak zapisovat data. Pro nás nejznámější formou je tabulka.

| Jméno |       Věc        | Částka v korunách |
| ----- | :--------------: | ----------------: |
| Petr  |   Prací prášek   |               399 |
| Ondra |       Savo       |                80 |
| Petr  |  Toaletní papír  |                65 |
| Libor |       Pivo       |               124 |
| Petr  | Pytel na odpadky |                75 |
| Míša  | Utěrky na nádobí |               130 |
| Ondra |  Toaletní papír  |               120 |
| Míša  |   Pečící papír   |                30 |
| Zuzka |       Savo       |                80 |
| Pavla |      Máslo       |                50 |
| Ondra |       Káva       |               300 |

S tabulkami pracujeme v software Microsoft Excel (soubory mají příponu `.xlsx`), případně v alternativách jako Google Spreadsheet. Python umí pracovat přímo se soubory XLSX, slouží k tomu modul ´openpylx´ (můžete ho stáhnout [zde](https://openpyxl.readthedocs.io/en/stable/)). Práce s nimi je ale poměrně složitá, proto budeme používat soubory CSV.

Soubor CSV obsahuje data v textové podobě ve struktuře podobné tabulce. Jednotlivé buňky jsou odděleny středníky nebo čárkami, většinou závisí na nastavení našeho systému.

```
Jméno,Věc,Částka v korunách
Petr,Prací prášek,399
Ondra,Savo,80
Petr,Toaletní papír,65
Libor,Pivo,124
Petr,Pytel na odpadky,75
Míša,Utěrky na nádobí,130
Ondra,Toaletní papír,120
Míša,Pečící papír,30
Zuzka,Savo,80
Pavla,Máslo,50
Ondra,Káva,300
```

Kromě CVS používáme další dva důležité formáty: JSON, XML.

Formát JSON ti bude povědomý, pokud už jsi v Pythonu pracovala se slovníky (`dict`), protože na první pohled vypadají téměř stejně. Python ti navíc jednoduše umožní data ve formátu JSON převést na slovníky a seznamy.

```
[
  {
    "Jméno": "Petr",
    "Věc": "Prací prášek",
    "Částka v korunách": 399
  },
  {
    "Jméno": "Ondra",
    "Věc": "Savo",
    "Částka v korunách": 80
  },
  {
    "Jméno": "Petr",
    "Věc": "Toaletní papír",
    "Částka v korunách": 65
  },
  {
    "Jméno": "Libor",
    "Věc": "Pivo",
    "Částka v korunách": 124
  },
  {
    "Jméno": "Petr",
    "Věc": "Pytel na odpadky",
    "Částka v korunách": 75
  },
  {
    "Jméno": "Míša",
    "Věc": "Utěrky na nádobí",
    "Částka v korunách": 130
  },
  {
    "Jméno": "Ondra",
    "Věc": "Toaletní papír",
    "Částka v korunách": 120
  },
  {
    "Jméno": "Míša",
    "Věc": "Pečící papír",
    "Částka v korunách": 30
  },
  {
    "Jméno": "Zuzka",
    "Věc": "Savo",
    "Částka v korunách": 80
  },
  {
    "Jméno": "Pavla",
    "Věc": "Máslo",
    "Částka v korunách": 50
  },
  {
    "Jméno": "Ondra",
    "Věc": "Káva",
    "Částka v korunách": 300
  }
]
```

Dalším používaným frormátem je XML. XML je velmi podobné HTML, tedy jazyku, kterým určujeme, jak bude vypadat webová stránka.

```
<?xml version="1.0" encoding="UTF-8"?>
<nakupy>
   <nakup jméno="Petr" věc="Prací prášek">399</nakup>
   <nakup jméno="Ondra" věc="Savo">80</nakup>
   <nakup jméno="Petr" věc="Toaletní papír">65</nakup>
   <nakup jméno="Libor" věc="Pivo">124</nakup>
   <nakup jméno="Petr" věc="Pytel na odpadky">75</nakup>
   <nakup jméno="Míša" věc="Utěrky na nádobí">130</nakup>
   <nakup jméno="Ondra" věc="Toaletní papír">120</nakup>
   <nakup jméno="Míša" věc="Pečící papír">30</nakup>
   <nakup jméno="Zuzka" věc="Savo">80</nakup>
   <nakup jméno="Pavla" věc="Máslo">50</nakup>
   <nakup jméno="Ondra" věc="Káva">300</nakup>
</nakupy>
```

Výhodou XML je, že můžeme snadno validovat.

### Čtení na doma - formát YAML

Nejnovějším z formátů je YAML, který vznikl v roce 2011.

```
- Jméno: Petr
  Věc: Prací prášek
  Částka v korunách: 399
- Jméno: Ondra
  Věc: Savo
  Částka v korunách: 80
- Jméno: Petr
  Věc: Toaletní papír
  Částka v korunách: 65
- Jméno: Libor
  Věc: Pivo
  Částka v korunách: 124
- Jméno: Petr
  Věc: Pytel na odpadky
  Částka v korunách: 75
- Jméno: Míša
  Věc: Utěrky na nádobí
  Částka v korunách: 130
- Jméno: Ondra
  Věc: Toaletní papír
  Částka v korunách: 120
- Jméno: Míša
  Věc: Pečící papír
  Částka v korunách: 30
- Jméno: Zuzka
  Věc: Savo
  Částka v korunách: 80
- Jméno: Pavla
  Věc: Máslo
  Částka v korunách: 50
- Jméno: Ondra
  Věc: Káva
  Částka v korunách: 300
```