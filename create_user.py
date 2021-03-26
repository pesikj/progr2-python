import pymongo
import csv
import pandas
import random
import string
import re

uzivatelskeJmeno = "pesikj"
heslo = ""
adresaServeru = "czechitas.westus2.cloudapp.azure.com"
klient = pymongo.MongoClient(
    f"mongodb://{uzivatelskeJmeno}:{heslo}@{adresaServeru}:27017/?"
)

nakup = {
    "Jméno": "Petr",
    "Věc": "Prací prášek",
    "Částka v korunách": 399,
    "Datum": "2020-03-04",
    "Značka": "Persil",
    "Hmotnost": 7.8,
}
# databaze = klient["jiripesik"]
# databaze.dropUser("jiripesik")
# kolekce = databaze["nakup"]
# id = kolekce.insert_one(nakup)
# print(kolekce.find())

myclient = klient

nakupy = [
    {
    "Jméno": "Petr",
    "Věc": "Prací prášek",
    "Částka v korunách": 399,
    "Datum": "2020-03-04",
    "Značka": "Persil",
    "Hmotnost": 7.8
    },
    {
        "Jméno": "Petr",
        "Věc": "Toaletní papír",
        "Částka v korunách": 65,
        "Počet rolí": 6,
    },
    {
        "Jméno": "Libor",
        "Věc": "Pivo na kolaudačku",
        "Částka v korunách": 124,
        "Vratná záloha": 20,
        "Datum": "2020-03-01",
        "Poznámka": "Vrátit otevírák sousedům",
    },
    {
        "Jméno": "Petr",
        "Věc": "Pytel na odpadky",
        "Částka v korunách": 75,
        "Objem pytle": 10,
        "Upozornění": "Příště koupit větší!!!",
    },
    {
        "Jméno": "Míša",
        "Věc": "Utěrky na nádobí",
        "Částka v korunách": 130,
        "Barva": "modrá",
        "Počet kusů v balení": 10,
    },
    {
        "Jméno": "Ondra",
        "Věc": "Toaletní papír",
        "Částka v korunách": 120,
        "Počet rolí": 15,
        "Běžná cena": 150,
    },
    {
        "Jméno": "Míša",
        "Věc": "Pečící papír",
        "Částka v korunách": 30,
        "Místo nákupu": "Albert",
        "Délka v metrech": 30,
        "Poznámka": "Peče celá země",
    },
    {
        "Jméno": "Zuzka",
        "Věc": "Savo",
        "Částka v korunách": 80,
        "Poznámka": "Dokoupit rukavice",
    },
    {
        "Jméno": "Pavla",
        "Věc": "Máslo",
        "Částka v korunách": 50,
        "Datum trvanlivosti": "2020-05-01",
    },
    {
        "Jméno": "Ondra",
        "Věc": "Káva",
        "Částka v korunách": 300,
        "Počet kusů": 2,
        "Značka": "Davidoff",
        "Poznámka": "Nejvíc vypila Míša",
    },
]

knihy = pandas.read_csv("books.csv", error_bad_lines=False)
knihy = knihy.set_index('bookID').to_dict(orient='records')

dataset = []
r = re.compile(r"@[.\w]*")
with open("maily.txt") as f:
    username_list = f.readlines()

    for username in username_list:
        username = r.sub("", username)
        username = username.replace(".", "").strip()
        print(username)
        newdb = myclient[username]
        
        password = "".join(random.choice(string.ascii_letters) for m in range(8))
        newdb.add_user(username, password, roles=[{'role':'readWrite','db':username}])
        dataset.append(
            {"uživatelskéJméno": username, "heslo": password, "databáze": username}
        )

        newcol = newdb["nakupy"]
        newcol.insert_many(nakupy)

        newcol = newdb["knihy"]
        newcol.insert_one({"První záznam": "užívej si Czechitas workshop"})
        newcol = newdb["hry"]
        newcol.insert_one({"První záznam": "užívej si Czechitas workshop"})
        newcol = newdb["goodreads"]
        newcol.insert_many(knihy)


    df = pandas.DataFrame(dataset)
    df.to_csv("dataset.csv")
