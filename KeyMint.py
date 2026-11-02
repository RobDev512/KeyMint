import ctypes
import os
import secrets
import string
import sys
import tkinter as tk

import customtkinter as ctk
import pyperclip
from PIL import Image, ImageDraw, ImageTk


APP_NAME = "KeyMint"
APP_VERSION = "1.1.0"

WINDOW_WIDTH = 455
WINDOW_HEIGHT = 440
COMPACT_BREAKPOINT = 380
WINDOW_RADIUS = 20

GWL_STYLE = -16
WS_SYSMENU = 0x00080000
WS_THICKFRAME = 0x00040000
WS_MINIMIZEBOX = 0x00020000
WS_MAXIMIZEBOX = 0x00010000

SWP_NOSIZE = 0x0001
SWP_NOMOVE = 0x0002
SWP_NOZORDER = 0x0004
SWP_NOACTIVATE = 0x0010
SWP_FRAMECHANGED = 0x0020

DWMWA_WINDOW_CORNER_PREFERENCE = 33
DWMWA_BORDER_COLOR = 34
DWMWCP_ROUND = 2


# ============================================================
# Rutas
# ============================================================

def get_project_root():
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        return sys._MEIPASS

    return os.path.dirname(os.path.abspath(__file__))


PROJECT_ROOT = get_project_root()


def resource_path(*parts):
    return os.path.join(PROJECT_ROOT, *parts)


# ============================================================
# Identidad visual
# ============================================================

MINT = "#35D6AE"
DEEP_MINT = "#1FA184"
GLOW = "#7EF0D1"

DARK_BG = "#071512"
DARK_SURFACE = "#0C211C"
DARK_SURFACE_2 = "#103028"
DARK_ENTRY = "#081A16"
DARK_TEXT = "#F3FFFB"
DARK_MUTED = "#9BC8BC"
DARK_LINE = "#1B5142"

LIGHT_BG = "#F2FBF8"
LIGHT_SURFACE = "#FFFFFF"
LIGHT_SURFACE_2 = "#E8F6F2"
LIGHT_ENTRY = "#FBFEFD"
LIGHT_TEXT = "#102C25"
LIGHT_MUTED = "#55756D"
LIGHT_LINE = "#B8DDD2"

BG = (LIGHT_BG, DARK_BG)
SURFACE = (LIGHT_SURFACE, DARK_SURFACE)
SURFACE_2 = (LIGHT_SURFACE_2, DARK_SURFACE_2)
ENTRY_BG = (LIGHT_ENTRY, DARK_ENTRY)
TEXT = (LIGHT_TEXT, DARK_TEXT)
MUTED = (LIGHT_MUTED, DARK_MUTED)
LINE = (LIGHT_LINE, DARK_LINE)

PRIMARY = (DEEP_MINT, MINT)
PRIMARY_HOVER = (MINT, GLOW)
PRIMARY_TEXT = ("#FFFFFF", DARK_BG)

FONT_UI = "Segoe UI"
FONT_MONO = "Cascadia Mono"


ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


# ============================================================
# Win32
# ============================================================

class RECT(ctypes.Structure):
    _fields_ = [
        ("left", ctypes.c_long),
        ("top", ctypes.c_long),
        ("right", ctypes.c_long),
        ("bottom", ctypes.c_long),
    ]


# ============================================================
# Aplicación
# ============================================================

class KeyMintApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self._drag_x = 0
        self._drag_y = 0
        self._restoring_from_minimize = False
        self._status_job = None
        self.password_visible = False

        self._configure_layout_mode()

        self.title(f"{APP_NAME} v{APP_VERSION}")
        self.geometry(
            f"{self.window_width}x{self.window_height}"
        )
        self.resizable(False, False)
        self.overrideredirect(True)
        self.configure(fg_color=BG)
        self.protocol("WM_DELETE_WINDOW", self.close_app)

        self._set_app_icon()
        self._load_interface_icons()

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self._build_titlebar()
        self._build_content()
        self._bind_shortcuts()

        self.bind("<Map>", self._on_map)

        # Windows y CustomTkinter terminan de resolver DPI después
        # de crear físicamente la ventana.
        self.after(40, self._finalize_window)
        self.after(180, self._finalize_window)

    def _configure_layout_mode(self):
        """Conserva una ventana fija, pero adapta la composición a poco ancho."""
        self.update_idletasks()

        available_width = max(
            340,
            self.winfo_screenwidth() - 40,
        )

        self.window_width = min(
            WINDOW_WIDTH,
            available_width,
        )

        self.compact_mode = (
            self.window_width < COMPACT_BREAKPOINT
        )

        self.window_height = (
            520
            if self.compact_mode
            else WINDOW_HEIGHT
        )

    # --------------------------------------------------------
    # Ventana
    # --------------------------------------------------------

    def _set_app_icon(self):
        try:
            path = resource_path(
                "assets",
                "branding",
                "KeyMintIcon.ico",
            )

            if os.path.exists(path):
                self.iconbitmap(path)
        except Exception:
            pass

    def _get_hwnd(self):
        if sys.platform != "win32":
            return None

        self.update_idletasks()

        hwnd = self.winfo_id()

        try:
            parent = ctypes.windll.user32.GetParent(hwnd)

            if parent:
                hwnd = parent
        except Exception:
            pass

        return hwnd

    def _get_real_window_size(self):
        if sys.platform == "win32":
            try:
                hwnd = self._get_hwnd()
                rect = RECT()

                if hwnd and ctypes.windll.user32.GetWindowRect(
                    hwnd,
                    ctypes.byref(rect),
                ):
                    return (
                        rect.right - rect.left,
                        rect.bottom - rect.top,
                    )
            except Exception:
                pass

        self.update_idletasks()
        return (
            self.winfo_width(),
            self.winfo_height(),
        )

    def _center_window(self):
        if sys.platform == "win32":
            try:
                hwnd = self._get_hwnd()

                if hwnd:
                    user32 = ctypes.windll.user32

                    rect = RECT()
                    user32.GetWindowRect(
                        hwnd,
                        ctypes.byref(rect),
                    )

                    width = rect.right - rect.left
                    height = rect.bottom - rect.top

                    work_area = RECT()

                    # SPI_GETWORKAREA = 0x0030
                    user32.SystemParametersInfoW(
                        0x0030,
                        0,
                        ctypes.byref(work_area),
                        0,
                    )

                    x = (
                        work_area.left
                        + (
                            work_area.right
                            - work_area.left
                            - width
                        ) // 2
                    )

                    y = (
                        work_area.top
                        + (
                            work_area.bottom
                            - work_area.top
                            - height
                        ) // 2
                    )

                    SWP_NOSIZE = 0x0001
                    SWP_NOZORDER = 0x0004
                    SWP_NOACTIVATE = 0x0010

                    user32.SetWindowPos(
                        hwnd,
                        0,
                        x,
                        y,
                        0,
                        0,
                        SWP_NOSIZE
                        | SWP_NOZORDER
                        | SWP_NOACTIVATE,
                    )

                    return

            except Exception:
                pass

        self.update_idletasks()

        width = self.winfo_width()
        height = self.winfo_height()

        x = (
            self.winfo_screenwidth()
            - width
        ) // 2

        y = (
            self.winfo_screenheight()
            - height
        ) // 2

        # Solo posición: CustomTkinter no escala x/y en este formato.
        self.geometry(f"+{x}+{y}")

    def _apply_windows_taskbar_style(self):
        if sys.platform != "win32":
            return

        try:
            hwnd = self._get_hwnd()

            if not hwnd:
                return

            user32 = ctypes.windll.user32

            GWL_EXSTYLE = -20
            WS_EX_TOOLWINDOW = 0x00000080
            WS_EX_APPWINDOW = 0x00040000

            style = user32.GetWindowLongW(
                hwnd,
                GWL_EXSTYLE,
            )

            style = (
                (style & ~WS_EX_TOOLWINDOW)
                | WS_EX_APPWINDOW
            )

            user32.SetWindowLongW(
                hwnd,
                GWL_EXSTYLE,
                style,
            )
        except Exception:
            pass

    def _apply_fixed_window_style(self):
        """Mantiene capacidades Win32 básicas sin permitir resize/maximizar."""
        if sys.platform != "win32":
            return

        try:
            hwnd = self._get_hwnd()

            if not hwnd:
                return

            user32 = ctypes.windll.user32

            style = user32.GetWindowLongW(
                hwnd,
                GWL_STYLE,
            )

            style |= (
                WS_SYSMENU
                | WS_MINIMIZEBOX
            )

            style &= ~(
                WS_THICKFRAME
                | WS_MAXIMIZEBOX
            )

            if user32.GetWindowLongW(
                hwnd,
                GWL_STYLE,
            ) != style:
                user32.SetWindowLongW(
                    hwnd,
                    GWL_STYLE,
                    style,
                )

                user32.SetWindowPos(
                    hwnd,
                    0,
                    0,
                    0,
                    0,
                    0,
                    SWP_NOMOVE
                    | SWP_NOSIZE
                    | SWP_NOZORDER
                    | SWP_NOACTIVATE
                    | SWP_FRAMECHANGED,
                )
        except Exception:
            pass

    @staticmethod
    def _hex_to_colorref(hex_color):
        """Convierte #RRGGBB al COLORREF esperado por Windows."""
        value = hex_color.lstrip("#")

        red = int(value[0:2], 16)
        green = int(value[2:4], 16)
        blue = int(value[4:6], 16)

        return (
            red
            | (green << 8)
            | (blue << 16)
        )

    def _apply_dwm_frame(self):
        """Pide a Windows 11 esquinas y borde nativos."""
        if sys.platform != "win32":
            return

        try:
            hwnd = self._get_hwnd()

            if not hwnd:
                return

            dwmapi = ctypes.windll.dwmapi

            corner_preference = ctypes.c_int(
                DWMWCP_ROUND
            )

            dwmapi.DwmSetWindowAttribute(
                hwnd,
                DWMWA_WINDOW_CORNER_PREFERENCE,
                ctypes.byref(corner_preference),
                ctypes.sizeof(corner_preference),
            )

            border_color = ctypes.c_uint(
                self._hex_to_colorref(GLOW)
            )

            dwmapi.DwmSetWindowAttribute(
                hwnd,
                DWMWA_BORDER_COLOR,
                ctypes.byref(border_color),
                ctypes.sizeof(border_color),
            )
        except Exception:
            pass


    def _finalize_window(self):
        self.update_idletasks()
        self._apply_windows_taskbar_style()
        self._apply_fixed_window_style()
        self._center_window()
        self._apply_dwm_frame()

    def start_drag(self, event):
        self._drag_x = (
            event.x_root
            - self.winfo_x()
        )
        self._drag_y = (
            event.y_root
            - self.winfo_y()
        )

    def drag_window(self, event):
        x = event.x_root - self._drag_x
        y = event.y_root - self._drag_y

        self.geometry(f"+{x}+{y}")

    def minimize_window(self):
        self._restoring_from_minimize = True
        self.overrideredirect(False)
        self.iconify()

    def _on_map(self, _event=None):
        if not self._restoring_from_minimize:
            return

        if self.state() == "normal":
            self._restoring_from_minimize = False
            self.after(
                20,
                self._restore_borderless_window,
            )

    def _restore_borderless_window(self):
        self.overrideredirect(True)
        self._apply_windows_taskbar_style()
        self._apply_fixed_window_style()
        self._apply_dwm_frame()

    def close_app(self):
        self.destroy()

    # --------------------------------------------------------
    # Recursos
    # --------------------------------------------------------

    def _load_image(self, path, size):
        try:
            image = Image.open(path).convert("RGBA")

            return ctk.CTkImage(
                light_image=image,
                dark_image=image,
                size=size,
            )
        except Exception:
            return None

    def _load_theme_image(self, filename, size):
        """Carga la misma familia visual clara/oscura de TecNet Finder."""
        light_path = resource_path(
            "assets",
            "icons",
            "ui",
            "Claro",
            filename,
        )

        dark_path = resource_path(
            "assets",
            "icons",
            "ui",
            "Oscuro",
            filename,
        )

        try:
            light_image = Image.open(
                light_path
            ).convert("RGBA")

            dark_image = Image.open(
                dark_path
            ).convert("RGBA")

            return ctk.CTkImage(
                light_image=light_image,
                dark_image=dark_image,
                size=size,
            )
        except Exception:
            return None

    def _load_visibility_theme_image(
        self,
        light_filename,
        dark_filename,
        size,
    ):
        try:
            light_image = Image.open(
                resource_path(
                    "assets",
                    "icons",
                    "visibility",
                    light_filename,
                )
            ).convert("RGBA")

            dark_image = Image.open(
                resource_path(
                    "assets",
                    "icons",
                    "visibility",
                    dark_filename,
                )
            ).convert("RGBA")

            return ctk.CTkImage(
                light_image=light_image,
                dark_image=dark_image,
                size=size,
            )
        except Exception:
            return None

    def _load_interface_icons(self):
        self.close_icon = self._load_theme_image(
            "Cerrar.png",
            (17, 17),
        )

        self.minimize_icon = self._load_theme_image(
            "Minimizar.png",
            (17, 17),
        )

        self.copy_icon = self._load_theme_image(
            "Copiar.png",
            (16, 16),
        )

        self.theme_to_light_icon = self._load_image(
            resource_path(
                "assets",
                "icons",
                "theme",
                "IconoClaro.png",
            ),
            (18, 18),
        )

        self.theme_to_dark_icon = self._load_image(
            resource_path(
                "assets",
                "icons",
                "theme",
                "IconoOscuro.png",
            ),
            (18, 18),
        )

        self.eye_open_image = self._load_visibility_theme_image(
            "VerAbierto_Claro.png",
            "VerAbierto_Oscuro.png",
            (19, 19),
        )

        self.eye_closed_image = self._load_visibility_theme_image(
            "VerCerrado_Claro.png",
            "VerCerrado_Oscuro.png",
            (19, 19),
        )

    # --------------------------------------------------------
    # Barra superior
    # --------------------------------------------------------

    def _bind_drag(self, widget):
        widget.bind(
            "<Button-1>",
            self.start_drag,
        )
        widget.bind(
            "<B1-Motion>",
            self.drag_window,
        )

    def _build_titlebar(self):
        self.titlebar = ctk.CTkFrame(
            self,
            height=44,
            corner_radius=0,
            fg_color=SURFACE,
        )
        self.titlebar.grid(
            row=0,
            column=0,
            sticky="ew",
        )
        self.titlebar.grid_propagate(False)

        self._bind_drag(self.titlebar)

        self.title_left = ctk.CTkFrame(
            self.titlebar,
            fg_color="transparent",
            corner_radius=0,
        )
        self.title_left.pack(
            side="left",
            fill="y",
        )
        self._bind_drag(self.title_left)

        self.title_right = ctk.CTkFrame(
            self.titlebar,
            fg_color="transparent",
            corner_radius=0,
        )
        self.title_right.pack(
            side="right",
            fill="y",
        )

        self.title_icon = self._load_image(
            resource_path(
                "assets",
                "branding",
                "KeyMintIcon.png",
            ),
            (24, 24),
        )

        self.brand_icon_label = ctk.CTkLabel(
            self.title_left,
            text="",
            image=self.title_icon,
            width=26,
        )
        self.brand_icon_label.pack(
            side="left",
            padx=(14, 7),
            pady=8,
        )
        self._bind_drag(self.brand_icon_label)

        self.title_text = ctk.CTkLabel(
            self.title_left,
            text=f"{APP_NAME}  ·  v{APP_VERSION}",
            font=ctk.CTkFont(
                family=FONT_UI,
                size=12,
                weight="bold",
            ),
            text_color=TEXT,
        )
        self.title_text.pack(
            side="left",
        )
        self._bind_drag(self.title_text)

        # Rectangulares y a toda la altura. La esquina superior
        # derecha la recorta la propia ventana, no el botón.
        self.close_host = ctk.CTkFrame(
            self.title_right,
            width=48,
            height=44,
            corner_radius=0,
            fg_color="transparent",
        )
        self.close_host.pack(
            side="right",
            fill="y",
        )
        self.close_host.pack_propagate(False)

        self.close_button = ctk.CTkButton(
            self.close_host,
            text="" if self.close_icon else "×",
            image=self.close_icon,
            command=self.close_app,
            width=48,
            height=44,
            corner_radius=0,
            border_width=0,
            fg_color="transparent",
            hover_color="#C42B1C",
            text_color=TEXT,
            font=ctk.CTkFont(
                family=FONT_UI,
                size=19,
            ),
        )
        self.close_button.place(
            x=0,
            y=0,
            relwidth=1,
            relheight=1,
        )

        self.minimize_button = ctk.CTkButton(
            self.title_right,
            text="" if self.minimize_icon else "—",
            image=self.minimize_icon,
            command=self.minimize_window,
            width=44,
            height=44,
            corner_radius=0,
            fg_color="transparent",
            hover_color=SURFACE_2,
            text_color=TEXT,
            font=ctk.CTkFont(
                family=FONT_UI,
                size=16,
            ),
        )
        self.minimize_button.pack(
            side="right",
            fill="both",
        )

        self.theme_button = ctk.CTkButton(
            self.title_right,
            text=self._theme_button_text(),
            image=self._theme_button_icon(),
            command=self.toggle_theme,
            width=44,
            height=44,
            corner_radius=0,
            fg_color="transparent",
            hover_color=SURFACE_2,
            text_color=TEXT,
            font=ctk.CTkFont(
                family=FONT_UI,
                size=15,
            ),
        )
        self.theme_button.pack(
            side="right",
            fill="both",
        )

    # --------------------------------------------------------
    # Contenido
    # --------------------------------------------------------

    def _build_content(self):
        self.content = ctk.CTkFrame(
            self,
            corner_radius=0,
            fg_color=BG,
        )
        self.content.grid(
            row=1,
            column=0,
            sticky="nsew",
        )

        horizontal_padding = (
            8
            if self.compact_mode
            else 10
        )

        self.hero = ctk.CTkFrame(
            self.content,
            fg_color="transparent",
            corner_radius=0,
        )
        self.hero.pack(
            fill="x",
            padx=horizontal_padding,
            pady=(18, 12),
        )

        self.eyebrow_label = ctk.CTkLabel(
            self.hero,
            text="GENERADOR SEGURO  ·  LOCAL",
            font=ctk.CTkFont(
                family=FONT_UI,
                size=10,
                weight="bold",
            ),
            text_color=MINT,
            anchor="w",
        )
        self.eyebrow_label.pack(
            anchor="w",
        )

        self.hero_title = ctk.CTkLabel(
            self.hero,
            text="KeyMint",
            font=ctk.CTkFont(
                family=FONT_UI,
                size=27 if self.compact_mode else 29,
                weight="bold",
            ),
            text_color=TEXT,
            anchor="w",
        )
        self.hero_title.pack(
            anchor="w",
            pady=(2, 0),
        )

        self.hero_description = ctk.CTkLabel(
            self.hero,
            text=(
                "Contraseñas fuertes generadas localmente, "
                "sin enviar datos a servicios externos."
            ),
            font=ctk.CTkFont(
                family=FONT_UI,
                size=12,
            ),
            text_color=MUTED,
            anchor="w",
            justify="left",
            wraplength=max(
                200,
                self.window_width
                - horizontal_padding * 2,
            ),
        )
        self.hero_description.pack(
            anchor="w",
            pady=(1, 0),
        )

        # Panel dibujado como una única superficie redondeada.
        # Esto imita el principio de border + border-radius de Qt
        # sin depender de border_width de CustomTkinter.
        self.generator_card_canvas = tk.Canvas(
            self.content,
            highlightthickness=0,
            bd=0,
            relief="flat",
            bg=self._appearance_color(BG),
        )
        self.generator_card_canvas.pack(
            fill="x",
            padx=horizontal_padding,
            pady=(0, 12),
        )

        self.generator_card = ctk.CTkFrame(
            self.generator_card_canvas,
            fg_color=SURFACE,
            bg_color=SURFACE,
            corner_radius=0,
            border_width=0,
        )

        self.generator_card_window = (
            self.generator_card_canvas.create_window(
                4,
                4,
                anchor="nw",
                window=self.generator_card,
            )
        )

        self.generator_card_canvas.bind(
            "<Configure>",
            self._resize_generator_card,
        )

        self.generator_card.bind(
            "<Configure>",
            self._sync_generator_card_height,
        )

        self._build_length_controls()
        self._build_password_controls()
        self._build_generate_button()

        self.after(
            0,
            self._sync_generator_card_height,
        )

        self.footer = ctk.CTkFrame(
            self.content,
            fg_color="transparent",
            corner_radius=0,
        )
        self.footer.pack(
            fill="x",
            padx=horizontal_padding,
            pady=(0, 13),
        )

        self.status_label = ctk.CTkLabel(
            self.footer,
            text="Listo para generar",
            font=ctk.CTkFont(
                family=FONT_UI,
                size=10,
            ),
            text_color=MUTED,
        )

        self.privacy_label = ctk.CTkLabel(
            self.footer,
            text="100% local  ·  sin conexión requerida",
            font=ctk.CTkFont(
                family=FONT_UI,
                size=10,
            ),
            text_color=MUTED,
        )

        if self.compact_mode:
            self.status_label.pack(
                anchor="w",
            )
            self.privacy_label.pack(
                anchor="w",
                pady=(2, 0),
            )
        else:
            self.status_label.pack(
                side="left",
            )
            self.privacy_label.pack(
                side="right",
            )


    def _appearance_color(self, color):
        if isinstance(color, (tuple, list)):
            return (
                color[0]
                if ctk.get_appearance_mode() == "Light"
                else color[1]
            )

        return color

    def _resize_generator_card(self, event):
        inner_width = max(
            1,
            event.width - 8,
        )

        self.generator_card_canvas.itemconfigure(
            self.generator_card_window,
            width=inner_width,
        )

        self._draw_generator_card_surface(
            event.width,
            max(
                1,
                self.generator_card_canvas.winfo_height(),
            ),
        )

    def _sync_generator_card_height(self, _event=None):
        requested = self.generator_card.winfo_reqheight()

        if requested <= 1:
            return

        canvas_height = requested + 8

        if (
            self.generator_card_canvas.winfo_height()
            != canvas_height
        ):
            self.generator_card_canvas.configure(
                height=canvas_height,
            )

        self._draw_generator_card_surface(
            max(
                1,
                self.generator_card_canvas.winfo_width(),
            ),
            canvas_height,
        )

    def _draw_generator_card_surface(
        self,
        width,
        height,
    ):
        if width <= 2 or height <= 2:
            return

        scale = 4
        radius = 12
        border_width = 1

        image = Image.new(
            "RGBA",
            (
                int(width * scale),
                int(height * scale),
            ),
            (0, 0, 0, 0),
        )

        draw = ImageDraw.Draw(image)

        surface = self._appearance_color(
            SURFACE
        )
        line = self._appearance_color(
            LINE
        )

        draw.rounded_rectangle(
            (
                0,
                0,
                int(width * scale) - 1,
                int(height * scale) - 1,
            ),
            radius=radius * scale,
            fill=surface,
            outline=line,
            width=border_width * scale,
        )

        image = image.resize(
            (
                int(width),
                int(height),
            ),
            Image.Resampling.LANCZOS,
        )

        self._generator_card_photo = (
            ImageTk.PhotoImage(image)
        )

        if not hasattr(
            self,
            "_generator_card_image_id",
        ):
            self._generator_card_image_id = (
                self.generator_card_canvas.create_image(
                    0,
                    0,
                    anchor="nw",
                    image=self._generator_card_photo,
                )
            )

            self.generator_card_canvas.tag_lower(
                self._generator_card_image_id,
            )
        else:
            self.generator_card_canvas.itemconfigure(
                self._generator_card_image_id,
                image=self._generator_card_photo,
            )

        self.generator_card_canvas.configure(
            bg=self._appearance_color(BG),
        )

    def _refresh_generator_card_surface(self):
        if not hasattr(
            self,
            "generator_card_canvas",
        ):
            return

        self._draw_generator_card_surface(
            max(
                1,
                self.generator_card_canvas.winfo_width(),
            ),
            max(
                1,
                self.generator_card_canvas.winfo_height(),
            ),
        )

    def _build_length_controls(self):
        header = ctk.CTkFrame(
            self.generator_card,
            fg_color="transparent",
            corner_radius=0,
        )
        header.pack(
            fill="x",
            padx=8,
            pady=(14, 5),
        )

        self.length_label = ctk.CTkLabel(
            header,
            text="Longitud de la contraseña",
            font=ctk.CTkFont(
                family=FONT_UI,
                size=12,
                weight="bold",
            ),
            text_color=TEXT,
        )
        self.length_label.pack(
            side="left",
        )

        self.length_var = ctk.StringVar(
            value="16"
        )

        self.length_entry = ctk.CTkEntry(
            header,
            width=44,
            height=30,
            corner_radius=5,
            fg_color=ENTRY_BG,
            border_color=LINE,
            border_width=1,
            text_color=TEXT,
            justify="center",
            textvariable=self.length_var,
            font=ctk.CTkFont(
                family=FONT_UI,
                size=12,
                weight="bold",
            ),
        )
        self.length_entry.pack(
            side="right",
        )

        self.length_entry.bind(
            "<FocusOut>",
            self._sync_entry_to_slider,
        )
        self.length_entry.bind(
            "<Return>",
            self._sync_entry_to_slider,
        )

        self.length_slider = ctk.CTkSlider(
            self.generator_card,
            from_=4,
            to=64,
            number_of_steps=60,
            command=self._slider_changed,
            height=14,
            corner_radius=6,
            button_length=16,
            button_corner_radius=8,
            fg_color=SURFACE_2,
            progress_color=DEEP_MINT,
            button_color=MINT,
            button_hover_color=GLOW,
            border_width=0,
        )
        self.length_slider.set(16)
        self.length_slider.pack(
            fill="x",
            padx=8,
            pady=(0, 12),
        )

        self._configure_slider_keyboard()


    def _configure_slider_keyboard(self):
        """Permite ajustar la longitud con las flechas cuando el slider tiene foco."""
        canvas = getattr(
            self.length_slider,
            "_canvas",
            None,
        )

        if canvas is None:
            return

        try:
            canvas.configure(
                takefocus=1,
            )
        except Exception:
            pass

        canvas.bind(
            "<Button-1>",
            self._focus_length_slider,
            add="+",
        )

        canvas.bind(
            "<Left>",
            lambda _event: self._step_length_slider(-1),
        )
        canvas.bind(
            "<Down>",
            lambda _event: self._step_length_slider(-1),
        )
        canvas.bind(
            "<Right>",
            lambda _event: self._step_length_slider(1),
        )
        canvas.bind(
            "<Up>",
            lambda _event: self._step_length_slider(1),
        )

    def _focus_length_slider(self, _event=None):
        canvas = getattr(
            self.length_slider,
            "_canvas",
            None,
        )

        if canvas is not None:
            self.after_idle(
                canvas.focus_set,
            )

    def _step_length_slider(self, delta):
        current = int(
            round(
                self.length_slider.get()
            )
        )

        updated = max(
            4,
            min(
                64,
                current + delta,
            ),
        )

        self.length_slider.set(
            updated
        )
        self.length_var.set(
            str(updated)
        )

        return "break"


    def _build_password_controls(self):
        self.password_label = ctk.CTkLabel(
            self.generator_card,
            text="Contraseña generada",
            font=ctk.CTkFont(
                family=FONT_UI,
                size=12,
                weight="bold",
            ),
            text_color=TEXT,
        )
        self.password_label.pack(
            anchor="w",
            padx=8,
            pady=(0, 5),
        )

        self.password_var = ctk.StringVar()
        self.password_display_var = ctk.StringVar()

        if self.compact_mode:
            self._build_compact_password_controls()
        else:
            self._build_desktop_password_controls()

    def _create_password_entry(self, parent):
        container = ctk.CTkFrame(
            parent,
            height=40,
            fg_color="transparent",
            corner_radius=0,
        )
        container.pack_propagate(False)

        entry = ctk.CTkEntry(
            container,
            height=40,
            corner_radius=5,
            fg_color=ENTRY_BG,
            border_color=LINE,
            border_width=1,
            text_color=TEXT,
            textvariable=self.password_display_var,
            font=ctk.CTkFont(
                family=FONT_MONO,
                size=14,
            ),
        )
        entry.place(
            x=0,
            y=0,
            relwidth=1,
            relheight=1,
        )

        self.password_text_entry = entry

        entry.bind(
            "<Button-1>",
            self._password_click_guard,
            add="+",
        )

        entry.bind(
            "<KeyPress>",
            self._password_key_guard,
            add="+",
        )

        native_entry = getattr(
            entry,
            "_entry",
            None,
        )

        self.password_scrollbar = ctk.CTkScrollbar(
            container,
            orientation="horizontal",
            width=92,
            height=9,
            corner_radius=4,
            command=(
                native_entry.xview
                if native_entry is not None
                else None
            ),
            fg_color=LINE,
            button_color=MINT,
            button_hover_color=GLOW,
        )

        if native_entry is not None:
            native_entry.configure(
                xscrollcommand=self.password_scrollbar.set,
            )

            native_entry.bind(
                "<Shift-MouseWheel>",
                self._password_horizontal_wheel,
                add="+",
            )
            # Button-6 / Button-7 son eventos X11 y no existen
            # en Tk sobre Windows. Solo se registran fuera de Windows.
            if sys.platform != "win32":
                try:
                    native_entry.bind(
                        "<Button-6>",
                        lambda _event: self._scroll_password_horizontal(-1),
                        add="+",
                    )
                    native_entry.bind(
                        "<Button-7>",
                        lambda _event: self._scroll_password_horizontal(1),
                        add="+",
                    )
                except tk.TclError:
                    pass

        self.password_scrollbar.bind(
            "<Shift-MouseWheel>",
            self._password_horizontal_wheel,
            add="+",
        )

        scrollbar_canvas = getattr(
            self.password_scrollbar,
            "_canvas",
            None,
        )

        if scrollbar_canvas is not None:
            scrollbar_canvas.bind(
                "<Shift-MouseWheel>",
                self._password_horizontal_wheel,
                add="+",
            )

        container.bind(
            "<Configure>",
            lambda _event: self.after_idle(
                self._update_password_scrollbar_visibility,
            ),
            add="+",
        )

        return container


    def _update_password_scrollbar_visibility(self):
        if not hasattr(
            self,
            "password_text_entry",
        ):
            return

        native_entry = getattr(
            self.password_text_entry,
            "_entry",
            None,
        )

        if native_entry is None:
            return

        if not self.password_var.get():
            self.password_scrollbar.place_forget()
            native_entry.xview_moveto(0)
            return

        try:
            first, last = native_entry.xview()
            overflow = (
                last - first
            ) < 0.995
        except Exception:
            overflow = False

        if overflow:
            container_width = max(
                92,
                self.password_scrollbar.master.winfo_width(),
            )

            scrollbar_width = min(
                92,
                max(
                    72,
                    container_width - 28,
                ),
            )

            self.password_scrollbar.configure(
                width=scrollbar_width,
            )

            self.password_scrollbar.place(
                relx=0.5,
                rely=1.0,
                y=-5,
                anchor="s",
            )
        else:
            self.password_scrollbar.place_forget()
            native_entry.xview_moveto(0)

    def _password_horizontal_wheel(self, event):
        delta = getattr(
            event,
            "delta",
            0,
        )

        if delta == 0:
            return "break"

        steps = (
            -1
            if delta > 0
            else 1
        )

        return self._scroll_password_horizontal(
            steps
        )

    def _scroll_password_horizontal(self, steps):
        if not hasattr(
            self,
            "password_text_entry",
        ):
            return "break"

        native_entry = getattr(
            self.password_text_entry,
            "_entry",
            None,
        )

        if native_entry is None:
            return "break"

        native_entry.xview_scroll(
            steps,
            "units",
        )

        return "break"

    def _password_click_guard(self, _event):
        if not self.password_var.get():
            self.focus_set()
            return "break"

        return None

    def _password_key_guard(self, event):
        ctrl_pressed = bool(event.state & 0x0004)

        if ctrl_pressed and event.keysym.lower() in {"c", "a"}:
            return None

        allowed = {
            "Left",
            "Right",
            "Home",
            "End",
            "Shift_L",
            "Shift_R",
            "Control_L",
            "Control_R",
        }

        if event.keysym in allowed:
            return None

        return "break"


    def _create_eye_button(self, parent):
        return ctk.CTkButton(
            parent,
            text="",
            image=self.eye_closed_image,
            command=self.toggle_password_visibility,
            width=32,
            height=40,
            corner_radius=5,
            fg_color=SURFACE_2,
            hover_color=LINE,
            border_width=1,
            border_color=LINE,
        )

    def _create_copy_button(self, parent):
        return ctk.CTkButton(
            parent,
            text="Copiar",
            image=self.copy_icon,
            compound="left",
            command=self.copy_password,
            width=62,
            height=40,
            corner_radius=5,
            fg_color=SURFACE_2,
            hover_color=LINE,
            border_width=1,
            border_color=LINE,
            text_color=TEXT,
            font=ctk.CTkFont(
                family=FONT_UI,
                size=11,
                weight="bold",
            ),
        )

    def _create_clear_button(self, parent):
        return ctk.CTkButton(
            parent,
            text="Limpiar",
            command=self.clear_password,
            width=62,
            height=40,
            corner_radius=5,
            fg_color=SURFACE_2,
            hover_color=LINE,
            border_width=1,
            border_color=LINE,
            text_color=TEXT,
            font=ctk.CTkFont(
                family=FONT_UI,
                size=11,
                weight="bold",
            ),
            state="disabled",
        )


    def _build_desktop_password_controls(self):
        row = ctk.CTkFrame(
            self.generator_card,
            fg_color="transparent",
            corner_radius=0,
        )
        row.pack(
            fill="x",
            padx=8,
        )

        self.clear_button = self._create_clear_button(
            row
        )
        self.clear_button.pack(
            side="right",
        )

        self.copy_button = self._create_copy_button(
            row
        )
        self.copy_button.pack(
            side="right",
            padx=(4, 4),
        )

        self.visibility_button = self._create_eye_button(
            row
        )
        self.visibility_button.pack(
            side="right",
            padx=(5, 0),
        )

        self.password_entry = self._create_password_entry(
            row
        )
        self.password_entry.pack(
            side="left",
            fill="x",
            expand=True,
        )

    def _build_compact_password_controls(self):
        wrapper = ctk.CTkFrame(
            self.generator_card,
            fg_color="transparent",
            corner_radius=0,
        )
        wrapper.pack(
            fill="x",
            padx=8,
        )

        self.password_entry = self._create_password_entry(
            wrapper
        )
        self.password_entry.pack(
            fill="x",
        )

        actions = ctk.CTkFrame(
            wrapper,
            fg_color="transparent",
            corner_radius=0,
        )
        actions.pack(
            fill="x",
            pady=(7, 0),
        )

        self.clear_button = self._create_clear_button(
            actions
        )
        self.clear_button.pack(
            side="right",
        )

        self.copy_button = self._create_copy_button(
            actions
        )
        self.copy_button.pack(
            side="right",
            padx=(0, 4),
        )

        self.visibility_button = self._create_eye_button(
            actions
        )
        self.visibility_button.pack(
            side="right",
            padx=(0, 4),
        )


    def _build_generate_button(self):
        self.generate_button = ctk.CTkButton(
            self.generator_card,
            text="Generar contraseña",
            command=self.generate_password,
            height=40,
            corner_radius=5,
            fg_color=PRIMARY,
            hover_color=PRIMARY_HOVER,
            text_color=PRIMARY_TEXT,
            font=ctk.CTkFont(
                family=FONT_UI,
                size=13,
                weight="bold",
            ),
        )
        self.generate_button.pack(
            fill="x",
            padx=8,
            pady=(12, 14),
        )

    # --------------------------------------------------------
    # Tema
    # --------------------------------------------------------

    def _theme_button_icon(self):
        if ctk.get_appearance_mode() == "Dark":
            return self.theme_to_light_icon

        return self.theme_to_dark_icon

    def _theme_button_text(self):
        # Respaldo si faltara alguno de los PNG.
        if self._theme_button_icon() is not None:
            return ""

        return (
            "☀"
            if ctk.get_appearance_mode() == "Dark"
            else "☾"
        )

    def toggle_theme(self):
        mode = ctk.get_appearance_mode()

        ctk.set_appearance_mode(
            "Light"
            if mode == "Dark"
            else "Dark"
        )

        self.theme_button.configure(
            text=self._theme_button_text(),
            image=self._theme_button_icon(),
        )

        self.after(
            20,
            self._apply_dwm_frame,
        )

        self.after(
            25,
            self._refresh_generator_card_surface,
        )

    # --------------------------------------------------------
    # Longitud
    # --------------------------------------------------------

    def _slider_changed(self, value):
        self.length_var.set(
            str(int(round(value)))
        )

    def _sync_entry_to_slider(
        self,
        _event=None,
    ):
        length = self._read_length(
            show_error=True
        )

        if length is None:
            return "break"

        self.length_slider.set(length)
        self.length_var.set(str(length))
        return "break"

    def _read_length(
        self,
        show_error=False,
    ):
        try:
            length = int(
                self.length_var.get()
            )
        except ValueError:
            if show_error:
                self.length_var.set("16")
                self.show_status(
                    "Introduce una longitud válida.",
                    error=True,
                )
            return None

        if not 4 <= length <= 64:
            if show_error:
                corrected = min(
                    64,
                    max(4, length),
                )

                self.length_var.set(
                    str(corrected)
                )
                self.length_slider.set(
                    corrected
                )

                self.show_status(
                    "La longitud debe estar entre 4 y 64.",
                    error=True,
                )

            return None

        return length

    # --------------------------------------------------------
    # Contraseñas
    # --------------------------------------------------------

    def generate_password(self):
        length = self._read_length(
            show_error=True
        )

        if length is None:
            return

        characters = (
            string.ascii_letters
            + string.digits
            + string.punctuation
        )

        password = "".join(
            secrets.choice(characters)
            for _ in range(length)
        )

        self.password_var.set(password)
        self._refresh_password_display()

        self.clear_button.configure(
            state="normal"
        )

        try:
            pyperclip.copy(password)
            self.show_status(
                "Contraseña generada y copiada."
            )
        except pyperclip.PyperclipException:
            self.show_status(
                "Generada, pero no pudo copiarse.",
                error=True,
            )

    def clear_password(self):
        if not self.password_var.get():
            return

        self.password_var.set("")
        self.password_visible = False
        self._refresh_password_display()

        if self.eye_closed_image is not None:
            self.visibility_button.configure(
                image=self.eye_closed_image
            )

        self.clear_button.configure(
            state="disabled"
        )

        self.focus_set()

        self.show_status(
            "Contraseña eliminada de la vista."
        )

    def copy_password(self):
        password = self.password_var.get()

        if not password:
            self.show_status(
                "Primero genera una contraseña.",
                error=True,
            )
            return

        try:
            pyperclip.copy(password)
            self.show_status(
                "Contraseña copiada."
            )
        except pyperclip.PyperclipException:
            self.show_status(
                "No se pudo acceder al portapapeles.",
                error=True,
            )

    def _refresh_password_display(self):
        password = self.password_var.get()

        if not password:
            self.password_display_var.set("")

            if hasattr(
                self,
                "password_text_entry",
            ):
                native_entry = getattr(
                    self.password_text_entry,
                    "_entry",
                    None,
                )

                if native_entry is not None:
                    native_entry.xview_moveto(0)

            self.after_idle(
                self._update_password_scrollbar_visibility,
            )
            return

        if self.password_visible:
            self.password_display_var.set(password)
        else:
            self.password_display_var.set(
                "•" * len(password)
            )

        if hasattr(
            self,
            "password_text_entry",
        ):
            native_entry = getattr(
                self.password_text_entry,
                "_entry",
                None,
            )

            if native_entry is not None:
                native_entry.xview_moveto(0)

        self.after_idle(
            self._update_password_scrollbar_visibility,
        )

    def toggle_password_visibility(self):
        self.password_visible = (
            not self.password_visible
        )

        self._refresh_password_display()

        if self.password_visible:
            if self.eye_open_image is not None:
                self.visibility_button.configure(
                    image=self.eye_open_image
                )
        else:
            if self.eye_closed_image is not None:
                self.visibility_button.configure(
                    image=self.eye_closed_image
                )

    # --------------------------------------------------------
    # Estado
    # --------------------------------------------------------

    def show_status(
        self,
        text,
        error=False,
    ):
        if self._status_job is not None:
            self.after_cancel(
                self._status_job
            )

        self.status_label.configure(
            text=text,
            text_color=(
                "#D44747"
                if error
                else MINT
            ),
        )

        self._status_job = self.after(
            3000,
            self._reset_status,
        )

    def _reset_status(self):
        self.status_label.configure(
            text="Listo para generar",
            text_color=MUTED,
        )
        self._status_job = None

    def _bind_shortcuts(self):
        self.bind(
            "<Escape>",
            lambda _event: self.close_app(),
        )


if __name__ == "__main__":
    app = KeyMintApp()
    app.mainloop()
