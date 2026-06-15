import sqlite3

DB_NAME = "inventario.db"

def conectar():
    """Crear y retornar conexion a la base de datos SQLite."""
    return sqlite3.connect(DB_NAME)

# # Función tipo crud para base de datos inventario.db
# def funcion_crud():
#     """docstrig"""
#     conexion=conectar()
#     cursor = conexion.cursor()
#     cursor.execute(
#         """CODIGO SQL para SQLITE3"""
#     )
#     conexion.commit()
#     conexion.close()

def crear_tablas():
    """Crea tablas si no existen"""
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute(
            """CREATE TABLE IF NOT EXISTS productos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                categoria TEXT NOT NULL,
                unidad_medida TEXT NOT NULL,
                stock_actual REAL NOT NULL DEFAULT 0,
                stock_minimo REAL NOT NULL DEFAULT 0
                )"""
    )

    conexion.commit()
    conexion.close()

def agregar_producto(
        nombre,
        categoria,
        unidad_medida,
        stock_actual,
        stock_minimo
        ):
    """Agrega un producto nuevo al inventario"""
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute(
            """INSERT INTO productos (
                nombre,
                categoria,
                unidad_medida,
                stock_actual,
                stock_minimo
                )
            VALUES (?, ?, ?, ?, ?)
            """, (nombre, categoria, unidad_medida, stock_actual, stock_minimo)
    )

    conexion.commit()
    conexion.close()


def obtener_productos():
    """Retorna productos registrados"""
    conexion=conectar()
    cursor = conexion.cursor()

    cursor.execute(
        """SELECT id, nombre, categoria, unidad_medida, stock_actual, stock_minimo
        FROM productos
        ORDER BY nombre ASC"""
    )

    productos = cursor.fetchall()
    conexion.close()

    return productos

# busca productos que contengan texto escrito
# cruzada con categoría indicada
def buscar_productos(texto_busqueda, categoria_busqueda):
    """Busca productos por nombre y/o categoría."""
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute(
        """SELECT id, nombre, categoria, unidad_medida, stock_actual, stock_minimo
        FROM productos
        WHERE nombre LIKE ?
        AND categoria LIKE ?
        ORDER BY nombre ASC""",
        (f"%{texto_busqueda}%", f"%{categoria_busqueda}%")
    )

    productos = cursor.fetchall()
    conexion.close()

    return productos