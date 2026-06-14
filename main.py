import customtkinter as ctk
from database import crear_tablas, agregar_producto, obtener_productos

# Crea tabla al iniciar aplicación:
crear_tablas()

# Configuración básica
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

# Ventana principal
app = ctk.CTk()
app.title("Sistema Inventario - Jardín Pippo")
app.geometry("900x600")

def registrar_producto():
    """toma datos del formulario y guarda en SQLite"""
    nombre = entrada_nombre.get()
    categoria = entrada_categoria.get()
    unidad_medida = entrada_unidad_medida.get()
    stock_actual = entrada_stock_actual.get()
    stock_minimo = entrada_stock_minimo.get()

    if nombre == "" or categoria == "" or unidad_medida == "":
        etiqueta_mensaje.configure(text="Completa nombre, categoría y unidad de medida")
        return
    
    try:
        stock_actual= float(stock_actual)
        stock_minimo = float(stock_minimo)
    except ValueError:
        etiqueta_mensaje.configure(text="Stock actual y mínimo deben ser números")
        return
    
    agregar_producto(nombre, categoria, unidad_medida, stock_actual, stock_minimo)
    
    etiqueta_mensaje.configure(text="Producto registrado correctamente")

    entrada_nombre.delete(0, "end")
    entrada_categoria.set("limpieza")
    entrada_unidad_medida.set("unidades enteras")
    entrada_stock_actual.delete(0, "end")
    entrada_stock_minimo.delete(0, "end")

    cargar_productos()


def cargar_productos():
    """Carga productos desde SQLite e imprímelos en pantalla"""
    caja_productos.delete("0.0", "end")
    
    productos = obtener_productos()

    if len(productos) == 0:
        caja_productos.insert("end", "No hay productos registrados todavía")
        return
    
    for producto in productos:
        id_producto, nombre, categoria, unidad_medida, stock_actual, stock_minimo = producto

        if stock_actual <= stock_minimo:
            estado = "URGENTE COMPRAR"
        else:
            estado = "Stock suficiente"
        
        texto = (
            f"ID: {id_producto} | "
            f"Producto: {nombre} | "
            f"Categoría: {categoria} | "
            f"Unidad: {unidad_medida} | "
            f"Stock: {stock_actual} | "
            f"Mínimo: {stock_minimo} | "
            f"Estado: {estado}\n"
        )

        caja_productos.insert("end", texto)

# Título
titulo = ctk.CTkLabel(app, text="Sistema de Inventario")
titulo.pack(pady=10)

# Marco formulario
marco_formulario = ctk.CTkFrame(app)
marco_formulario.pack(pady=10, padx=20, fill="x")

entrada_nombre = ctk.CTkEntry(marco_formulario, placeholder_text="Nombre del producto")
entrada_nombre.grid(row=0, column=0, padx=10, pady=10)

opciones_categoria = ["limpieza", "educativo", "oficina"]
opciones_unidad = ["unidades enteras", "litros", "kilogramos", "metros"]

entrada_categoria = ctk.CTkOptionMenu(
    marco_formulario,
    values=opciones_categoria
)
entrada_categoria.grid(row=0, column=1, padx=10, pady=10)
entrada_categoria.set("limpieza")

entrada_unidad_medida = ctk.CTkOptionMenu(
    marco_formulario,
    values=opciones_unidad
)
entrada_unidad_medida.grid(row=0, column=2, padx=10, pady=10)
entrada_unidad_medida.set("unidades enteras")

entrada_stock_actual = ctk.CTkEntry(marco_formulario, placeholder_text="Stock actual")
entrada_stock_actual.grid(row=1, column=0, padx=10, pady=10)

entrada_stock_minimo = ctk.CTkEntry(marco_formulario, placeholder_text="Stock mínimo")
entrada_stock_minimo.grid(row=1, column=1, padx=10, pady=10)

# Botón
boton_registrar = ctk.CTkButton(
    marco_formulario,
    text="Registrar producto",
    command=registrar_producto
)
boton_registrar.grid(row=1, column=2, padx=10, pady=10)

# Mensaje
etiqueta_mensaje = ctk.CTkLabel(app, text="")
etiqueta_mensaje.pack(pady=5)

# Se define caja de productos para listar
caja_productos = ctk.CTkTextbox(app, width=850, height=300)
caja_productos.pack(pady=10)

# Ejecutar
cargar_productos()
app.mainloop()