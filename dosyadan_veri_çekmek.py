name = "Data Science"

folder = dict()

for ifade in name:
    if ifade not in folder:
        folder[ifade] = 1
    else:
        folder[ifade] = folder[ifade]  + 1

print(folder)
