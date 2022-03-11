"""
U zaměstnanců budeme nově evidovat, jestli jsou ve zkušební době.

Rozšiř funkci __init__ třídy Employee o parametr probation, který bude typu bool. ¨
Tuto hodnotu ulož jako atribut třídy Employee.

Uprav funkci getInfo. Pokud je zaměstnanec ve zkušební době, 
přidej k jeho/jejímu výpisu text Je ve zkušební době.
"""

class Zamestnanec:
    def __str__(self):
        text = f"Jméno: {self.jmeno}, pozice: {self.pozice}."
        if zkusebni_doba:
          text = text + " Je ve zkušební době."
        return text
    def cerpani_dovolene(self, dny):
        if self.pocet_dni_dovolene >= dny:
            self.pocet_dni_dovolene = self.pocet_dni_dovolene - dny
            return "Dovolená schválena"
        else:
            return f"Neschváleno, zbývá pouze {self.pocet_dni_dovolene} dní."
    def __init__(self, jmeno, pozice, zkusebni_doba):
        self.jmeno = jmeno
        self.pozice = pozice
        self.zkusebni_doba = zkusebni_doba
        self.pocet_dni_dovolene = 25
