import flet as ft
import random
from datetime import datetime

PRIMARY = "#ff4d4d"
BG = "#0d0d0d"
CARD = "#1a1a1a"
TEXT_GRAY = "#bfbfbf"

# =======================================
#     TARJETAS DE ESTADÍSTICAS
# =======================================

def stat_card(icon, value, label):
    return ft.Container(
        bgcolor=CARD,
        padding=15,
        border_radius=20,
        width=110,
        height=120,
        content=ft.Column(
            alignment="center",
            horizontal_alignment="center",
            spacing=5,
            controls=[
                ft.Text(icon, size=28),
                ft.Text(value, size=22, weight="bold", color="white"),
                ft.Text(label, size=12, color=TEXT_GRAY)
            ],
        ),
    )

# =======================================
#     PANTALLA PRINCIPAL (HOME)
# =======================================

def home_view(page, go_register, runs):
    # Mini gráfica tipo barras
    data = [random.randint(3, 10) for _ in range(7)]
    chart = [
        ft.Container(
            width=20,
            height=v * 10,
            bgcolor=PRIMARY,
            border_radius=8,
            animate=ft.Animation(300, "easeOut"),
        ) for v in data
    ]

    return ft.Column(
        expand=True,
        spacing=20,
        controls=[
            ft.Text("🏃 RYNO", size=32, weight="bold", color="white"),
            ft.Text("Tu rendimiento general", size=15, color=TEXT_GRAY),

            # Estadísticas principales
            ft.Row(
                alignment="spaceBetween",
                controls=[
                    stat_card("🔥", "345", "Calorías"),
                    stat_card("⏱️", "5.12", "Ritmo/km"),
                    stat_card("📏", "7.2", "Km hoy"),
                ],
            ),

            ft.Text("Progreso semanal", size=18, weight="bold", color="white"),

            ft.Container(
                bgcolor=CARD,
                padding=15,
                border_radius=15,
                height=180,
                content=ft.Row(alignment="end", spacing=12, controls=chart),
            ),
        ]
    )

# =======================================
#     REGISTRAR CARRERA
# =======================================

def register_view(page, go_back, runs):
    dist = ft.TextField(label="Distancia (km)", width=200)
    time = ft.TextField(label="Tiempo (min)", width=200)
    notes = ft.TextField(label="Notas", width=300)

    def save(e):
        try:
            d = float(dist.value)
            t = float(time.value)
        except:
            page.snack_bar = ft.SnackBar(ft.Text("Datos inválidos"), open=True)
            page.update()
            return

        runs.append({
            "date": datetime.now().strftime("%d/%m/%Y %H:%M"),
            "distance": d,
            "time": t,
            "notes": notes.value
        })
        go_back()

    return ft.Column(
        spacing=20,
        controls=[
            ft.Text("Registrar carrera", size=28, weight="bold", color="white"),
            dist,
            time,
            notes,
            ft.ElevatedButton("Guardar", bgcolor=PRIMARY, color="white", on_click=save),
        ]
    )

# =======================================
#     HISTORIAL
# =======================================

def history_view(page, runs):
    if not runs:
        return ft.Text("No hay carreras registradas aún.", color=TEXT_GRAY)

    items = []
    for r in reversed(runs):
        items.append(
            ft.Container(
                bgcolor=CARD,
                padding=15,
                border_radius=15,
                content=ft.Column(
                    controls=[
                        ft.Text(f"📅 {r['date']}", color="white"),
                        ft.Text(f"{r['distance']} km en {r['time']} min", color=TEXT_GRAY),
                        ft.Text(f"📝 {r['notes']}", color=TEXT_GRAY),
                    ]
                ),
            )
        )
    return ft.Column(spacing=10, controls=items)

# =======================================
#     MAIN APP
# =======================================

def main(page: ft.Page):
    page.title = "RYNO Running App"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = BG
    page.padding = 15

    runs = []
    current_tab = ft.Tabs(
        selected_index=0,
        tab_alignment="center",
        indicator_color=PRIMARY,
        tabs=[
            ft.Tab(text="Inicio"),
            ft.Tab(text="Historial"),
        ],
    )

    # Contenido dinámico
    body = ft.Container(expand=True)

    def update_content():
        if current_tab.selected_index == 0:
            body.content = home_view(page, open_register, runs)
        else:
            body.content = history_view(page, runs)
        page.update()

    def open_register(e):
        page.views.append(
            ft.View(
                "/register",
                bgcolor=BG,
                controls=[
                    register_view(page, go_back, runs)
                ]
            )
        )
        page.update()

    def go_back():
        page.views.pop()
        update_content()

    current_tab.on_change = lambda e: update_content()

    update_content()

    # Botón flotante para registrar carrera
    fab = ft.FloatingActionButton(
        bgcolor=PRIMARY,
        content=ft.Text("+", size=35, weight="bold", color="white"),
        on_click=open_register,
    )

    page.add(body, current_tab, fab)

ft.app(target=main)
