import pandas as pd
from classes.pessoa.comissario_de_voo import ComissarioDeVoo
from classes.pessoa.piloto import Piloto
from modulos.manipula_arquivos import ManipulaArquivos

CAMINHO_TRIPULACAO = "base_dados/voo/tripulacoes.json"
cabecalho = 'Tripulacoes'
colunas = ["id","comissarios_voo","pilotos"]


class Tripulacao():

    def __init__(self) -> None:
        self.__comissarios_voo = None
        self.__pilotos = None  
        self.__id = id(self)

    #--------------GET--------------

    @property
    def comissarios_voo(self):
        return self.__comissarios_voo
    
    @property
    def pilotos(self):
        return self.__pilotos
        
    @property
    def id(self):
        return self.__id
    
    #--------------SET--------------

    @comissarios_voo.setter
    def comissarios_voo(self, valor):
        if len(valor) != len(set(valor)):
            raise Exception("Os comissários não podem se repetir!")
        else:
            self.__comissarios_voo = valor
    
    @pilotos.setter
    def pilotos(self, valor):
        self.__pilotos = valor
        
        
    #--------------PUBLIC---------------

    def contruir_tripulacao(piloto, copiloto, comissarios):
        if piloto.split(',')[1] == copiloto.split(',')[1]:
            raise Exception("Piloto principal e copiloto não podem ser a mesma pessoa!")

        tripulacao = Tripulacao()
        tripulacao.pilotos = [piloto, copiloto]
        tripulacao.comissarios_voo = comissarios

        df = Tripulacao.carregarListaTripulacao()
        nova_tripulacao = pd.DataFrame([
            {
                "id": tripulacao.id,
                "comissarios_voo": tripulacao.comissarios_voo,
                "pilotos": tripulacao.pilotos,
            }
        ])

        df = pd.concat([df, nova_tripulacao], ignore_index=True)
        ManipulaArquivos.salvar_informacoes(df, CAMINHO_TRIPULACAO, cabecalho)
    
    def carregarListaTripulacao():
        lista_tripulacoes = ManipulaArquivos.carregar_informacoes(CAMINHO_TRIPULACAO, cabecalho, colunas)
        return lista_tripulacoes