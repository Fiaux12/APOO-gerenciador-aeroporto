from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, cpf) -> None:
        self._nome = nome
        self._cpf = cpf


    #--------------GET--------------

    @property
    def nome(self):
        return self._nome
    
        
    @property
    def cpf(self):
        return self._cpf

    #--------------SET--------------

    @cpf.setter
    def cpf(self, valor):
        if valor.isdigit():  
            self._cpf = valor
        else:
            raise ValueError("CPF inválido!")
