import re
import time


class Kayit:
    def __init__(self, programad):
        self.programad=programad
        self.dongu=True





    def program(self):
        secim=self.menu()

        if secim=="1":
            print("Kayit ekleme menusune yonlendiriliyorsunuz...")
            time.sleep(3)
            self.kayitekle()

        if secim=="2":
            print("Kayit silme menusune yonlendiriliyorsunuz...")
            time.sleep(3)
            self.kayitcikar()

        if secim=="1":
            print("Kayitlara erisiliyor...")
            time.sleep(3)
            self.kayitoku()

        if secim=="4":
            self.cikis()




    def menu(self):
        def kontrol(secim):
            if re.search("[^1,4]", secim):
                raise Exception ("Lutfen 1 ve 4 arasinda gecerli bir secim yapiniz...")
            elif len(secim) !=1:
                raise Exception ("Lutfen 1 ve 4 arasinda gecerli bir secim yapiniz...")

        while True:
            try:
                secim=input("Merhabalar,{} otomasyon sistemine hosgeldiniz.\n\nLutfen yapmak istediginiz islemi seciniz...\n\n[1]-Kayit Ekle\n[2]-Kayit Sil\n[3]-Kayit oku\n[4]-Cikis\n\n".format(self.programad))
                kontrol(secim)
            except Exception as hata:
                print(hata)
                time.sleep(3)
            else:
                break
        return secim




    def kayitekle(self):
        def kontrolad(Ad):
            if Ad.isalpha()==False:
                raise Exception ("Adiniz sadece alfabetik karakterlerden olusmalidir...")
        while True:
            try:
                Ad=input("adiniz: ")
                kontrolad(Ad)
            except Exception as hataad:
                print(hataad)
                time.sleep(3)
            else:
                break
        

        def kontrolsoyad(Soyad):
            if Soyad.isalpha()==False:
                raise Exception ("Soyadiniz sadece alfabetik karakterlerden olusmalidir...")
        while True:
            try:
                Soyad=input("Soyadiniz: ")
                kontrolsoyad(Soyad)
            except Exception as hatasoyad:
                print(hatasoyad)
                time.sleep(3)
            else:
                break 

        def kontrolyas(Yas):
            if Yas.isdigit()==False:
                raise Exception ("Yasiniz sadece rakamlardan olusmalidir...")
        while True:
            try:
                Yas=input("Yasiniz: ")
                kontrolyas(Yas)
            except Exception as hatayas:
                print(hatayas)
                time.sleep(3)
            else:
                break   

        def kontroltc(TC):
            if TC.isdigit()==False:
                raise Exception ("Kimlik numaraniz sadece rakamlardan olusmalidir...")
            elif len(TC) != 11:
                raise Exception ("Kimlik numaraniz on bir rakamdan olusmalidir...")

        while True:
            try:
                TC=input("Kimlik numaraniz: ")
                kontroltc(TC)
            except Exception as hatatc:
                print(hatatc)
                time.sleep(3)
            else:
                break   
   
   
        def kontrolmail(Mail):
            if not re.search("@" and ".com", Mail):
                raise Exception ("Gecerli bir mail adresi giriniz...")

        while True:
            try:
                Mail=input("Mail adresiniz: ")
                kontrolmail(Mail)
            except Exception as hatamail:
                print(hatamail)
                time.sleep(3)
            else:
                break

        with open("C:/Users/rahime/Desktop/Bilgiler.txt", "r", encoding="utf-8") as Dosya:
            satirsayisi=Dosya.readlines()
        if len(satirsayisi)==0:
            Id=1
        else:
            with  open("C:/Users/rahime/Desktop/Bilgiler.txt", "r", encoding="utf-8") as Dosya:
                Id=int(Dosya.readlines()[-1].split("-")[0])+1

        with  open("C:/Users/rahime/Desktop/Bilgiler.txt", "a+", encoding="utf-8") as Dosya:
            Dosya.write("{} {} {} {} {}\n".format(Id,Ad, Soyad, TC, Yas, Mail))
            print("Veriler Islenmistir..")  
        self.menudon()



    
    
    
    
    
    
    
    
    
    def kayitcikar(self):
        y=input("Lutfen silmek istediginiz kisinin ID numarasini giriniz..")
        with open("C:/Users/rahime/Desktop/Bilgiler.txt", "r", encoding="utf-8") as Dosya:
            liste=[]
            liste2=Dosya.readlines()
            for i in range(0,len(liste2)):
                liste.append(liste2[i].split("-")[0])
        


        


    def kayitoku(self):
        pass
    def cikis(self):
        pass
    def menudon(self):
        pass












Sistem=Kayit("Rahime Veritabani")
while Sistem.dongu:
    Sistem.program()