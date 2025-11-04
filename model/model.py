from database.DB_connect import get_connection
from model.automobile import Automobile
from model.noleggio import Noleggio
import mysql.connector

'''
    MODELLO: 
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''

class Autonoleggio:
    def __init__(self, nome, responsabile):
        self._nome = nome
        self._responsabile = responsabile

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile

    def get_automobili(self) -> list[Automobile] | None:
        """
            Funzione che legge tutte le automobili nel database
            :return: una lista con tutte le automobili presenti oppure None
        """
        # TODO

        try:
            cnx = mysql.connector.connect(user='root',
                                          password='',
                                          database = 'autonoleggio')   # connessione al database
            cursor = cnx.cursor()    # creazione del cursore
            mostra_auto = """SELECT * FROM automobile"""   # la query da eseguire
            cursor.execute(mostra_auto)
            risultato = cursor.fetchall() # prendo tutti i risultati della query dal cursore
            lista_automobili = []
            for riga in risultato:
                auto = Automobile(riga[0], riga[1], riga[2], riga[3], riga[4], riga[5]) # trasformiamo il risultato in un tipo Automobile
                lista_automobili.append(auto)
            cursor.close()
            cnx.close()
            return lista_automobili
        except mysql.connector.Error as err:
            print('Connessione al database non riuscita')
            return None

    def cerca_automobili_per_modello(self, modello) -> list[Automobile] | None:
        """
            Funzione che recupera una lista con tutte le automobili presenti nel database di una certa marca e modello
            :param modello: il modello dell'automobile
            :return: una lista con tutte le automobili di marca e modello indicato oppure None
        """
        # TODO
        try:
            cnx = mysql.connector.connect(user='root',
                                          password='',
                                          database='autonoleggio')  # connessione al database
            cursor = cnx.cursor()  # creazione del cursore
            cerca_auto = "SELECT * FROM automobile WHERE modello=%s"
            cursor.execute(cerca_auto, (modello,))  # evitiamo query injection
            risultato = cursor.fetchall() # prendo tutti i risultati della query dal cursore
            lista_auto_per_modello = []
            for riga in risultato:
                auto = Automobile(riga[0], riga[1], riga[2], riga[3], riga[4], riga[5]) # trasformiamo il risultato in un tipo Automobile
                lista_auto_per_modello.append(auto)
            cursor.close()
            cnx.close()
            return lista_auto_per_modello
        except mysql.connector.Error as err:
            print('Connessione al database non riuscita')
            return None