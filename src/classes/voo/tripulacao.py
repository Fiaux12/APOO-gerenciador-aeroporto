
class Tripulacao():
    def __init__(self) -> None:
        self.__comissarios_voo = None
        self.__pilotos = None  

    #--------------GET--------------

    @property
    def comissarios_voo(self):
        return self.__comissarios_voo
    
    @property
    def pilotos(self):
        return self.__pilotos
    
    #--------------SET--------------

    @comissarios_voo.setter
    def comissarios_voo(self, valor):
        self.__comissarios_voo = valor
    
    @pilotos.setter
    def pilotos(self, valor):
        self.__pilotos = valor
        
        
    #--------------PUBLIC---------------

    def contruir_tripulacao(piloto, copiloto, comissarios):
        lista_pilotos = [piloto, copiloto]
        tripulacao = Tripulacao()
        tripulacao.pilotos = lista_pilotos
        tripulacao.comissarios_voo = comissarios

