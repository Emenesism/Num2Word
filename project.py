
ykbis = [" ", "yek", "do", "se", "chahar", "panj", "shish", "haft", "hasht", "noh",
         "dah", "yazdah", "davazdah", "sizdah",  "chardah", "panozdah", "shanozdah", "hevdah", "hejdah", "noozdah"]

bis100 = ["", "", "bist", "si", "chehel", "panjah",
          "shast", "haftad", "hashtad", "navad"]

tahezar = ["", "sad", "divist", "sisad", "charsad",
           "pounsad", "sheshsad", "haftsad", "hashtsad", "nohsad"]

bign = [" hezar", " million", " billion", " trillion", " quadrillion", " quintillion", " sextillion", " septillion", " octillion",
        " nonillion", " decillion", " undecillion", " duodecillion", " tredecillion", " quattuordecillion", " quindecillion",
        " sexdecillion", " septemdecillion", " octodecillion", " novemdecillion", "Vigintillion"]


y = int(input("Mablag Khod ra be toman vared konid: "))
y *= 10


def numtoword(x):
    global ykbis
    global bis100
    global tahezar
    o = " o "
    if x == 0:
        return "Sefr"
    if x < 20:
        return ykbis[x].removesuffix(" o ")
    if x < 10**2:
        q, w = divmod(x, 10)
        if w == 0:
            return bis100[q]
        else:
            return bis100[q] + o + numtoword(w).removesuffix(" o ")
    if x < 10**3:
        q, w = divmod(x, 10**2)
        if w == 0:
            return tahezar[q]
        else:
            return tahezar[q] + o + numtoword(w).removesuffix(" o ")
    if x < 10**6:
        q, w = divmod(x, 10**3)
        if w == 0:
            return numtoword(q) + bign[0]
        else:
            return numtoword(q) + bign[0] + o + numtoword(w).removesuffix(" o ")
    if x < 10**9:
        q, w = divmod(x, 10**6)
        if w == 0:
            return numtoword(q) + bign[1]
        else:
            return numtoword(q) + bign[1] + o + numtoword(w).removesuffix(" o ")
    if x < 10**12:
        q, w = divmod(x, 10**9)
        if w == 0:
            return numtoword(q) + bign[2]
        else:
            return numtoword(q) + bign[2] + o + numtoword(w).removesuffix(" o ")
    if x < 10**15:
        q, w = divmod(x, 10**12)
        if w == 0:
            return numtoword(q) + bign[3]
        else:
            return numtoword(q) + bign[3] + o + numtoword(w).removesuffix(" o ")
    if x < 10**18:
        q, w = divmod(x, 10**15)
        if w == 0:
            return numtoword(q) + bign[4]
        else:
            return numtoword(q) + bign[4] + o + numtoword(w).removesuffix(" o ")
    if x < 10**21:
        q, w = divmod(x, 10**18)
        if w == 0:
            return numtoword(q) + bign[5]
        else:
            return numtoword(q) + bign[5] + o + numtoword(w).removesuffix(" o ")
    if x < 10**24:
        q, w = divmod(x, 10**21)
        if w == 0:
            return numtoword(q) + bign[6]
        else:
            return numtoword(q) + bign[6] + o + numtoword(w).removesuffix(" o ")
    if x < 10**27:
        q, w = divmod(x, 10**24)
        if w == 0:
            return numtoword(q) + bign[7]
        else:
            return numtoword(q) + bign[7] + o + numtoword(w).removesuffix(" o ")
    if x < 10**30:
        q, w = divmod(x, 10**27)
        if w == 0:
            return numtoword(q) + bign[8]
        else:
            return numtoword(q) + bign[8] + o + numtoword(w).removesuffix(" o ")
    if x < 10**33:
        q, w = divmod(x, 10**30)
        if w == 0:
            return numtoword(q) + bign[9]
        else:
            return numtoword(q) + bign[9] + o + numtoword(w).removesuffix(" o ")
    if x < 10**36:
        q, w = divmod(x, 10**33)
        if w == 0:
            return numtoword(q) + bign[10]
        else:
            return numtoword(q) + bign[10] + o + numtoword(w).removesuffix(" o ")
    if x < 10**39:
        q, w = divmod(x, 10**36)
        if w == 0:
            return numtoword(q) + bign[11]
        else:
            return numtoword(q) + bign[11] + o + numtoword(w).removesuffix(" o ")
    if x < 10**42:
        q, w = divmod(x, 10**39)
        if w == 0:
            return numtoword(q) + bign[12]
        else:
            return numtoword(q) + bign[12] + o + numtoword(w).removesuffix(" o ")
    if x < 10**45:
        q, w = divmod(x, 10**42)
        if w == 0:
            return numtoword(q) + bign[13]
        else:
            return numtoword(q) + bign[13] + o + numtoword(w).removesuffix(" o ")
    if x < 10**48:
        q, w = divmod(x, 10**45)
        if w == 0:
            return numtoword(q) + bign[14]
        else:
            return numtoword(q) + bign[14] + o + numtoword(w).removesuffix(" o ")
    if x < 10**51:
        q, w = divmod(x, 10**48)
        if w == 0:
            return numtoword(q) + bign[15]
        else:
            return numtoword(q) + bign[15] + o + numtoword(w).removesuffix(" o ")
    if x < 10**54:
        q, w = divmod(x, 10**51)
        if w == 0:
            return numtoword(q) + bign[16]
        else:
            return numtoword(q) + bign[16] + o + numtoword(w).removesuffix(" o ")
    if x < 10**57:
        q, w = divmod(x, 10**54)
        if w == 0:
            return numtoword(q) + bign[17]
        else:
            return numtoword(q) + bign[17] + o + numtoword(w).removesuffix(" o ")
    if x < 10**60:
        q, w = divmod(x, 10**57)
        if w == 0:
            return numtoword(q) + bign[18]
        else:
            return numtoword(q) + bign[18] + o + numtoword(w).removesuffix(" o ")

    if x < 10**63:
        q, w = divmod(x, 10**60)
        if w == 0:
            return numtoword(q) + bign[19]
        else:
            return numtoword(q) + bign[19] + o + numtoword(w).removesuffix(" o ")


print("Mablag shoma be digit",y )
print()
try:
    print((numtoword(y)) + " Rial")
except TypeError:
    print("Adad kharej az mahdoode ast")
    y = int(input("Mablag Khod ra be toman vared konid: "))
    y *= 10
    print((numtoword(y)) + " Rial")

