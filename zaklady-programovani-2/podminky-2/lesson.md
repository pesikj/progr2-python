V této kapitle rozšíříme naše znalosti podmínek a cyklů. Vyzkoušíme si, jak vložit více podmínek do jednoho příkazu `if` a jak určit vztah mezi nimi. Dále si vyzkoušíme, jak pracovat s cykly i bez seznamů.

## Vícenásobné podmínky

Uvažujme, že chceme, aby se náš program rozhodoval na základě více podmínek. Máme-li dvě podmínky, musíme si nejprve určit **vztah mezi nimi**. Příkazu `if` totiž vždy musíme předat jen jednu hodnotu `True` nebo `False`. Musíme tedy **zkombinovat** obě podmínky tak, aby z nich vzešel jen jeden výsledek.

Máme dvě možnosti, jak podmínky kombinovat:

- logický součet (`or`),
- logický součin (`and`).

### Logické sčítání - OR

Nejprve si ukážeme, jak funguje logický součet. Výsledek logického součtu je `True`, jakmile má hodnotu `True` **alespoň jeden** ze dvou výrazů, za kterých se součet skládá.

Uvažujme následující dvě skutečnosti:

- Venku pršelo.
- Projel kropící vůz.

Za jakých okolností bude ulice mokrá? K tomu, aby byla ulice mokrá, stačí, aby byla splněna jedna ze dvou skutečností.

| Pršelo | Kropící vůz | Mokrá ulice|
|------------|--------------------|----|
| `False` |  `False` | `False` |
| `True` |  `False` | `True` |
| `False` |  `True` | `True` |
| `True` |  `True` | `True` |

Při zápisu do Pythonu používáme slovo `or`:

```py
rain = True
wateringTruck = True
if rain == True or wateringTruck == True:
  wetStreet = True
else:
  wetStreet = False
print(wetStreet)
```

#### Tip

Část `== True` můžete vynechat, následující kód provede to samé.

```py
rain = True
wateringTruck = True
if rain or wateringTruck:
  wetStreet = True
else:
  wetStreet = False
print(wetStreet)
```

### Logický součin - AND

Výsledek logického součinu je `True` pouze tehdy, mají-li hodnotu `True` **oba výrazy**, ze kterých se součin skládá. Uvažujme například dvě skutečnosti:

- Venku je mokrá ulice.
- Jdu ven.

Za jakých okolností budu mít mokré boty? Pouze v případě, kdy mají oba z předchozích výrazů hodnotu `True`. Pokud bychom zůstali doma nebo naopak vyšli za suchého počasí, naše boty zůstanou suché.

| Mokrá ulice | Jdu ven | Mokré boty |
|------------|--------------------|----|
| `False` |  `False` | `False` |
| `True` |  `False` | `False` |
| `False` |  `True` | `False` |
| `True` |  `True` | `True` |

K zápisu do Pythonu používáme slovo `and`.

```py
wetStreet = False
goOut = True
if wetStreet and goOut:
  wetShoes = True
else:
  wetShoes = False
print(wetShoes)
```

### Kombinace součtu a součinu

Součet a součin můžeme zkombinovat do jedné podmínky pomocí závorek. Zkusme si třeba vyhodnotit, zda budou naše boty mokré, pomocí informace o dešti a projetí kropícího vozu. Logický součet `or` proměnných `rain` a `wateringTruck` si vložíme do závorky a za něj napíšeme logický násobek `and` proměnnou `goOut`.

```py
rain = True
wateringTruck = False
goOut = True
if (rain or wateringTruck) and goOut:
  wetShoes = True
else:
  wetShoes = False
print(wetShoes)
```

### Kombinace operátorů

Další příklad nás zavede zpět k divadlu Pěst na oko. Uvažujme, že divadlo zjednodušilo cenovou politiku a dává slevu 50 % všem osobám do 26 let a nad 65 let. Náš program má určitě cenu vstupenky pro konkrétního návštěvníka na základě jeho věku. Pro poskytnutí slevy však musí být návštěvník členem klubu Přátele Divadla Pěst na oko.

```py
price = 250
age = int(input("Zadejte věk: "))
clubMember = input("Jste členem klubu přátel divadla? [ano/ne] ")
clubMember = clubMember.lower() == "ano"
if (age <= 26 or age >= 65) and clubMember:
  price = round(0.5 * price)
print(f"Cena vstupenky je {price}.")
```

#### Tip

Závorky můžeš *někdy* vynechat, pokud ale kombinuješ operátory `or` a `and` v jedné podmínce, použitím závorek si *vždy* usnadníš život. Nemusíš totiž myslet nad pravidly pro priority logických operací. Ta říkají, že operace `and` má vyšší prioritu než `or`. Je to podobné, jako když má běžné násobení vyšší prioritu než sčítání.

@exercises ## Další možnosti podmínek [

- delitelnost
- gymnazium
- gymnazium-2 ]@

@exercises bonuses [

- soutez ]@