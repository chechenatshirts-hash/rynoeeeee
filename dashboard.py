from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

Window.clearcolor = (0, 0, 0, 1)  # Fondo negro estilo RYNO

KV = """
Screen:
    BoxLayout:
        orientation: "vertical"
        padding: 20
        spacing: 20

        # Título
        Label:
            text: "Dashboard"
            font_size: "36sp"
            bold: True
            color: 1, 0, 0, 1  # Rojo RYNO
            size_hint_y: None
            height: 60

        # Tarjetas
        GridLayout:
            cols: 2
            spacing: 15
            size_hint_y: None
            height: 300

            # Ritmo
            BoxLayout:
                orientation: "vertical"
                padding: 15
                spacing: 5
                canvas.before:
                    Color:
                        rgba: .15, .15, .15, 1
                    RoundedRectangle:
                        pos: self.pos
                        size: self.size
                        radius: [20]
                Label:
                    text: "Ritmo"
                    font_size: "18sp"
                    color: 1,1,1,1
                Label:
                    text: "5:20 /km"
                    font_size: "32sp"
                    bold: True
                    color: 1,0,0,1

            # Distancia
            BoxLayout:
                orientation: "vertical"
                padding: 15
                spacing: 5
                canvas.before:
                    Color:
                        rgba: .15, .15, .15, 1
                    RoundedRectangle:
                        pos: self.pos
                        size: self.size
                        radius: [20]
                Label:
                    text: "Distancia"
                    font_size: "18sp"
                    color: 1,1,1,1
                Label:
                    text: "3.4 km"
                    font_size: "32sp"
                    bold: True
                    color: 1,0,0,1

            # Tiempo
            BoxLayout:
                orientation: "vertical"
                padding: 15
                spacing: 5
                canvas.before:
                    Color:
                        rgba: .15, .15, .15, 1
                    RoundedRectangle:
                        pos: self.pos
                        size: self.size
                        radius: [20]
                Label:
                    text: "Tiempo"
                    font_size: "18sp"
                    color: 1,1,1,1
                Label:
                    text: "18:42"
                    font_size: "32sp"
                    bold: True
                    color: 1,0,0,1

            # Récord Personal
            BoxLayout:
                orientation: "vertical"
                padding: 15
                spacing: 5
                canvas.before:
                    Color:
                        rgba: .15, .15, .15, 1
                    RoundedRectangle:
                        pos: self.pos
                        size: self.size
                        radius: [20]
                Label:
                    text: "Récord"
                    font_size: "18sp"
                    color: 1,1,1,1
                Label:
                    text: "4:35 /km"
                    font_size: "32sp"
                    bold: True
                    color: 1,0,0,1

        # Botón iniciar carrera
        Button:
            text: "Iniciar carrera"
            font_size: "24sp"
            bold: True
            background_color: 1,0,0,1
            color: 1,1,1,1
            size_hint_y: None
            height: 70
            background_normal: ""
"""

class DashboardApp(App):
    def build(self):
        return Builder.load_string(KV)

DashboardApp().run()
