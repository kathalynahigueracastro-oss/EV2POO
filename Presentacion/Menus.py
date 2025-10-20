from colorama import init, Fore, Back, Style
from Aplicacion.ReglasEmpleado import ReglasEmpleado
from Aplicacion.ReglasDepartamento import ReglasDepartamento
from Aplicacion.ReglasProyecto import ReglasProyecto

class MenuSistema:
    def __init__(self):
        self.reglas_empleado = ReglasEmpleado()
        self.reglas_departamento = ReglasDepartamento()
        self.reglas_proyecto = ReglasProyecto()

    def menu_principal():
        
        print(Back.WHITE + Fore.MAGENTA)
        print("\n === Menú Principal === \n 1) Empleado \n 2) Departamentos \n 3) Proyectos \n 0) Salir")
        opcion = int(input("Seleccione una opción: "))

#--------Menú Empleados--------#
        if opcion == 1: 
            print("\n === Menú Empleados === \n 1) Agregar Empleado \n 2) Eliminar Empleado \n 3) Actualizar Empleado \n 4) Consultar Todos los Empleados \n 5) Buscar Empleado por ID \n 6)Buscar Empleado por Nombre \n 0) Volver Atrás")
            opcion2 = int(input("Seleccione una opción: "))
            if opcion2 == 1:
                id_empleado = int(input("ID del empleado: "))
                nombre = input("Nombre: ")
                correo = input("Correo: ")
                direccion = input("Dirección: ")
                contrasena = input("Contraseña: ")
                rol = input("Rol: ")
                telefono = input("Teléfono: ")
                fecha_contrato = input("Fecha de contratación (YYYY-MM-DD): ")
                salario = int(input("Salario: "))
                id_departamento = input("Id Departamento: ")
                
                self.reglas_empleado.crear_empleado(id_empleado, nombre, correo, direccion, contrasena, rol, telefono, fecha_contrato, salario, id_departamento)
                print("Empleado agregado exitosamente.")
                
            elif opcion2 == 2: 
                eliminar_empleado()
            elif opcion2 == 3: 
                actualizar_empleado()
            elif opcion2 == 4: 
                consultar_todos_los_empleados()
            elif opcion2 == 5:
                buscar_empleado_por_id()
            elif opcion2 == 6:
                buscar_empleado_por_nombre()
            elif opcion2 == 0:
                menu_principal()
            else: 
                print("Opción inválida, intente nuevamente.")
                menu_principal()
            
#--------Menú Departamentos--------#
        elif opcion == 2: 
            print("\n === Menú Departamentos === \n 1) Agregar Departamento \n 2) Eliminar Departamento \n 3) Actualizar Departamento \n 4) Consultar Todos Los Departamentos \n 5) Buscar Deparamento por ID \n 6)Buscar Departamento por Nombre \n 0) Volver Atrás")
            opcion2 = int(input("Seleccione una opción: "))
            if opcion2 == 1: 
                agregar_departamento()
            elif opcion2 == 2: 
                eliminar_departamento()
            elif opcion2 == 3: 
                actualizar_departamento()
            elif opcion2 == 4: 
                consultar_todos_los_departamentos()
            elif opcion2 == 5: 
                buscar_departamento_por_id()
            elif opcion2 == 6:
                buscar_departamento_por_nombre()
            elif opcion2 == 0: 
                menu_principal()
            else: 
                print("Opción inválida, intente nuevamente.")
                menu_principal()

#--------Menú Proyectos--------#
        elif opcion == 3: 
            print("\n === Menú Proyectos === \n 1) Agregar Proyecto \n 2) Eliminar Proyecto \n 3) Actualizar Proyecto \n 4) Consultar todos los Proyectos \n 5) Buscar Proyecto por ID \n 6)Buscar Proyecto por Nombre \n 0) Volver Atrás")
            opcion2 = int(input("Seleccione una opción: "))
            if opcion2 == 1: 
                agregar_proyecto()
            elif opcion2 == 2: 
                eliminar_proyecto()
            elif opcion2 == 3: 
                actualizar_proyecto()
            elif opcion2 == 4: 
                consultar_todos_los_proyectos()
            elif opcion2 == 5: 
                buscar_proyecto_por_id()
            elif opcion2 == 6:
                buscar_proyecto_por_nombre()
            elif opcion2 == 0: 
                menu_principal()
            else: 
                print("Opción inválida, intente nuevamente.")
                menu_principal()

#--------Salir--------#
        elif opcion == 0: 
            print("Saliendo del programa...")
            exit()
        else: 
            print("Opción inválida, intente nuevamente.")
            menu_principal()
        return opcion

menu_principal()