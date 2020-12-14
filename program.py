text = """j
Kód	Kraj	2001–2004	Od 2004 do současnosti	Verze s písmenem na třetím místě	Zatím nejvyšší řada [9]
A	Praha	CZ-Praha-old.jpg	Czech registration 4542.jpg	Czech Republic license plate EU.JPG	8AL
B	Jihomoravský kraj		CZ-Brno-new.jpg		2BS
C	Jihočeský kraj	SPZ jihočeského kraje z let 2001-2004.jpg	CZ-SPZ-7C25025 01.jpg		9C2
E	Pardubický kraj		CZ-Padubice-new.jpg		6E7
H	Královéhradecký kraj	Czech registration 2000s 2627.jpg	CZ-Hradec-new.jpg		7H8
J	Kraj Vysočina	CZ-SPZ-2J26382.jpg	CZECH REPUBLIC EEC, c. 2009 -LICENSE PLATE - Flickr - woody1778a.jpg		6J9
K	Karlovarský kraj		CZ-KarlovyVary-new.jpg		4K8
L	Liberecký kraj		CZ-Liberec-new.jpg		6L3
M	Olomoucký kraj	CZ-SPZ-1M40000.jpg	CZ-SPZ-6M13246.jpg		7M3
P	Plzeňský kraj	CZECH REPUBLIC 2002-04 -LATEST NUMBERING SEQUENCE PRE EEC - Flickr - woody1778a.jpg	CZ-SPZ-7P24159.jpg		8P4
S	Středočeský kraj	CZ-Stredni-old.jpg	Czech registration 6737.JPG		5SK
T	Moravskoslezský kraj		CZ-MSkraj-new.jpg		2TB
U	Ústecký kraj		CZ-SPZ-6U32183.jpg		1UI
Z	Zlínský kraj	
"""

for line in text.splitlines():
    print(line[0], end=" ")