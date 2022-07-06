print('''Hos geldiniz!!
Hesap Makinesi
[1]) Toplama
[2] Cikarma
[3] Carpma
[4] Bolme
[5] Us Alma
[Q] Cikis
''')

islem= input('lutfen yapmak istediginiz islemi seciniz')

if islem=="1":
    sayi1=float(input('lutfen ilk sayisi giriniz'))
    sayi2= float(input('lutfen ikinci sayiyi giriniz'))
    print('Toplama isleminin sonucu {}'.format(sayi1 +sayi2))
elif islem=="2":
    sayi1=float(input('lutfen ilk sayisi giriniz'))
    sayi2= float(input('lutfen ikinci sayiyi giriniz'))
    print('Cikarma isleminin sonucu {}'.format(sayi1 - sayi2))
elif islem=="3":
    sayi1=float(input('lutfen ilk sayisi giriniz'))
    sayi2= float(input('lutfen ikinci sayiyi giriniz'))
    print('Carpma isleminin sonucu {}'.format(sayi1 * sayi2))
elif islem=="4":
    sayi1=float(input('lutfen ilk sayisi giriniz'))
    sayi2= float(input('lutfen ikinci sayiyi giriniz'))
    print('Bolme isleminin sonucu {}'.format(sayi1 / sayi2))

elif islem=='Q' or islem=='q':
    print("hesap makinesinden ciktiniz")




