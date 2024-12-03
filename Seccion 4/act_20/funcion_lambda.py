
x  = lambda y: y *2
suma = lambda x,y,z: x*y*z

def producto(n):
    return lambda x: x*n

doble = producto(2)
triple = producto(3)

print(doble(6))
print(triple(6))
print("-------------")

print(x(10))
print(x(7))
print(x(5))

print("-------------")
print("Suma")
a = 10
b = 20
c= 30
print(a,"*",b,"*",c,"=",suma(a,b,c))