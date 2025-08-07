class Curso:
    def __init__(self, nombre, codigo, creditos, salon, horario):
        self.__nombre = nombre
        self.__codigo = codigo
        self.__creditos = creditos
        self.__salon = salon
        self.__horario = horario
        self.__estudiantes = []
        self.__docente = None
        self.__asignaturas = []

    def agregarEstudiante(self, estudiante):
        self.__estudiantes.append(estudiante)

    def listarEstudiante(self):
        for est in self.__estudiantes:
            print(est.get_nombre())

    def asignarDocente(self, docente):
        self.__docente = docente

    def definirHorario(self, horario):
        self.__horario = horario

    def cancelarCurso(self):
        self.__estudiantes.clear()

    def get_nombre(self):
        return self.__nombre

    def get_horario(self):
        return self.__horario

    def agregarAsignatura(self, asignatura):
        self.__asignaturas.append(asignatura)

    def removerEstudiante(self, estudiante):
        if estudiante in self.__estudiantes:
            self.__estudiantes.remove(estudiante)
