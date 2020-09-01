toplam = 0


while True:
    sayı = input("Sayı giriniz :")
    if sayı  == 'q':
        break
    toplam += int(sayı)


print("Toplam :",toplam)
print("Döngü bitti")
