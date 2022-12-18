from math import ceil
ykbis = ["", "yek", "do", "se", "chahar", "panj", "shish", "haft", "hasht", "noh",
         "dah", "yazdah", "davazdah", "sizdah",  "chardah", "panozdah", "shanozdah", "hevdah", "hejdah", "noozdah"]

bis100 = ["", "", "bist", "si", "chehel", "panjah",
          "shast", "haftad", "hashtad", "navad"]

tahezar = ["", "sad", "divist", "sisad", "charsad",
           "pounsad", "sheshsad", "haftsad", "hashtsad", "nohsad"]

bign = ["", "", "hezar", "million", "billion", "trillion", "quadrillion", "quintillion", "sextillion", "septillion", "octillion",
        "nonillion", "decillion", "undecillion", "duodecillion", "tredecillion", "quattuordecillion", "quindecillion",
        "sexdecillion", "septemdecillion", "octodecillion", "novemdecillion", "Vigintillion"]

x = input("Adad khod ra vared konid: ")
x += '0'
X, zarib, o, O, lst = x[::-1], ceil(len(x) / 3), 0, 3, []

for i in range(zarib):
    lst.append(X[o:O])
    o += 3
    O += 3
lst2 = lst[::-1]


def numtoword(x):
    global ykbis
    global bis100
    global tahezar
    if x < 20:
        return ykbis[x]
    if x < 100:
        div, mod = divmod(x, 10)
        if mod == 0:
            return bis100[div]
        else:
            return bis100[div] + " o " + numtoword(mod)
    if x < 1000:
        div, mod = divmod(x, 100)
        if mod == 0:
            return tahezar[div]
        else:

            return tahezar[div] + " o " + numtoword(mod)


if int(x) == 0:
    print("sefr")
else:
    za = zarib
    for i in lst2:
        ireverse = int(i[::-1])
        if ireverse == 0:
            print(numtoword(ireverse), end="")
        else:
            print(numtoword(ireverse), bign[za], end=" ")
        if za != 0:
            za -= 1
        if lst2.index(i) == len(lst2) - 1:
            print("Rial ", end="")
