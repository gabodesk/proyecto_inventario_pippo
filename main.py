import customtkinter as ctk

# configuración predeterminada
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

# ventana principal
app = ctk.CTk()
app.title("Sistema de Inventario - Jardín Pippo")
app.geometry("800x500")

# Títulos
titulo = ctk.CTkLabel(
    app,
    text="Sistema de Gestión de Inventario",
    font=("Arial", 20, "bold")
)
titulo.pack(pady=20)

subtitulo = ctk.CTkLabel(
    app,
    text="Prototipo funcional para artículos de limpieza",
    font=("Arial", 16)
)

# Probando botones
boton = ctk.CTkButton(
    app,
    text= "Probar botón",
    command=lambda: print("La aplicación está funcionando")
)
boton.pack(pady=20)

# Ejecutar ventana
app.mainloop()