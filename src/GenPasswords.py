import secrets
import string
import pyperclip
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk  # Asegúrate de tener Pillow instalado: pip install pillow
import os
import platform
import subprocess

APP_NAME = "PasswGen"
APP_VERSION = "1.0.0"

# Obtener la ruta absoluta del directorio del archivo actual
current_dir = os.path.dirname(os.path.abspath(__file__))

# Función para generar la contraseña
def generarContraseña():
    try:
        longitud = int(spinLongitud.get())  # Obtener la longitud de la contraseña
        if longitud < 4:
            messagebox.showwarning('Advertencia', 'La longitud debe ser mayor o igual a 4.')
            return
        caracteres = string.ascii_letters + string.digits + string.punctuation
        contraseña = ''.join(secrets.choice(caracteres) for _ in range(longitud))
        
        entResultado.config(state='normal')
        entResultado.delete(0, tk.END)
        entResultado.insert(0, contraseña)

        pyperclip.copy(contraseña)
        messagebox.showinfo('Contraseña generada', 'Contraseña copiada al portapapeles automáticamente.')

    except ValueError:
        messagebox.showerror('Error', 'Introduce un número válido.')

# Función para copiar la contraseña manualmente
def copiarContraseña():
    contraseña = entResultado.get()
    if contraseña:
        pyperclip.copy(contraseña)
        messagebox.showinfo('Contraseña copiada', 'Contraseña copiada al portapapeles.')
    else:
        messagebox.showwarning('Advertencia', 'No hay contraseña generada para copiar.')

def salir():
    pregunta = messagebox.askyesno('Salir', '¿Estás seguro de que quieres salir?')
    if pregunta:
        ventana.quit()

# Función para detectar si el sistema está en modo oscuro
def sistemaModoOscuro():
    sistema = platform.system()
    print(f"Detectando modo oscuro en {sistema}...")
    if sistema == "Windows":
        try:
            import winreg

            registry = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
            key = winreg.OpenKey(registry, r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize")
            value, _ = winreg.QueryValueEx(key, "AppsUseLightTheme")
            dark_mode = value == 0
            print(f"Modo oscuro en Windows: {dark_mode}")
            return dark_mode
        except Exception as e:
            print(f"No se pudo detectar el modo oscuro en Windows: {e}")
            return False
    elif sistema == "Darwin":  # macOS
        try:
            result = subprocess.run(
                ["defaults", "read", "-g", "AppleInterfaceStyle"],
                capture_output=True, text=True
            )
            dark_mode = "Dark" in result.stdout
            print(f"Modo oscuro en macOS: {dark_mode}")
            return dark_mode
        except Exception as e:
            print(f"No se pudo detectar el modo oscuro en macOS: {e}")
            return False
    elif sistema == "Linux":
        try:
            result = subprocess.run(
                ["gsettings", "get", "org.gnome.desktop.interface", "gtk-theme"],
                capture_output=True, text=True
            )
            dark_mode = "dark" in result.stdout.lower()
            print(f"Modo oscuro en Linux: {dark_mode}")
            return dark_mode
        except Exception as e:
            print(f"No se pudo detectar el modo oscuro en Linux: {e}")
            return False
    print("Sistema operativo no soportado para detección de modo oscuro.")
    return False

# Función para alternar entre modo oscuro y claro
def alternarModo():
    global darkMode
    darkMode = not darkMode
    aplicarEstilo()

# Aplicar estilos según el modo
def aplicarEstilo():
    bg_color = "#2E2E2E" if darkMode else "#FFFFFF"  
    fg_color = "#FFFFFF" if darkMode else "#000000"  
    entry_bg = "#555555" if darkMode else "#F0F0F0"
    entry_fg = "#FFFFFF" if darkMode else "#000000"
    btn_bg = "#444444" if darkMode else "#D9D9D9"  
    btn_fg = "#FFFFFF" if darkMode else "#000000"  
    btn_hover_bg = "#555555" if darkMode else "#C0C0C0"  # Color de fondo al pasar el mouse
    border_color = "#FFDD57" if darkMode else "#007ACC"  

    ventana.configure(bg=bg_color)
    framePrincipal.configure(style="Custom.TFrame")
    frameIzquierda.configure(style="Custom.TFrame")
    frameBotones.configure(style="Custom.TFrame")

    style.configure("Custom.TFrame", background=bg_color)
    style.configure("TLabel", font=("Arial", 14, "bold italic"), background=bg_color, foreground=fg_color)
    style.configure("TButton", font=("Arial", 15, "bold"), padding=5)
    style.configure("TEntry", font=("Arial", 13), padding=5, fieldbackground=entry_bg, foreground=entry_fg, 
                    bordercolor=border_color, relief="solid")
    

    # Aplicar colores a las entradas y spinbox
    entResultado.config(bg=entry_bg, fg=entry_fg, insertbackground=fg_color)
    spinLongitud.config(bg=entry_bg, fg=entry_fg, insertbackground=fg_color)
    
    # Aplicar colores a los botones
    btnGenerar.config(bg=btn_bg, fg=btn_fg, width=20, height=2, font=("Arial", 13, "bold"))
    btnCopiar.config(bg=btn_bg, fg=btn_fg, width=20, height=2, font=("Arial", 13, "bold"))
    btnSalir.config(bg=btn_bg, fg=btn_fg, width=20, height=2, font=("Arial", 13, "bold"))
    
    # Aplicar color al botón de alternar visibilidad
    btnMostrar.config(bg=btn_bg, activebackground=btn_bg, relief="flat", width=30, height=30)

    # Aplicar color al botón de alternar modo
    btnModo.config(fg=fg_color, bg=bg_color, activebackground=bg_color, relief="flat")

        # Añadir eventos para cambiar el color de fondo al pasar el mouse
    for btn in [btnGenerar, btnCopiar, btnSalir, btnMostrar]:
        btn.bind("<Enter>", lambda e, b=btn: b.config(bg=btn_hover_bg))
        btn.bind("<Leave>", lambda e, b=btn: b.config(bg=btn_bg))

    # Cambiar el color del botón de alternar modo
    btnModo.bind("<Enter>", lambda e: btnModo.config(bg=btn_hover_bg))
    btnModo.bind("<Leave>", lambda e: btnModo.config(bg=bg_color))

# Función para centrar la ventana en la pantalla
def centrarVentana(ventana):
    ventana.update_idletasks()
    ancho = ventana.winfo_width()
    alto = ventana.winfo_height()
    x = (ventana.winfo_screenwidth() // 2) - (ancho // 2)
    y = (ventana.winfo_screenheight() // 2) - (alto // 2)
    ventana.geometry(f'{ancho}x{alto}+{x}+{y}')

# Detectar el modo del sistema
darkMode = sistemaModoOscuro()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title(f"Generador de Contraseñas Seguras - {APP_NAME} v{APP_VERSION}")
ventana.geometry("")
ventana.resizable(False, False)

# Aplicar estilos con ttk
style = ttk.Style()

# Crear el marco principal antes de aplicar estilos
framePrincipal = ttk.Frame(ventana, padding=15)
framePrincipal.pack(fill="both", expand=True)

# Frame para los elementos de la izquierda
frameIzquierda = ttk.Frame(framePrincipal)
frameIzquierda.grid(row=0, column=0, padx=5, pady=5)

# Etiqueta y campo para la longitud de la contraseña
ttk.Label(frameIzquierda, text="Longitud de la contraseña:").grid(row=0, column=0, sticky="w", padx=5, pady=5)

# `Spinbox` para seleccionar la longitud de la contraseña
spinLongitud = tk.Spinbox(frameIzquierda, from_=4, to=50, width=5, font=("Arial", 13), justify="center")
spinLongitud.grid(row=0, column=1, padx=5, pady=5)

# Establecer el valor inicial correctamente
spinLongitud.delete(0, tk.END)
spinLongitud.insert(0, "12")

# Cargar imágenes para los iconos
try:
    ojo_abierto_img = Image.open(os.path.join(current_dir, "ver.png"))
    ojo_cerrado_img = Image.open(os.path.join(current_dir, "ojo.png"))

    # Redimensionar las imágenes para que se adapten al botón
    ojo_abierto_img = ojo_abierto_img.resize((20, 20), Image.LANCZOS)
    ojo_cerrado_img = ojo_cerrado_img.resize((20, 20), Image.LANCZOS)

    # Convertir las imágenes a un formato que Tkinter pueda usar
    ojo_abierto = ImageTk.PhotoImage(ojo_abierto_img)
    ojo_cerrado = ImageTk.PhotoImage(ojo_cerrado_img)
except FileNotFoundError as e:
    messagebox.showerror("Error", f"No se encontraron las imágenes: {e}")
    ventana.destroy()
    exit()

# Etiqueta para la contraseña generada
ttk.Label(frameIzquierda, text="Contraseña generada:").grid(row=1, column=0, sticky="w", padx=5, pady=5)

# Variable para controlar la visibilidad de la contraseña
mostrar_contraseña = tk.BooleanVar(value=False)

# Función para alternar la visibilidad de la contraseña
def alternarVisibilidad():
    if mostrar_contraseña.get():
        entResultado.config(show="")
        btnMostrar.config(image=ojo_cerrado)
    else:
        entResultado.config(show="*")
        btnMostrar.config(image=ojo_abierto)

# Campo de texto donde aparece la contraseña
entResultado = tk.Entry(frameIzquierda, justify="center", font=("Arial", 20), width=20, show="*")
entResultado.grid(row=2, column=0, padx=(5, 0), pady=5, sticky="ew")

# Botón para alternar la visibilidad de la contraseña
btnMostrar = tk.Checkbutton(frameIzquierda, image=ojo_abierto, command=alternarVisibilidad, relief="flat", bd=0, variable=mostrar_contraseña, indicatoron=False)
btnMostrar.grid(row=2, column=1, padx=(0, 5), pady=5, sticky="w")

# Deshabilitar la interacción del mouse
entResultado.bind("<FocusIn>", lambda event: entResultado.tk_focusNext().focus_set())
entResultado.bind("<Button-1>", lambda event: "break")

# Botones alineados a la derecha
frameBotones = ttk.Frame(framePrincipal)
frameBotones.grid(row=0, column=3, padx=5, pady=5)

btnGenerar = tk.Button(frameBotones, text="Generar", command=generarContraseña)
btnGenerar.grid(row=0, column=0, padx=5, pady=5)

btnCopiar = tk.Button(frameBotones, text="Copiar", command=copiarContraseña)
btnCopiar.grid(row=1, column=0, padx=5, pady=5)

# Botón de alternar modo en la esquina superior izquierda
btnModo = tk.Button(ventana, text="⚫", command=alternarModo, font=("Arial", 12, "bold"), relief="flat", width=2, height=1, bd=0)
btnModo.place(x=5, y=5)  # Se coloca en la esquina superior izquierda

btnSalir = tk.Button(frameBotones, text="Salir", command=salir)
btnSalir.grid(row=3, column=0, padx=5, pady=5)

# Aplicar estilos ahora que los elementos ya existen
aplicarEstilo()

# Centrar la ventana después de ajustar elementos
centrarVentana(ventana)

# Añadir el logo al programa
logo_path = os.path.join(current_dir, "Logo.ico")
ventana.iconbitmap(logo_path)

# Ejecutar la interfaz gráfica
ventana.mainloop()
