print("""\t******Merhaba Rbank'a hosgeldiniz******
\t\t\t ***Lutfen Kartinizi Takiniz...*** 
""")

Veritabani={"Ahmethesap":{
    "isim":"Ahmet",
    "soyisim":"Candan",
    "kartsifre":"1357",
    "Hesapbakiye":5000,
    "kredikartborc":4200,
    "kredikartborctarih":"21/11/2021"},
      "Mehmethesap":{
          "isim":"Mehmet",
    "soyisim":"Duyar",
    "kartsifre":"2468",
    "Hesapbakiye":6000,
    "kredikartborc":3800,
    "kredikartborctarih":"28/11/2021"}
    }
    
Takkart=dict(Veritabani["Ahmethesap"])

Hak=2
for i in range(0,3):
   sifre=input("Lutfen dort haneli sifrenizi giriniz:  ")
   if sifre==Takkart.get("kartsifre"):
      print("Hosgeldiniz Sayin {} {} , Lutfen yapmak istediginiz islemi secin ??".format(Takkart.get("isim"), Takkart.get("soyisim")))

      sec=input("""
      [1] Bakiye Sorma
      [2] Kredi Karti Borc Sorgulama
      [3] Para Cekme
      [4] Para Yatirma
      [Q] Kart Iade\n""")
      break
   elif sifre!=Takkart.get("kartsifre") and Hak !=0:
      print("Hatali sifre girdiniz... Kalan hakkiniz {}".format(Hak))
      Hak -= 1
   elif sifre!=Takkart.get("kartsifre") and Hak ==0:
      print("""Sifrenizi 3 defa hatali girdiniz, kartiniz bloke olmustur. Lutfen en yakin banka subemize basvurunuz..""")

      exit()
    

if sec=="1":
    print(""" Hesap bakiyeniz: {} TL'dir.""".format(Takkart.get("Hesapbakiye")))

elif sec=="2":
    print("""Kredi Karti borcunuz: {} son odeme tarihli, {} Tl'dir.""".format(Takkart.get("kredikartborctarih"), Takkart.get("kredikartborc")))

elif sec=="3":
   Miktar1=int(input("Lutfen cekeceginiz miktari giriniz:  "))
   if Takkart.get("Hesapbakiye")<Miktar1:
      print("Yetersiz Bakiye")
   else:
      print("Lutfen Paranizi aliniz..")
      Yenibakiye1=Takkart.get("Hesapbakiye")-Miktar1
      print("Hesap Bakiyeniz {} Tl'dir".format(Yenibakiye1))
if sec=="4":
   Miktar2=int(input("Lutfen Yaticaginiz Miktari Giriniz.."))
   print("Paraniz hesabiniza yatirilmistir.")
   Yenibakiye2=Takkart.get("Hesapbakiye") + Miktar2
   print("Geriye kalan bakiyeniz {}'dir.".format(Yenibakiye2))

if sec=="Q" or sec=="q":
   print("Tesekkur ederiz..")
   
   exit()

else:
   print("Lutfen gecerli bir islem yapiniz...")
