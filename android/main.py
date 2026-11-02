import secrets
import string

from kivy.app import App
from kivy.clock import Clock
from kivy.core.clipboard import Clipboard
from kivy.core.window import Window
from kivy.metrics import dp, sp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.uix.textinput import TextInput

APP_VERSION = "1.1.0"

MINT = (0.208, 0.839, 0.682, 1)
DARK = {
    "bg": (0.027, 0.082, 0.071, 1),
    "surface": (0.047, 0.129, 0.110, 1),
    "surface2": (0.063, 0.188, 0.157, 1),
    "entry": (0.031, 0.102, 0.086, 1),
    "text": (0.953, 1.0, 0.984, 1),
    "muted": (0.608, 0.784, 0.737, 1),
}
LIGHT = {
    "bg": (0.949, 0.984, 0.973, 1),
    "surface": (1, 1, 1, 1),
    "surface2": (0.910, 0.965, 0.949, 1),
    "entry": (0.984, 0.996, 0.992, 1),
    "text": (0.063, 0.173, 0.145, 1),
    "muted": (0.333, 0.459, 0.427, 1),
}


class KeyMintButton(Button):
    def __init__(self, primary=False, **kwargs):
        super().__init__(**kwargs)
        self.primary = primary
        self.background_normal = ""
        self.background_down = ""
        self.bold = True
        self.font_size = sp(14)
        self.size_hint_y = None
        self.height = dp(46)

    def apply_theme(self, theme):
        if self.primary:
            self.background_color = MINT
            self.color = DARK["bg"]
        else:
            self.background_color = theme["surface2"]
            self.color = theme["text"]


class KeyMintAndroid(App):
    def build(self):
        self.title = "KeyMint Android Preview"
        self.dark_mode = True
        self.password = ""
        self.password_visible = False
        Window.softinput_mode = "below_target"

        self.root_box = BoxLayout(
            orientation="vertical",
            padding=dp(18),
            spacing=dp(14),
        )

        self._build_header()
        self._build_generator()
        self._build_footer()
        self.apply_theme()
        return self.root_box

    def make_label(self, text, size, bold=False, height=None):
        label = Label(
            text=text,
            font_size=sp(size),
            bold=bold,
            halign="left",
            valign="middle",
            size_hint_y=None if height else 1,
            height=dp(height) if height else 100,
        )
        label.bind(
            size=lambda widget, value: setattr(widget, "text_size", value)
        )
        return label

    def _build_header(self):
        row = BoxLayout(size_hint_y=None, height=dp(58), spacing=dp(8))
        brand = BoxLayout(orientation="vertical")

        self.title_label = self.make_label("KeyMint", 24, True)
        self.version_label = self.make_label(
            f"v{APP_VERSION} · Android Preview",
            10,
        )
        brand.add_widget(self.title_label)
        brand.add_widget(self.version_label)

        self.theme_button = KeyMintButton(
            text="Claro",
            size_hint_x=None,
            width=dp(72),
        )
        self.theme_button.bind(on_release=lambda *_: self.toggle_theme())

        row.add_widget(brand)
        row.add_widget(self.theme_button)
        self.root_box.add_widget(row)

    def _build_generator(self):
        self.panel = BoxLayout(
            orientation="vertical",
            padding=dp(16),
            spacing=dp(12),
        )

        heading = BoxLayout(size_hint_y=None, height=dp(34))
        self.generator_title = self.make_label(
            "Generador de contraseñas",
            18,
            True,
        )
        self.length_value = Label(
            text="16",
            bold=True,
            font_size=sp(16),
            size_hint_x=None,
            width=dp(46),
        )
        heading.add_widget(self.generator_title)
        heading.add_widget(self.length_value)
        self.panel.add_widget(heading)

        self.length_label = self.make_label(
            "Longitud de contraseña",
            12,
            height=24,
        )
        self.panel.add_widget(self.length_label)

        self.slider = Slider(
            min=4,
            max=64,
            value=16,
            step=1,
            size_hint_y=None,
            height=dp(38),
        )
        self.slider.bind(
            value=lambda _, value: setattr(
                self.length_value,
                "text",
                str(int(round(value))),
            )
        )
        self.panel.add_widget(self.slider)

        self.password_input = TextInput(
            readonly=True,
            password=True,
            multiline=False,
            size_hint_y=None,
            height=dp(52),
            padding=[dp(12), dp(14), dp(12), dp(10)],
            font_size=sp(15),
            cursor_width=0,
        )
        self.panel.add_widget(self.password_input)

        actions = BoxLayout(size_hint_y=None, height=dp(46), spacing=dp(8))
        self.visibility_button = KeyMintButton(text="Mostrar")
        self.copy_button = KeyMintButton(text="Copiar")
        self.clear_button = KeyMintButton(text="Limpiar")

        self.visibility_button.bind(
            on_release=lambda *_: self.toggle_visibility()
        )
        self.copy_button.bind(on_release=lambda *_: self.copy_password())
        self.clear_button.bind(on_release=lambda *_: self.clear_password())

        for button in (
            self.visibility_button,
            self.copy_button,
            self.clear_button,
        ):
            actions.add_widget(button)

        self.panel.add_widget(actions)

        self.generate_button = KeyMintButton(
            text="Generar contraseña",
            primary=True,
        )
        self.generate_button.bind(
            on_release=lambda *_: self.generate_password()
        )
        self.panel.add_widget(self.generate_button)

        self.status_label = self.make_label(
            "Todo se genera localmente en tu dispositivo.",
            11,
            height=38,
        )
        self.panel.add_widget(self.status_label)
        self.root_box.add_widget(self.panel)

    def _build_footer(self):
        self.footer_label = Label(
            text="Privacidad local · Sin servicios externos",
            size_hint_y=None,
            height=dp(38),
            font_size=sp(10),
        )
        self.root_box.add_widget(self.footer_label)

    def generate_password(self):
        characters = (
            string.ascii_letters
            + string.digits
            + string.punctuation
        )
        self.password = "".join(
            secrets.choice(characters)
            for _ in range(int(self.slider.value))
        )
        self.password_visible = False
        self.password_input.password = True
        self.password_input.text = self.password
        self.visibility_button.text = "Mostrar"
        self.copy_password(silent=True)
        self.show_status("Contraseña generada y copiada.")

    def copy_password(self, silent=False):
        if not self.password:
            if not silent:
                self.show_status(
                    "Primero genera una contraseña.",
                    error=True,
                )
            return

        try:
            Clipboard.copy(self.password)
            if not silent:
                self.show_status("Contraseña copiada.")
        except Exception:
            if not silent:
                self.show_status(
                    "No se pudo acceder al portapapeles.",
                    error=True,
                )

    def clear_password(self):
        if not self.password:
            return
        self.password = ""
        self.password_visible = False
        self.password_input.text = ""
        self.password_input.password = True
        self.visibility_button.text = "Mostrar"
        self.show_status("Contraseña eliminada de la vista.")

    def toggle_visibility(self):
        if not self.password:
            self.show_status(
                "Primero genera una contraseña.",
                error=True,
            )
            return

        self.password_visible = not self.password_visible
        self.password_input.password = not self.password_visible
        self.visibility_button.text = (
            "Ocultar" if self.password_visible else "Mostrar"
        )

    def toggle_theme(self):
        self.dark_mode = not self.dark_mode
        self.apply_theme()

    def apply_theme(self):
        theme = DARK if self.dark_mode else LIGHT
        Window.clearcolor = theme["bg"]
        self.panel.canvas.before.clear()
        self.password_input.background_normal = ""
        self.password_input.background_active = ""
        self.password_input.background_color = theme["entry"]
        self.password_input.foreground_color = theme["text"]
        self.password_input.selection_color = (
            MINT[0],
            MINT[1],
            MINT[2],
            0.35,
        )

        self.title_label.color = theme["text"]
        self.generator_title.color = theme["text"]
        self.length_value.color = MINT
        self.version_label.color = theme["muted"]
        self.length_label.color = theme["muted"]
        self.status_label.color = theme["muted"]
        self.footer_label.color = theme["muted"]
        self.theme_button.text = "Claro" if self.dark_mode else "Oscuro"

        for button in (
            self.theme_button,
            self.visibility_button,
            self.copy_button,
            self.clear_button,
            self.generate_button,
        ):
            button.apply_theme(theme)

    def show_status(self, text, error=False):
        self.status_label.text = text
        self.status_label.color = (
            (0.85, 0.28, 0.28, 1)
            if error
            else MINT
        )
        Clock.unschedule(self._restore_status)
        Clock.schedule_once(self._restore_status, 2.2)

    def _restore_status(self, *_):
        self.status_label.text = (
            "Todo se genera localmente en tu dispositivo."
        )
        self.status_label.color = (
            DARK if self.dark_mode else LIGHT
        )["muted"]


if __name__ == "__main__":
    KeyMintAndroid().run()
