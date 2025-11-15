import flet as ft
import base64

def main(page: ft.Page):
    page.title = "RYNO - Running App"
    page.theme_mode = "light"
    page.padding = 0
    page.spacing = 0
    page.window_min_width = 350

    # ---- FILE PICKER ----
    file_picker = ft.FilePicker()
    page.overlay.append(file_picker)

    # ---- FOTO DE PERFIL INICIAL (DEFAULT) ----
    profile_image = ft.Image(
        src="/assets/rhino.png",  # IMPORTANTE: usar /assets/
        width=120,
        height=120,
        fit="cover",
        border_radius=60,
    )

    # ---- CAMBIAR FOTO DE PERFIL ----
    def change_profile_picture(e):
        if not file_picker.result or not file_picker.result.files:
            return
        
        file = file_picker.result.files[0]

        # Convertir imagen a BASE64
        with open(file.path, "rb") as img:
            base64_str = base64.b64encode(img.read()).decode("utf-8")

        # Establecer imagen base64 en el avatar
        profile_image.src_base64 = base64_str
        profile_image.update()

    file_picker.on_result = change_profile_picture

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
                        colors=["#000000", "#5200FF"],
                        begin=ft.alignment.top_center,
                        end=ft.alignment.bottom_center,
                    ),
                    content=ft.Column(
                        alignment="center",
                        horizontal_alignment="center",
                        spacing=20,
                        controls=[
                            ft.Text("BIENVENIDO A RYNO",
                                    size=32,
                                    weight="bold",
                                    color="white"),

                            ft.Container(
                                content=profile_image,
                                on_click=lambda _: file_picker.pick_files(
                                    allow_multiple=False,
                                    file_type=ft.FilePickerFileType.IMAGE,
                                ),
                                ink=True,
                            ),

                            ft.Text("Foto de perfil", color="white"),

                            ft.TextField(
                                label="Nombre",
                                label_style=ft.TextStyle(color="white"),
                                width=280,
                                border_radius=12,
                                cursor_color="white",
                                color="white"
                            ),
                            ft.TextField(
                                label="Contraseña",
                                password=True,
                                can_reveal_password=True,
                                width=280,
                                border_radius=12,
                                label_style=ft.TextStyle(color="white"),
                                cursor_color="white",
                                color="white"
                            ),

                            ft.ElevatedButton(
                                text="Entrar",
                                width=200,
                                height=45,
                                bgcolor="#ffffff",
                                color="black",
                                on_click=go_dashboard,
                            ),

                            ft.Text(
                                "Creado por Juan Manuel Reyes Alegría\n y Arturo Triano Izquierdo",
                                size=12,
                                color="white",
                                text_align="center",
                            ),
                        ],
                    ),
                )
            ],
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
                                controls=[
                                    ft.Text("Tu progreso", size=20, weight="bold"),
                                    ft.Text("Kilómetros esta semana: 12.4"),
                                ]
                            ),
                        ),
                    ],
                ),

                ft.NavigationBar(
                    destinations=[
                        ft.NavigationDestination(icon="home", label="Home"),
                        ft.NavigationDestination(icon="run_circle", label="Entrenar"),
                        ft.NavigationDestination(icon="person", label="Perfil"),
                    ]
                ),
            ],
        )

    page.views.append(login_view())
    page.go("/")

ft.app(target=main, assets_dir="assets", view=ft.WEB_BROWSER)



ft.app(target=main, view=ft.WEB_BROWSER)
