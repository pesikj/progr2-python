

```
pip install forex-python
```

```py
python
>>> from forex_python.converter import CurrencyRates
>>> c = CurrencyRates()
```

```py
from forex_python.converter import CurrencyRates
c = CurrencyRates()
```

```py
>>> c.get_rates('CZK') 
{'GBP': 0.0324795265, 'HKD': 0.3163155152, 'IDR': 641.344922573, 'ILS': 0.1462179869, 'DKK': 0.277780673, 'INR': 3.1080256105, 'CHF': 0.0392458309, 'MXN': 0.9621984812, 'CZK': 1.0, 'SGD': 0.0577762061, 'THB': 1.3348719476, 'HRK': 0.283390411, 'EUR': 0.0372245384, 'MYR': 0.1768463371, 'NOK': 0.4210765337, 'CNY': 0.2879913639, 'BGN': 0.0728037522, 'PHP': 2.0642123288, 'PLN': 0.1692711435, 'ZAR': 0.745439994, 
'CAD': 0.0567934783, 'ISK': 5.803305539, 'BRL': 0.2106350506, 'RON': 0.1799545861, 'NZD': 0.0670339488, 'TRY': 0.2772185825, 'JPY': 4.37983919, 'RUB': 2.9925662597, 'KRW': 49.6028141751, 'USD': 0.0408092615, 'AUD': 0.0637991364, 'HUF': 13.0546456224, 'SEK': 0.4063356164}
```