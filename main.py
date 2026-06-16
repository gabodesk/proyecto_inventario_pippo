import customtkinter as ctk
from database import crear_tablas, agregar_producto, obtener_productos, buscar_productos, actualizar_producto

# Crea tabla al iniciar aplicación:
crear_tablas()

# Configuración básica
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

# Ventana principal
app = ctk.CTk()
app.title("Sistema Inventario - Jardín Pippo")

# se aumentó tamaño ventana
app.geometry("1000x600")

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

    # se agrega limpiar campo id
    entrada_id.delete(0, "end")
    entrada_nombre.delete(0, "end")
    entrada_categoria.set("limpieza")
    entrada_unidad_medida.set("unidades enteras")
    entrada_stock_actual.delete(0, "end")
    entrada_stock_minimo.delete(0, "end")


    cargar_productos()


def cargar_productos():
    """Carga todos los productos desde SQLite."""
    productos = obtener_productos()
    mostrar_productos(productos)


def mostrar_productos(productos):
    """Muestra en pantalla una lista de productos."""
    caja_productos.delete("0.0", "end")

    if len(productos) == 0:
        caja_productos.insert("end", "No hay productos para mostrar")
        return
    
    urgentes = []
    suficientes = []

    for producto in productos:
        id_producto, nombre, categoria, unidad_medida, stock_actual, stock_minimo = producto

        if stock_actual <= stock_minimo:
            urgentes.append(producto)
        else:
            suficientes.append(producto)

    productos_ordenados = urgentes + suficientes

    for producto in productos_ordenados:
        id_producto, nombre, categoria, unidad_medida, stock_actual, stock_minimo = producto

        if stock_actual <= stock_minimo:
            estado = "Urgente Comprar"
            etiqueta_color = "urgente"
        else:
            estado = "Stock suficiente"
            etiqueta_color = "suficiente"

        texto = (
            f"ID: {id_producto} | "
            f"Producto: {nombre} | "
            f"Categoría: {categoria} | "
            f"Unidad: {unidad_medida} | "
            f"Stock: {stock_actual} | "
            f"Mínimo: {stock_minimo} | "
            f"Estado: {estado}\n"
        )

        posicion_inicio = caja_productos._textbox.index("end-1c")
        caja_productos.insert("end", texto)
        posicion_final = caja_productos._textbox.index("end-1c")

        caja_productos._textbox.tag_add(etiqueta_color, posicion_inicio, posicion_final)

def buscar_en_pantalla():
    """Busca productos según texto y categoría seleccionada."""
    texto = entrada_busqueda.get()
    categoria = busqueda_categoria.get()

    if categoria == "todas":
        categoria = ""

    productos = buscar_productos(texto, categoria)

    mostrar_productos(productos)


def editar_producto():
    """Actualiza producto existente según ID."""
    try: 
        id_producto = int(entrada_id.get())
        nombre = entrada_nombre.get()
        categoria = entrada_categoria.get()
        unidad_medida = entrada_unidad_medida.get()
        stock_actual = float(entrada_stock_actual.get())
        stock_minimo = float(entrada_stock_minimo.get())

        if nombre == "": #campo vacio?
            etiqueta_mensaje.configure(text="Completa el nombre de producto")
            return
        
        actualizado = actualizar_producto(
            id_producto,
            nombre,
            categoria,
            unidad_medida,
            stock_actual,
            stock_minimo
        )

        # actualizado returns True or False
        if actualizado:
            etiqueta_mensaje.configure(text="Producto actualizado exitosamente")
            # faltaba cargar:
            cargar_productos()
        else:
            etiqueta_mensaje.configure(text="No se encontró producto con ese ID")
        
    except ValueError:
        etiqueta_mensaje.configure(text="ID, stock actual y stock mínimo deben ser números")








###### CUSTOMTKINTER INTERFAZ: ######

# Título -------------------------------
titulo = ctk.CTkLabel(app, text="Sistema de Inventario")
titulo.pack(pady=10)

# Marco formulario -------------------------------
marco_formulario = ctk.CTkFrame(app)
marco_formulario.pack(pady=10, padx=20, fill="x")

entrada_id = ctk.CTkEntry(marco_formulario, placeholder_text="ID (Solo para Editar)")
entrada_id.grid(row=0, column=0, padx=10, pady=10)

# se cambió de columna la entrada de nombre
entrada_nombre = ctk.CTkEntry(marco_formulario, placeholder_text="Nombre del producto")
entrada_nombre.grid(row=0, column=1, padx=10, pady=10)

opciones_categoria = ["limpieza", "educativo", "oficina"]
opciones_unidad = ["unidades enteras", "litros", "kilogramos", "metros"]

entrada_categoria = ctk.CTkOptionMenu(
    marco_formulario,
    values=opciones_categoria
)

# se cambia de columna entrada categoria
entrada_categoria.grid(row=0, column=2, padx=10, pady=10)
entrada_categoria.set("limpieza")

entrada_unidad_medida = ctk.CTkOptionMenu(
    marco_formulario,
    values=opciones_unidad
)
entrada_unidad_medida.grid(row=0, column=3, padx=10, pady=10)
entrada_unidad_medida.set("unidades enteras")

entrada_stock_actual = ctk.CTkEntry(marco_formulario, placeholder_text="Stock actual")
entrada_stock_actual.grid(row=1, column=0, padx=10, pady=10)

entrada_stock_minimo = ctk.CTkEntry(marco_formulario, placeholder_text="Stock mínimo")
entrada_stock_minimo.grid(row=1, column=1, padx=10, pady=10)


# Marco búsqueda -------------------------------
marco_busqueda = ctk.CTkFrame(app)
marco_busqueda.pack(pady=10, padx=20, fill="x")

entrada_busqueda = ctk.CTkEntry(
    marco_busqueda,
    placeholder_text="Buscar por nombre"
)
entrada_busqueda.grid(row=0, column=0, padx=10, pady=10)

busqueda_categoria = ctk.CTkOptionMenu(
    marco_busqueda,
    values=["todas", "limpieza", "educativo", "oficina"]
)
busqueda_categoria.grid(row=0, column=1, padx=10, pady=10)
busqueda_categoria.set("todas")

#   Botón Busqueda:
boton_buscar = ctk.CTkButton(
    marco_busqueda,
    text="Buscar",
    command=buscar_en_pantalla
)
boton_buscar.grid(row=0, column=2, padx=10, pady=10)

boton_mostrar_todos = ctk.CTkButton(
    marco_busqueda,
    text="Mostrar todos",
    command=cargar_productos
)
boton_mostrar_todos.grid(row=0, column=3, padx=10, pady=10)


# Botón registrar y actualizar
boton_registrar = ctk.CTkButton(
    marco_formulario,
    text="Registrar producto",
    command=registrar_producto
)
boton_registrar.grid(row=1, column=2, padx=10, pady=10)

boton_editar = ctk.CTkButton(
    marco_formulario,
    text="Editar producto",
    command=editar_producto
)
boton_editar.grid(row=1, column=3, padx=10, pady=10)
# Mensaje
etiqueta_mensaje = ctk.CTkLabel(app, text="")
etiqueta_mensaje.pack(pady=5)

# Se define caja de productos para listar -------------------------------
caja_productos = ctk.CTkTextbox(app, width=850, height=300)
caja_productos.pack(pady=10)

# Simbología de Color -------------------------------
caja_productos._textbox.tag_configure("urgente", foreground="#ff5555")
caja_productos._textbox.tag_configure("suficiente", foreground="#55ff55")

# Ejecutar -------------------------------
cargar_productos()
app.mainloop()


    ## Deprecated
    # for producto in productos_ordenados:
    #     id_producto, nombre, categoria, unidad_medida, stock_actual, stock_minimo = producto

    #     if stock_actual <= stock_minimo:
            
    #         estado = "URGENTE COMPRAR"
    #         etiqueta_color ="urgente"
    #     else:
    #         estado = "Stock suficiente"
    #         etiqueta_color = "suficiente"
