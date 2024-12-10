from tripulacao import Tripulacao
from aviao import Aviao
from pista import Pista
from local import Local
import math

class Voo():
    def __init__(self, tripulacao:Tripulacao, aviao: Aviao, origem: Local, destino: Local) -> None:
        self.__tripulacao = tripulacao
        self.__aviao = aviao
        self.__origem = origem
        self.__destino = destino
        self.__duracao_estimada = 0

    def calcula_duracao(self):
        # Formula de Haversine:
        # usada para calcula a distancia entre dois pontos da terra
        raio_terra = 6371

        delta_lat = self.origem.coordenadas.latitude - self.destino.coordenadas.latitude
        delta_lon = self.origem.coordenadas.longitude - self.destino.coordenadas.longitude
        
        aux1 = math.sin(delta_lat / 2)**2 + math.cos(self.origem.coordenadas.latitude) * math.cos(self.destino.coordenadas.latitude) * math.sin(delta_lon / 2)**2
        distancia = 2 * raio_terra * math.asin(math.sqrt(aux1))

        self.duracao_estimada =  distancia / self.aviao.velocidade_maxima
