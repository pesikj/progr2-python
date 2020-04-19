sharing = input("Sdílel(a) jste alespoň 5 příspěvků? [ano/ne] ")
plays = input("Navštívil(a) jste alespoň 5 představení? [ano/ne] ")
clubMember = input("Jste členem klubu přátel divadla? [ano/ne] ")
if (sharing == "ano" and plays == "ano") or clubMember == "ano":
  print("Jste zařazen(a) do soutěže.")
else:
  print("Nemůžete být zařazen(a) do soutěže.")
