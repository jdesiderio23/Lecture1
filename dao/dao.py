import mysql.connector

from gestionale.core.cliente import ClienteRecord
from gestionale.core.prodotto import ProdottoRecord


class DAO:

    def getAllProdotti(self):
        cnx = mysql.connector.connect(
            user = "root",
            password = "password",
            host = "127.0.0.1",
            database = "sw_gestionale"
        )

        cursor = cnx.cursor(dictionary=True)
        cursor.execute("SELECT * FROM prodotti")
        row = cursor.fetchall()

        res = []
        for p in row:
            res.append(ProdottoRecord(p["nome"], p["prezzo"]))

        cursor.close()
        cnx.close()
        return res

    def getAllClienti(self):
        cnx = mysql.connector.connect(
            user="root",
            password="password",
            host="127.0.0.1",
            database="sw_gestionale"
        )

        cursor = cnx.cursor(dictionary=True)
        cursor.execute("SELECT * FROM clienti")
        row = cursor.fetchall()

        res = []
        for p in row:
            res.append(ClienteRecord(p["nome"], p["mail"], p["categoria"]))

        cursor.close()
        cnx.close()
        return res

if __name__ == "__main__":
    mydao = DAO()
    mydao.getAllProdotti()
