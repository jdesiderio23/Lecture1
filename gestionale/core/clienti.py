# Scrivere una classe Cliente che abbia i campi
# "nome", "email", "categoria" ("Gold", "Silver", "Bronze").
# Vorremmo che questa classe avesse un metodo che chiamiamo "descrizione"
# che deve restituire una stringa formattata ad es
# "Cliente Fulvio Bianchi (Gold) - fulvio@google.com"
from dataclasses import dataclass

# Si modifichi la classe Cliente in maniera tale che la proprietà categoria
# sia protetta e accetti solo ("Gold","Silver","Bronze")

categorie_valide = {"Gold", "Silver", "Bronze"}

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
        if categoria not in categorie_valide:
            raise ValueError("Attenzione, categoria non valida. Scegliere tra Gold, Silver o Bronze")
        self._categoria = categoria

@dataclass
class ClienteRecord:
    name: str
    email: str
    categoria: str

    def __str__(self):
        return f"{self.name} -- {self.email} ({self.categoria})"

def _test_modulo():
    c1 = Cliente("Fulvio Bianchi", "fulvio@google.com", "Gold")
    # c2 = Cliente("Carlo Masone","carlo.masone@polito.it","Platinum")
    print(c1.descrizione())

if __name__ == "__main__":
    _test_modulo()