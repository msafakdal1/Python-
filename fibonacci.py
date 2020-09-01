ilk = 0
ikinci = 1


for i in range(1,21):
    sonraki  = ilk + ikinci
    ilk = ikinci
    ikinci = sonraki
    print(sonraki)
