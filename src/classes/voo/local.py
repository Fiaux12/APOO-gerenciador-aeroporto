from classes.voo.coordenadas import Coordenadas
from modulos.manipula_arquivos import ManipulaArquivos

CAMINHO = "base_dados/voo/locais.json"
cabecalho = 'Locais'
colunas = ["cidade","estado", "pais", "coordenadas"]


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

    @coordenadas.setter
    def coordenadas(self, valor):
        if not isinstance(valor, Coordenadas):
            raise TypeError("O valor deve ser uma instância da classe Coordenadas.")
        
        self.__coordenadas = valor
            
    #--------------PUBLIC---------------

    def carregarListaLocal():
        lista = ManipulaArquivos.carregar_informacoes(CAMINHO, cabecalho, colunas)
        return lista