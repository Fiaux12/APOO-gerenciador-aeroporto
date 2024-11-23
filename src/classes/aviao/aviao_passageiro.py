from aviao import Aviao

class Aviao():
    def __init__(self, capacidade_maxima, velocidade_maxima, qtd_motores, modelo, consumo , peso_maximo, numero_serie, passageiros) -> None:
        super().__init__(capacidade_maxima, velocidade_maxima, qtd_motores, modelo, consumo , peso_maximo, numero_serie)
        self.__passageiros = passageiros
        
