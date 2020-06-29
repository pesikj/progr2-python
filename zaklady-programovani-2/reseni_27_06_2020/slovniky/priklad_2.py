"""
Vydavatel detektivek si eviduje prodané kusy u jednotlivých knih. V následujícím slovníku najdeš tři knihy 
a u každé z nich je počet prodaných kusů.

sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}

- Zkopíruj si slovník do svého programu.
- Přidej do slovníku nově vydanou detektivku `"Noc, která mě zabila"`, která zatím nebyla uvedena na trh, je tedy prodáno `0` kusů.
- U knihy `"Vrah zavolá v deset"` zvyš počet prodaných kusů o `100`.
"""

sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}
sales["Noc, která mě zabila"] = 0
sales["Vrah zavolá v deset"] += 100

# Pro kontrolu
print(sales)