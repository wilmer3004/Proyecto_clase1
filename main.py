from estudiante import Estudiante
from docente import Docente
from curso import Curso
from asignatura import Asignatura
from nota import Nota

# Listas globales
estudiantes = []
docentes = []
cursos = []
asignaturas = []
notas = []

# ==============================
# FUNCIONES DE CADA SECCIÓN
# ==============================

# -------- ESTUDIANTE --------
def menu_estudiante():
    while True:
        print("\n--- MENÚ ESTUDIANTE ---")
        print("1. Registrar estudiante")
        print("2. Calcular promedio")
        print("3. Consultar notas")
        print("4. Eliminar cuenta")
        print("5. Volver")
        op = input("Seleccione: ")

        if op == "1":
            nombre = input("Nombre: ")
            codigo = input("Código: ")
            correo = input("Correo: ")
            semestre = int(input("Semestre: "))
            est = Estudiante(nombre, codigo, correo, semestre)
            estudiantes.append(est)
            print("✅ Estudiante registrado.")

        elif op == "2":
            if not estudiantes:
                print("⚠️ No hay estudiantes.")
                continue
            for e in estudiantes:
                print(f"{e.get_nombre()} - Promedio: {e.calcularPromedio():.2f}")

        elif op == "3":
            if not estudiantes:
                print("⚠️ No hay estudiantes.")
                continue
            for i, e in enumerate(estudiantes, 1):
                print(f"{i}. {e.get_nombre()}")
            idx = int(input("Seleccione estudiante: ")) - 1
            estudiantes[idx].consultarNotas()

        elif op == "4":
            if not estudiantes:
                print("⚠️ No hay estudiantes.")
                continue
            for i, e in enumerate(estudiantes, 1):
                print(f"{i}. {e.get_nombre()}")
            idx = int(input("Seleccione estudiante: ")) - 1
            estudiantes[idx].eliminarCuenta()

        elif op == "5":
            break
        else:
            print("⚠️ Opción inválida.")


# -------- DOCENTE --------
def menu_docente():
    while True:
        print("\n--- MENÚ DOCENTE ---")
        print("1. Registrar docente")
        print("2. Crear curso")
        print("3. Asignar nota")
        print("4. Modificar horario")
        print("5. Consultar horario")
        print("6. Retirar estudiante de curso")
        print("7. Volver")
        op = input("Seleccione: ")

        if op == "1":
            nombre = input("Nombre: ")
            id_docente = input("ID: ")
            correo = input("Correo: ")
            area = input("Área: ")
            categoria = input("Categoría: ")
            doc = Docente(nombre, id_docente, correo, area, categoria)
            docentes.append(doc)
            print("✅ Docente registrado.")

        elif op == "2":
            if not docentes or not cursos:
                print("⚠️ Necesita docentes y cursos registrados.")
                continue
            for i, d in enumerate(docentes, 1):
                print(f"{i}. {d.get_nombre()}")
            idx = int(input("Seleccione docente: ")) - 1
            for i, c in enumerate(cursos, 1):
                print(f"{i}. {c.get_nombre()}")
            cidx = int(input("Seleccione curso: ")) - 1
            docentes[idx].crearCurso(cursos[cidx])

        elif op == "3":
            if not docentes or not estudiantes or not notas:
                print("⚠️ Necesita docentes, estudiantes y notas registradas.")
                continue
            for i, d in enumerate(docentes, 1):
                print(f"{i}. {d.get_nombre()}")
            didx = int(input("Seleccione docente: ")) - 1
            for i, e in enumerate(estudiantes, 1):
                print(f"{i}. {e.get_nombre()}")
            eidx = int(input("Seleccione estudiante: ")) - 1
            for i, n in enumerate(notas, 1):
                print(f"{i}. {n.consultarNota()}")
            nidx = int(input("Seleccione nota: ")) - 1
            docentes[didx].asignarNota(estudiantes[eidx], notas[nidx])

        elif op == "4":
            if not docentes or not cursos:
                print("⚠️ Necesita docentes y cursos.")
                continue
            for i, d in enumerate(docentes, 1):
                print(f"{i}. {d.get_nombre()}")
            didx = int(input("Seleccione docente: ")) - 1
            for i, c in enumerate(cursos, 1):
                print(f"{i}. {c.get_nombre()}")
            cidx = int(input("Seleccione curso: ")) - 1
            nuevo_horario = input("Nuevo horario: ")
            docentes[didx].modificarHorario(cursos[cidx], nuevo_horario)

        elif op == "5":
            if not docentes:
                print("⚠️ No hay docentes.")
                continue
            for d in docentes:
                d.consultarHorario()

        elif op == "6":
            if not docentes or not cursos or not estudiantes:
                print("⚠️ Faltan datos.")
                continue
            for i, d in enumerate(docentes, 1):
                print(f"{i}. {d.get_nombre()}")
            didx = int(input("Seleccione docente: ")) - 1
            for i, c in enumerate(cursos, 1):
                print(f"{i}. {c.get_nombre()}")
            cidx = int(input("Seleccione curso: ")) - 1
            for i, e in enumerate(estudiantes, 1):
                print(f"{i}. {e.get_nombre()}")
            eidx = int(input("Seleccione estudiante: ")) - 1
            docentes[didx].retirarEstudiante(cursos[cidx], estudiantes[eidx])

        elif op == "7":
            break
        else:
            print("⚠️ Opción inválida.")


# -------- CURSO --------
def menu_curso():
    while True:
        print("\n--- MENÚ CURSO ---")
        print("1. Registrar curso")
        print("2. Agregar estudiante a curso")
        print("3. Listar estudiantes")
        print("4. Asignar docente")
        print("5. Definir horario")
        print("6. Cancelar curso")
        print("7. Volver")
        op = input("Seleccione: ")

        if op == "1":
            nombre = input("Nombre: ")
            codigo = input("Código: ")
            creditos = int(input("Créditos: "))
            salon = input("Salón: ")
            horario = input("Horario: ")
            curso = Curso(nombre, codigo, creditos, salon, horario)
            cursos.append(curso)
            print("✅ Curso registrado.")

        elif op == "2":
            if not cursos or not estudiantes:
                print("⚠️ Faltan cursos o estudiantes.")
                continue
            for i, e in enumerate(estudiantes, 1):
                print(f"{i}. {e.get_nombre()}")
            eidx = int(input("Seleccione estudiante: ")) - 1
            for i, c in enumerate(cursos, 1):
                print(f"{i}. {c.get_nombre()}")
            cidx = int(input("Seleccione curso: ")) - 1
            estudiantes[eidx].registrarCurso(cursos[cidx])

        elif op == "3":
            if not cursos:
                print("⚠️ No hay cursos.")
                continue
            for i, c in enumerate(cursos, 1):
                print(f"{i}. {c.get_nombre()}")
            idx = int(input("Seleccione curso: ")) - 1
            cursos[idx].listarEstudiante()

        elif op == "4":
            if not cursos or not docentes:
                print("⚠️ Faltan cursos o docentes.")
                continue
            for i, c in enumerate(cursos, 1):
                print(f"{i}. {c.get_nombre()}")
            cidx = int(input("Seleccione curso: ")) - 1
            for i, d in enumerate(docentes, 1):
                print(f"{i}. {d.get_nombre()}")
            didx = int(input("Seleccione docente: ")) - 1
            cursos[cidx].asignarDocente(docentes[didx])

        elif op == "5":
            if not cursos:
                print("⚠️ No hay cursos.")
                continue
            for i, c in enumerate(cursos, 1):
                print(f"{i}. {c.get_nombre()}")
            idx = int(input("Seleccione curso: ")) - 1
            nuevo_horario = input("Nuevo horario: ")
            cursos[idx].definirHorario(nuevo_horario)

        elif op == "6":
            if not cursos:
                print("⚠️ No hay cursos.")
                continue
            for i, c in enumerate(cursos, 1):
                print(f"{i}. {c.get_nombre()}")
            idx = int(input("Seleccione curso: ")) - 1
            cursos[idx].cancelarCurso()

        elif op == "7":
            break
        else:
            print("⚠️ Opción inválida.")


# -------- ASIGNATURA --------
def menu_asignatura():
    while True:
        print("\n--- MENÚ ASIGNATURA ---")
        print("1. Registrar asignatura")
        print("2. Modificar información")
        print("3. Consultar detalles")
        print("4. Listar cursos")
        print("5. Archivar asignatura")
        print("6. Volver")
        op = input("Seleccione: ")

        if op == "1":
            nombre = input("Nombre: ")
            codigo = input("Código: ")
            semestre = input("Semestre: ")
            tipo = input("Tipo: ")
            descripcion = input("Descripción: ")
            asig = Asignatura(nombre, codigo, semestre, tipo, descripcion)
            asignaturas.append(asig)
            print("✅ Asignatura registrada.")

        elif op == "2":
            if not asignaturas:
                print("⚠️ No hay asignaturas.")
                continue
            for i, a in enumerate(asignaturas, 1):
                print(f"{i}. {a.get_nombre()}")
            idx = int(input("Seleccione asignatura: ")) - 1
            nombre = input("Nuevo nombre: ")
            codigo = input("Nuevo código: ")
            semestre = input("Nuevo semestre: ")
            tipo = input("Nuevo tipo: ")
            descripcion = input("Nueva descripción: ")
            asignaturas[idx].modificarInfo(nombre, codigo, semestre, tipo, descripcion)

        elif op == "3":
            if not asignaturas:
                print("⚠️ No hay asignaturas.")
                continue
            for a in asignaturas:
                print(a.consultarDetalles())

        elif op == "4":
            if not asignaturas or not cursos:
                print("⚠️ Faltan datos.")
                continue
            for i, a in enumerate(asignaturas, 1):
                print(f"{i}. {a.get_nombre()}")
            idx = int(input("Seleccione asignatura: ")) - 1
            asignaturas[idx].listarCurso(cursos)

        elif op == "5":
            if not asignaturas:
                print("⚠️ No hay asignaturas.")
                continue
            for i, a in enumerate(asignaturas, 1):
                print(f"{i}. {a.get_nombre()}")
            idx = int(input("Seleccione asignatura: ")) - 1
            asignaturas[idx].archivarAsignatura()

        elif op == "6":
            break
        else:
            print("⚠️ Opción inválida.")


# -------- NOTA --------
def menu_nota():
    while True:
        print("\n--- MENÚ NOTA ---")
        print("1. Registrar nota")
        print("2. Modificar nota")
        print("3. Consultar nota")
        print("4. Calcular nota final")
        print("5. Eliminar nota")
        print("6. Volver")
        op = input("Seleccione: ")

        if op == "1":
            if not estudiantes:
                print("⚠️ No hay estudiantes.")
                continue
            for i, e in enumerate(estudiantes, 1):
                print(f"{i}. {e.get_nombre()}")
            eidx = int(input("Seleccione estudiante: ")) - 1
            valor = float(input("Valor: "))
            tipo = input("Tipo: ")
            fecha = input("Fecha: ")
            obs = input("Observación: ")
            porcentaje = float(input("Porcentaje: "))
            nota = Nota(valor, tipo, fecha, obs, porcentaje)
            notas.append(nota)
            nota.registrarNota(estudiantes[eidx])

        elif op == "2":
            if not notas:
                print("⚠️ No hay notas.")
                continue
            for i, n in enumerate(notas, 1):
                print(f"{i}. {n.consultarNota()}")
            idx = int(input("Seleccione nota: ")) - 1
            nuevo_valor = float(input("Nuevo valor: "))
            nueva_obs = input("Nueva observación: ")
            notas[idx].modificarNota(nuevo_valor, nueva_obs)

        elif op == "3":
            if not notas:
                print("⚠️ No hay notas.")
                continue
            for n in notas:
                print(n.consultarNota())

        elif op == "4":
            if not notas:
                print("⚠️ No hay notas.")
                continue
            print(f"Nota final: {Nota.calcularNotaFinal(notas):.2f}")

        elif op == "5":
            if not estudiantes or not notas:
                print("⚠️ No hay estudiantes o notas.")
                continue
            for i, e in enumerate(estudiantes, 1):
                print(f"{i}. {e.get_nombre()}")
            eidx = int(input("Seleccione estudiante: ")) - 1
            for i, n in enumerate(notas, 1):
                print(f"{i}. {n.consultarNota()}")
            nidx = int(input("Seleccione nota: ")) - 1
            notas[nidx].eliminarNota(estudiantes[eidx])

        elif op == "6":
            break
        else:
            print("⚠️ Opción inválida.")


# ==============================
# MENÚ PRINCIPAL
# ==============================
while True:
    print("\n=== SISTEMA UNIVERSIDAD ===")
    print("1. Notas")
    print("2. Estudiantes")
    print("3. Asignaturas")
    print("4. Docentes")
    print("5. Cursos")
    print("6. Salir")
    op = input("Seleccione: ")

    if op == "1":
        menu_nota()
    elif op == "2":
        menu_estudiante()
    elif op == "3":
        menu_asignatura()
    elif op == "4":
        menu_docente()
    elif op == "5":
        menu_curso()
    elif op == "6":
        print("👋 Saliendo...")
        break
    else:
        print("⚠️ Opción inválida.")
