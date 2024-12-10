from .pessoa import Pessoa
from ..enums.enum_tipo_aviao import EnumTipoAviao

class Piloto(Pessoa):
    def __init__(self, nome, cpf) -> None:
        super().__init__(nome, cpf)
        self.__tipo_aviao = 0
        self.__numero_licenca = 0


    #--------------GET--------------

    @property
    def tipo_aviao(self):
        return self.__tipo_aviao
    
        
    @property
    def numero_licenca(self):
        return self.__numero_licenca
    

    #--------------SET--------------

    @tipo_aviao.setter
    def tipo_aviao(self, valor):
        if valor in (EnumTipoAviao.CARGA, EnumTipoAviao.PASSAGEIRO):  
            self.__tipo_aviao = valor
        else:
            raise ValueError("Tipo de avião inválido!")
    
    @numero_licenca.setter
    def numero_licenca(self, valor):
        if valor.isdigit():  
            self.__numero_licenca = valor
        else:
            raise ValueError("Número da licença inválido!")
        
    #--------------PRIVATE--------------

    #--------------PUBLIC---------------

    def cadastrar(nome, cpf, tipo_aviao: EnumTipoAviao, numero_licenca):
        piloto = Piloto(nome, cpf)
        print('CHEOU AQUIIIIIIIIIIIIIIIIIIIIIII')
        piloto.tipo_aviao = tipo_aviao
        piloto.numero_licenca = numero_licenca
        

