import matplotlib.pyplot as plt
import pandas
import requests

# 1

url = "https://kodim.cz/czechitas/progr2-python/python-pro-data-1/vizualizace/excs/hazeni-kostkami/assets/kostky.csv"
r = requests.get(url, allow_redirects=True, verify=False)
open('kostky.txt', 'wb').write(r.content)

# Načtěte tato data do tabulky a zobrazte histogram hodů. Zvolte vhodné rozložení přihrádek a zodpovězte následující dotazy:
# Jaká je nejčastější hodnota, která na dvou kostkách padne?
# Je větší šance, že padne hodnota 12 než že padne hodnota 2?
kostky = pandas.read_csv("kostky.txt")
kostky.hist(bins=[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# kostky.hist(bins=11)
plt.show()

url = "https://kodim.cz/czechitas/progr2-python/python-pro-data-1/vizualizace/excs/call-centrum/assets/callcentrum.csv"
r = requests.get(url, allow_redirects=True, verify=False)
open('callcentrum.txt', 'wb').write(r.content)

# 2
callcentrum = pandas.read_csv("callcentrum.txt")
callcentrum = callcentrum["hodnota"].str.split(':', expand=True).astype(int)
callcentrum["vteriny"] = callcentrum[0] * 60 + callcentrum[1]

callcentrum["vteriny"].hist()
plt.show()

callcentrum["vteriny"].plot(kind='box', whis=[0, 100])
plt.show()

# 3
snih = [
  [1968, 480, 351],
  [1969, 462, 663],
  [1970, 443, 490],
  [1971, 518, 444],
  [1972, 537, 420],
  [1973, 446, 941],
  [1974, 446, 691],
  [1975, 450, 477],
  [1976, 356, 395],
  [1977, 381, 652],
  [1978, 345, 525],
  [1979, 430, 762],
  [1980, 266, 316],
  [1981, 533, 781],
  [1982, 471, 769],
  [1983, 407, 801],
  [1984, 526, 633],
  [1985, 391, 488],
  [1986, 361, 624],
  [1987, 470, 471],
  [1988, 506, 514],
  [1989, 333, 208],
  [1990, 462, 909],
  [1991, 438, 443],
  [1992, 364, 488],
  [1993, 452, 579],
  [1994, 484, 519],
  [1995, 460, 809],
  [1996, 465, 682],
  [1997, 431, 814],
  [1998, 463, 595],
  [1999, 460, 512],
  [2000, 503, 750],
  [2001, 462, 951],
  [2002, 429, 413],
  [2003, 405, 738],
  [2004, 477, 777],
  [2005, 385, 316],
  [2006, 368, 417],
  [2007, 513, 635],
  [2008, 448, 689],
  [2009, 525, 443],
  [2010, 427, 225],
  [2011, 460, 618],
  [2012, 417, 742],
  [2013, 517, 247],
  [2014, 466, 552],
  [2015, 523, 441],
  [2016, 422, 690],
  [2017, 420, 699]
]

snihdf = pandas.DataFrame(snih, columns=['rok', 'hora', 'udoli'])
snihdf = snihdf.set_index('rok')
snihdf.plot(kind='box', whis=[0, 100])
plt.show()
