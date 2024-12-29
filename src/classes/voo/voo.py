from classes.enums.enum_tipo_aviao import EnumTipoAviao
from classes.voo.tripulacao import Tripulacao
from classes.aviao.aviao import Aviao
from .local import Local
from .coordenadas import Coordenadas
import math
from datetime import datetime, timedelta

class Voo():
    def __init__(self) -> None:
        self.__tripulacao_id = None     #int
        self.__aviao = None             #Aviao
        self.__origem = None            #Local
        self.__destino = None           #Local
        self.__duracao_estimada = None  #float | em horas
        self.__saida = None             #Datetime
        self.__chegada = None           #Datetime

   #--------------GET--------------

    @property
    def tripulacao(self):
        return self.__tripulacao_id
    
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
    
    @property
    def saida(self):
        return self.__saida
    
    @property
    def chegada(self):
        return self.__chegada
    
        #--------------SET--------------

    @tripulacao.setter
    def tripulacao(self, valor: int):
        self.__tripulacao_id = valor
    
    @aviao.setter
    def aviao(self, valor: Aviao):
        self.__aviao = valor

    @origem.setter
    def origem(self, valor: Local):
        if not isinstance(valor, Local):
            raise ValueError("Local de origem inválido.")
        self.__origem = valor

    @destino.setter
    def destino(self, valor: Local):
        if not isinstance(valor, Local):
            raise ValueError("Local de destino inválido.")
        self.__destino = valor
            
    @duracao_estimada.setter
    def duracao_estimada(self, valor: int):
            self.__duracao_estimada = valor

    @saida.setter
    def saida(self, valor: datetime):
        if not isinstance(valor, datetime):
            raise ValueError("Data de saída inválida.")
        self.__saida = valor
            
    @chegada.setter
    def chegada(self, valor: datetime):
        if not isinstance(valor, datetime):
            raise ValueError("Data de Chegada inválida.")
        self.__chegada = valor
            
        
    #--------------PUBLIC---------------

    def calcula_duracao(self):
        # Formula de Haversine:
        # usada para calcula a distancia entre dois pontos da terra
        raio_terra = 6371

        delta_lat = self.origem.coordenadas.latitude - self.destino.coordenadas.latitude
        delta_lon = self.origem.coordenadas.longitude - self.destino.coordenadas.longitude
        
        aux1 = math.sin(delta_lat / 2)**2 + math.cos(self.origem.coordenadas.latitude) * math.cos(self.destino.coordenadas.latitude) * math.sin(delta_lon / 2)**2
        distancia = 2 * raio_terra * math.asin(math.sqrt(aux1))

        self.duracao_estimada =  distancia / float(self.aviao.velocidade_maxima) # h = km/(km/h)

    def cadastrar_voo(tripulacao_id, numero_serie_aviao, origem, destino, saida):
        voo = Voo()

        tripulacoes = Tripulacao.carregarListaTripulacao()
        for _, tripulacao in tripulacoes.iterrows():
            if tripulacao["id"] == int(tripulacao_id):
                voo.tripulacao = tripulacao_id
                break
            
        avioes = Aviao.carregarListaAvioes()
        for _, aviao in avioes.iterrows():
            if aviao["numero_serie"] == numero_serie_aviao:
                cad_aviao = Aviao()
                cad_aviao.capacidade_maxima = aviao["capacidade_maxima"]
                cad_aviao.velocidade_maxima = aviao["velocidade_maxima"]
                cad_aviao.qtd_motores = aviao["qtd_motores"]
                cad_aviao.modelo = aviao["modelo"]
                cad_aviao.consumo = aviao["consumo"]
                cad_aviao.numero_serie  = aviao["numero_serie"]
                if aviao["tipo"] == EnumTipoAviao.CARGA.value:
                    cad_aviao.tipo = EnumTipoAviao.CARGA
                else:
                    cad_aviao.tipo = EnumTipoAviao.PASSAGEIRO

                
                voo.aviao = cad_aviao
                break

        if origem == destino:
            ValueError("O local de destino não pode ser o mesmo que a origem")
        else:
            locais = Local.carregarListaLocal()
            for _, local in locais.iterrows():
                if local["cidade"] == origem:
                    coordenadas = Coordenadas()
                    coordenadas.latitude = float(local["coordenadas"]["latitude"])
                    coordenadas.longitude = float(local["coordenadas"]["longitude"])
                    voo.origem = Local(local["cidade"], local["estado"], local["pais"], coordenadas)

                if local["cidade"] == destino:
                    destino_coordenadas = Coordenadas()
                    destino_coordenadas.latitude = float(local["coordenadas"]["latitude"])
                    destino_coordenadas.longitude = float(local["coordenadas"]["longitude"])
                    voo.destino = Local(local["cidade"], local["estado"], local["pais"], destino_coordenadas)

        voo.saida = saida
        voo.calcula_duracao()

        dias = int(voo.duracao_estimada // 24)
        horas_restantes = voo.duracao_estimada % 24
        horas = int(horas_restantes)
        minutos = int((horas_restantes - horas) * 60)
        segundos = int(((horas_restantes - horas) * 60 - minutos) * 60)
        
        # print(f"Duração estimada: {dias} dias, {horas} horas, {minutos} minutos, {segundos} segundos")

        voo.chegada = saida + timedelta(days=dias, hours=horas, minutes=minutos, seconds=segundos)
        # print(f"Data de chegada: {voo.chegada}")

        
    def cria_retorno():
        pass
