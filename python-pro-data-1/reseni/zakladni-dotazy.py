import pandas

#----------------------Jmena 1 -----------------------------------#
jmena = pandas.read_csv("jmena.csv")
jmena = jmena.set_index("jméno")
print(jmena)

# Vypište na konzoli informace o jménu Jiří.
print(jmena.loc["Jiří"])
# Vypište na konzoli informace pro jména Martin, Zuzana a Josef.
print(jmena.loc[["Martin", "Zuzana", "Josef"]])
# Vypište na konzoli informace o všech nejčastějších jménech až po Martina.
print(jmena.loc[:"Martin"])
# Vypište pouze průměrné věky osob mající jména mezi Martinem a Terezou.
print(jmena.loc["Martin": "Tereza", "věk"])
# Vypište průměrný věk a původ pro všechna jména od Libora dolů.
print(jmena.loc["Libor":,["věk", "původ"]])
# Vypište sloupečky mezi věkem a původem pro všechna jména v tabulce.
print(jmena.loc[:,"věk":"původ"])


#----------------------Jmena 2 -----------------------------------#
jmena = pandas.read_csv("jmena.csv")
# Vypiš všechny řádky se jmény, jejichž nositelé mají průměrný věk vyšší než 60.
print(jmena[jmena["věk"] > 60])
# Vypiš pouze jména z těch řádků, kde četnost je mezi 80 000 a 100 000.
print(jmena[(jmena["četnost"] > 80_000) & (jmena["četnost"] < 100_000)])
# Vypiš jména a četnost pro jména se slovanským nebo hebrejským původem. Kolik takových jmen je?
vybrana_jmena = jmena[jmena["původ"].isin(["slovanský","hebrejský"])]
print(vybrana_jmena["četnost"])
# Vypiš všechna jména, která mají svátek první 3 dny v prosinci.
jmena_prosinec = jmena[jmena["svátek"].isin(["1.12","2.12","3.12"])]
print(jmena_prosinec.shape)
print(jmena_prosinec)
