
""""
Python ile veri analizi

Merkezi Limit Teoremi: Uygun bir sekilde secilen orneklem tum populasyona benzer.Populasyon icerisinden defalarca rastgele orneklem alirsak bu orneklem ortalamasi populasyon ortalasi etrafinda normal dagilima yakinsar.
Neden normal dagilima dogru gitmek istiyoruz? 
Normal dagilima dogru gidersek hesaplamamiz daha kolay oluyor.

seaborn kutuphanesi ile veri gorsellestirme.
Seaborn matplotlib ile birlikte calismaktadir.
Standart hata: orneklemin ortalamadan ne kadar uzak oldugunun gostergesidir. Formulu s/karekok gozlem sayisi

z score: dagilimdaki verilerin ortalamadan kac standart sapma uzaklikta oldugunu verir. 
Can egrisi icinde kalan kisim bir alandir.

Random veri uretirken numpy arrayde seed fonksiyonu kullanilarak secilen random numaralari sabitlemeye yarar. 
np.random.seed(0)

Normal dagilim Ortalamasi=0 ve Standart Sapmasi=1 olan dagilimdir.

Standartlastirma(Z-Score):
Ortalamasi 0 olmayan dagilimi normal dagilima cevirmektir. Icindeki olasilik alaninin hesaplayabilecegimiz bir dagilam donusturuyoruz. 
Standartlastirma(Z-Score)= (veri-Ortalama)/Standart sapma

Bir veriden basit bir sekilde anlamli veriler olusutrmak icin kullanilan yontemdir standartlastirma ve zscore altinda kalan alani bulmak.

"""