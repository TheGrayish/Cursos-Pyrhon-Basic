x= 10
y = 50
z = 100

if y > x: 
    print("Y es mayor que x")
print("----------------------------------------------")

if y > x : 
    print("X es mayor que Y")
elif x < y : 
    print("X es mayor que Y")
else:
    print("X es igual a Y")

print("----------------------------------------------")

print('X') if x > y else print('Y')
print("----------------------------------------------")

print('X') if x > y else print('Y') if x == y else print ('HOla')
print("----------------------------------------------")

if x > y and y < z:  print("Las dos son verdaderas")
print("----------------------------------------------")

if x > y or y < z:  print("Solo una es verdadera")
print("----------------------------------------------")