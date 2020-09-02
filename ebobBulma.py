def ebob(x,y):
    max = 0
    if x > y:
        for i in range(1,x):
            if x % i == 0 and y % i == 0:
                if i > max:
                    max = i
    elif y > x:
        for i in range(1,y):
            if x % i == 0 and y % i == 0:
                if i > max:
                    max = i
    return max

x = int(input("x sayısını giriniz :"))
y = int(input("y sayısını giriniz :"))

print("{} ile {} sayılarının ebob 'u  {}".format(x,y,ebob(x,y)))
