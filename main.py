import flet as ft

def main(page: ft.Page):

    page.title = "RYNO - Running App"
    page.theme_mode = "light"
    page.padding = 0
    page.spacing = 0
    page.window_min_width = 350

    # ------------ LOGIN SCREEN ------------
    def go_dashboard(e):
        page.views.append(dashboard_view())
        page.go("/dashboard")

    def login_view():
        return ft.View(
            "/",
            controls=[
                ft.Container(
                    width=page.width,
                    height=page.height,
                    gradient=ft.LinearGradient(
                        begin=ft.alignment.top_center,
                        end=ft.alignment.bottom_center,
                        colors=["#000000", "#5200FF"],
                    ),
                    content=ft.Column(
                        alignment="center",
                        horizontal_alignment="center",
                        spacing=25,
                        controls=[
                            ft.Text("BIENVENIDO A RYNO",
                                    size=32,
                                    weight="bold",
                                    color="white"),
                            
                            ft.CircleAvatar(
                                content=ft.Icon("person", size=50),
                                radius=45,
                                bgcolor="white",
                            ),

                            ft.TextField(
                                label="Nombre",
                                width=280,
                                border_radius=12,
                            ),
                            ft.TextField(
                                label="Contraseña",
                                password=True,
                                can_reveal_password=True,
                                width=280,
                                border_radius=12,
                            ),

                            ft.ElevatedButton(
                                text="Entrar",
                                width=200,
                                height=45,
                                bgcolor="#ffffff",
                                color="black",
                                on_click=go_dashboard,
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=20)
                                ),
                            ),

                            ft.Text(
                                "Creado por Juan Manuel Reyes Alegría\n y Arturo Triano Izquierdo",
                                size=12,
                                color="white",
                                text_align="center",
                            )
                        ]
                    )
                )
            ]
        )

    # ------------ DASHBOARD ------------
    def dashboard_view():
        return ft.View(
            "/dashboard",
            controls=[
                ft.Column(
                    spacing=10,
                    expand=True,
                    controls=[
                        ft.Text("Inicio", size=26, weight="bold"),

                        ft.Container(
                            padding=15,
                            border_radius=20,
                            bgcolor="#f5f5f5",
                            content=ft.Column(
                                spacing=5,
                                controls=[
                                    ft.Text("Tu progreso", size=20, weight="bold"),
                                    ft.Text("Kilómetros esta semana: 12.4", size=16),
                                ]
                            )
                        ),

                        ft.Container(
                            padding=15,
                            border_radius=20,
                            bgcolor="#f5f5f5",
                            content=ft.Column(
                                spacing=5,
                                controls=[
                                    ft.Text("Último entrenamiento", size=20, weight="bold"),
                                    ft.Text("5.3 km · 28 min", size=16),
                                ]
                            )
                        ),
                    ]
                ),

                ft.NavigationBar(
                    destinations=[
                        ft.NavigationDestination(icon="home", label="Home"),
                        ft.NavigationDestination(icon="run_circle", label="Entrenar"),
                        ft.NavigationDestination(icon="person", label="Perfil"),
                    ]
                )
            ]
        )

    # ------------ ROUTES ------------
    page.views.append(login_view())

    def route_change(route):
        pass

    page.on_route_change = route_change
    page.go("/")


ft.app(target=main, view=ft.WEB_BROWSER)
