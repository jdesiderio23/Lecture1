# Scriviamo un codice python che modelli un semplice gestionale
# aziendale. Dovremo prevedere la possibilità di definire entità che
# modellano i prodotti, i clienti, offrire interfacce per calcolare i
# prezzi, eventualmente scontati, ...

class Prodotto:
    def __init__(self, name: str, price: float, quantity: int, supplier = None):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.supplier = supplier

    def valore(self):
        return self.price * self.quantity

myproduct1 = Prodotto("Laptop", 1200.0, 12, "ABC")

print(f"Nome prodotto: {myproduct1.name} - prezzo: {myproduct1.price}")

myproduct2 = Prodotto("Mouse",10,25,"CDE")
print(f"Nome prodotto: {myproduct2.name} - prezzo: {myproduct2.price}")

# Scrivere una classe Cliente che abbia i campi
# "nome", "email", "categoria" ("Gold", "Silver", "Bronze").
# Vorremmo che questa classe avesse un metodo che chiamiamo "descrizione"
# che deve restituire una stringa formattata ad es
# "Cliente Fulvio Bianchi (Gold) - fulvio@google.com"