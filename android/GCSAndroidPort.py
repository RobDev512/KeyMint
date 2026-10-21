from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
import random
import string
import pyperclip

class PasswordGeneratorApp(App):
    def build(self):
        self.title = "Generador de Contraseñas Seguras"
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Etiqueta y entrada para la longitud de la contraseña
        self.label = Label(text="Longitud de la contraseña:")
        layout.add_widget(self.label)

        self.text_input = TextInput(text='12', multiline=False, input_filter='int')
        layout.add_widget(self.text_input)

        # Etiqueta y entrada para mostrar la contraseña generada
        self.result_label = Label(text="Contraseña generada:")
        layout.add_widget(self.result_label)

        self.result_input = TextInput(multiline=False, readonly=True)
        layout.add_widget(self.result_input)

        # Botón para generar la contraseña
        generate_button = Button(text="Generar")
        generate_button.bind(on_press=self.generate_password)
        layout.add_widget(generate_button)

        # Botón para copiar la contraseña
        copy_button = Button(text="Copiar")
        copy_button.bind(on_press=self.copy_password)
        layout.add_widget(copy_button)

        return layout

    def generate_password(self, instance):
        try:
            length = int(self.text_input.text)
            if length < 4:
                self.show_popup('Advertencia', 'La longitud debe ser mayor o igual a 4.')
                return
            characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(characters) for _ in range(length))
            self.result_input.text = password
            pyperclip.copy(password)
            self.show_popup('Contraseña generada', 'Contraseña copiada al portapapeles automáticamente.')
        except ValueError:
            self.show_popup('Error', 'Introduce un número válido.')

    def copy_password(self, instance):
        password = self.result_input.text
        if password:
            pyperclip.copy(password)
            self.show_popup('Contraseña copiada', 'Contraseña copiada al portapapeles.')
        else:
            self.show_popup('Advertencia', 'No hay contraseña generada para copiar.')

    def show_popup(self, title, message):
        popup = Popup(title=title, content=Label(text=message), size_hint=(0.8, 0.4))
        popup.open()

if __name__ == '__main__':
    PasswordGeneratorApp().run()