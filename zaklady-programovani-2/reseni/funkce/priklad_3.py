def monthOfBirth(birthNumber):
  month = birthNumber[2] + birthNumber[3]
  month = int(month)
  month = month % 50
  return month

print(monthOfBirth("9555125899"))