import pandas as pd
from classes.enums.enum_status_voo import EnumStatusVoo
from classes.enums.enum_tipo_aviao import EnumTipoAviao
from classes.voo.tripulacao import Tripulacao
from classes.aviao.aviao import Aviao
from modulos.manipula_arquivos import ManipulaArquivos
from .local import Local
from .coordenadas import Coordenadas
import math
from datetime import datetime, timedelta

CAMINHO_VOOS = "base_dados/voo/voos.json"
cabecalho = 'Voos'
colunas = ["tripulacao_id","aviao","origem","destino", "duracao_estimada", "saida", "chegada", "status"]


class Voo():
    def __init__(self) -> None:
        self.__tripulacao_id = None     #int
        self.__aviao = None             #Aviao
        self.__origem = None            #Local
        self.__destino = None           #Local
        self.__duracao_estimada = None  #float | em horas
        self.__saida = None             #Datetime
        self.__chegada = None           #Datetime
        self.__status = None            #EnumStatusVoo
        self.__id = id(self)


   #--------------GET--------------

    @property
    def tripulacao_id(self):
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
    
    @property
    def status(self):
        return self.__status
    
    @property
    def str_status(self):
        return self.__status.value
    
    @property
    def id(self):
        return self.__id
    
    #--------------SET--------------

    @tripulacao_id.setter
    def tripulacao_id(self, valor: int):
        self.__tripulacao_id = valor
    
    @aviao.setter
    def aviao(self, valor: Aviao):
        self.__aviao = valor

    @origem.setter
    def origem(self, valor: Local):
        if not isinstance(valor, Local):
            raise Exception("Local de origem inválido.")
        self.__origem = valor

    @destino.setter
    def destino(self, valor: Local):
        if not isinstance(valor, Local):
            raise Exception("Local de destino inválido.")
        self.__destino = valor
            
    @duracao_estimada.setter
    def duracao_estimada(self, valor: int):
            self.__duracao_estimada = valor

    @saida.setter
    def saida(self, valor: datetime):
        if not isinstance(valor, datetime):
            raise Exception("Data de saída inválida.")
        self.__saida = valor
            
    @chegada.setter
    def chegada(self, valor: datetime):
        if not isinstance(valor, datetime):
            raise Exception("Data de Chegada inválida.")
        self.__chegada = valor

    @status.setter
    def status(self, valor):
        if valor == EnumStatusVoo.PLANEJADO:  
            self.__status = valor
        else:
            raise Exception("Status do voo não pode ser diferente de Planejado durante a criação!")
            
        
    #--------------PRIVATE---------------

    def __calcula_duracao(self):
        # Formula de Haversine:
        # usada para calcula a distancia entre dois pontos da terra
        raio_terra = 6371

        delta_lat = self.origem.coordenadas.latitude - self.destino.coordenadas.latitude
        delta_lon = self.origem.coordenadas.longitude - self.destino.coordenadas.longitude
        
        aux1 = math.sin(delta_lat / 2)**2 + math.cos(self.origem.coordenadas.latitude) * math.cos(self.destino.coordenadas.latitude) * math.sin(delta_lon / 2)**2
        distancia = 2 * raio_terra * math.asin(math.sqrt(aux1))

        self.duracao_estimada =  distancia / float(self.aviao.velocidade_maxima) # h = km/(km/h)
    
        
    def __cria_retorno(self):
        dias = int(self.duracao_estimada // 24)
        horas_restantes = self.duracao_estimada % 24
        horas = int(horas_restantes)
        minutos = int((horas_restantes - horas) * 60)
        segundos = int(((horas_restantes - horas) * 60 - minutos) * 60)
        # print(f"Duração estimada: {dias} dias, {horas} horas, {minutos} minutos, {segundos} segundos")
        
        return timedelta(days=dias, hours=horas, minutes=minutos, seconds=segundos)
    
    def __cadastra_voo(self):
        df = Voo.carregarListaVoos()
        novo_voo = pd.DataFrame([
            {
                "id": self.id,
                "tripulacao_id": self.tripulacao_id,
                "aviao": self.aviao.numero_serie,
                "origem": self.origem.cidade,
                "destino": self.destino.cidade,
                "duracao_estimada": self.duracao_estimada,
                "saida": self.saida.isoformat(),
                "chegada": self.chegada.isoformat(),
                "status": self.str_status,
            }
        ])


        df = pd.concat([df, novo_voo], ignore_index=True)
        ManipulaArquivos.salvar_informacoes(df, CAMINHO_VOOS, cabecalho)

    #--------------PUBLIC---------------

    def constroi_voo(tripulacao_id, numero_serie_aviao, origem, destino, saida):
        voo = Voo()

        tripulacoes = Tripulacao.carregarListaTripulacao()
        for _, tripulacao in tripulacoes.iterrows():
            if tripulacao["id"] == int(tripulacao_id):
                voo.tripulacao_id = tripulacao_id
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
            raise Exception("O local de destino não pode ser o mesmo que a origem")
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
        voo.__calcula_duracao()
        voo.chegada = saida + voo.__cria_retorno()
        voo.status = EnumStatusVoo.PLANEJADO
        voo.__cadastra_voo()

    def carregarListaVoos():
        lista_voos = ManipulaArquivos.carregar_informacoes(CAMINHO_VOOS, cabecalho, colunas)
        return lista_voos
    
    def atualizar_status_voo(valor, id):
        df = Voo.carregarListaVoos()
        # Terminar depois