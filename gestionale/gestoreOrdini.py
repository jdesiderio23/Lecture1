"""
Scrivere un software gestionale che abbia le seguenti funzionalità:
1) supportare l'arrivo e la gestione di ordini.
1bis) quando arriva un nuovo ordine lo aggiungo a una coda,
assicurandomi che sia eseguito solo dopo gli altri.
2) avere delle funzionalità per avere statistiche sugli ordini
3) fornire statistiche sulla distribuzione di ordini per categoria di cliente.
"""
from collections import deque, defaultdict, Counter

from gestionale.vendite.ordini import Ordine


class GestoreOrdini:

    def __init__(self):
        self._ordini_da_processare = deque()
        self._ordini_processati = []
        self._statistiche_prodotti = Counter()
        self._ordini_per_categoria = defaultdict(list)

    def add_ordine(self, ordine: Ordine):
        """Aggiunge un nuovo ordine agli elementi da gestire"""
        self._ordini_da_processare.append(ordine)
        print(f"Ricevuto un nuovo ordine da parte di {ordine.cliente}.")
        print(f"Ordini ancora da evadere: {len(self._ordini_da_processare)}")

    def processa_prossimo_ordine(self):
        """Questo metodo legge il prossimo ordine in coda e lo gestisce"""

        #Assicuriamoci che un ordine da processare esista
        if not self._ordini_da_processare:
            print("Non ci sono ordini in coda.")
            return False

        #Se esiste, gestiamo il primo in coda.
        ordine = self._ordini_da_processare.popleft() # Logica FIFO

        print(f"Sto processando l'ordine di {ordine.cliente}")
        print(ordine.riepilogo())

        #Aggiornare statistiche sui prodotti venduti --
        # Laptop - 10 +1
        # Mouse - 5 +2
        for riga in ordine.righe:
            self._statistiche_prodotti[riga.prodotto.name] += riga.quantita

        #Raggruppare gli ordini per categoria
        self._ordini_per_categoria[ordine.cliente.categoria].append(ordine)

        #Archiviamo l'ordine
        self._ordini_processati.append(ordine)

        print("Ordine correttamente processato.")

        return True

    def processa_tutti_ordini(self):
        """Processa tutti gli ordini attualmente presenti in coda."""
        print(f"Processando {len(self._ordini_da_processare)} ordini")
        while self._ordini_da_processare:
            self.processa_prossimo_ordine()
        print("Tutti gli ordini sono stati processati.")

    def get_statistiche_prodotti(self, top_n: int = 5):
        """Questo metodo restituisce info sui prodotti più venduti"""

    def get_distribuzione_categorie(self):
        pass

    def stampa_riepilogo(self):
        pass