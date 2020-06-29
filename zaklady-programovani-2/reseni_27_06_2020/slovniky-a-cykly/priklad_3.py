"""
V následujícím slovníků je evidence automobilů. Klíčem jsou státní poznávací značky (SPZ) a hodnotou je jméno majitele vozu. 
Napiš program, který vypíše všechny majitele, jejichž vozidlo je registrováno v Plzňském kraji, 
tj. na druhém místě (index 1!) řetězce v klíči je písmeno P.

plates = {"4A2 3000": "František Novák", 
  "6P5 4747": "Jana Pilná",
  "3B7 3652": "Jaroslav Sečkár", 
  "1P5 5269": "Marta Nováková", 
  "37E 1252": "Martina Matušková",
  "2A5 2241": "Jan Král"}
"""

plates = {"4A2 3000": "František Novák", 
  "6P5 4747": "Jana Pilná",
  "3B7 3652": "Jaroslav Sečkár", 
  "1P5 5269": "Marta Nováková", 
  "37E 1252": "Martina Matušková",
  "2A5 2241": "Jan Král"}

for key, value in plates.items():
  if key[1] == "P":
    print(value)