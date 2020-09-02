"""
Kullanıcıdan 2 basamaklı bir sayı alın ve bu sayının okunuşunu bulan bir fonksiyon yazın.

Örnek: 97 ---------> Doksan Yedi"""

def sayıOkuma(sayı):
    liste1 = ["","bir","iki","üç","dört","beş","altı","yedi","sekiz","dokuz"]
    liste2 = ["","On","Yirmi","Otuz","Kırk","Elli","Altmış","Yetmiş","Seksen","doksan"]

    birler = sayı % 10
    onlar = sayı // 10

    print(liste2[onlar] + " " +  liste1[birler])

sayıOkuma(17)
