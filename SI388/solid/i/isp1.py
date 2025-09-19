
from abc import ABC, abstractmethod

class ServicioMatriculas(ABC):
   @abstractmethod
   def matricular_curso(self, estudiante, curso):
       pass
class ServicioCalificaciones(ABC):
   @abstractmethod
   def calificar_estudiante(self, estudiante, curso, nota):
       pass
class ServicioHorarios(ABC):
   @abstractmethod
   def generar_horarios(self, semestre):
       pass
class ServicioPagos(ABC):
   @abstractmethod
   def procesar_pagos(self, estudiante, monto):
       pass
class GestorMatriculas(ServicioMatriculas):
   def matricular_curso(self, estudiante, curso):
       pass
