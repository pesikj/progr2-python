markAverage = float(input("Zadej průměr známek: "))
markMath = int(input("Zadej známku z matematiky: "))
mathContest = input("Zúčastnil ses okresního kola krajské olympiády? [a/n] ")
if markAverage <= 1.8 and (markMath <= 2 or mathContest == "a"):
  print("Přijmeme vás bez přijímací zkoušky.")
else:
  print("Musíte splnit přijímací zkoušku.")