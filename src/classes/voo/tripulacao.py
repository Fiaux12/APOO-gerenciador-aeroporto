import pandas as pd
from modulos.manipula_arquivos import ManipulaArquivos

CAMINHO_TRIPULACAO = "base_dados/voo/tripulacoes.json"
cabecalho = 'Tripulacoes'
colunas = ["id","comissarios_voo","pilotos"]


class Tripulacao():

    def __init__(self) -> None:

        # Lista de comissarios de voo - Lista de str
        self.__comissarios_voo = None

        # Lista coposta por piloto e copiloto - Lista de str
        self.__pilotos = None  

        # Identificação da tripulação
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
        if not valor:
            raise Exception("Selecione os comissários!")
        
        if len(valor) != len(set(valor)):
            raise Exception("Os comissários não podem se repetir!")
        else:
            self.__comissarios_voo = valor
    
    @pilotos.setter
    def pilotos(self, valor):
        if not valor or len(valor) == 1:
            raise Exception("Selecione um piloto e um copiloto piloto!")
        else:
            self.__pilotos = valor
        
        
    #--------------PUBLIC---------------

    def contruir_tripulacao(piloto, copiloto, comissarios):
        if not piloto or not copiloto:
            raise Exception("Selecione um piloto e um copiloto piloto!")
        
        if piloto.split(',')[1] == copiloto.split(',')[1]:
            raise Exception("Piloto principal e copiloto não podem ser a mesma pessoa!")

        tripulacao = Tripulacao()
        tripulacao.pilotos = [piloto, copiloto]
        tripulacao.comissarios_voo = comissarios

        df = Tripulacao.carregarLista()
        nova_tripulacao = pd.DataFrame([
            {
                "id": tripulacao.id,
                "comissarios_voo": tripulacao.comissarios_voo,
                "pilotos": tripulacao.pilotos,
            }
        ])

        df = pd.concat([df, nova_tripulacao], ignore_index=True)
        ManipulaArquivos.salvar_informacoes(df, CAMINHO_TRIPULACAO, cabecalho)
    
    def carregarLista():
        lista_tripulacoes = ManipulaArquivos.carregar_informacoes(CAMINHO_TRIPULACAO, cabecalho, colunas)
        return lista_tripulacoes
    
    def getTripulacaoById(id):
        lista_tripulacoes = ManipulaArquivos.carregar_informacoes(CAMINHO_TRIPULACAO, cabecalho, colunas)
        trip_procurada = None
        for _, tripulacao in lista_tripulacoes.iterrows():
            if str(tripulacao["id"]) == id:
                trip_procurada = tripulacao
        
        return trip_procurada