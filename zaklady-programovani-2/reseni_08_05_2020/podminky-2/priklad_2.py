"""
Matematické gymnázium nabízí aplikaci, která sděluje informaci o povinnosti vykonání přijímací zkoušky. 
Požádejte uživatele o zadání známky z matematiky a průměru všech známek na posledním vysvědčení. 
Pokud má zájemce proměr známek nižší než 1.8 a z matematiky nejhůře dvojku, vypište text: "Přijmeme vás bez přijímací zkoušky.". 
V opačném případě vypište "Musíte splnit přijímací zkoušku.".

3
"""

markAverage = float(input("Zadej průměr známek: "))
markMath = int(input("Zadej známku z matematiky: "))
if markAverage <= 1.8 and markMath <= 2:
  print("Přijmeme vás bez přijímací zkoušky.")
else:
  print("Musíte splnit přijímací zkoušku.")