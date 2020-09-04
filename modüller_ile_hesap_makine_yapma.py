#Math modülündeki hazır fonksiyonları kullanarak gelişmiş bir hesap makinesi geliştirmeye çalışın.

from math import*
from time import*

while True:
    sayı1 = input("1. sayıyı giriniz :")
    sayı2 = input("2. sayıyı giriniz :")

    if sayı1 == 'q' and sayı2 == 'q':
        print("Çıkılıyor")
        sleep(2)
        break

    secim = input("""Toplam(+)\n
                Cıkarma(-)
                Carpma(-)
                Bolme(/)
                Mod(%)""")

    if secim == '+':
        sayı1 = int(sayı1)
        sayı2 = int(sayı2)

        toplama = sum(sayı1,sayı2)

        print("Toplama : ",toplama)

    elif secim == '-':
        sayı1 = int(sayı1)
        sayı2 = int(sayı2)
        if sayı1 > sayı2:
            cıkarma =  sayı1 - sayı2
            print("Çıkarma : ",cıkarma)
        elif sayı2 > sayı1:
            cıkarma = sayı2 - sayı1
            print("Çıkarma : ",cıkarma)
    elif secim == '*':
            sayı1 = int(sayı1)
            sayı2 = int(sayı2)
            carpma  = sayı1 * sayı2
            print("Çarpma : ",carpma)
    elif secim == '/':
        if sayı1 > sayı2:
            sayı1 = int(sayı1)
            sayı2 = int(sayı2)
            bolme = sayı1 / sayı2
            print("Bolme :",bolme)
        elif sayı2 > sayı1:
            sayı1 = int(sayı1)
            sayı2 = int(sayı2)
            bolme = sayı2 / sayı1
            print("Bolme :",bolme)
    elif secim == '%':
        if sayı1 > sayı2:
            sayı1 = int(sayı1)
            sayı2 = int(sayı2)
            kalan = sayı1 % sayı2
            print("Kalan : ",kalan)
        elif sayı2 >sayı1:
            sayı1 = int(sayı1)
            sayı2 = int(sayı2)
            kalan = sayı2 % sayı1
            print("Kalan : ",kalan)
    else:
        print("Geçerli bir işlem seçimi yapınız")
