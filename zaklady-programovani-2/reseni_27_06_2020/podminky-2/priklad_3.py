"""
Modifikujme si předchozí příklad. Horší známku z matematiky může student kompenzovat tím, 
že uspěje v matematické olympiádě. Přidejte tedy dotaz, zda se uchazeč zúčastnil okresního 
kola matematické olympiády. Pokud ano, bude mu zkouška odpuštěna, i kdyby jeho známka z matematiky byla horší. 
Požadavek na celkový průměr známek je však třeba stále dodržet.

Otázka může vypadat například takto:

input("Zúčastnil ses okresního kola krajské olympidáy? [a/n] ")
Pokud se student olympidáy zůstatnil, odpoví a.
"""


markAverage = float(input("Zadej průměr známek: "))
markMath = int(input("Zadej známku z matematiky: "))
mathContest = input("Zúčastnil ses okresního kola krajské olympiády? [a/n] ")
if markAverage <= 1.8 and (markMath <= 2 or mathContest == "a"):
  print("Přijmeme vás bez přijímací zkoušky.")
else:
  print("Musíte splnit přijímací zkoušku.")