class Docente:
    def __init__(self, nombre, id_docente, correo, area, categoria):
        self.__nombre = nombre
        self.__id = id_docente
        self.__correo = correo
        self.__area = area
        self.__categoria = categoria
        self.__cursos = []

    def crearCurso(self, curso):
        self.__cursos.append(curso)

    def asignarNota(self, estudiante, nota):
        estudiante.agregarNota(nota)

    def modificarHorario(self, curso, nuevo_horario):
        curso.definirHorario(nuevo_horario)

    def consultarHorario(self):
        for curso in self.__cursos:
            print(f"{curso.get_nombre()} - {curso.get_horario()}")

    def retirarEstudiante(self, curso, estudiante):
        curso.removerEstudiante(estudiante)

    # Métodos de acceso
    def get_nombre(self):
        return self.__nombre

    def get_id(self):
        return self.__id

    def get_correo(self):
        return self.__correo

    def get_area(self):
        return self.__area

    def get_categoria(self):
        return self.__categoria

# Hola como estas