# isim=str(input("Lutfen Adinizi Giriniz"))
# Yas=int(input("Lutfen Yasinizi Giriniz"))
# Egitim=str(input("Lutfen Egitim Durumunuzu Giriniz"))
# Egitim_dr=("Ilkokul", "Ortaokul", "Lise", "Universite")

# if Egitim not in Egitim_dr:
#     print("Lutfen Gecerli bir Egitim Durumu Giriniz!!")
# elif (Yas>=18) and (Egitim=="Lise" or Egitim=="Universite"):
#     print("Ehliyet Sartlari Gecildi!!")
# else:
#     print("Ehliyet Sartlari Gerceklesmiyor!!")

# sayi=int(input("Bir sayi giriniz? "))
# kontrol=(sayi>0) and (sayi%2==1)
# if kontrol==True:
#     print("{} pozitif tek bir sayidir".format(sayi))
# else:
#     print("tekrar bir sayi giriniz? ")

print(""" Hesap Makinesi Hosgeldiniz!!!!

[1]Toplama
[2]Cikarma
[3]Carpma
[4]Bolme
[5]Us Alma
[Q]Cikis

""")

islem=input("Lutfen Yapmak Istediginiz Islemi Seciniz:")

if islem=="1":
    sayi1=float(input("Lutfen Ilk Sayiyi Giriniz:"))
    sayi2=float(input("Lutfen Ikinci Sayiyi Giriniz:"))
    print("Toplama Isleminizin Sonucu {}".format(sayi1+sayi2))
elif islem=="2":
    sayi1=float(input("Lutfen Ilk Sayiyi Giriniz:"))
    sayi2=float(input("Lutfen Ikinci Sayiyi Giriniz:"))
    print("Cikarma Isleminizin Sonucu {}".format(sayi1-sayi2))

elif islem=="3":
    sayi1=float(input("Lutfen Ilk Sayiyi Giriniz:"))
    sayi2=float(input("Lutfen Ikinci Sayiyi Giriniz:"))
    print("Carpma Isleminizin Sonucu {}".format(sayi1*sayi2))
elif islem=="4":
    sayi1=float(input("Lutfen Ilk Sayiyi Giriniz:"))
    sayi2=float(input("Lutfen Ikinci Sayiyi Giriniz:"))
    print("Bolme Isleminizin Sonucu {}".format(sayi1/sayi2))
elif islem=="5":
    sayi1=float(input("Lutfen Ilk Sayiyi Giriniz:"))
    sayi2=float(input("Lutfen Kuvvet Derecesini Giriniz:"))
    print("Isleminizin Sonucu {}".format(sayi1**sayi2))
elif islem=="Q" or islem=="q":
    print("hesaplama islemi bitti!!!")
