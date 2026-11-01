import os
import platform
import secrets
import string
import subprocess
import sys
import tkinter as tk
from tkinter import ttk, messagebox

import pyperclip
from PIL import Image, ImageTk


APP_NAME = "KeyMint"
APP_VERSION = "1.1.0-dev"


# ============================================================
# Rutas
# ============================================================

def get_project_root():
    """
    Devuelve la raíz del proyecto tanto al ejecutar desde código fuente
    como al ejecutar una compilación de PyInstaller.
    """
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        return sys._MEIPASS

    return os.path.dirname(os.path.abspath(__file__))


PROJECT_ROOT = get_project_root()
BRANDING_DIR = os.path.join(PROJECT_ROOT, "assets", "branding")
ICONS_DIR = os.path.join(PROJECT_ROOT, "assets", "icons")


def resource_path(*parts):
    return os.path.join(PROJECT_ROOT, *parts)


# ============================================================
# Paleta oficial KeyMint
# ============================================================

KEYMINT_MINT = "#35D6AE"
KEYMINT_DEEP_MINT = "#1FA184"
KEYMINT_GLOW = "#7EF0D1"

KEYMINT_NAVY = "#0F1720"
KEYMINT_SURFACE = "#18232D"

KEYMINT_LIGHT = "#F3FFFB"
KEYMINT_LIGHT_SURFACE = "#E4FAF3"
KEYMINT_DARK_TEXT = "#14312A"

WHITE = "#FFFFFF"
MUTED_DARK = "#A9C9C0"
MUTED_LIGHT = "#52756C"


# ============================================================
# Lógica
# ============================================================

def generar_contrasena():
    try:
        longitud = int(spin_longitud.get())

        if longitud < 4:
            messagebox.showwarning(
                "Longitud inválida",
                "La longitud debe ser mayor o igual a 4."
            )
            return

        caracteres = string.ascii_letters + string.digits + string.punctuation
        contrasena = "".join(secrets.choice(caracteres) for _ in range(longitud))

        ent_resultado.config(state="normal")
        ent_resultado.delete(0, tk.END)
        ent_resultado.insert(0, contrasena)

        pyperclip.copy(contrasena)
        messagebox.showinfo(
            "Contraseña generada",
            "La contraseña se copió automáticamente al portapapeles."
        )

    except ValueError:
        messagebox.showerror(
            "Valor inválido",
            "Introduce un número válido para la longitud."
        )


def copiar_contrasena():
    contrasena = ent_resultado.get()

    if contrasena:
        pyperclip.copy(contrasena)
        messagebox.showinfo(
            "Contraseña copiada",
            "La contraseña se copió al portapapeles."
        )
    else:
        messagebox.showwarning(
            "Sin contraseña",
            "Primero genera una contraseña."
        )


def salir():
    if messagebox.askyesno("Salir de KeyMint", "¿Quieres cerrar KeyMint?"):
        ventana.destroy()


# ============================================================
# Tema del sistema
# ============================================================

def sistema_modo_oscuro():
    sistema = platform.system()
    print(f"Detectando modo oscuro en {sistema}...")

    if sistema == "Windows":
        try:
            import winreg

            registry = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
            key = winreg.OpenKey(
                registry,
                r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize"
            )
            value, _ = winreg.QueryValueEx(key, "AppsUseLightTheme")

            dark_mode = value == 0
            print(f"Modo oscuro en Windows: {dark_mode}")
            return dark_mode

        except Exception as exc:
            print(f"No se pudo detectar el modo oscuro en Windows: {exc}")
            return False

    if sistema == "Darwin":
        try:
            result = subprocess.run(
                ["defaults", "read", "-g", "AppleInterfaceStyle"],
                capture_output=True,
                text=True,
                check=False,
            )
            dark_mode = "Dark" in result.stdout
            print(f"Modo oscuro en macOS: {dark_mode}")
            return dark_mode

        except Exception as exc:
            print(f"No se pudo detectar el modo oscuro en macOS: {exc}")
            return False

    if sistema == "Linux":
        try:
            result = subprocess.run(
                ["gsettings", "get", "org.gnome.desktop.interface", "gtk-theme"],
                capture_output=True,
                text=True,
                check=False,
            )
            dark_mode = "dark" in result.stdout.lower()
            print(f"Modo oscuro en Linux: {dark_mode}")
            return dark_mode

        except Exception as exc:
            print(f"No se pudo detectar el modo oscuro en Linux: {exc}")
            return False

    print("Sistema operativo no soportado para detección automática de tema.")
    return False


def alternar_modo():
    global dark_mode
    dark_mode = not dark_mode
    aplicar_estilo()


# ============================================================
# Interfaz
# ============================================================

def aplicar_estilo():
    if dark_mode:
        bg = KEYMINT_NAVY
        surface = KEYMINT_SURFACE
        text = KEYMINT_LIGHT
        muted = MUTED_DARK
        entry_bg = "#101C24"
        entry_fg = KEYMINT_LIGHT
        border = KEYMINT_DEEP_MINT
        button_bg = KEYMINT_MINT
        button_fg = KEYMINT_NAVY
        button_hover = KEYMINT_GLOW
        secondary_bg = "#22333D"
        secondary_hover = "#2C414C"
    else:
        bg = KEYMINT_LIGHT
        surface = KEYMINT_LIGHT_SURFACE
        text = KEYMINT_DARK_TEXT
        muted = MUTED_LIGHT
        entry_bg = WHITE
        entry_fg = KEYMINT_DARK_TEXT
        border = KEYMINT_DEEP_MINT
        button_bg = KEYMINT_DEEP_MINT
        button_fg = WHITE
        button_hover = KEYMINT_MINT
        secondary_bg = "#D4F3EA"
        secondary_hover = "#C0EADF"

    ventana.configure(bg=bg)

    style.configure("Root.TFrame", background=bg)
    style.configure("Surface.TFrame", background=surface)

    style.configure(
        "Title.TLabel",
        font=("Segoe UI", 22, "bold"),
        background=surface,
        foreground=text,
    )

    style.configure(
        "Subtitle.TLabel",
        font=("Segoe UI", 10),
        background=surface,
        foreground=muted,
    )

    style.configure(
        "Field.TLabel",
        font=("Segoe UI", 11, "bold"),
        background=surface,
        foreground=text,
    )

    style.configure(
        "Version.TLabel",
        font=("Segoe UI", 9),
        background=surface,
        foreground=muted,
    )

    frame_principal.configure(style="Root.TFrame")
    panel.configure(style="Surface.TFrame")
    header.configure(style="Surface.TFrame")
    frame_campos.configure(style="Surface.TFrame")
    frame_botones.configure(style="Surface.TFrame")

    spin_longitud.config(
        bg=entry_bg,
        fg=entry_fg,
        insertbackground=entry_fg,
        buttonbackground=surface,
        relief="flat",
        highlightthickness=1,
        highlightbackground=border,
        highlightcolor=KEYMINT_MINT,
    )

    ent_resultado.config(
        bg=entry_bg,
        fg=entry_fg,
        insertbackground=entry_fg,
        relief="flat",
        highlightthickness=1,
        highlightbackground=border,
        highlightcolor=KEYMINT_MINT,
        disabledbackground=entry_bg,
        disabledforeground=entry_fg,
    )

    btn_generar.config(
        bg=button_bg,
        fg=button_fg,
        activebackground=button_hover,
        activeforeground=KEYMINT_NAVY if dark_mode else KEYMINT_DARK_TEXT,
    )

    for btn in (btn_copiar, btn_salir):
        btn.config(
            bg=secondary_bg,
            fg=text,
            activebackground=secondary_hover,
            activeforeground=text,
        )

    btn_mostrar.config(
        bg=entry_bg,
        activebackground=entry_bg,
        selectcolor=entry_bg,
    )

    btn_modo.config(
        bg=surface,
        fg=text,
        activebackground=secondary_hover,
        activeforeground=text,
        text="☀" if dark_mode else "☾",
    )

    btn_generar.bind(
        "<Enter>",
        lambda event: btn_generar.config(bg=button_hover)
    )
    btn_generar.bind(
        "<Leave>",
        lambda event: btn_generar.config(bg=button_bg)
    )

    for btn in (btn_copiar, btn_salir):
        btn.bind(
            "<Enter>",
            lambda event, b=btn: b.config(bg=secondary_hover)
        )
        btn.bind(
            "<Leave>",
            lambda event, b=btn: b.config(bg=secondary_bg)
        )

    btn_modo.bind(
        "<Enter>",
        lambda event: btn_modo.config(bg=secondary_hover)
    )
    btn_modo.bind(
        "<Leave>",
        lambda event: btn_modo.config(bg=surface)
    )


def centrar_ventana():
    ventana.update_idletasks()

    ancho = ventana.winfo_width()
    alto = ventana.winfo_height()

    x = (ventana.winfo_screenwidth() // 2) - (ancho // 2)
    y = (ventana.winfo_screenheight() // 2) - (alto // 2)

    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")


def alternar_visibilidad():
    if mostrar_contrasena.get():
        ent_resultado.config(show="")
        btn_mostrar.config(image=ojo_cerrado)
    else:
        ent_resultado.config(show="*")
        btn_mostrar.config(image=ojo_abierto)


# ============================================================
# Inicio
# ============================================================

dark_mode = sistema_modo_oscuro()

ventana = tk.Tk()
ventana.title(f"{APP_NAME} — Generador Seguro de Contraseñas — v{APP_VERSION}")
ventana.resizable(False, False)
ventana.protocol("WM_DELETE_WINDOW", salir)

# Icono oficial de KeyMint
try:
    icono_ico = resource_path("assets", "branding", "KeyMintIcon.ico")
    if os.path.exists(icono_ico):
        ventana.iconbitmap(icono_ico)
except Exception as exc:
    print(f"No se pudo cargar el icono de KeyMint: {exc}")

style = ttk.Style()

# Mejor comportamiento visual entre plataformas
try:
    style.theme_use("clam")
except tk.TclError:
    pass

frame_principal = ttk.Frame(ventana, padding=18, style="Root.TFrame")
frame_principal.pack(fill="both", expand=True)

panel = ttk.Frame(frame_principal, padding=18, style="Surface.TFrame")
panel.pack(fill="both", expand=True)

# ============================================================
# Encabezado
# ============================================================

header = ttk.Frame(panel, style="Surface.TFrame")
header.grid(row=0, column=0, columnspan=2, sticky="ew", pady=(0, 18))

header.columnconfigure(1, weight=1)

try:
    logo_img = Image.open(
        resource_path("assets", "branding", "KeyMintIcon.png")
    ).convert("RGBA")
    logo_img.thumbnail((72, 72), Image.Resampling.LANCZOS)
    logo_keymint = ImageTk.PhotoImage(logo_img)

    lbl_logo = tk.Label(
        header,
        image=logo_keymint,
        borderwidth=0,
        highlightthickness=0,
    )
    lbl_logo.grid(row=0, column=0, rowspan=2, padx=(0, 12))
except Exception as exc:
    print(f"No se pudo cargar el logo de KeyMint: {exc}")
    lbl_logo = ttk.Label(
        header,
        text="K",
        style="Title.TLabel"
    )
    lbl_logo.grid(row=0, column=0, rowspan=2, padx=(0, 12))

lbl_titulo = ttk.Label(
    header,
    text=APP_NAME,
    style="Title.TLabel",
)
lbl_titulo.grid(row=0, column=1, sticky="sw")

lbl_subtitulo = ttk.Label(
    header,
    text="Generador seguro de contraseñas",
    style="Subtitle.TLabel",
)
lbl_subtitulo.grid(row=1, column=1, sticky="nw")

btn_modo = tk.Button(
    header,
    text="☾",
    command=alternar_modo,
    font=("Segoe UI Symbol", 13, "bold"),
    relief="flat",
    borderwidth=0,
    width=3,
    height=1,
    cursor="hand2",
)
btn_modo.grid(row=0, column=2, rowspan=2, padx=(12, 0))

# ============================================================
# Campos
# ============================================================

frame_campos = ttk.Frame(panel, style="Surface.TFrame")
frame_campos.grid(row=1, column=0, sticky="nsew", padx=(0, 18))

ttk.Label(
    frame_campos,
    text="Longitud de la contraseña",
    style="Field.TLabel",
).grid(row=0, column=0, sticky="w", pady=(0, 7))

spin_longitud = tk.Spinbox(
    frame_campos,
    from_=4,
    to=128,
    width=7,
    font=("Segoe UI", 12),
    justify="center",
)
spin_longitud.grid(row=1, column=0, sticky="w", pady=(0, 18))
spin_longitud.delete(0, tk.END)
spin_longitud.insert(0, "16")

ttk.Label(
    frame_campos,
    text="Contraseña generada",
    style="Field.TLabel",
).grid(row=2, column=0, sticky="w", pady=(0, 7))

frame_resultado = tk.Frame(frame_campos, borderwidth=0, highlightthickness=0)
frame_resultado.grid(row=3, column=0, sticky="ew")
frame_resultado.columnconfigure(0, weight=1)

ent_resultado = tk.Entry(
    frame_resultado,
    justify="center",
    font=("Consolas", 16),
    width=28,
    show="*",
)
ent_resultado.grid(row=0, column=0, sticky="ew")

# Cargar iconos de visibilidad existentes
try:
    ojo_abierto_img = Image.open(
        resource_path("assets", "icons", "eye-open.png")
    ).resize((20, 20), Image.Resampling.LANCZOS)

    ojo_cerrado_img = Image.open(
        resource_path("assets", "icons", "eye-closed.png")
    ).resize((20, 20), Image.Resampling.LANCZOS)

    ojo_abierto = ImageTk.PhotoImage(ojo_abierto_img)
    ojo_cerrado = ImageTk.PhotoImage(ojo_cerrado_img)

except FileNotFoundError as exc:
    messagebox.showerror(
        "Recursos faltantes",
        f"No se pudieron cargar los iconos de visibilidad:\n{exc}"
    )
    ventana.destroy()
    raise SystemExit(1)

mostrar_contrasena = tk.BooleanVar(value=False)

btn_mostrar = tk.Checkbutton(
    frame_resultado,
    image=ojo_abierto,
    command=alternar_visibilidad,
    relief="flat",
    borderwidth=0,
    variable=mostrar_contrasena,
    indicatoron=False,
    cursor="hand2",
)
btn_mostrar.grid(row=0, column=1, padx=(7, 0))

# Evitar edición accidental del resultado
ent_resultado.bind(
    "<Key>",
    lambda event: "break"
)

# ============================================================
# Botones
# ============================================================

frame_botones = ttk.Frame(panel, style="Surface.TFrame")
frame_botones.grid(row=1, column=1, sticky="ns")

boton_config = {
    "width": 18,
    "height": 2,
    "font": ("Segoe UI", 11, "bold"),
    "relief": "flat",
    "borderwidth": 0,
    "cursor": "hand2",
}

btn_generar = tk.Button(
    frame_botones,
    text="Generar",
    command=generar_contrasena,
    **boton_config,
)
btn_generar.grid(row=0, column=0, pady=(0, 8))

btn_copiar = tk.Button(
    frame_botones,
    text="Copiar",
    command=copiar_contrasena,
    **boton_config,
)
btn_copiar.grid(row=1, column=0, pady=8)

btn_salir = tk.Button(
    frame_botones,
    text="Salir",
    command=salir,
    **boton_config,
)
btn_salir.grid(row=2, column=0, pady=(8, 0))

# ============================================================
# Pie
# ============================================================

ttk.Label(
    panel,
    text=f"{APP_NAME} v{APP_VERSION} · Las contraseñas se generan localmente",
    style="Version.TLabel",
).grid(
    row=2,
    column=0,
    columnspan=2,
    sticky="w",
    pady=(18, 0),
)

aplicar_estilo()

# Ajustar el fondo del logo al tema inicial
if "lbl_logo" in globals():
    try:
        lbl_logo.configure(
            bg=KEYMINT_SURFACE if dark_mode else KEYMINT_LIGHT_SURFACE
        )
    except tk.TclError:
        pass

centrar_ventana()
ventana.mainloop()
