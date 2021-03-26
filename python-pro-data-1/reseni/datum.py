from datetime import datetime, timedelta

#-------------------- Apollo ----------------------------#
apollo_start = datetime(1969, 7, 16, 14, 32)
print(apollo_start.strftime("%#m/%d/%Y")) 

#- ("%m/%d/%Y") muzu pouzit # pro dani nuly pryc

#-------------------- Cas od startu ----------------------#
soStart = datetime(2020, 2, 10, 5, 3)
soStart.weekday()
uplynulo = datetime.now() - soStart
print(uplynulo)

#-------------------- Doprava Vecere ----------------------#
objednavka = datetime(2020, 11, 13, 19, 47)
prevzeti = timedelta(minutes=8,seconds=35)
priprava = timedelta (minutes=30)
doprava = timedelta(minutes=25, seconds=30)


celkem = objednavka +  prevzeti + priprava + doprava
print(celkem)