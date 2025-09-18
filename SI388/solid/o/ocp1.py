class TipoEstudiante:
   def calcular_costo(self):
       pass


class Pregrado(TipoEstudiante):
   def calcular_costo(self):
       return 1500


class Maestria(TipoEstudiante):
   def calcular_costo(self):
       return 2500


class Doctorado(TipoEstudiante):
   def calcular_costo(self):
       return 3500

class SecEspecialidad(TipoEstudiante):
   def calcular_costo(self):
       return 4000


class CalculadorMatricula:
   def calcular_costo(self, tipo_estudiante: TipoEstudiante):
       return tipo_estudiante.calcular_costo()

ca = CalculadorMatricula()
print(ca.calcular_costo(Doctorado()))
print(ca.calcular_costo(SecEspecialidad()))