class Estudiante:
    def __init__(self, nombre, codigo, correo, semestre):
        self.__nombre = nombre
        self.__codigo = codigo
        self.__correo = correo
        self.__semestre = semestre
        self.__promedio = 0
        self.__notas = []

    def registrarCurso(self, curso):
        curso.agregarEstudiante(self)

    def calcularPromedio(self):
        if not self.__notas:
            return 0
        self.__promedio = sum(n.get_valor() * n.get_porcentaje()/100 for n in self.__notas)
        return self.__promedio

    def consultarNotas(self):
        if not self.__notas:
            print("⚠️ No hay notas registradas.")
        for i, nota in enumerate(self.__notas, 1):
            print(f"{i}. {nota.consultarNota()}")

    def eliminarCuenta(self):
        self.__notas.clear()
        print(f"Cuenta del estudiante {self.__nombre} eliminada.")

    def agregarNota(self, nota):
        self.__notas.append(nota)

    def get_nombre(self):
        return self.__nombre

    def get_codigo(self):
        return self.__codigo

    def get_correo(self):
        return self.__correo

    def get_semestre(self):
        return self.__semestre

