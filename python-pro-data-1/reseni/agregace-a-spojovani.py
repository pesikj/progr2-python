import pandas

studenti1 = pandas.read_csv("studenti1.csv")
studenti2 = pandas.read_csv("studenti2.csv")
studenti = pandas.concat([studenti1, studenti2], ignore_index=True)
print(studenti)

print(studenti[studenti["rocnik"].isnull()].shape)
print(studenti[studenti["kruh"].isnull()].shape)


studenti = studenti.dropna()
studenti.shape
studenti.groupby("obor").count()
studenti.groupby("obor")["prospeh"].mean()

jmena = pandas.read_csv("jmena.csv")

pandas.merge(studenti, jmena)

studentiPlusJmena = pandas.merge(studenti, jmena)
studentiPlusJmena.columns
studentiPlusJmena.groupby("pohlavi").count()
