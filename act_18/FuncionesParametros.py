def saludo(nombre ="Sin Nombre"):
    print("Hola" , nombre, "Buenos Dias")

def Lista_Compras(lista):
    for x in lista:
        print(x)

def cuadrado(num):
    return num * num
        

saludo("Yezael")
saludo("Ana")
saludo("Yair")

saludo()

frutas = ["Manzana","Pera", "Palatano", "Naranaja"]

Lista_Compras(frutas)

print(cuadrado(5)+1)
print(cuadrado(15))
print(cuadrado(25))