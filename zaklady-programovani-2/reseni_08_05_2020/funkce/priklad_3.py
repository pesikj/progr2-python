"""
Napiš funkce monthOfBirth, která bude mít jeden parametr - rodné číslo. 
Funkce ze zadaného rodného čísla určí měsíc narození, které vrátí jako výstup. 
Nezapomeň, že pro ženy je k měsíci připočtena hodnota 50.

Příklad: Pro hodnotu 9207054439 vrátí 7. Pro hodnotu 9555125899 vrátí 5.
"""

def monthOfBirth(birthNumber):
  month = birthNumber[2] + birthNumber[3]
  month = int(month)
  month = month % 50
  return month

print(monthOfBirth("9555125899"))
