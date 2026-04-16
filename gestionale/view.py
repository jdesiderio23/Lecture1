import flet as ft

class View:

    def __init__(self, page):
        self._page = page
        self._controller = None
        self._page.title = "TdP 2025 - Software Gestionale"
        self._page.horizontal_alignment = "CENTER"
        self._page.theme_mode = ft.ThemeMode.LIGHT
        self._page.update()

    def carica_interfaccia(self):
        # Prodotto
        self._txtInNomeP = ft.TextField(label = "Nome Prodotto", width = 200)
        self._txtInPrezzo= ft.TextField(label = "Prezzo", width = 200)
        self._txtInQuantita = ft.TextField(label = "Quantità", width = 200)
        row1 = ft.Row(controls = [self._txtInNomeP, self._txtInPrezzo, self._txtInQuantita],
                      alignment = ft.MainAxisAlignment.CENTER)

        self._page.add(row1)

    def set_controller(self, c):
        self._controller = c

    def update_page(self):
        self._page.update()