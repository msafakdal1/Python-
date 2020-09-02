#1'den 100'e kadar olan sayılardan pisagor üçgeni oluşturanları ekrana yazdıran bir fonksiyon yazın.(a <= 100,b <= 100)

i = None
def pisagor():

    for i in range (1,101):
        for j in range(1,101):
            for k in range(1,101):
                if i == (j**2 + k**2)**0.5:
                    print("{} = {} * {}".format(i,j,k))

pisagor()
