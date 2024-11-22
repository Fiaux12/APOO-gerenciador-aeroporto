from aviao import Aviao

class Aviao():
    def __init__(self, capacidade_maxima, cargas, velocidade_maxima) -> None:
        super().__init__(capacidade_maxima, velocidade_maxima)
        self.__cargas = cargas