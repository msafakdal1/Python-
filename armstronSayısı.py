toplam = 0

sayı = int(input("Bir sayı giriniz :"))
basamak = int(input("Basamak miktarını giriniz :"))

sayı1 = sayı

while  sayı != 0:
    sonuc = sayı % 10
    toplam += sonuc**basamak
    sayı = sayı // 10



print("Toplam : ",toplam)

if toplam == sayı1:
    print("Armstrong Sayısıdır")
else:
    print("Armstrong sayısı değildir")
