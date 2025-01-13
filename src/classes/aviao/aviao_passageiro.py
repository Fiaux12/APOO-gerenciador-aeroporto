from .aviao import Aviao

class AviaoPassageiro(Aviao):
    def __init__(self, capacidade_maxima, velocidade_maxima, qtd_motores, modelo, consumo , peso_maximo, numero_serie, passageiros) -> None:
        super().__init__(capacidade_maxima, velocidade_maxima, qtd_motores, modelo, consumo , peso_maximo, numero_serie)
        self.__passageiros = passageiros
        
    #--------------GET--------------

    @property
    def passageiros(self):
        return self.__passageiros

    #--------------SET--------------

    @passageiros.setter
    def passageiros(self, valor):
        if isinstance(valor, list):  # Verifica se passageiros é uma lista
            self.__passageiros = valor
        else:
            raise ValueError("Passageiros deve ser uma lista.")