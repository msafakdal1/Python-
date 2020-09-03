#Sonsuz bir döngü oluştur ve "done" girene kadar o döngümün ortalamaasını kaç adet sayı olduğunu ve aritmetik ortalamasını bul


total = 0.0
count = 0


while True :
    sayı = input("Enter a number")
    if sayı == 'done':
        break
    try:
        sayı = float(sayı)
    except:
        print("İnvalid value")
        continue

    total = total + sayı
    count = count + 1

average = total / count

print("Total : \nAverage : \nCount : ",total,average,count)
    
