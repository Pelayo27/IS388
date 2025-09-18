class CalculadorMatricula:
   def calcular_costo(self, tipo_estudiante):
       if tipo_estudiante == "pregrado":
           return 1500
       elif tipo_estudiante == "maestria":
           return 2500
       elif tipo_estudiante == "doctorado":
           return 3000

ma = CalculadorMatricula()
print(ma.calcular_costo("pregrado"))
print(ma.calcular_costo("maestria"))