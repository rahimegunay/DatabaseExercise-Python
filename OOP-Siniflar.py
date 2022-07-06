class Insan():
    def __init__(self, Ad, Soyad, Dogumyili):
        self.Ad=Ad
        self.Soyad=Soyad
        self.Dogumyili=Dogumyili

    def bilgi(self):
        print( "Merhaba benim adim {}, soyadim {}, {} yilinda dogdum".format(self.Ad, self.Soyad, self.Dogumyili))

    def Yas(self):
        return 2022-self.Dogumyili

Insan1=Insan("Ahmet", "Can", 1980)
Insan2=Insan("Mehmet","Dur",1999)
Insan1.bilgi()

print(Insan1.Yas())