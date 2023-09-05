from kivymd.app import MDApp
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.clock import Clock
from kivy.utils import get_color_from_hex
from kivy.core.window import Window

class ExponenteApp(MDApp):
    def build(self):
        self.title = "Calculadora de imaginario"

        layout = MDBoxLayout(
            orientation='vertical',
            spacing=10,
            padding=20,
            md_bg_color=get_color_from_hex("#000000")
        )

        self.exponenteEnt = TextInput(
            font_size=40,
            multiline=False,
            readonly=True,
            halign="center",
            background_color=(1, 1, 1, 1),
            size_hint=(1, 0.2)
        )

        button_layout = GridLayout(cols=3, spacing=10, size_hint_y=None, height=Window.height * 0.6)

        for num in range(1, 10):
            button = Button(text=str(num), on_press=lambda x, num=num: self.entryText(str(num)), background_color=(0.9, 0.9, 0.9, 1), size_hint=(None, None), size=(Window.width * 0.2, Window.height * 0.2))
            button_layout.add_widget(button)

        # Botón "0"
        zero_button = Button(text="0", on_press=lambda x: self.entryText("0"), background_color=(0.9, 0.9, 0.9, 1), size_hint=(None, None), size=(Window.width * 0.2, Window.height * 0.2))
        button_layout.add_widget(zero_button)

        # Botón "Calcular"
        calcularBtn = Button(text="CALCULAR", on_press=self.calculate_result, background_color=(0, 0.7, 0, 1), color=(1, 1, 1, 1), size_hint=(None, None), size=(Window.width * 0.2, Window.height * 0.2))
        button_layout.add_widget(calcularBtn)

        # Botón "Borrar"
        calcBtnDel = Button(text="<<<", on_press=self.clearText, background_color=(1, 0, 0, 1), color=(1, 1, 1, 1), size_hint=(None, None), size=(Window.width * 0.2, Window.height * 0.2))
        button_layout.add_widget(calcBtnDel)

        layout.add_widget(self.exponenteEnt)
        layout.add_widget(button_layout)

        return layout

    def entryText(self, num):
        self.exponenteEnt.text += num

    def clearText(self, instance):
        self.exponenteEnt.text = ""

    def calculate_result(self, instance):
        try:
            exp = int(self.exponenteEnt.text)
            mod = exp % 4

            if mod == 0:
                self.exponenteEnt.text = "1"
            elif mod == 1:
                self.exponenteEnt.text = "i"
            elif mod == 2:
                self.exponenteEnt.text = "-1"
            elif mod == 3:
                self.exponenteEnt.text = "-i"
        except ValueError as e:
            print("Error:", e)
            self.exponenteEnt.text = "Error"

        Clock.schedule_once(self.clearTextAfterDelay, 3)

    def clearTextAfterDelay(self, dt=""):
        self.exponenteEnt.text = ""


if __name__ == '__main__':
    ExponenteApp().run()
