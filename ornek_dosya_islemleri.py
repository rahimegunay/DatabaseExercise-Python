with open("C:/Users/rahime/Desktop/Merhaba.txt", "r", encoding="utf-8") as Dosya:
    Dosya.seek(10)
    print(Dosya.read(10))
    print(Dosya.tell())