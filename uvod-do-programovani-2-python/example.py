birthNumber = input("Zadejte rodné číslo: ")
yearOfBirth = birthNumber[0] + birthNumber[1]
yearOfBirth = int(yearOfBirth)
if yearOfBirth > 20:
  yearOfBirth = 1900 + yearOfBirth
else:
  yearOfBirth = 2000 + yearOfBirth
print(f"Uživatel(ka) se narodil(a) v roce {yearOfBirth}.")