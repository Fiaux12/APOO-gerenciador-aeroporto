from coordenadas import Coordenadas

# Define, tanto o local de partida, quanto o local de destino
class Local():
    def __init__(self, cidade, estado, pais, coordenadas: Coordenadas) -> None:
        self.__cidade = cidade
        self.__estado = estado
        self.__pais = pais
        self.__coordenadas = coordenadas