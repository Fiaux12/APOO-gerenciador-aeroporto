from .pessoa import Pessoa
from modulos.manipula_arquivos import ManipulaArquivos

CAMINHO_PASSAGEIROS = "base_dados/voo/passageiros.json"
cabecalho = 'Passageiros'
colunas = ["nome","cpf","passaporte"]


class Passageiro(Pessoa):
    def __init__(self, nome:str, cpf:int) -> None:
        super().__init__(nome, cpf)
        self.__passaporte = None 

   #--------------GET--------------

    @property
    def passaporte(self):
        return self.__passaporte

    #--------------SET--------------

    @passaporte.setter
    def latitude(self, valor):
        self.__passaporte = valor

    #--------------PRIVATE--------------

    #--------------PUBLIC--------------

    def carregarListaPassageiros():
        lista_passageiros = ManipulaArquivos.carregar_informacoes(CAMINHO_PASSAGEIROS, cabecalho, colunas)
        return lista_passageiros
    