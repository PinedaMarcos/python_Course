"""Ejercicio 1

Realizar un programa que conste de una clase
llamada Alumno que tenga como atributos el 
nombre y la nota del alumno. Definir los 
métodos para inicializar sus atributos, 
imprimirlos y mostrar un mensaje con el 
resultado de la nota y si ha aprobado o no."""

#clase
class Estudiante():
#atributos
     def __init__(self, nombre, nota):
          self.nombre = nombre
          self.nota = nota

     def imprimir(self):
        print("Nombre: {} \nNota: {}".format(self.nombre, self.nota))

     def resultados(self):
        if self.nota < 7:
            print("Chale mi crack, REPROBASTE")

        else:
            print("Eres un master Crack, APROBASTE")

estudiante1 = Estudiante("Daniel", 10)
estudiante1.imprimir()
estudiante1.resultados()