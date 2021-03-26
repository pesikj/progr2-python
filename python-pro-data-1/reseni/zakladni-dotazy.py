#----------------------Jmena 1 -----------------------------------#
jmena = pandas.read_csv("jmena100.csv")
jmena = jmena.set_index("jméno")
print(jmena)
print(jmena.loc["Jiří"])
print(jmena.loc[["Martin", "Zuzana", "Josef"]])
print(jmena.loc[:"Petr"])

print(jmena.loc["Martin": "Tereza", "věk"])
print(jmena.loc["Libor":,["věk", "původ"]])
print(jmena.loc[:,"věk":"původ"])


#----------------------Jmena 2 -----------------------------------#
print(jmena[jmena["věk"] > 60])
print(jmena[(jmena["četnost"] > 80_000) & (jmena["četnost"] < 100_000)])

vybranaJmena = jmena[jmena["původ"].isin(["slovanský","hebrejský"])]
print(vybranaJmena["četnost"])

unorJmena = jmena[jmena["svátek"].isin(["7.5","24.5","26.5"])] # Únorové svátky nikdo tam neni - takže jsem vybral tyhle 3 data
print(unorJmena.shape)
print(unorJmena)