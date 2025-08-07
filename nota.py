class Nota:
    def __init__(self, valor, tipo, fecha, observacion, porcentaje):
        self.__valor = valor
        self.__tipo = tipo
        self.__fecha = fecha
        self.__observacion = observacion
        self.__porcentaje = porcentaje

    # Registrar nota dentro de un estudiante
    def registrarNota(self, estudiante):
        estudiante.agregarNota(self)
        print(f"✅ Nota '{self.__tipo}' registrada para {estudiante.get_nombre()}.")

    # Modificar valor y observación
    def modificarNota(self, nuevo_valor=None, nueva_obs=None):
        if nuevo_valor is not None:
            self.__valor = nuevo_valor
        if nueva_obs is not None:
            self.__observacion = nueva_obs
        print(f"✏️ Nota '{self.__tipo}' modificada.")

    def consultarNota(self):
        return f"{self.__tipo}: {self.__valor} ({self.__porcentaje}%) - {self.__observacion}"

    @staticmethod
    def calcularNotaFinal(notas):
        return sum(n.get_valor() * n.get_porcentaje()/100 for n in notas)

    # Eliminar nota de un estudiante
    def eliminarNota(self, estudiante):
        if self in estudiante._Estudiante__notas:  # accediendo a la lista privada
            estudiante._Estudiante__notas.remove(self)
            print(f"🗑️ Nota '{self.__tipo}' eliminada de {estudiante.get_nombre()}.")
        else:
            print("⚠️ La nota no existe para este estudiante.")

    # Getters
    def get_valor(self):
        return self.__valor

    def get_porcentaje(self):
        return self.__porcentaje
