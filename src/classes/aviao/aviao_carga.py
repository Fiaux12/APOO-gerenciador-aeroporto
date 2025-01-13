from .aviao import Aviao

class AviaoCarga(Aviao):
    def __init__(self, capacidade_maxima, velocidade_maxima, qtd_motores, modelo, consumo , peso_maximo, numero_serie, cargas) -> None:
        super().__init__(capacidade_maxima, velocidade_maxima, qtd_motores, modelo, consumo , peso_maximo, numero_serie)
        self.__cargas = cargas
        
    #--------------GET--------------

    @property
    def cargas(self):
        return self.__cargas

    #--------------SET--------------

    @cargas.setter
    def cargas(self, valor):
        if isinstance(valor, list):  # Verifica se cargas é uma lista
            self.__cargas = valor
        else:
            raise ValueError("Cargas deve ser uma lista.")