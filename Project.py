sekil = input("Üçgen mi dörtgen mi?")

if sekil == 'Dikdörtgen':
    kenar1 = int(input("Kenar giriniz :"))
    kenar2 = int(input("Kenar giriniz :"))
    kenar3 = int(input("Kenar giriniz :"))
    kenar4 = int(input("Kenar giriniz :"))

    if kenar1 == kenar2 == kenar3 == kenar4:
        print("Dörtgendir")

    else:
        print("Karedir")

if sekil == 'Üçgen':
    kenar1 = int(input("Kenar Giriniz :"))
    kenar2 = int(input("Kenar Giriniz"))
    kenar3 = int(input("Kenar Giriniz"))

    if (abs(kenar2 - kenar3) < kenar1 < kenar2 + kenar3) and (abs(kenar1 - kenar3) < kenar2 < kenar1 + kenar3) and (abs(kenar1 - kenar2) <kenar3 <kenar1 + kenar2):
        if kenar1 == kenar2 == kenar3:
            print("Eşkenar Üçgendir")
        elif kenar1 == kenar2 or kenar1 == kenar3 or kenar2 == kenar3:
            print("İkiz Kenar Üçgendir")
        else:
            print("Sıradan Bir Üçgendir")

    else:
        print("Üçgen Belirtmiyor")
