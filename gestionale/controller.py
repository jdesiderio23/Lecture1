import flet as ft
class Controller:
    def __init__(self, v):
        self._view = v

    def add_ordine(self, e):
        # Prodotto
        nomePstr = self._view._txtInNomeP.value
        try:
            prezzo = float(self._view._txtInPrezzo.value)
        except ValueError:
            self._view._lvOut.controls.append(
                ft.Text("Attenzione! Il prezzo deve essere un numero.",
                        color = "red")
            )
            self._view.update_page()
            return

        try:
            quantita = int(self._view._txtInQuantita.value)
        except ValueError:
            self._view._lvOut.controls.append(
                ft.Text("Attenzione! La quantità deve essere un numero.",
                        color = "red")
            )
            self._view.update_page()
            return

    def gestisci_ordine(self, e):
        pass

    def gestisci_all_ordini(self, e):
        pass

    def stampa_sommario(self, e):
        pass

