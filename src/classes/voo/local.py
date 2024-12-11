from classes.voo.coordenadas import Coordenadas

# Define, tanto o local de partida, quanto o local de destino
class Local():
    def __init__(self, cidade:str, estado:str, pais:str, coordenadas: Coordenadas) -> None:
        self.__cidade = cidade
        self.__estado = estado
        self.__pais = pais
        self.__coordenadas = coordenadas

   #--------------GET--------------

    @property
    def cidade(self):
        return self.__cidade
    @property
    def estado(self):
        return self.__estado
    @property
    def pais(self):
        return self.__pais
    @property
    def coordenadas(self):
        return self.__coordenadas
    
    #--------------SET--------------

    @cidade.setter
    def cidade(self, valor):
        self.__cidade = valor
    
    @estado.setter
    def estado(self, valor):
        self.__estado = valor

    @pais.setter
    def pais(self, valor):
        self.__pais = valor

# TODO: verificar se da certo
    @coordenadas.setter
    def coordenadas(self, valor):
        coord = Coordenadas(valor)
        self.__coordenadas = coord
   