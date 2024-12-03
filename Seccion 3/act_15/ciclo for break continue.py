fruta = ["fruta 1", "fruta 2", "fruta 3", "fruta 4"]
colores = ["Rojo", "Amarillo", "Verde"]

for x in fruta:
    if x == "fruta 3":
        break
    print(x)
print("------------------")

for x in fruta:
    if x == "fruta 3":
        continue
    print(x)
print("------------------")

for x in fruta:
    print(x)
else:
    print("son todas  las frutas")
print("------------------")

for x in colores:
    for y in fruta:
        print(x,y)
print("------------------")