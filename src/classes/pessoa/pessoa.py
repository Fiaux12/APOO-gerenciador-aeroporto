from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, cpf) -> None:
        self._nome = None
        self._cpf = None
        self.nome = nome    # Chama o setter do nome
        self.cpf = cpf      # Chama o setter do cpf


    #--------------GET--------------

    @property
    def nome(self):
        return self._nome
    
        
    @property
    def cpf(self):
        return self._cpf

    #--------------SET--------------

    @nome.setter
    def nome(self, valor):
        if valor and valor.strip():  
            self._nome = valor
        else:
            raise Exception("Nome inválido!")
        
    @cpf.setter
    def cpf(self, valor):
        if valor.isdigit():  
            self._cpf = valor
        else:
            raise Exception("CPF inválido!")
