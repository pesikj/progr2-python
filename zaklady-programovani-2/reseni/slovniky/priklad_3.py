plates = {"4A2 3000": "František Novák", 
  "6P5 4747": "Jana Pilná",
  "3B7 3652": "Jaroslav Sečkár", 
  "1P5 5269": "Marta Nováková", 
  "37E 1252": "Martina Matušková",
  "2A5 2241": "Jan Král"}

for plate, owner in plates.items():
  if plate[1] == 'P':
    print(owner)