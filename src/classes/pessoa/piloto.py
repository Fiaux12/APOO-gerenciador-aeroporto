import pandas as pd
from .pessoa import Pessoa
from ..enums.enum_tipo_aviao import EnumTipoAviao
from modulos.manipula_arquivos import ManipulaArquivos

CAMINHO_PILOTOS = "base_dados/tripulacao/pilotos.json"
cabecalho = 'Pilotos'
colunas = ["nome","cpf","tipo_aviao","numero_licenca"]

class Piloto(Pessoa):
    def __init__(self, nome, cpf) -> None:
        super().__init__(nome, cpf)
        self.__tipo_aviao = 0
        self.__numero_licenca = 0


    #--------------GET--------------
    
    # @property
    # def nome(self):
    #     return self._nome
    
        
    # @property
    # def cpf(self):
    #     return self._cpf

    @property
    def tipo_aviao(self):
        return self.__tipo_aviao
    
    @property
    def str_tipo_aviao(self):
        return self.__tipo_aviao.value
        
    @property
    def numero_licenca(self):
        return self.__numero_licenca
    

    #--------------SET--------------

    @tipo_aviao.setter
    def tipo_aviao(self, valor):
        if valor in (EnumTipoAviao.CARGA, EnumTipoAviao.PASSAGEIRO):  
            self.__tipo_aviao = valor
        else:
            raise Exception("Tipo de avião inválido!")
    
    @numero_licenca.setter
    def numero_licenca(self, valor):
        if valor.isdigit():  
            self.__numero_licenca = valor
        else:
            raise Exception("Número da licença inválido!")
        
    #--------------PRIVATE--------------

    #--------------PUBLIC---------------

    def cadastrar(nome, cpf, tipo_aviao: EnumTipoAviao, numero_licenca):
        piloto = Piloto(nome, cpf)
        piloto.tipo_aviao = tipo_aviao
        piloto.numero_licenca = numero_licenca

        pilotos = Piloto.carregarListaPilotos()

        for _, piloto_ in pilotos.iterrows():
            if piloto_["cpf"] == cpf:
                raise Exception("Já existe um piloto com esse CPF!")
        
        novo_piloto = pd.DataFrame([
            {
                "nome": piloto.nome,
                "cpf": piloto.cpf,
                "tipo_aviao": piloto.str_tipo_aviao,
                "numero_licenca": piloto.numero_licenca
            }
        ])

        pilotos = pd.concat([pilotos, novo_piloto], ignore_index=True)
        ManipulaArquivos.salvar_informacoes(pilotos, CAMINHO_PILOTOS, cabecalho)
    
    def carregarListaPilotos():
        lista_pilotos = ManipulaArquivos.carregar_informacoes(CAMINHO_PILOTOS, cabecalho, colunas)
        return lista_pilotos
    
        
        