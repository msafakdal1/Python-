toplam = 0
durum  = 0

sayı = int(input("Bir sayı giriniz :"))


for i in range(1,sayı):
    if sayı % i == 0:
        toplam += i
        if toplam == sayı:
            durum = 1
        else:
            durum = 0

if durum == 1:
    print("Mükemmel Sayıdır")
elif durum == 0:
    print("Mükemmel Sayı Değildir")
