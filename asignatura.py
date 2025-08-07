class Asignatura:
    def __init__(self, nombre, codigo, semestre, tipo, descripcion):
        self.__nombre = nombre
        self.__codigo = codigo
        self.__semestre = semestre
        self.__tipo = tipo
        self.__descripcion = descripcion
        self.__notas = []

    def asignarCurso(self, curso):
        curso.agregarAsignatura(self)

    def modificarInfo(self, nombre, codigo, semestre, tipo, descripcion):
        """Modifica toda la información de la asignatura."""
        self.__nombre = nombre
        self.__codigo = codigo
        self.__semestre = semestre
        self.__tipo = tipo
        self.__descripcion = descripcion

    def consultarDetalles(self):
        return (f"{self.__nombre} ({self.__codigo}) - Semestre: {self.__semestre}, "
                f"Tipo: {self.__tipo}, Descripción: {self.__descripcion}")

    def listarCurso(self, cursos):
        for curso in cursos:
            print(curso.get_nombre())

    def archivarAsignatura(self):
        print(f"Asignatura {self.__nombre} archivada.")

    # Métodos de acceso
    def get_nombre(self):
        return self.__nombre

    def get_codigo(self):
        return self.__codigo

    def get_semestre(self):
        return self.__semestre

    def get_tipo(self):
        return self.__tipo

    def get_descripcion(self):
        return self.__descripcion
