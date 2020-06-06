"""
Divadlo Pěst na oko pořádá soutěž o lístky na premiéru nového představení Zločin v podmínce. 

Pro účast v soutěži musí zájemce splnit následující dvě podmínky:
- Sdílel alespoň 5 příspěvků divadla na sociálních sítích.
- Letos navštívil(a) alespoň 5 představení.

Současně platí, že soutěžit můžou všichni členové Klubu přátel Divadla Pěst na oko, i kdyby podmínky nesplnili.

Tvým úkolem je vytvořit program, který se uživatele zeptá na všechny potřebné informace 
(stačí odpověď ano/ne) a vyhodnotí, zda se může zúčastnit soutěže.
"""



sharing = input("Sdílel(a) jste alespoň 5 příspěvků? [ano/ne] ")
plays = input("Navštívil(a) jste alespoň 5 představení? [ano/ne] ")
clubMember = input("Jste členem klubu přátel divadla? [ano/ne] ")
if (sharing == "ano" and plays == "ano") or clubMember == "ano":
  print("Jste zařazen(a) do soutěže.")
else:
  print("Nemůžete být zařazen(a) do soutěže.")
