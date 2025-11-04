import flet as ft
import mysql.connector
from UI.view import View
from model.model import Autonoleggio

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view : View, model : Autonoleggio):
        self._model = model
        self._view = view

    def get_nome(self):
        return self._model.nome

    def get_responsabile(self):
        return self._model.responsabile

    def set_responsabile(self, responsabile):
        self._model.responsabile = responsabile

    def conferma_responsabile(self, e):
        self._model.responsabile = self._view.input_responsabile.value
        self._view.txt_responsabile.value = f"Responsabile: {self._model.responsabile}"
        self._view.update()

    # Altre Funzioni Event Handler
    # TODO
    #def mostra_automobili(self):
    def mostra_automobili(self, e):
        self._view.lista_auto.controls.clear()   # ripulisco la lista in caso di ripetizioni successive
        auto_mostrate = self._model.get_automobili()
        for auto in auto_mostrate:
            self._view.lista_auto.controls.append(ft.Text(auto))   # aggiungo la lista alla vista
        self._view.update()


    #def cerca_automobili(self):
    def cerca_automobili(self, e):
        modello = self._view.input_modello_auto.value
        if modello != "": # se la lista è vuota non fa nulla
            auto_per_modello_mostrate = self._model.cerca_automobili_per_modello(modello) # metodo da model con parametro modello
            self._view.lista_auto_ricerca.controls.clear()  # ripulisco la lista in caso di ripetizioni successive
            for auto in auto_per_modello_mostrate:
                self._view.lista_auto_ricerca.controls.append(ft.Text(auto)) # aggiungo la lista alla vista
            self._view.update()