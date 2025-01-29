# Herencia y sobre escritura de metodos

#Clase Base
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def saludo(self):
        print ("Hola, ",self.nombre,""+self.apellido," Buenos Dias")

#Clase Derivada
class Empleado(Persona):
    def __init__(self, nombre, apellido, salario):
        #Añadir funcionalidad
        Persona.__init__(self, nombre, apellido)
        self.salario = salario
    def despedia(self):
        print("Estas despedido",self.nombre,"",self.apellido,""+"Tu salario era de",self.salario)


#Crea la instancia
juan = Empleado("Juan", "Perez", 2000)
juan.saludo()
print(juan. salario)
juan.despedia()