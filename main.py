# Scriviamo un codice python che modelli un semplice gestionale
# aziendale. Dovremo prevedere la possibilità di definire entità che
# modellano i prodotti, i clienti, offrire interfacce per calcolare i
# prezzi, eventualmente scontati, ...

class Prodotto:
    aliquota_iva = 0.22 # variabile di classe, ovvero è la stessa per tutte le istanze che verranno create
    def __init__(self, name: str, price: float, quantity: int, supplier = None):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.supplier = supplier

    def valore_netto(self):
        return self.price * self.quantity

    def valore_lordo(self):
        netto = self.valore_netto()
        lordo = netto*(1+self.aliquota_iva)
        return lordo

    @classmethod
    def costruttore_con_quantità_uno(cls, name: str, price:float, supplier:str):
        cls(name, price, 1, supplier)

    @staticmethod
    def applica_sconto(price,percentage):
        return price*(1-percentage)

myproduct1 = Prodotto("Laptop", 1200.0, 12, "ABC")

print(f"Nome prodotto: {myproduct1.name} - prezzo: {myproduct1.price}")

print(f"Il totale lordo di myproduct1 è {myproduct1.valore_lordo()}") #uso un metodo di istanza

p3 = Prodotto.costruttore_con_quantità_uno("Auricolari",200.0,"ABC") #modo per chiamare un metodo di classe

print(f"Prezzo scontato di myproduct1 {Prodotto.applica_sconto(myproduct1.price,0.15)}") #modo per chiamare un metodo statico

myproduct2 = Prodotto("Mouse",10,25,"CDE")
print(f"Nome prodotto: {myproduct2.name} - prezzo: {myproduct2.price}")

# Scrivere una classe Cliente che abbia i campi
# "nome", "email", "categoria" ("Gold", "Silver", "Bronze").
# Vorremmo che questa classe avesse un metodo che chiamiamo "descrizione"
# che deve restituire una stringa formattata ad es
# "Cliente Fulvio Bianchi (Gold) - fulvio@google.com"

class Cliente:
    def __init__(self, nome, mail, categoria):
        self.nome = nome
        self.mail = mail
        self.categoria = categoria

    def descrizione(self):
        return f"Cliente {self.nome} ({self.categoria}) - {self.mail}"

c1 = Cliente("Fulvio Bianchi", "fulvio@google.com", "Gold")
print(c1.descrizione())