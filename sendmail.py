import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def send_email(email_recipient,
               email_subject,
               email_message):

    email_sender = 'jiri.pesik@outlook.cz'

    msg = MIMEMultipart()
    msg['From'] = email_sender
    msg['To'] = email_recipient
    msg['Subject'] = email_subject

    msg.attach(MIMEText(email_message, 'plain'))

    try:
        server = smtplib.SMTP('smtp.office365.com', 587)
        server.ehlo()
        server.starttls()
        server.login('jiri.pesik@outlook.cz', 'sjdbtobcjrurtwgy')
        text = msg.as_string()
        server.sendmail(email_sender, email_recipient, text)
        print('email sent to ' + email_recipient)
        server.quit()
    except:
        print("SMPT server connection error")
    return True


mailList = []
with open("maily.txt") as f:
    for line in f:
        mailList.append(line.strip())

with open('dataset.csv', encoding="UTF-8") as csvfile:
    spamreader = csv.DictReader(csvfile)
    for row in spamreader:
        content = f"""
import pymongo
uzivatelskeJmeno = "{row["uživatelskéJméno"]}"
heslo = "{row["heslo"]}"
adresaServeru = "czechitas.westus2.cloudapp.azure.com"
databaze = "{row["uživatelskéJméno"]}"
klient = pymongo.MongoClient(f"mongodb://{row["uživatelskéJméno"]}:{row["heslo"]}@czechitas.westus2.cloudapp.azure.com:27017/{row["uživatelskéJméno"]}")
databaze = klient["{row["uživatelskéJméno"]}"]

# Toto slouží pro test
kolekce = databaze["nakupy"]
nakup = kolekce.find_one()
print(nakup)
        """
        for mail in mailList:
            if row["uživatelskéJméno"] in mail.replace(".", ""):
                send_email(mail, "Přihlášení k databázi Mongo", content)
