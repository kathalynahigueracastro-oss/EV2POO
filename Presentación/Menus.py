def menu_principal():
    print("\n === Menú Principal === \n 1) Empleado \n 2) Departamentos \n 3) Proyectos \n 0) Salir")
    opcion = input("Seleccione una opción: ")

#--------Menú Empleados--------#
    if opcion == 1: 
        print("\n === Menú Empleados === \n 1) Agregar Empleado \n 2) Eliminar Empleado \n 3) Actualizar Empleado \n 4) Consultar Empleado \n 0) Volver Atrás")
        opcion2 = input("Seleccione una opción: ")
        if opcion2 == 1:
            pass
        elif opcion2 == 2: 
            pass
        elif opcion2 == 3: 
            pass
        elif opcion2 == 4: 
            pass
        elif opcion2 == 0:
            menu_principal()
        else: 
            print("Opción inválida, intente nuevamente.")
            menu_principal()
            
#--------Menú Departamentos--------#
    elif opcion == 2: 
        print("\n === Menú Departamentos === \n 1) Agregar Departamento \n 2) Eliminar Departamento \n 3) Actualizar Departamento \n 4) Consultar Departamento \n 0) Volver Atrás")
        opcion2 = input("Seleccione una opción: ")
        if opcion2 == 1: 
            pass
        elif opcion2 == 2: 
            pass
        elif opcion2 == 3: 
            pass
        elif opcion2 == 4: 
            pass
        elif opcion2 == 0: 
            menu_principal()
        else: 
            print("Opción inválida, intente nuevamente.")
            menu_principal()

#--------Menú Proyectos--------#
    elif opcion == 3: 
        print("\n === Menú Proyectos === \n 1) Agregar Proyecto \n 2) Eliminar Proyecto \n 3) Actualizar Proyecto \n 4) Consultar Proyecto \n 0) Volver Atrás")
        opcion2 = input("Seleccione una opción: ")
        if opcion2 == 1: 
            pass
        elif opcion2 == 2: 
            pass
        elif opcion2 == 3: 
            pass
        elif opcion2 == 4: 
            pass
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