
class MiClase:
    num = 10

    def __init__(this, nombre):
        this.nombre = nombre

    def saludo(ref):
        print("Hola "+ ref.nombre +" como estas")

num1 = MiClase("Pedro Picapiedra")

#num1.num = 33

print(num1.num)
num1.saludo()

# del num1.num
# print(num1.num)

del num1
print(num1)