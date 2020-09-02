def ekok(x,y):
    sonuc = 1

    if x > y :
        for i  in range(1,y):
            if x % i == 0 or y % i == 0:
                sonuc *= i
    elif y > x:
        for i in range(1,x):
            if x % i == 0 or y % i == 0:
                sonuc *= i

    return sonuc

x = int(input("x sayısını giriniz :"))
y = int(input("y sayısını giriniz :"))

print("{} sayısı ile {} sayısının ekok 'u : {}".format(x,y,ekok(x,y)))
