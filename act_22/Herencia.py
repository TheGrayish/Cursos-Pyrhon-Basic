
#Clase Base
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def saludo(self):
        print ("Hola, ",self.nombre,""+self.apellido," Buenos Dias")

#Clase Derivada
class Empleado(Persona):
    pass

#Crea la instancia
juan = Empleado("Juan", "Perez")
juan.saludo()