import re
dogumtarihi="1998"
karakter=["\?","\!","\*","\%"]

def sifrekontrol(sifre):
    if len(sifre)<8:
        raise Exception ("Sifreniz en az 8 karakterden olusmalidir!!")
    elif not re.search("[a-z]",sifre):
        raise Exception ("Sifreniz en az bir tane kucuk harf icermelidr!!!")
    elif not re.search("[A-Z]",sifre):
        raise Exception ("Sifreniz en az bir tane buyuk harf icermelidr!!!")
    elif not re.search("[0-9]",sifre):
        raise Exception ("Sifreniz en az bir tane rakam icermelidr!!!")
    elif not re.search(str(karakter),sifre):
        raise Exception ("Sifreniz en az bir tane karakter icermelidr!!!")
    elif sifre.startswith(dogumtarihi)==True:
        raise Exception ("Sifreniz dogum tarihinizle baslayamaz!!!!!!")
    elif sifre.endswith(dogumtarihi)==True:
        raise Exception ("Sifreniz dogum tarihinizle bitemez!!!!!!")
    else:
        print("Sifreniz basarili sekilde olusturulmustur...")

while True:
    try:
        sifre=input("Lutfen sifrenizi olusturunuz..:?")

        sifrekontrol(sifre)
    except Exception as hata:
        print(hata)
    else:
        break
