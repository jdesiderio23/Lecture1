import copy

from gestionale.core.prodotti import ProdottoRecord

p1 = ProdottoRecord("Laptop", 1200.0)
p2 = ProdottoRecord("Mouse", 20.0)
p3 = ProdottoRecord("Auricolari", 250.0)

carrello = [p1, p2, p3, ProdottoRecord("Tablet",700.0)]

print("Prodotti nel carrello: ")
for i, p in enumerate(carrello):
    print(f"{i+1} {p.name} - {p.prezzo_unitario}")

#Aggiungere ad una lista
carrello.append(ProdottoRecord("Monitor", 150.0))

carrello.sort(key = lambda x: x.prezzo_unitario, reverse = True)

print("Prodotti nel carrello: ")
for i, p in enumerate(carrello):
    print(f"{i+1} {p.name} - {p.prezzo_unitario}")

tot = sum(p.prezzo_unitario for p in carrello)
print(f"Totale del carrello: {tot}")

#Aggiungere
carrello.append(ProdottoRecord("Propdo", 100.0))
carrello.extend([ProdottoRecord("aaa", 100.0), ProdottoRecord("bbb", 100.0)])
carrello.insert(2, ProdottoRecord("ccc", 100.0))

#Rimuovere
carrello.pop() # rimuove l'ultimo elemento
carrello.pop(2) # rimuove l'elemento in posizione 2
carrello.remove(p1) # elimina la prima occorrenza di p1
# carrello.clear() # svuota la lista

#Sorting
# carrello.sort() # ordina seguendo ordinamento naturale -- non funziona se gli oggetti contenuti non definiscono un metodo __lt__
# carrello.sort(reverse=True) # ordina al contrario
# carrello.sort(key = function)
# carrello_ordinato = sorted(carrello)

#Copie e altro
carrello.reverse() # inverte l'ordine
carrello_copia = carrello.copy() # shallow copy, lista diversa ma oggetti sono gli stessi
carrello_copia2 = copy.deepcopy(carrello) # deep copy, lista diversa con oggetti diversi, memorizzati in posti diversi ecc.

# TUPLE
sede_principale = (45, 8) #lat e long della sede di Torino
sede_milano = (45,9) #lat e long della sede di Milano

print(f"Sede principale lat: {sede_principale[0]}, long: {sede_principale[1]}")

AliquoteIVA = (
    ("Standard", 0.22),
    ("Ridotta", 0.10),
    ("Alimentari", 0.04),
    ("Esente", 0.0)
)

for descr, valore in AliquoteIVA:
    print(f"{descr}: {valore*100}%")

def calcola_statistiche_carrello(carrello):
    """Restituisce prezzo totale, prezzo medio, massimo e minimo"""
    prezzi = [p.prezzo_unitario for p in carrello]
    return(sum(prezzi), sum(prezzi)/len(prezzi), max(prezzi), min(prezzi))

tot, media, max, min = calcola_statistiche_carrello(carrello)

tot, * altri_campi = calcola_statistiche_carrello(carrello)
print(tot)

#SET