markAverage = float(input("Zadej průměr známek: "))
markMath = int(input("Zadej známku z matematiky: "))
if markAverage <= 1.8 and markMath <= 2:
  print("Přijmeme vás bez přijímací zkoušky.")
else:
  print("Musíte splnit přijímací zkoušku.")