# Scriviamo un codice python che modelli un semplice gestionale
# aziendale. Dovremo prevedere la possibilità di definire entità che
# modellano i prodotti, i clienti, offrire interfacce per calcolare i
# prezzi, eventualmente scontati, ...

class Prodotto:
    aliquota_iva = 0.22 # variabile di classe, ovvero è la stessa per tutte le istanze che verranno create
    def __init__(self, name: str, price: float, quantity: int, supplier = None):
        self.name = name
        self._price = None
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

    @property
    def price(self): #eq. getter
        return self._price
    @price.setter
    def price(self, value):
        self._price = value
        if value < 0:
            raise ValueError("Attenzione, il prezzo non può essere neagativo")

    def __str__(self):
        return f"{self.name} - disponibili {self.quantity} pezzi a {self.price} $"

    def __repr__(self):
        return f"Prodotto(name = {self.name}, price = {self.price}, quantity = {self.quantity}, supplier = {self.supplier})"

    def __eq__(self, other: object) -> bool:

        if not isinstance(other, Prodotto):
            return NotImplemented
        return (self.name == other.name
        and self.price == other.price
             and self.quantity == other.quantity
             and self.supplier == other.supplier)

    def __lt__(self, other:"Prodotto") -> bool:
        return self.price < other.price

    def prezzo_finale(self) -> float:
        return self.price*(1+self.aliquota_iva)

class ProdottoScontato(Prodotto):
    def __init__(self,name: str, price: float, quantity: int, supplier : str, sconto_percento: float):
        #Prodotto.__init__()
        super().__init__(name,price,quantity,supplier)
        self.sconto_percento = sconto_percento

    def prezzo_finale(self) -> float:
        return self.valore_lordo()*(1-self.sconto_percento/100)

class Servizio(Prodotto):
    def __init__(self,name: str, tariffa_oraria: float, ore: int):
        super().__init__(name = name, price = tariffa_oraria, quantity = 1, supplier = None)
        self.ore = ore

    def prezzo_finale(self) -> float:
        return self.price * self.ore

myproduct1 = Prodotto("Laptop", 1200.0, 12, "ABC")

print(f"Nome prodotto: {myproduct1.name} - prezzo: {myproduct1.price}")

print(f"Il totale lordo di myproduct1 è {myproduct1.valore_lordo()}") #uso un metodo di istanza

p3 = Prodotto.costruttore_con_quantità_uno("Auricolari",200.0,"ABC") #modo per chiamare un metodo di classe

print(f"Prezzo scontato di myproduct1 {Prodotto.applica_sconto(myproduct1.price,0.15)}") #modo per chiamare un metodo statico

myproduct2 = Prodotto("Mouse",10,25,"CDE")
print(f"Nome prodotto: {myproduct2.name} - prezzo: {myproduct2.price}")

print(f"Valore lordo di myproduct1:{myproduct1.valore_lordo()}")

Prodotto.aliquota_iva = 0.24

print(f"Valore lordo di myproduct1:{myproduct1.valore_lordo()}")

print(myproduct1)

p_a = Prodotto("Laptop", 1200.0, 12, "ABC")
p_b = Prodotto("Mouse", 10, 14, "CDE")

print("myproduct1 == p_a?", myproduct1 == p_a) #va a chiamare il metodo __eq__ appena implementato. Mi aspetto TRUE
print("myproduct2 == p_b?", myproduct1 == p_b) #FALSE

mylist = [p_a,p_b,myproduct1]
mylist.sort()

print("lista di prodotti ordinata")
for p in mylist:
    print(f"- {p}")

my_product_scontato = ProdottoScontato(name = "Auricolari",price = 320, quantity = 1, supplier = "ABC", sconto_percento = 10)
my_service = Servizio(name = "Consulenza", tariffa_oraria = 100, ore = 3)

mylist.append(my_product_scontato)
mylist.append(my_service)

for elem in mylist:
    print(elem.name, "->", elem.prezzo_finale())
# Scrivere una classe Cliente che abbia i campi
# "nome", "email", "categoria" ("Gold", "Silver", "Bronze").
# Vorremmo che questa classe avesse un metodo che chiamiamo "descrizione"
# che deve restituire una stringa formattata ad es
# "Cliente Fulvio Bianchi (Gold) - fulvio@google.com"

# Si modifichi la classe Cliente in maniera tale che la proprietà categoria
# sia protetta e accetti solo ("Gold","Silver","Bronze")

class Cliente:
    def __init__(self, nome, mail, categoria):
        self.nome = nome
        self.mail = mail
        self._categoria = None
        self.categoria= categoria

    def descrizione(self):
        return f"Cliente {self.nome} ({self.categoria}) - {self.mail}"
    @property
    def categoria(self):
        return self._categoria
    @categoria.setter
    def categoria(self, categoria):
        if categoria != "Gold" and categoria != "Silver" and categoria != "Bronze":
            raise ValueError("Attenzione, categoria non valida. Scegliere tra Gold, Silver o Bronze")
        self._categoria = categoria


c1 = Cliente("Fulvio Bianchi", "fulvio@google.com", "Gold")
# c2 = Cliente("Carlo Masone","carlo.masone@polito.it","Platinum")
print(c1.descrizione())