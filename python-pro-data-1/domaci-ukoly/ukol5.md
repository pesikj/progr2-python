# Teplota ve městech podruhé

Pokračuj ve své práci s informacemi o průměrných teplotách. Pokud jsi zpracovala pokročilou variantu, můžeš pracovat s teplotami ve stupních Celsia.

Vypiš si prvních několik řádků, ať si prohlédneš strukturu tabulky. Dále napiš následující dotazy:

1. Dotaz na řádky z 13. listopadu 2017 (sloupec `Day` musí mít hodnotu 13).
1. Dotaz na řádky z 13. listopadu 2017 ze Spojených států amerických (sloupec `Day` musí mít hodnotu 13 a sloupec `Country` hodnotu US). Výsledek dotazu si ulož do nové tabulky a použij ji jako vstup pro následující dotaz.
1. Pro data z předchozího dotazu napiš dotaz na řádky ve městech (sloupec `City`) Washington a Philadelphia.
1. Vrať se k pomocné tabulce, kterou jsi vytvořila v bodu 2. Vypiš průměrnou hodnotu ze všech měření, která byla provedena 13. listopadu 2017 na území Spojených států amerických. K tomu využij funkci `.mean()`, která funguje stejně jako funkce `.sum()`, kterou jsme si ukazovali na lekci. Pokud znáš základy statistiky, zkus funkci pro medián `.median()` a rozptyl `.var()`.
