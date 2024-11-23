from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, cpf) -> None:
        self._nome = nome
        self._cpf = cpf

