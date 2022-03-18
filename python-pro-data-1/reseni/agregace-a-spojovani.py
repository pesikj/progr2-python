import pandas

studenti1 = pandas.read_csv("studenti1.csv")
studenti2 = pandas.read_csv("studenti2.csv")

# Načti dva datové sety studentů do oddělených pandas DataFrame a pomocí funkce `concat` je spoj do jednoho setu.
studenti = pandas.concat([studenti1, studenti2], ignore_index=True)
print(studenti)

# Pokud studentovi chybí ročník, znamená to, že již nestuduje. Pokud mu chybí číslo skupiny, znamená to, že jde o dálkového studenta. Kolik studentů v datovém setu již nestuduje a kolik jsou dálkoví studenti?
print(studenti[studenti["ročník"].isnull()].shape)
print(studenti[studenti["kruh"].isnull()].shape)

# Vyčisti data od studentů, kteří nestudují nebo studují jen dálkově. Nadále budeme pracovat pouze s prezenčními studenty.
studenti = studenti.dropna()
studenti.shape

# Zjisti průměrný prospěch studentů v každém oboru.
studenti.groupby("obor").count()
studenti.groupby("obor")["prospěch"].mean()

# Načti datový set s křestními jmény. Proveď join s tabulkou studentů tak, abychom věděli pohlaví jednotlivých studentů.
jmena = pandas.read_csv("jmena.csv")

pandas.merge(studenti, jmena)
studenti_se_jmeny = pandas.merge(studenti, jmena)
studenti_se_jmeny.columns

# Zjisti, zda na naší fakultě studují IT spíše ženy nebo spíše muži.
studenti_se_jmeny.groupby("pohlaví").count()
# studenti_se_jmeny.groupby("pohlaví").size()
