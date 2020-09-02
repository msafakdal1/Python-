def tamBolen(sayı):
    liste = list()
    for i in range(2,sayı):
        if sayı % i == 0:
            liste.append(i)
    return liste


while True:
    sayı = input("Bir sayı giriniz :")

    if sayı == 'q':
        print("Çıkılıyor")
        break

    else:
        sayı = int(sayı)

        print(tamBolen(sayı))
