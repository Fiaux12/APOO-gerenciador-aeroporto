from classes.voo.tripulacao import Tripulacao
from classes.aviao.aviao import Aviao
from .local import Local
import math

class Voo():
    def __init__(self) -> None:
        self.__tripulacao_id = None    #Do tipo Tripulacao
        self.__aviao = None         #Do tipo Aviao
        self.__origem = None        #Do tipo Local
        self.__destino = None       #Do tipo Local
        self.__duracao_estimada = self.calcula_duracao()#Do tipo decimal

   #--------------GET--------------

    @property
    def tripulacao(self):
        return self.__tripulacao
    
    @property
    def aviao(self):
        return self.__aviao
    
    @property
    def origem(self):
        return self.__origem
    
    @property
    def destino(self):
        return self.__destino
    
    @property
    def duracao_estimada(self):
        return self.__duracao_estimada
    
        #--------------SET--------------

    @tripulacao.setter
    def tripulacao(self, valor):
        self.__tripulacao = valor
    
    @aviao.setter
    def aviao(self, valor):
        self.__aviao = valor

    @origem.setter
    def origem(self, valor):
        if not isinstance(valor, Local):
            raise ValueError("Local de origem inválido.")
        self.__origem = valor

    @destino.setter
    def destino(self, valor):
        if not isinstance(valor, Local):
            raise ValueError("Local de destino inválido.")
        self.__destino = valor
            
    #--------------PUBLIC---------------

    def calcula_duracao(self):
        # Formula de Haversine:
        # usada para calcula a distancia entre dois pontos da terra
        raio_terra = 6371

        delta_lat = self.origem.coordenadas.latitude - self.destino.coordenadas.latitude
        delta_lon = self.origem.coordenadas.longitude - self.destino.coordenadas.longitude
        
        aux1 = math.sin(delta_lat / 2)**2 + math.cos(self.origem.coordenadas.latitude) * math.cos(self.destino.coordenadas.latitude) * math.sin(delta_lon / 2)**2
        distancia = 2 * raio_terra * math.asin(math.sqrt(aux1))

        self.duracao_estimada =  distancia / self.aviao.velocidade_maxima

    def construir_voo(tripulacao_id, aviao, origem, destino):
        voo = Voo()

        tripulacoes = Tripulacao.carregarListaTripulacao()
        if tripulacao_id in tripulacoes['id'].values:
            voo.tripulacao = tripulacao_id

