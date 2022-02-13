import pandas

# Načti data do `DataFrame`, který si pojmenuj `jobs`.
jobs = pandas.read_csv("DataAnalyst.csv")

# Nech si zobrazit názvy sloupců, které jsou v souboru uloženy.
print(jobs.head())
# print(jobs.columns)
# print(jobs.info())

# Podívej se, kolik má soubor řádek.
print(jobs.shape)
# print(jobs.shape[0])  # vypise jen pocet radek
# print(jobs)  # na zaver vypise i rozmer tabulky

# Zjisti všechny informace o pracovní pozici na desátém řádku.
print(jobs.iloc[9])

# Podívej se, kde budou pracovat zájemci vybraní na dvanáctou až dvacátou pozici.
print(jobs.iloc[11:20, 6])  # Location
print(jobs.iloc[11:20, 5:8])  # Company Name, Location, Headquarters
