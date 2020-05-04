"""
Vraťme se k funkci getMark, která určuje známku na základě bodů v testu. 
Uvažujme nyní, že studenti mají možnost získat bonusové body (např. za odevzdání úkolů), 
které se pak připočítávají k bodům z testu.

Upravte funkci getMark tak, aby měla druhý parametr bonusPoints. Tyto bonusové body pak připočtěte k bodům z testu.
Nastavte parametr bonusPoints jako nepovinný s výchozí hodnotou 0.
"""

def getMark(points, bonusPoints=0):
  points += bonusPoints
  if points <= 60:
    mark = 5
  elif points <= 70:
    mark = 4
  elif points <= 80:
    mark = 3
  elif points <= 90:
    mark = 2
  else:
    mark = 1
  return mark