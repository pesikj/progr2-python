import json
from xml.etree.ElementTree import Element, SubElement, Comment, tostring, ElementTree
from xml.dom import minidom

data = """
[
  {
    "Jméno": "Petr",
    "Věc": "Prací prášek",
    "Částka v korunách": 399
  },
  {
    "Jméno": "Ondra",
    "Věc": "Savo",
    "Částka v korunách": 80
  },
  {
    "Jméno": "Petr",
    "Věc": "Toaletní papír",
    "Částka v korunách": 65
  },
  {
    "Jméno": "Libor",
    "Věc": "Pivo",
    "Částka v korunách": 124
  },
  {
    "Jméno": "Petr",
    "Věc": "Pytel na odpadky",
    "Částka v korunách": 75
  },
  {
    "Jméno": "Míša",
    "Věc": "Utěrky na nádobí",
    "Částka v korunách": 130
  },
  {
    "Jméno": "Ondra",
    "Věc": "Toaletní papír",
    "Částka v korunách": 120
  },
  {
    "Jméno": "Míša",
    "Věc": "Pečící papír",
    "Částka v korunách": 30
  },
  {
    "Jméno": "Zuzka",
    "Věc": "Savo",
    "Částka v korunách": 80
  },
  {
    "Jméno": "Pavla",
    "Věc": "Máslo",
    "Částka v korunách": 50
  },
  {
    "Jméno": "Ondra",
    "Věc": "Káva",
    "Částka v korunách": 300
  }
]"""

data = json.loads(data)
top = Element('nakupy')
for row in data:
    nakup = SubElement(top, 'nakup')
    nakup.text = str(row["Částka v korunách"])
    nakup.set("jméno", row["Jméno"])
    nakup.set("věc", row["Věc"])
tree = ElementTree(top)
tree.write('export.xml', encoding='utf-8')