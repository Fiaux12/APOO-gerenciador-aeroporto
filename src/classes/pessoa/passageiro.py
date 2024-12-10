from pessoa import Pessoa

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
   