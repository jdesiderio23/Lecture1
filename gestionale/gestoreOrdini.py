"""
Scrivere un software gestionale che abbia le seguenti funzionalità:
1) supportare l'arrivo e la gestione di ordini.
1bis) quando arriva un nuovo ordine lo aggiungo a una coda,
assicurandomi che sia eseguito solo dopo gli altri.
2) avere delle funzionalità per avere statistiche sugli ordini
3) fornire statistiche sulla distribuzione di ordini per categoria di cliente.
"""
from collections import deque

from gestionale.vendite.ordini import Ordine


class GestoreOrdini:

    def __init__(self):
        self.ordini_da_processare = deque()
        self.ordini_processati = []

    def add_ordine(self, ordine: Ordine):
        """Aggiunge un nuovo ordine agli elementi da gestire"""
        self.ordini_da_processare.append(ordine)
        print(f"Ricevuto un nuovo ordine da parte di {ordine.cliente}.")
        print(f"Ordini ancora da evadere: {len(self.ordini_da_processare)}")

    def processa_prossimo_ordine(self):
        """Questo metodo legge il prossimo ordine in coda e lo gestisce"""

        if not self.ordini_da_processare:
            print("Non ci sono ordini in coda.")
            return False

        ordine = self.ordini_da_processare.popleft() # Logica FIFO

        print(f"Sto processando l'ordine di {ordine.cliente}")
        print(ordine.riepilogo())

