"""
Zkus dotáhnout náš program na finanční vypořádání spolubydlících. 
Z lekce si můžeš zkopírovat kódy, které vytvoří slovník s útratami jednotlivých spolubydlících 
a výpočet průměrné útraty na osobu. Dopiš cyklus, který projde slovník sumPerPerson 
a pro každého ze spolubydlících vypíše, kolik by měl doplatit (pokud utratil(a) méně než průměr), 
případně kolik by měl obdržet (pokud utratil(a) více než průměr).
"""

purchaseList = [
  {"person": "Petr", "item": "Prací prášek", "value": 399},
  {"person": "Ondra", "item": "Savo", "value": 80},
  {"person": "Petr", "item": "Toaletní papír", "value": 65},
  {"person": "Libor", "item": "Pivo", "value": 124},
  {"person": "Petr", "item": "Pytel na odpadky", "value": 75},
  {"person": "Míša", "item": "Utěrky na nádobí", "value": 130},
  {"person": "Ondra", "item": "Toaletní papír", "value": 120},
  {"person": "Míša", "item": "Pečící papír", "value": 30},
  {"person": "Zuzka", "item": "Savo", "value": 80},
  {"person": "Pavla", "item": "Máslo", "value": 50},
  {"person": "Ondra", "item": "Káva", "value": 300}
]

sumPerPerson = {}
totalSum = 0
for purchase in purchaseList:
  person = purchase["person"]
  value = purchase["value"]
  if person in sumPerPerson:
    sumPerPerson[person] += value
  else:
    sumPerPerson[person] = value
  totalSum += value


averagePerPerson = totalSum/len(sumPerPerson)
for person, sum in sumPerPerson.items():
  if sum > averagePerPerson:
    print(f"{person} má obdržet {round(sum - averagePerPerson)} Kč.")
  else:
    print(f"{person} má doplatit {round(averagePerPerson - sum)} Kč.")
