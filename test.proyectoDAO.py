from Dominio.Proyecto import Proyecto
from Persistencia.Conexion import Conexion
from Persistencia.ProyectoDAO import ProyectoDao 

# Crear instancia de prueba
proyecto = Proyecto(
    id_proyecto=1,
    nombre="Sistema de Ventas",
    descripcion="Aplicación web para ventas minoristas",
    fecha_inicio="2025-01-01",
    fecha_fin="2025-06-01",
    presupuesto=25000.00
)

# === PRUEBA 1: Insertar ===
ProyectoDao.agregar_proyecto(proyecto)
print("Proyecto insertado correctamente.")

# === PRUEBA 2: Consultar ===
resultado = ProyectoDao.obtener_proyecto_por_id(1)
print("Proyecto obtenido:", resultado)

# === PRUEBA 3: Actualizar ===
proyecto_actualizado = Proyecto(
    id_proyecto=1,
    nombre="Sistema de Ventas v2",
    descripcion="Versión actualizada del sistema",
    fecha_inicio="2025-01-15",
    fecha_fin="2025-06-15",
    presupuesto=30000.00
)
ProyectoDao.actualizar_proyecto(proyecto_actualizado)
print("Proyecto actualizado correctamente.")

# === PRUEBA 4: Mostrar todos ===
todos = ProyectoDao.mostrar_todos_los_proyectos()
for p in todos:
    print(p)

# === PRUEBA 5: Eliminar ===
ProyectoDao.eliminar_proyecto(1)
print("Proyecto eliminado correctamente.")


